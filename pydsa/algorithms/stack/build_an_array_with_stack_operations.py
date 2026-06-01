METADATA = {
    "id": 1441,
    "name": "Build an Array With Stack Operations",
    "slug": "build-an-array-with-stack-operations",
    "category": "Simulation",
    "aliases": [],
    "tags": ["stack", "simulation", "array"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Construct a target array using stack operations (push and pop) from a stream of integers starting from 1.",
}

def solve(target: list[int]) -> list[list[str]]:
    """
    Simulates the process of building a target array using stack operations.

    Args:
        target: A list of integers representing the desired final array.

    Returns:
        A list of lists, where each inner list contains the sequence of 
        operations ('Push' or 'Pop') performed to reach the target.

    Examples:
        >>> solve([1, 3])
        [['Push', 'Pop', 'Push']]
        >>> solve([1, 2, 3, 4])
        [['Push', 'Push', 'Push', 'Push']]
    """
    operations = []
    current_stream_value = 1
    target_index = 0
    target_length = len(target)

    # Iterate until we have successfully built the entire target array
    while target_index < target_length:
        # Every number in the stream must be 'pushed' to be considered
        operations.append("Push")
        
        # If the current stream value matches the target value, move to next target
        if current_stream_value == target[target_index]:
            target_index += 1
        else:
            # If it doesn't match, it must be 'popped' immediately to remove it
            operations.append("Pop")
        
        # Increment the stream value for the next iteration
        current_stream_value += 1

    return operations
