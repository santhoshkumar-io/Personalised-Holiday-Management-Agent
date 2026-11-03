from autogen_agentchat.conditions import MaxMessageTermination, TextMentionTermination


def get_termination_condition(mention_text: str = "TERMINATE", max_messages: int = 10):
    """
    Create the team's termination condition.

    The chat stops when any message contains `mention_text`, or after
    `max_messages` messages as a safety limit, whichever comes first.

    Args:
        mention_text (str): The text that, when mentioned, ends the conversation.
        max_messages (int): Hard upper limit on the number of messages.

    Returns:
        TerminationCondition: The combined termination condition.
    """
    return TextMentionTermination(mention_text) | MaxMessageTermination(max_messages)
