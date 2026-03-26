from pydantic import BaseModel
from typing import List, Dict

class DevOutput(BaseModel):
    architecture_notes: List[str]
    file_structure: List[str]
    implementation_tasks: List[str]
    code_snippets: Dict[str, str]