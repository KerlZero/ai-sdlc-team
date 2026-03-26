from pydantic import BaseModel
from typing import List, Dict

class TesterOutput(BaseModel):
    test_scenarios: List[str]
    test_cases: List[str]
    risks: List[str]
    playwright_files: Dict[str, str]