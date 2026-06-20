from __future__ import annotations

from app.agent.planner import build_plan
from app.agent.reviewer import review_draft
from app.llm import DraftGenerator
from app.retrieval.indexer import build_index
from app.retrieval.retriever import RepoRetriever
from app.validation.compile_runner import DBTRunner


def run_task(task: str, repo_root: str = "dbt_project", top_k: int = 5) -> dict:
    documents, style_profile = build_index(repo_root)
    retriever = RepoRetriever(documents)
    context = retriever.search(task, top_k=top_k)

    plan = build_plan(task, style_profile, context)
    draft = DraftGenerator().draft(task, context, style_profile)

    runner = DBTRunner(project_dir=repo_root)
    compile_result = runner.compile()
    test_result = runner.test()

    review = review_draft(draft, compile_result, test_result, style_profile)

    return {
        "task": task,
        "plan": plan,
        "context": context,
        "draft": draft,
        "validation": {
            "compile": compile_result,
            "test": test_result,
        },
        "review": review,
        "style_profile": style_profile,
    }