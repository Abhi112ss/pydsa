METADATA = {
    "id": 1369,
    "name": "Get the Second Most Recent Activity",
    "slug": "get-the-second-most-recent-activity",
    "category": "Sorting",
    "aliases": [],
    "tags": ["sorting", "hash_map"],
    "difficulty": "easy",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(n)",
    "description": "Retrieve the activity with the second largest timestamp from a list of activity records.",
}

from typing import Optional, Any


def solve(activities: list[dict[str, Any]]) -> Optional[dict[str, Any]]:
    """
    Retrieves the activity record with the second largest timestamp.

    Args:
        activities: A list of dictionaries, where each dictionary represents 
            an activity and contains at least a 'timestamp' key.

    Returns:
        The dictionary representing the second most recent activity, 
        or None if there are fewer than two activities.

    Examples:
        >>> solve([{"id": 1, "timestamp": 10}, {"id": 2, "timestamp": 30}, {"id": 3, "timestamp": 20}])
        {'id': 3, 'timestamp': 20}
        >>> solve([{"id": 1, "timestamp": 10}])
        None
    """
    # If there are fewer than 2 activities, a second most recent cannot exist
    if len(activities) < 2:
        return None

    # Sort the activities based on the 'timestamp' key in descending order
    # This places the most recent activity at index 0 and the second most recent at index 1
    sorted_activities = sorted(activities, key=lambda x: x["timestamp"], reverse=True)

    # Return the second element in the sorted list
    return sorted_activities[1]
