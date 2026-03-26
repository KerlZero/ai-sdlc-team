from pydantic import BaseModel
from typing import List

class SAOutput(BaseModel):
    system_flow: List[str]
    modules: List[str]
    api_endpoints: List[str]
    validations: List[str]
    edge_cases: List[str]