from __future__ import annotations

import json

from app.agent.orchestrator import run_task


def main() -> None:
    result = run_task("Create a monthly revenue mart from the enriched orders model.")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()