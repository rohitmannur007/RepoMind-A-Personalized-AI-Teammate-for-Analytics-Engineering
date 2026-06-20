from __future__ import annotations

from pathlib import Path
from typing import Any

from app.retrieval.repo_parser import build_style_profile, collect_documents, save_json


def build_index(repo_root: str, output_dir: str = "data/processed") -> tuple[list[dict[str, Any]], dict[str, Any]]:
    docs = collect_documents(repo_root)
    style_profile = build_style_profile(docs)

    out = Path(output_dir)
    out.mkdir(parents=True, exist_ok=True)

    save_json(str(out / "repo_docs.json"), {"documents": docs})
    save_json(str(out / "style_profile.json"), style_profile)

    return docs, style_profile