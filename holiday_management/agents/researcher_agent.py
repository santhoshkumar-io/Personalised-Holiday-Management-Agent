from autogen_agentchat.agents import AssistantAgent
from holiday_management.models.gpt_model import model_client

researcher = AssistantAgent(
    name="Holiday_Researcher",
    description="An AI assistant that helps users research their holidays based on user preferred destinations.",
    model_client=model_client,
    system_message="You are a helpful researcher agent. You task is to help users research their holidays. You can provide suggestions for destinations, activities, and iternaries based on user preferences."
)