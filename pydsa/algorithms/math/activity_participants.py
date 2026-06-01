METADATA = {
    "id": 1355,
    "name": "Activity Participants",
    "slug": "activity-participants",
    "category": "SQL",
    "aliases": [],
    "tags": ["sql", "aggregation", "filtering"],
    "difficulty": "medium",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(n)",
    "description": "Identify activities that do not have the maximum or minimum number of participants.",
}

from collections import Counter

def solve(activities: list[dict[str, str]]) -> list[str]:
    """
    Identifies activities that do not have the maximum or minimum number of participants.

    Args:
        activities: A list of dictionaries where each dictionary represents an 
            entry with 'activity_name' and 'participant_name'.

    Returns:
        A list of activity names that are neither the most popular nor the least 
        popular (excluding ties for max/min).

    Examples:
        >>> data = [
        ...     {"activity_name": "Running", "participant_name": "Alice"},
        ...     {"activity_name": "Running", "participant_name": "Bob"},
        ...     {"activity_name": "Swimming", "participant_name": "Charlie"},
        ...     {"activity_name": "Swimming", "participant_name": "David"},
        ...     {"activity_name": "Swimming", "participant_name": "Eve"},
        ...     {"activity_name": "Yoga", "participant_name": "Frank"}
        ... ]
        >>> solve(data)
        ['Running']
    """
    if not activities:
        return []

    # Step 1: Aggregate counts per activity
    # We use a Counter to map activity names to their respective participant counts
    activity_counts = Counter()
    for entry in activities:
        activity_counts[entry["activity_name"]] += 1

    if not activity_counts:
        return []

    # Step 2: Find the global maximum and minimum participant counts
    # We extract all counts to determine the boundaries
    counts = list(activity_counts.values())
    max_count = max(counts)
    min_count = min(counts)

    # Step 3: Filter activities
    # An activity is included if its count is strictly between the min and max
    # Note: If all activities have the same count, max_count == min_count, 
    # and the result will correctly be an empty list.
    result = []
    for activity, count in activity_counts.items():
        if min_count < count < max_count:
            result.append(activity)

    # Sorting the result to ensure deterministic output (standard for LeetCode SQL results)
    return sorted(result)
