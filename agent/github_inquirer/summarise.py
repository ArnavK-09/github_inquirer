from typing import List, Any
from langchain_core.runnables import RunnableConfig
from .model import get_llm
from typing_extensions import TypedDict


class InputState(TypedDict):
    """Defines the structure for the input state containing a query and a list of repositories."""

    query: str
    repos: List[Any]


async def summarise_node(state: InputState, config: RunnableConfig):
    """
    Summarizes insights from GitHub repositories based on the provided state data.

    Args:
        state: A dictionary containing the query and repository data.
        config: The configuration to be passed when invoking the LLM.

    Returns:
        A dictionary containing the summarized insights under the key "output".
    """

    # Prepare the query to summarize insights from the provided repository data
    repos_data = state.get(
        "repos",
        "We encountered an issue fetching GitHub repositories. Please inform the user about the error in a single line.",
    )  # Default fallback message if repos are not found
    query = f"""
    Analyze the following GitHub repositories. Summarize the key insights, focusing on repository relevance, activity, and unique features. Your summary should be concise, informative, and under 250 words.

    <repos>
    {repos_data}
    </repos>
    """

    try:
        # Call the LLM to generate a summary based on the query
        response = await get_llm().ainvoke([query], config)
        return {"output": response.content}  # Return the generated summary

    except Exception as e:
        # Handle any errors when contacting the LLM and return a fallback message
        return {
            "output": "There was an issue fetching the insights. Please try again later."
        }
