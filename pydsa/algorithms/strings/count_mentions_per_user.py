METADATA = {
    "id": 3433,
    "name": "Count Mentions Per User",
    "slug": "count-mentions-per-user",
    "category": "Hash Table",
    "aliases": [],
    "tags": ["hash_map", "string", "counting"],
    "difficulty": "easy",
    "time_complexity": "O(n + m)",
    "space_complexity": "O(m)",
    "description": "Count how many times each user is mentioned across a list of messages.",
}

def solve(messages: list[str], users: list[int]) -> list[int]:
    """
    Counts the number of times each user ID appears in the given messages.

    Args:
        messages: A list of strings where each string contains space-separated 
            integers representing user IDs.
        users: A list of user IDs for which we need to count mentions.

    Returns:
        A list of integers where the i-th element is the number of times 
        users[i] was mentioned in the messages.

    Examples:
        >>> solve(["1 2 3", "2 3 4", "1 5"], [1, 2, 3])
        [2, 2, 2]
        >>> solve(["1 1 1", "2 2", "3"], [1, 2, 3, 4])
        [3, 2, 1, 0]
    """
    mention_counts: dict[int, int] = {}

    # Iterate through each message and split by whitespace to find user IDs
    for message in messages:
        # Split the message into individual tokens (user IDs)
        tokens = message.split()
        for token in tokens:
            user_id = int(token)
            # Increment the count for the specific user ID in the hash map
            mention_counts[user_id] = mention_counts.get(user_id, 0) + 1

    # Construct the result list based on the order of the input users list
    result: list[int] = []
    for user_id in users:
        # If the user was never mentioned, the count is 0
        result.append(mention_counts.get(user_id, 0))

    return result
