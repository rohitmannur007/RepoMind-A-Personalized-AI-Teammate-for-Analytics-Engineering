from __future__ import annotations

from typing import Any


def review_draft(draft: str, compile_result: dict[str, Any], test_result: dict[str, Any], style_profile: dict[str, Any]) -> dict[str, Any]:
    issues: list[str] = []

    if not compile_result.get("success", False):
        issues.append("dbt compile failed")
    if not test_result.get("success", False):
        issues.append("dbt test failed")

    if "ref(" not in draft and "select" in draft.lower():
        issues.append("draft does not use dbt refs")

    if style_profile.get("num_sql_files", 0) > 0 and "```sql" not in draft.lower():
        issues.append("draft is not formatted as SQL")

    verdict = "pass" if not issues else "needs_work"
    return {"verdict": verdict, "issues": issues}