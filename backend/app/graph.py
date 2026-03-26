from langgraph.graph import StateGraph, END
from app.state import SDLCState
from app.nodes.ba_node import ba_node
from app.nodes.sa_node import sa_node
from app.nodes.dev_node import dev_node
from app.nodes.tester_node import tester_node
from app.nodes.devops_node import devops_node

def build_graph():
    graph = StateGraph(SDLCState)

    graph.add_node("ba", ba_node)
    graph.add_node("sa", sa_node)
    graph.add_node("dev", dev_node)
    graph.add_node("tester", tester_node)
    graph.add_node("devops", devops_node)

    graph.set_entry_point("ba")
    graph.add_edge("ba", "sa")
    graph.add_edge("sa", "dev")
    graph.add_edge("dev", "tester")
    graph.add_edge("tester", "devops")
    graph.add_edge("devops", END)

    return graph.compile()