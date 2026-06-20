from __future__ import annotations

from typing import Any


class DraftGenerator:
    def draft(self, task: str, context: list[dict[str, Any]], style_profile: dict[str, Any]) -> str:
        task_lower = task.lower()
        model_hint = self._best_model_hint(context)

        if any(word in task_lower for word in ["create", "build", "mart", "model"]):
            return self._draft_model(task, model_hint)

        if "test" in task_lower:
            return self._draft_tests(model_hint)

        if "fix" in task_lower:
            return self._draft_fix(task, model_hint)

        if "lineage" in task_lower or "impact" in task_lower:
            return self._draft_lineage_answer(model_hint)

        return self._generic_answer(task, model_hint)

    def _best_model_hint(self, context: list[dict[str, Any]]) -> str:
        for doc in context:
            path = doc["path"]
            if path.endswith(".sql"):
                return path.split("/")[-1].replace(".sql", "")
        return "stg_orders"

    def _draft_model(self, task: str, model_hint: str) -> str:
        return f"""```sql
-- Draft for: {task}
with base as (
    select *
    from {{{{ ref('{model_hint}') }}}}
)
select
    date_trunc('month', order_date) as month,
    count(*) as total_rows,
    sum(gross_revenue) as gross_revenue
from base
group by 1
order by 1
```"""

    def _draft_tests(self, model_hint: str) -> str:
        return f"""```yaml
version: 2

models:
  - name: {model_hint}
    columns:
      - name: id
        tests:
          - not_null
          - unique
```"""

    def _draft_fix(self, task: str, model_hint: str) -> str:
        return f"""```sql
-- Draft fix for: {task}
with source as (
    select *
    from {{{{ ref('{model_hint}') }}}}
)
select *
from source
```"""

    def _draft_lineage_answer(self, model_hint: str) -> str:
        return (
            f"The main upstream anchor appears to be `{model_hint}`. "
            "Any downstream mart using that model should be checked for broken refs, changed grain, or renamed columns."
        )

    def _generic_answer(self, task: str, model_hint: str) -> str:
        return f"Task: {task}\nSuggested anchor model: {model_hint}\nFocus on repo style, refs, and dbt validation."