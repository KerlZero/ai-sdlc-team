from app.state import SDLCState
from app.schemas.tester import TesterOutput
from app.utils.file_writer import save_playwright_files

def tester_node(state: SDLCState) -> SDLCState:
    result = TesterOutput(
        test_scenarios=["design scenario for create test case"],
        test_cases=["create detail and condition for test case by case"],
        risks=["due date timing for execute test"],
        playwright_files={
            "tests/login.spec.ts": "create test script playwright"
        }
    )
    state["tester_output"] = result.model_dump()
    save_playwright_files(result.playwright_files)

    state["current_step"] = "tester_completed"
    state.setdefault("logs", []).append("TESTER agent completed")
    return state

if __name__ == "__main__":
    sample_state: SDLCState = {
        "raw_requirement": "Build login module",
        "ba_output": {},
        "sa_output": {},
        "dev_output": {},
        "logs": [],
        "errors": []
    }

    result = tester_node(sample_state)
    print("final result =", result)