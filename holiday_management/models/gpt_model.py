from autogen_ext.models.openai import OpenAIChatCompletionClient
from holiday_management.config.settings import OPENAI_API_KEY, MODEL_NAME

model_client = OpenAIChatCompletionClient(
    model=MODEL_NAME,
    api_key=OPENAI_API_KEY
)
