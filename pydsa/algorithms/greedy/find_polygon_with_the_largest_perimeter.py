METADATA = {
    "id": 2971,
    "name": "Find Polygon With the Largest Perimeter",
    "slug": "find-polygon-with-the-largest-perimeter",
    "category": "Greedy",
    "aliases": [],
    "tags": ["greedy", "sorting"],
    "difficulty": "medium",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(1)",
    "description": "Find the largest perimeter of a polygon that can be formed using a subset of the given side lengths.",
}

def solve(dimensions: list[int]) -> int:
    """
    Finds the largest perimeter of a polygon that can be formed using a subset 
    of the given side lengths. A polygon can be formed if the longest side 
    is strictly less than the sum of all other sides.

    Args:
        dimensions: A list of integers representing the lengths of available sides.

    Returns:
        The largest possible perimeter of a valid polygon, or -1 if no polygon can be formed.

    Examples:
        >>> solve([3, 2, 3, 4, 1])
        12
        >>> solve([1, 2, 1])
        -1
        >>> solve([1, 1, 1, 1])
        4
    """
    # Sort dimensions in ascending order to easily calculate prefix sums
    # or to check the polygon inequality condition efficiently.
    dimensions.sort()
    n = len(dimensions)
    
    # Calculate the total sum of all sides initially.
    # We want to find the largest subset, so we start with all sides.
    total_sum = sum(dimensions)
    
    # Iterate from the largest side downwards.
    # If the current largest side is less than the sum of all other sides,
    # we have found the largest possible perimeter.
    for i in range(n - 1, 1, -1):
        longest_side = dimensions[i]
        sum_of_others = total_sum - longest_side
        
        # The polygon inequality theorem: longest side < sum of all other sides.
        if longest_side < sum_of_others:
            return total_sum
        
        # If the condition is not met, this longest side cannot be part of a 
        # valid polygon using the current set of sides. Remove it and try the next.
        total_sum -= longest_side
        
    return -1
