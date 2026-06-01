METADATA = {
    "id": 1243,
    "name": "Array Transformation",
    "slug": "array-transformation",
    "category": "Simulation",
    "aliases": [],
    "tags": ["simulation", "iteration"],
    "difficulty": "medium",
    "time_complexity": "O(n * max_val)",
    "space_complexity": "O(n)",
    "description": "Transform an array by replacing each element with the count of elements in the previous state that are strictly greater than it, until no changes occur.",
}

def solve(start_array: list[int]) -> int:
    """
    Simulates the array transformation process and returns the number of steps taken.

    The transformation rule: Each element in the new array is the count of elements 
    in the current array that are strictly greater than the current element.
    The process stops when the array remains unchanged.

    Args:
        start_array: A list of integers representing the initial state.

    Returns:
        The total number of transformation steps performed.

    Examples:
        >>> solve([3, 4, 3])
        1
        >>> solve([1, 1, 3, 5])
        2
        >>> solve([0, 4, 2, 1])
        1
    """
    current_array = list(start_array)
    steps = 0
    n = len(current_array)

    while True:
        # Create a new array to store the results of this transformation step
        # This ensures we use the 'previous state' for all calculations
        next_array = [0] * n
        
        # For each element, count how many elements in the current array are greater
        for i in range(n):
            count_greater = 0
            for j in range(n):
                if current_array[j] > current_array[i]:
                    count_greater += 1
            next_array[i] = count_greater

        # If the array hasn't changed, the transformation is complete
        if next_array == current_array:
            break
        
        # Update the current state and increment the step counter
        current_array = next_array
        steps += 1

    return steps
