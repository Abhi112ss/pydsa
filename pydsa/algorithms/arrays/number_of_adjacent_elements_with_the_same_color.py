METADATA = {
    "id": 2672,
    "name": "Number of Adjacent Elements With the Same Color",
    "slug": "number-of-adjacent-elements-with-the-same-color",
    "category": "Array",
    "aliases": [],
    "tags": ["array", "sliding_window"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Count the number of adjacent elements in an array that have the same color.",
}

def solve(colors: list[int]) -> int:
    """
    Counts how many adjacent elements in the colors array have the same value.

    Args:
        colors: A list of integers representing the colors of adjacent elements.

    Returns:
        The total count of adjacent pairs that share the same color.

    Examples:
        >>> solve([1, 2, 3, 4, 5])
        0
        >>> solve([1, 1, 2, 2, 3, 3])
        3
        >>> solve([1, 1, 1, 1])
        3
    """
    adjacent_matches = 0
    
    # Iterate from the first element to the second-to-last element
    for index in range(len(colors) - 1):
        # Compare the current element with the next one
        if colors[index] == colors[index + 1]:
            adjacent_matches += 1
            
    return adjacent_matches
