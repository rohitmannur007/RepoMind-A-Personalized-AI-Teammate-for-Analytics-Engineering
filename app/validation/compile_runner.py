from __future__ import annotations

import os
import subprocess
from pathlib import Path
from typing import Any

from dotenv import load_dotenv


class DBTRunner:
    def __init__(self, project_dir: str = "dbt_project"):
        load_dotenv()
        self.project_dir = Path(project_dir)
        self.profiles_dir = Path(os.getenv("DBT_PROFILES_DIR", str(self.project_dir / "profiles")))

    def _base_env(self) -> dict[str, str]:
        env = os.environ.copy()
        env["DBT_PROFILES_DIR"] = str(self.profiles_dir)
        return env

    def _run(self, args: list[str]) -> dict[str, Any]:
        proc = subprocess.run(
            args,
            cwd=str(self.project_dir),
            env=self._base_env(),
            capture_output=True,
            text=True,
        )
        return {
            "success": proc.returncode == 0,
            "returncode": proc.returncode,
            "stdout": proc.stdout[-4000:],
            "stderr": proc.stderr[-4000:],
        }

    def seed(self) -> dict[str, Any]:
        return self._run(["dbt", "seed"])

    def compile(self) -> dict[str, Any]:
        return self._run(["dbt", "compile"])

    def test(self) -> dict[str, Any]:
        return self._run(["dbt", "test"])