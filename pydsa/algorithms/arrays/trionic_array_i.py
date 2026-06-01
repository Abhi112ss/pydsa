METADATA = {
    "id": 3637,
    "name": "Trionic Array I",
    "slug": "trionic_array_i",
    "category": "Arrays",
    "aliases": [],
    "tags": ["arrays", "pattern_matching", "linear_scan"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Determine if an array follows a trionic pattern of alternating increasing and decreasing segments.",
}

def solve(nums: list[int]) -> bool:
    """
    Determines if the given array follows a trionic pattern.
    A trionic array is defined as an array that changes direction exactly twice:
    once from increasing to decreasing, and once from decreasing to increasing.

    Args:
        nums: A list of integers to evaluate.

    Returns:
        True if the array follows the trionic pattern, False otherwise.

    Examples:
        >>> solve([1, 3, 5, 4, 2, 3, 6])
        True
        >>> solve([1, 2, 3, 4, 5])
        False
        >>> solve([5, 4, 2, 3, 6, 5, 1])
        True
    """
    n = len(nums)
    if n < 4:
        return False

    # direction: 0 = unknown, 1 = increasing, -1 = decreasing
    current_direction = 0
    direction_changes = 0

    for i in range(1, n):
        if nums[i] > nums[i - 1]:
            new_direction = 1
        elif nums[i] < nums[i - 1]:
            new_direction = -1
        else:
            # If elements are equal, it breaks the strict trionic pattern
            return False

        if current_direction == 0:
            # Initialize the first direction
            current_direction = new_direction
        elif new_direction != current_direction:
            # A change in direction has occurred
            direction_changes += 1
            current_direction = new_direction
            
            # Optimization: if we exceed 2 changes, it's not trionic
            if direction_changes > 2:
                return False

    # A trionic array must have exactly 2 direction changes
    # (e.g., Up -> Down -> Up OR Down -> Up -> Down)
    return direction_changes == 2
