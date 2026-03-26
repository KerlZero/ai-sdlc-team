from typing import TypedDict, Optional, List, Dict, Any

class SDLCState(TypedDict, total=False):
    raw_requirement: str

    ba_output: Dict[str, Any]
    sa_output: Dict[str, Any]
    dev_output: Dict[str, Any]
    tester_output: Dict[str, Any]
    devops_output: Dict[str, Any]

    logs: List[str]
    current_step: str
    errors: List[str]