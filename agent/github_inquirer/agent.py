from typing import List, Any, Optional, Annotated
from typing_extensions import TypedDict
from langgraph.graph import StateGraph, END
from langgraph.checkpoint.memory import MemorySaver
from langgraph.graph.message import add_messages

# Import nodes for graph
from .generate_query import generate_query_node
from .github_results import github_results_node
from .summarise import summarise_node


# Define the state structure for the graph
class State(TypedDict):
    messages: Annotated[list, add_messages]  # Messages associated with the workflow
    query: Optional[str]  # Query generated or received from the user
    repos: Optional[List[Any]]  # List of repository data
    summary: Optional[str]  # Summary of the results
    output: Optional[str]  # Final output of the workflow


# Initialize the state graph
workflow = StateGraph(State)

# Add nodes representing different processing stages in the workflow
workflow.add_node(
    "generate_query", generate_query_node
)  # Generate query based on input
workflow.add_node(
    "github_results", github_results_node
)  # Fetch GitHub results based on the query
workflow.add_node("summarise_query", summarise_node)  # Summarize the fetched results

# Set the entry point for the workflow
workflow.set_entry_point("generate_query")

# Define edges to connect nodes, establishing the flow of execution
workflow.add_edge(
    "generate_query", "github_results"
)  # From query generation to fetching results
workflow.add_edge(
    "github_results", "summarise_query"
)  # From fetching results to summarization
workflow.add_edge("summarise_query", END)

# Memory saver for maintaining workflow state across executions
memory = MemorySaver()

# Compile the graph with the memory checkpointer
graph = workflow.compile(checkpointer=memory)
