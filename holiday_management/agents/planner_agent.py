from autogen_agentchat.agents import AssistantAgent
from holiday_management.models.gpt_model import model_client

planner = AssistantAgent(
    name="Holiday_Planner",
    description="An AI assistant that helps users plan their holidays based on user preferences.",
    model_client=model_client,
    system_message="You are a helpful assistant that helps users plan their holidays. You can provide suggestions for destinations, activities, and itineraries based on user preferences. Once the researcher has shared their findings and you have produced the final itinerary, end your message with the word TERMINATE."

)