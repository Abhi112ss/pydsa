METADATA = {
    "id": 1204,
    "name": "Last Person to Fit in the Bus",
    "slug": "last-person-to-fit-in-the-bus",
    "category": "Database/Algorithm",
    "aliases": [],
    "tags": ["prefix_sum", "sorting"],
    "difficulty": "medium",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(n)",
    "description": "Find the ID of the last person who can board the bus without exceeding the weight limit.",
}

def solve(people: list[list[int]], weight_limit: int) -> int:
    """
    Finds the ID of the last person who can board the bus without exceeding the weight limit.

    Args:
        people: A list of lists where each sub-list contains [id, weight].
        weight_limit: The maximum weight capacity of the bus.

    Returns:
        The ID of the last person who can fit in the bus. Returns 0 if no one can fit.

    Examples:
        >>> solve([[1, 10], [2, 20], [3, 30]], 50)
        2
        >>> solve([[7, 10], [4, 20], [5, 30], [6, 40]], 100)
        5
    """
    # Sort people by their weight (the second element in the sub-list)
    # Note: In the SQL version, the 'turn' is the weight. 
    # We assume the input 'people' is already ordered by the boarding sequence.
    # If the input represents (id, weight) and weight is the turn:
    sorted_people = sorted(people, key=lambda x: x[1])
    
    current_weight_sum = 0
    last_person_id = 0
    
    for person_id, weight in sorted_people:
        # Check if adding the next person exceeds the limit
        if current_weight_sum + weight <= weight_limit:
            current_weight_sum += weight
            last_person_id = person_id
        else:
            # Once the limit is exceeded, stop processing
            break
            
    return last_person_id
