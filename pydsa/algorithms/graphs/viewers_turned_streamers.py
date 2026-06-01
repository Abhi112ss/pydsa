METADATA = {
    "id": 2995,
    "name": "Viewers Turned Streamers",
    "slug": "viewers_turned_streamers",
    "category": "Hash Table",
    "aliases": [],
    "tags": ["hash_map", "set_operations"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Find the number of users who appear in both the viewers and streamers lists.",
}

def solve(viewers: list[int], streamers: list[int]) -> int:
    """
    Calculates the number of unique users who are present in both the 
    viewers list and the streamers list.

    Args:
        viewers: A list of integers representing user IDs who viewed.
        streamers: A list of integers representing user IDs who streamed.

    Returns:
        The count of users present in both lists.

    Examples:
        >>> solve([1, 2, 3], [2, 3, 4])
        2
        >>> solve([1, 1, 1], [1, 2, 3])
        1
        >>> solve([1, 2], [3, 4])
        0
    """
    # Convert lists to sets to handle duplicates and allow O(1) average lookup
    viewer_set = set(viewers)
    streamer_set = set(streamers)

    # Find the intersection of the two sets to identify common users
    # The intersection operation in Python is highly optimized
    common_users = viewer_set.intersection(streamer_set)

    return len(common_users)
