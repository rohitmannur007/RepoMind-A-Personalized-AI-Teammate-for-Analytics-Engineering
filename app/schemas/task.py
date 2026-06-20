from pydantic import BaseModel


class TaskRequest(BaseModel):
    task: str
    repo_root: str = "dbt_project"
    top_k: int = 5