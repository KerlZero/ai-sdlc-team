from app.schemas.ba import SAOutput

def run_sa_agent(raw_requirement: str) -> SAOutput:
    # ตรงนี้ภายหลังค่อยต่อ LLM จริง
    return SAOutput(
        system_flow="Summarize the user's requested system_flow outcome //system_flow",
        modules=[
            "As a user, I want to perform the requested action //modules."
        ],
        api_endpoints=[
            "System should satisfy the described requirement //api_endpoints."
        ],
        validations=[],
        edge_cases=[]
    )