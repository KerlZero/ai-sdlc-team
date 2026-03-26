from app.schemas.ba import DevOpsOutput

def run_devops_agent(raw_requirement: str) -> DevOpsOutput:
    # ตรงนี้ภายหลังค่อยต่อ LLM จริง
    return DevOpsOutput(
        docker_notes="Summarize the user's requested business outcome//docker_notes",
        ci_steps=[
            "As a user, I want to perform the requested action.//ci_steps"
        ],
        env_variables=[
            "System should satisfy the described requirement.//env_variables"
        ],
        pipeline_files=[]
    )