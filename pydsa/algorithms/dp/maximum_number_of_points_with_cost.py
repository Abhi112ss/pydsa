METADATA = {
    "id": 1937,
    "name": "Maximum Number of Points with Cost",
    "slug": "maximum-number-of-points-with-cost",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dp", "arrays"],
    "difficulty": "hard",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Calculate the maximum points reachable at each index considering costs to move left or right.",
}

def solve(points: list[int], max_cost: int) -> list[int]:
    """
    Calculates the maximum points reachable at each index given a budget.

    Args:
        points: A list of integers representing the points at each index.
        max_cost: An integer representing the maximum total cost allowed.

    Returns:
        A list of integers where each element at index i is the maximum points 
        attainable at index i within the max_cost constraint.

    Examples:
        >>> solve([1, 1, 1, 1], 2)
        [3, 3, 3, 3]
        >>> solve([1, 1, 1, 1], 0)
        [1, 1, 1, 1]
        >>> solve([1, 2, 3, 4], 1)
        [1, 3, 4, 4]
    """
    n = len(points)
    left_max = [0] * n
    right_max = [0] * n

    # Pass 1: Left-to-right
    # Calculate the maximum points reachable at index i by moving only left.
    # We use a sliding window/two-pointer approach to maintain the sum of points
    # within the allowed cost range [i - max_cost, i].
    current_left_sum = 0
    left_pointer = 0
    for right_pointer in range(n):
        current_left_sum += points[right_pointer]
        
        # If the distance exceeds max_cost, shrink the window from the left
        while right_pointer - left_pointer > max_cost:
            current_left_sum -= points[left_pointer]
            left_pointer += 1
        
        left_max[right_pointer] = current_left_sum

    # Pass 2: Right-to-left
    # Calculate the maximum points reachable at index i by moving only right.
    # We use a sliding window to maintain the sum of points
    # within the allowed cost range [i, i + max_cost].
    current_right_sum = 0
    right_pointer = n - 1
    for left_pointer in range(n - 1, -1, -1):
        current_right_sum += points[left_pointer]
        
        # If the distance exceeds max_cost, shrink the window from the right
        while right_pointer - left_pointer > max_cost:
            current_right_sum -= points[right_pointer]
            right_pointer -= 1
            
        right_max[left_pointer] = current_right_sum

    # Combine results: The max points at index i is the sum of points 
    # reachable to the left and points reachable to the right, 
    # minus the point at index i (since it's counted in both passes).
    result = []
    for i in range(n):
        result.append(left_max[i] + right_max[i] - points[i])

    return result
