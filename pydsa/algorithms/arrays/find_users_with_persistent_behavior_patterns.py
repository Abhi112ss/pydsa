METADATA = {
    "id": 3832,
    "name": "Find Users with Persistent Behavior Patterns",
    "slug": "find-users-with-persistent-behavior-patterns",
    "category": "Hash Table",
    "aliases": [],
    "tags": ["hash_map", "arrays", "string"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Identify users who exhibit a specific repeating sequence of actions within their activity logs.",
}

def solve(user_logs: list[list[str]], target_pattern: str) -> list[int]:
    """
    Identifies users whose action sequences contain the target pattern as a substring.

    Args:
        user_logs: A list of lists, where each inner list contains strings 
            representing the sequence of actions performed by a specific user.
            The index of the inner list corresponds to the user ID.
        target_pattern: A string representing the specific sequence of actions 
            to look for.

    Returns:
        A list of user IDs (indices) who have the target pattern in their logs.

    Examples:
        >>> solve([["a", "b", "c", "a", "b"], ["a", "c", "b"], ["a", "b"]], "ab")
        [0, 2]
        >>> solve([["x", "y", "z"], ["y", "z", "x"], ["z", "x", "y"]], "xyz")
        [0]
    """
    persistent_users = []
    pattern_length = len(target_pattern)

    for user_id, actions in enumerate(user_logs):
        # Convert the list of actions into a single string for efficient substring searching
        # We use a delimiter to ensure that actions like 'a' and 'b' don't merge 
        # incorrectly if actions were multi-character, though here they are single chars.
        # For standard LeetCode string pattern matching, joining is O(N).
        user_sequence = "".join(actions)
        
        # Check if the target pattern exists within the user's action sequence
        if target_pattern in user_sequence:
            persistent_users.append(user_id)

    return persistent_users
