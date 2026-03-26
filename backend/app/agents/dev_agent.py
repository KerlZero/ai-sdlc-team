from app.schemas.ba import DevOutput

def run_dev_agent(raw_requirement: str) -> DevOutput:
    # ตรงนี้ภายหลังค่อยต่อ LLM จริง
    return DevOutput(
        architecture_notes="Summarize the user's requested system_flow outcome //architecture_notes",
        file_structure=[
            "As a user, I want to perform the requested action //file_structure."
        ],
        implementation_tasks=[
            "System should satisfy the described requirement //implementation_tasks."
        ],
        code_snippets=[]
    )