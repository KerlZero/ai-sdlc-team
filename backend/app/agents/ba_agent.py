from app.schemas.ba import BAOutput

def run_ba_agent(raw_requirement: str) -> BAOutput:
    # ตรงนี้ภายหลังค่อยต่อ LLM จริง
    return BAOutput(
        business_goal="Summarize the user's requested business outcome",
        user_stories=[
            "As a user, I want to perform the requested action."
        ],
        acceptance_criteria=[
            "System should satisfy the described requirement."
        ],
        assumptions=[],
        open_questions=[]
    )