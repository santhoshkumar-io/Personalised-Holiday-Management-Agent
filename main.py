from autogen_agentchat.messages import TextMessage
from holiday_management.teams.holliday_team import team
import asyncio

async def main():
    message = TextMessage(
        content="Hello! I am planning a holiday for a week with my friends to nagaland. Can you help me with the planning and research for the same?",
        source="User"
    )
    response = await team.run(task = message)    

    for msg in response.messages:
        print(f"{msg.source}: {msg.content}")


if __name__ == "__main__":
    asyncio.run(main())
