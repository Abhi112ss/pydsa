METADATA = {
    "id": 1848,
    "name": "Minimum Distance to the Target Element",
    "slug": "minimum-distance-to-the-target-element",
    "category": "Array",
    "aliases": [],
    "tags": ["array", "two_pointer", "greedy"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Find the minimum absolute distance between a given index and any index containing the target value in an array.",
}

def solve(nums: list[int], index: int, target: int) -> int:
    """
    Finds the minimum distance between the given index and the nearest occurrence of target.

    Args:
        nums: A list of integers.
        index: The starting index to measure distance from.
        target: The integer value to search for.

    Returns:
        The minimum absolute distance to the target element.

    Examples:
        >>> solve([1, 2, 3, 4, 5], 3, 1)
        3
        >>> solve([1, 2, 3, 4, 5], 3, 5)
        1
        >>> solve([1, 2, 3, 4, 5], 3, 2)
        2
    """
    min_distance = float('inf')
    
    # Iterate through the array once to find all occurrences of target
    for current_index, value in enumerate(nums):
        if value == target:
            # Calculate absolute distance from the provided index
            current_distance = abs(current_index - index)
            
            # Update the minimum distance found so far
            if current_distance < min_distance:
                min_distance = current_distance
                
            # Optimization: If distance is 0, we found the exact index
            if min_distance == 0:
                return 0
                
    return int(min_distance)
