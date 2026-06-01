METADATA = {
    "id": 2456,
    "name": "Most Popular Video Creator",
    "slug": "most-popular-video-creator",
    "category": "Hash Table",
    "aliases": [],
    "tags": ["hash_map", "counting"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Find the creator ID that appears most frequently in a list of video IDs.",
}

def solve(video_ids: list[int]) -> int:
    """
    Finds the most popular video creator based on the frequency of their video IDs.

    Args:
        video_ids: A list of integers representing the video IDs of various creators.

    Returns:
        The creator ID (video ID) that appears most frequently.

    Examples:
        >>> solve([1, 2, 3, 1, 1])
        1
        >>> solve([1, 1, 2, 2, 2, 3])
        2
    """
    # Dictionary to store the frequency of each video ID
    counts: dict[int, int] = {}
    
    # Track the current maximum frequency and the corresponding ID
    max_count: int = 0
    popular_creator: int = -1

    for video_id in video_ids:
        # Increment the count for the current video_id
        counts[video_id] = counts.get(video_id, 0) + 1
        
        # Update the most popular creator if the current count exceeds the max_count
        if counts[video_id] > max_count:
            max_count = counts[video_id]
            popular_creator = video_id
            
    return popular_creator
