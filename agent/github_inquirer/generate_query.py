from langchain_core.messages import HumanMessage
from langchain_core.runnables import RunnableConfig
from langgraph.graph import MessagesState
from .model import get_llm


async def generate_query_node(state: MessagesState, config: RunnableConfig):
    """
    Generates a refined GitHub search query based on the user's input.
    """

    query = state["messages"][-1]
    prompt = f"""
# Task: Transform User Query into Optimized GitHub Search Query

Your goal is to convert the given user query into an optimized GitHub search query. Use GitHub's search filters wherever possible to maximize relevance and precision. Leverage the provided cheat sheet for inspiration, and ensure the output query can effectively narrow down search results to match the intent behind the user's query.
# BY ANY MEANS YOUR TASK IS TO RESPONSE GITHUB SEARCH QUERY WHETHER USE PROVIDED TERMS OR NOT, DO NOT REPLY ANY OTHER THINGS
## Guidelines:
1. **Identify Intent**: Understand whether the user is searching for repositories, code, issues, pull requests, or users.
2. **Apply Filters**: Use filters like `stars`, `forks`, `size`, `user`, `language`, `repo`, `is:`, `created:`, `updated:`, etc., to create a precise search query.
3. **Syntax Accuracy**: Ensure correct syntax for all GitHub filters.
4. **Maximize Output**: Provide an optimized query that effectively captures the user's intent.

---

## Input:
**USER_QUERY**: `{query}`

## Expected Output:
"<Optimized Query>"

---

## Examples:

### Example 1:
USER_QUERY: js repos  
OUTPUT: language:javascript

### Example 2:
USER_QUERY: popular Python projects  
OUTPUT: language:python stars:>1000

### Example 3:
USER_QUERY: issues with bugs 
OUTPUT: label:bug is:issue is:open

### Example 4:
USER_QUERY: active contributors in San Francisco  
OUTPUT: location:"San Francisco" repos:>10

### Example 5:
USER_QUERY: code for authentication in Node.js  
OUTPUT: authentication language:javascript

### Example 6:
USER_QUERY: find forks of a repo updated in 2023  
OUTPUT: fork:true pushed:>=2023-01-01

---
"""
    # Return the tool's output arguments
    try:
        # Call the LLM to generate a summary based on the query
        response = await get_llm().ainvoke([prompt], config)
        return {"query": response.content}  # Return the generated summary

    except Exception as e:
        # Handle any errors when contacting the LLM and return a fallback message
        return {"query": ""}
