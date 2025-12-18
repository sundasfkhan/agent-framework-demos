import os
from dotenv import load_dotenv
from agent_framework.openai import OpenAIChatClient

# Load environment variables from .env file
load_dotenv()

def get_openai_client():
    """
    Creates and returns an OpenAI client with credentials from environment variables.

    Returns:
        OpenAIChatClient: Configured OpenAI client instance
    """
    client = OpenAIChatClient(
        api_key=os.getenv('API_KEY'),
        base_url=os.getenv('BASE_URL'),
        model_id=os.getenv('MODEL_ID')
    )
    return client

