from __future__ import annotations

from typing import Any


def build_plan(task: str, style_profile: dict[str, Any], context: list[dict[str, Any]]) -> list[str]:
    task_lower = task.lower()
    plan = [
        "Read the most relevant repo files.",
        "Match the change to the repo's style profile.",
        "Draft the SQL or test patch.",
        "Validate using dbt compile and dbt test.",
        "Review failures and refine the answer.",
    ]

    if "test" in task_lower:
        plan.insert(2, "Focus on not_null, unique, and relationship tests for key columns.")
    if "lineage" in task_lower or "impact" in task_lower:
        plan.insert(2, "Trace upstream refs and downstream model impact.")
    if "fix" in task_lower:
        plan.insert(2, "Locate the failing model and inspect the surrounding joins and CTEs.")
    if "create" in task_lower or "build" in task_lower:
        plan.insert(2, "Use nearby marts and intermediate models as a template.")

    if style_profile.get("model_names"):
        plan.append(f"Known models: {', '.join(style_profile['model_names'][:6])}")

    if context:
        plan.append(f"Top context file: {context[0]['path']}")

    return plan