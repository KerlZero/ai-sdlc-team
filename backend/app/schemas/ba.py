from pydantic import BaseModel
from typing import List

class BAOutput(BaseModel):
    business_goal: str
    user_stories: List[str]
    acceptance_criteria: List[str]
    assumptions: List[str]
    open_questions: List[str]