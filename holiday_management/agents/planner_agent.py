from autogen_agentchat.agents import AssistantAgent
from holiday_management.models.gpt_model import model_client

planner = AssistantAgent(
    name="Holiday Planner",
    description="An AI assistant that helps users plan their holidays based on user preferences.",
    model_client=model_client,
    system_message="You are a helpful assistant that helps users plan their holidays. You can provide suggestions for destinations, activities, and iternaries based on user preferences."

)