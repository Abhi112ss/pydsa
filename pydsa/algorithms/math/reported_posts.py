METADATA = {
    "id": 1113,
    "name": "Reported Posts",
    "slug": "reported_posts",
    "category": "Hash Table",
    "aliases": [],
    "tags": ["hash_map", "arrays", "filtering"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Count unique post IDs reported for each reason within a specific time range.",
}

def solve(reports: list[dict], start_date: int, end_date: int) -> dict[str, int]:
    """
    Counts the number of unique post IDs reported for each reason within a given date range.

    Args:
        reports: A list of dictionaries, where each dictionary contains:
            - 'post_id' (int): The ID of the post.
            - 'reason' (str): The reason for the report.
            - 'timestamp' (int): The time the report was made.
        start_date: The inclusive start of the time range.
        end_date: The inclusive end of the time range.

    Returns:
        A dictionary where keys are report reasons and values are the count of 
        unique post IDs associated with that reason within the time range.

    Examples:
        >>> reports = [
        ...     {"post_id": 1, "reason": "spam", "timestamp": 10},
        ...     {"post_id": 1, "reason": "spam", "timestamp": 15},
        ...     {"post_id": 2, "reason": "spam", "timestamp": 20},
        ...     {"post_id": 3, "reason": "harassment", "timestamp": 15}
        ... ]
        >>> solve(reports, 10, 20)
        {'spam': 2, 'harassment': 1}
    """
    # Map each reason to a set of unique post IDs to handle duplicates automatically
    reason_to_unique_posts: dict[str, set[int]] = {}

    for report in reports:
        timestamp = report["timestamp"]
        
        # Filter reports based on the provided time window [start_date, end_date]
        if start_date <= timestamp <= end_date:
            reason = report["reason"]
            post_id = report["post_id"]
            
            if reason not in reason_to_unique_posts:
                reason_to_unique_posts[reason] = set()
            
            # Adding to a set ensures we only count unique post IDs per reason
            reason_to_unique_posts[reason].add(post_id)

    # Convert the sets of unique IDs into their respective counts
    return {reason: len(post_ids) for reason, post_ids in reason_to_unique_posts.items()}
