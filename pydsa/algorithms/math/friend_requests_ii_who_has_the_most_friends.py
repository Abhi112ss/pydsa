METADATA = {
    "id": 602,
    "name": "Friend Requests II: Who Has the Most Friends",
    "slug": "friend-requests-ii-who-has-the-most-friends",
    "category": "Hash Table",
    "aliases": [],
    "tags": ["hash_map", "counting"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Find the user ID that appears most frequently in a list of friend request pairs.",
}

def solve(friendships: list[list[int]]) -> int:
    """
    Finds the user ID that has the most friends based on a list of friendship pairs.

    Args:
        friendships: A list of pairs where each pair [a, b] represents a friendship 
            between user a and user b.

    Returns:
        The ID of the user with the maximum number of friends. If there is a tie, 
        the smallest ID is returned.

    Examples:
        >>> solve([[1, 2], [2, 3], [3, 4]])
        2
        >>> solve([[1, 1], [2, 2]])
        1
        >>> solve([[1, 2], [2, 3], [3, 1], [4, 5]])
        1
    """
    if not friendships:
        return 0

    friend_counts: dict[int, int] = {}

    # Iterate through each friendship pair
    for user_a, user_b in friendships:
        # Increment count for both users in the pair
        # Note: If user_a == user_b, we only count them once to represent 
        # the person's presence in the friendship list, though the problem 
        # constraints usually imply distinct users.
        friend_counts[user_a] = friend_counts.get(user_a, 0) + 1
        
        # Only increment the second user if they are different from the first
        # to avoid double counting a self-loop as two friends.
        if user_a != user_b:
            friend_counts[user_b] = friend_counts.get(user_b, 0) + 1

    max_friends = -1
    result_user_id = float('inf')

    # Find the user with the maximum count. 
    # In case of a tie, pick the smallest user ID.
    for user_id, count in friend_counts.items():
        if count > max_friends:
            max_friends = count
            result_user_id = user_id
        elif count == max_friends:
            if user_id < result_user_id:
                result_user_id = user_id

    return int(result_user_id)
