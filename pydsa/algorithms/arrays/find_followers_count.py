METADATA = {
    "id": 1729,
    "name": "Find Followers Count",
    "slug": "find_followers_count",
    "category": "Hash Table",
    "aliases": [],
    "tags": ["hash_map"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Count how many followers each user has from a list of follow relationships.",
}


def solve(follow_relationships: list[list[int]]) -> list[list[int]]:
    """Count followers for each user.

    Args:
        follow_relationships: A list where each element is a two‑element list
            [follower_id, followee_id] representing that `follower_id` follows
            `followee_id`.

    Returns:
        A list of two‑element lists [user_id, follower_count] for every user
        that is followed, sorted by `user_id` in ascending order.

    Examples:
        >>> solve([[1, 2], [3, 2], [4, 5]])
        [[2, 2], [5, 1]]
        >>> solve([])
        []
    """
    # Hash map: key = followee_id, value = number of followers
    follower_counts: dict[int, int] = {}

    for relationship in follow_relationships:
        # Each relationship is guaranteed to have exactly two integers
        followee_id = relationship[1]
        if followee_id in follower_counts:
            follower_counts[followee_id] += 1
        else:
            follower_counts[followee_id] = 1

    # Build result list sorted by user id (followee_id)
    result: list[list[int]] = [
        [user_id, count] for user_id, count in sorted(follower_counts.items())
    ]
    return result