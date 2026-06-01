METADATA = {
    "id": 2391,
    "name": "Minimum Amount of Time to Collect Garbage",
    "slug": "minimum-amount-of-time-to-collect-garbage",
    "category": "Simulation",
    "aliases": [],
    "tags": ["greedy", "simulation"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Calculate the minimum time to collect all garbage by traveling from the first to the last garbage position and adding fixed collection time.",
}

def solve(garbage: list[str]) -> int:
    """
    Calculates the minimum time required to collect all garbage in a street.

    The total time consists of:
    1. The time taken to travel from the first garbage position to the last.
    2. The fixed time taken to collect each unit of garbage (1 minute per 'g').

    Args:
        garbage: A list of strings where each string represents a house. 
                 A house can contain 'g' (garbage) or '.' (empty).

    Returns:
        The minimum total time (travel time + collection time) as an integer.

    Examples:
        >>> solve(["g", ".", "g", ".", "g"])
        10
        >>> solve([".", "g", ".", "g", "."])
        7
    """
    total_collection_time = 0
    first_garbage_index = -1
    last_garbage_index = -1

    # Single pass to find the range of garbage and count total garbage units
    for index, house in enumerate(garbage):
        if house == "g":
            # Update the first occurrence found
            if first_garbage_index == -1:
                first_garbage_index = index
            
            # Continuously update the last occurrence found
            last_garbage_index = index
            
            # Each 'g' takes 1 minute to collect
            total_collection_time += 1

    # If no garbage is found, return 0
    if first_garbage_index == -1:
        return 0

    # Travel time is the distance between the first and last garbage positions
    travel_time = last_garbage_index - first_garbage_index

    return travel_time + total_collection_time
