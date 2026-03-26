from app.state import SDLCState
from app.schemas.sa import SAOutput

def sa_node(state: SDLCState) -> SDLCState:
    result = SAOutput(
        system_flow=["User submits request", "System validates input", "System processes result"],
        modules=["requirement-parser", "workflow-engine", "artifact-generator"],
        api_endpoints=["POST /run"],
        validations=["raw_requirement must not be empty"],
        edge_cases=["Empty requirement", "Conflicting requirement"]
    )
    state["sa_output"] = result.model_dump()
    state["current_step"] = "sa_completed"
    state.setdefault("logs", []).append("SA agent completed")
    return state