from app.retrieval.repo_parser import collect_documents, build_style_profile


def test_collect_documents():
    docs = collect_documents("dbt_project")
    assert len(docs) > 0


def test_style_profile():
    docs = collect_documents("dbt_project")
    profile = build_style_profile(docs)
    assert profile["num_documents"] > 0