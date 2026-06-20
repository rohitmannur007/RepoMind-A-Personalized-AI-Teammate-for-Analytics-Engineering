from __future__ import annotations

import json

from app.retrieval.indexer import build_index


def main() -> None:
    docs, style = build_index("dbt_project")
    print(f"Indexed {len(docs)} documents")
    print(json.dumps(style, indent=2))


if __name__ == "__main__":
    main()