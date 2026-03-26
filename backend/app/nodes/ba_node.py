from app.state import SDLCState
from app.agents.ba_agent import run_ba_agent

def ba_node(state: SDLCState) -> SDLCState:
    result = run_ba_agent(state["raw_requirement"])
    state["ba_output"] = result.model_dump()
    state["current_step"] = "ba_completed"
    state.setdefault("logs", []).append("BA agent completed")
    return state