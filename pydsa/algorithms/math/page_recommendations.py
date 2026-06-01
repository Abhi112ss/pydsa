METADATA = {
    "id": 1264,
    "name": "Page Recommendations",
    "slug": "page-recommendations",
    "category": "Hash Table",
    "aliases": [],
    "tags": ["hash_set", "logic", "array", "hash table"],
    "difficulty": "medium",
    "time_complexity": "O(N + M)",
    "space_complexity": "O(N + M)",
    "description": "Recommend pages to a user based on their friends' likes, excluding pages the user has already seen.",
}

def solve(friends: list[list[int]], user_likes: list[list[int]], target_user: int) -> list[list[int]]:
    """
    Recommends pages to a target user based on the pages liked by their friends.
    
    A page is recommended if:
    1. It is liked by at least one friend of the target user.
    2. It has not been liked by the target user themselves.
    3. It is among the top 2 most frequently liked pages by the target user's friends.
    4. In case of a tie in frequency, the page with the smaller ID is preferred.

    Args:
        friends: A list of lists where friends[i] contains the IDs of friends of user i.
        user_likes: A list of lists where user_likes[i] contains the IDs of pages liked by user i.
        target_user: The ID of the user for whom to generate recommendations.

    Returns:
        A list of lists, where each inner list contains up to 2 recommended page IDs.

    Examples:
        >>> friends = [[1, 2], [0], [0]]
        >>> user_likes = [[1, 2], [1], [2]]
        >>> target_user = 0
        >>> solve(friends, user_likes, target_user)
        [[1, 2]]
    """
    # Convert user's own likes to a set for O(1) lookup
    user_seen_pages = set(user_likes[target_user])
    
    # Dictionary to count frequency of pages liked by friends
    friend_page_counts: dict[int, int] = {}
    
    # Identify all friends of the target user
    target_friends = friends[target_user]
    
    for friend_id in target_friends:
        # Iterate through pages liked by each friend
        for page_id in user_likes[friend_id]:
            # Only consider pages the target user hasn't liked yet
            if page_id not in user_seen_pages:
                friend_page_counts[page_id] = friend_page_counts.get(page_id, 0) + 1
                
    # Sort the candidate pages:
    # 1. Primary key: frequency (descending, hence -count)
    # 2. Secondary key: page ID (ascending)
    # This handles the tie-breaking rule automatically
    recommended_pages = sorted(
        friend_page_counts.keys(),
        key=lambda page_id: (-friend_page_counts[page_id], page_id)
    )
    
    # Return the top 2 recommendations
    return [recommended_pages[:2]]
