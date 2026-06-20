from app.agent.planner import build_plan
from app.llm import DraftGenerator


def test_planner_returns_steps():
    plan = build_plan("Create a test", {"model_names": ["stg_orders"]}, [])
    assert len(plan) > 0


def test_draft_generator_works():
    draft = DraftGenerator().draft("Create a revenue mart", [], {"model_names": ["stg_orders"]})
    assert "ref(" in draft or "Task:" in draft