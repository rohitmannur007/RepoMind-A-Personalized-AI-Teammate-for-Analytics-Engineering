from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any


TEXT_EXTENSIONS = {".sql", ".yml", ".yaml", ".md", ".txt", ".json", ".csv"}


def read_text_safe(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        return path.read_text(encoding="utf-8", errors="ignore")


def collect_documents(repo_root: str) -> list[dict[str, Any]]:
    base = Path(repo_root)
    docs: list[dict[str, Any]] = []

    for path in base.rglob("*"):
        if not path.is_file():
            continue
        if path.name.startswith("."):
            continue
        if path.suffix.lower() not in TEXT_EXTENSIONS:
            continue

        text = read_text_safe(path)
        docs.append(
            {
                "path": str(path),
                "name": path.name,
                "suffix": path.suffix.lower(),
                "content": text,
            }
        )
    return docs


def extract_model_names(docs: list[dict[str, Any]]) -> list[str]:
    model_names = []
    for doc in docs:
        path = Path(doc["path"])
        if path.suffix.lower() == ".sql":
            model_names.append(path.stem)
    return sorted(set(model_names))


def build_style_profile(docs: list[dict[str, Any]]) -> dict[str, Any]:
    sql_docs = [d for d in docs if d["suffix"] == ".sql"]
    yml_docs = [d for d in docs if d["suffix"] in {".yml", ".yaml"}]

    sql_text = "\n".join(d["content"] for d in sql_docs)
    yml_text = "\n".join(d["content"] for d in yml_docs)

    profile = {
        "num_documents": len(docs),
        "num_sql_files": len(sql_docs),
        "num_yaml_files": len(yml_docs),
        "num_refs": len(re.findall(r"ref\(", sql_text)),
        "num_ctes": len(re.findall(r"\bwith\b|\bcte\b", sql_text, flags=re.IGNORECASE)),
        "num_tests": len(re.findall(r"\btests?:\b", yml_text, flags=re.IGNORECASE)),
        "materializations": sorted(set(re.findall(r"materialized:\s*(\w+)", yml_text))),
        "model_names": extract_model_names(docs),
    }
    return profile


def save_json(path: str, payload: dict[str, Any]) -> None:
    output = Path(path)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(payload, indent=2), encoding="utf-8")