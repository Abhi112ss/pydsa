METADATA = {
    "id": 1762,
    "name": "Buildings With an Ocean View",
    "slug": "buildings-with-an-ocean-view",
    "category": "Array",
    "aliases": [],
    "tags": ["monotonic_stack", "array", "greedy"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Find the indices of buildings that have an unobstructed view of the ocean to the right.",
}

def solve(heights: list[int]) -> list[int]:
    """
    Finds the indices of buildings that can see the ocean.
    A building has an ocean view if all buildings to its right are strictly shorter.

    Args:
        heights: A list of integers representing the heights of buildings.

    Returns:
        A list of indices of buildings that have an ocean view, sorted in ascending order.

    Examples:
        >>> solve([4, 2, 3, 1])
        [0, 2, 3]
        >>> solve([4, 3, 2, 1])
        [0, 1, 2, 3]
        >>> solve([1, 3, 2, 4])
        [3]
    """
    n = len(heights)
    ocean_view_indices = []
    max_height_to_right = -1

    # Iterate from right to left to keep track of the tallest building seen so far
    for i in range(n - 1, -1, -1):
        current_height = heights[i]
        
        # If the current building is taller than all buildings to its right, it has a view
        if current_height > max_height_to_right:
            ocean_view_indices.append(i)
            # Update the maximum height encountered so far
            max_height_to_right = current_height

    # Since we iterated backwards, the indices are collected in descending order
    # We reverse them to return the result in ascending order
    ocean_view_indices.reverse()
    return ocean_view_indices
