from __future__ import annotations

from app.validation.compile_runner import DBTRunner


def run_dbt_tests(project_dir: str = "dbt_project") -> dict:
    runner = DBTRunner(project_dir=project_dir)
    return runner.test()