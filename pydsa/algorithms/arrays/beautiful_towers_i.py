METADATA = {
    "id": 2865,
    "name": "Beautiful Towers I",
    "slug": "beautiful-towers-i",
    "category": "Array",
    "aliases": [],
    "tags": ["arrays", "greedy"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Count the number of beautiful towers where all elements are equal and the tower is non-empty.",
}

def solve(heights: list[int]) -> int:
    """
    Args:
        heights: A list of integers representing the heights of the tower.

    Returns:
        The total number of beautiful towers.
    """
    total_beautiful_towers = 0
    n = len(heights)
    current_run_length = 0
    previous_height = -1

    for i in range(n):
        if heights[i] == previous_height:
            current_run_length += 1
        else:
            current_run_length = 1
            previous_height = heights[i]
        
        total_beautiful_towers += current_run_length

    return total_beautiful_towers