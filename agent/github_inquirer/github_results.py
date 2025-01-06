from typing_extensions import TypedDict
import requests
import os


class InputState(TypedDict):
    """
    Represents the input state for GitHub repository search.
    """

    query: str


# Securely retrieve the GitHub Personal Access Token from environment variables
GITHUB_TOKEN = os.getenv("GITHUB_PAT")

GITHUB_API_URL = "https://api.github.com"


def extract_repository_data(items):
    """
    Extracts and structures relevant data from a list of GitHub repository items.

    Args:
        items (list): List of repository items from GitHub API response.

    Returns:
        list: Structured data containing key information about repositories.
    """
    return [
        {
            "name": item.get("name"),
            "full_name": item.get("full_name"),
            "owner": (
                {
                    "login": item["owner"].get("login"),
                    "id": item["owner"].get("id"),
                    "html_url": item["owner"].get("html_url"),
                }
                if item.get("owner")
                else None
            ),
            "description": item.get("description"),
            "url": item.get("html_url"),
            "license": (
                {
                    "key": item["license"].get("key"),
                    "name": item["license"].get("name"),
                    "url": item["license"].get("html_url"),
                }
                if item.get("license")
                else None
            ),
        }
        for item in items
    ]


def list_repositories(query):
    """
    Fetches repositories from GitHub API based on the search query.

    Args:
        query (str): The search query string.

    Returns:
        dict: JSON response containing repository data.

    Raises:
        Exception: If the API request fails or returns a non-200 status code.
    """
    headers = {"Authorization": f"token {GITHUB_TOKEN}"}
    try:
        response = requests.get(
            f"{GITHUB_API_URL}/search/repositories?q={query}&per_page=10",
            headers=headers,
        )
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        raise Exception(f"Error fetching repositories: {e}")


async def github_results_node(state: InputState):
    """
    Processes the user's query to fetch and structure GitHub repository data.

    Args:
        state (InputState): The input state containing the user's query.

    Returns:
        dict: A dictionary containing structured repository data, or empty list if an error occurs.
    """
    try:
        # Fetch repository data from GitHub API
        repos = list_repositories(state.get("query", "default-query"))

        # Extract and structure the repository data
        structured_repos = extract_repository_data(repos.get("items", []))

        # Return the structured data as part of the node output
        return {"repos": structured_repos}

    except Exception as e:
        # If any error occurs, return an empty list for repositories
        print(f"Error occurred: {e}")
        return {"repos": []}
