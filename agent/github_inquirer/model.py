from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.language_models.chat_models import BaseChatModel


def get_llm() -> BaseChatModel:
    """
    Retrieves a Generative AI chat model instance configured with specific parameters.
    """
    return ChatGoogleGenerativeAI(temperature=0, model="gemini-1.5-flash")
