METADATA = {
    "id": 881,
    "name": "Boats to Save People",
    "slug": "boats-to-save-people",
    "category": "Greedy",
    "aliases": [],
    "tags": ["two_pointer", "sorting", "greedy"],
    "difficulty": "medium",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(1)",
    "description": "Find the minimum number of boats required to carry all people given a weight limit per boat, where each boat can carry at most two people.",
}

def solve(people: list[int], limit: int) -> int:
    """
    Calculates the minimum number of boats required to carry all people.
    
    Each boat has a weight limit and can carry at most two people at a time.
    The strategy is to use a greedy approach with two pointers: try to pair 
    the heaviest person with the lightest person.

    Args:
        people: A list of integers representing the weight of each person.
        limit: An integer representing the maximum weight capacity of a single boat.

    Returns:
        The minimum number of boats needed to carry everyone.

    Examples:
        >>> solve([3, 2, 2, 1], 3)
        3
        >>> solve([3, 5, 3, 4], 5)
        4
    """
    # Sort people by weight to allow two-pointer approach
    people.sort()
    
    left_index = 0
    right_index = len(people) - 1
    boats_count = 0
    
    while left_index <= right_index:
        # If the lightest person and the heaviest person can fit together
        if people[left_index] + people[right_index] <= limit:
            # Move the left pointer to include the lightest person in this boat
            left_index += 1
            
        # The heaviest person is always accounted for in this boat
        # (either alone or paired with the lightest)
        right_index -= 1
        
        # Increment the boat count for every iteration
        boats_count += 1
        
    return boats_count
