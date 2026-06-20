from __future__ import annotations

from typing import Any

from app.validation.compile_runner import DBTRunner


class ToolRouter:
    def __init__(self, project_dir: str = "dbt_project"):
        self.runner = DBTRunner(project_dir=project_dir)

    def run_compile(self) -> dict[str, Any]:
        return self.runner.compile()

    def run_test(self) -> dict[str, Any]:
        return self.runner.test()

    def run_seed(self) -> dict[str, Any]:
        return self.runner.seed()