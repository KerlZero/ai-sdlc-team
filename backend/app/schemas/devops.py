from pydantic import BaseModel
from typing import List, Dict

class DevOpsOutput(BaseModel):
    docker_notes: List[str]
    ci_steps: List[str]
    env_variables: List[str]
    pipeline_files: Dict[str, str]