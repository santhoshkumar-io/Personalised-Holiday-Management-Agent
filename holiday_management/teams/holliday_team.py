from autogen_agentchat.teams import RoundRobinGroupChat
from holiday_management.agents.planner_agent import planner
from holiday_management.agents.researcher_agent import researcher
from holiday_management.utils.utils import get_termination_condition

team = RoundRobinGroupChat(
    participants=[planner, researcher],
    termination_condition=get_termination_condition()
)