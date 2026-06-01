METADATA = {
    "id": 1488,
    "name": "Avoid Flood in The City",
    "slug": "avoid-flood-in-the-city",
    "category": "Greedy",
    "aliases": [],
    "tags": ["greedy", "binary_search", "hash_table"],
    "difficulty": "medium",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(n)",
    "description": "Determine if it is possible to avoid flooding lakes by strategically using dry days to empty them.",
}

import bisect

def solve(rains: list[int]) -> list[int]:
    """
    Determines a sequence of lake drying actions to avoid flooding.

    The algorithm uses a greedy approach with binary search. We track the last 
    day each lake was filled. When a lake is encountered that is already full, 
    we look for the earliest available dry day (a day where rains[i] == 0) 
    that occurred after the lake was last filled.

    Args:
        rains: A list of integers where rains[i] > 0 represents a lake index 
               being filled, and rains[i] == 0 represents a dry day.

    Returns:
        A list of integers representing the action taken on each day. 
        If rains[i] > 0, result[i] = -1. 
        If rains[i] == 0, result[i] is the lake index to dry, or 1 if no lake is dried.
        If flooding is unavoidable, returns an empty list [].

    Examples:
        >>> solve([1, 2, 0, 1, 2])
        [-1, -1, 1, -1, -1]
        >>> solve([1, 2, 0, 0])
        [-1, -1, 1, 2]
        >>> solve([1, 2, 0, 1, 2]) # (Wait, example 1 is actually [-1, -1, 1, -1, -1])
        >>> solve([1, 2, 0, 1, 2])
        [-1, -1, 1, -1, -1]
        >>> solve([1, 2, 0, 0, 1, 2])
        [-1, -1, 1, 2, -1, -1]
    """
    n = len(rains)
    ans = [-1] * n
    # Stores indices of days where rains[i] == 0
    dry_days = []
    # Maps lake_id -> the index of the day it was last filled
    last_filled_day = {}

    for i, lake in enumerate(rains):
        if lake == 0:
            # Mark this as a potential day to dry a lake
            dry_days.append(i)
            # Default action for a dry day is to dry lake 1 (per problem spec)
            ans[i] = 1
        else:
            if lake in last_filled_day:
                # Lake is already full, we must have used a dry day since last_filled_day[lake]
                prev_day = last_filled_day[lake]
                
                # Find the first available dry day after the lake was last filled
                # bisect_right finds the insertion point for prev_day to maintain order
                idx = bisect.bisect_right(dry_days, prev_day)
                
                if idx < len(dry_days):
                    # We found a valid dry day to empty this lake
                    dry_day_index = dry_days.pop(idx)
                    ans[dry_day_index] = lake
                else:
                    # No dry days available between the two fills
                    return []
            
            # Update the last time this lake was filled
            last_filled_day[lake] = i

    return ans
