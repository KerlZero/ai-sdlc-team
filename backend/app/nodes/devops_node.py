from app.state import SDLCState
from app.schemas.devops import DevOpsOutput

def devops_node(state: SDLCState) -> SDLCState:
    result = DevOpsOutput(
        docker_notes=["detail docker note for deploy"],
        ci_steps=["step by step deployment"],
        env_variables=["config var"],
        pipeline_files=["piplinecheck"]
    )
    state["devops_output"] = result.model_dump()
    state["current_step"] = "devops_completed"
    state.setdefault("logs", []).append("DEVOPS agent completed")
    return state