from typing import Any

from pydantic import BaseModel


class RetrievedDocument(BaseModel):
    path: str
    score: float
    snippet: str


class AgentResponse(BaseModel):
    task: str
    plan: list[str]
    context: list[RetrievedDocument]
    draft: str
    validation: dict[str, Any]
    review: dict[str, Any]
    style_profile: dict[str, Any]