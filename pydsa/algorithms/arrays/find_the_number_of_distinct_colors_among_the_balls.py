METADATA = {
    "id": 3160,
    "name": "Find the Number of Distinct Colors Among the Balls",
    "slug": "find-the-number-of-distinct-colors-among-the-balls",
    "category": "Hash Table",
    "aliases": [],
    "tags": ["arrays", "hash_map"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Calculate the number of distinct colors present in a collection of balls after several additions.",
}

def solve(colors: list[int], queries: list[list[int]]) -> list[int]:
    """
    Calculates the number of distinct colors in the balls array after each query.

    Args:
        colors: A list of integers representing the initial colors of the balls.
        queries: A list of queries where each query is [index, color].

    Returns:
        A list of integers representing the count of distinct colors after each query.

    Examples:
        >>> solve([1, 2, 3], [[0, 1], [1, 2]])
        [3, 3]
        >>> solve([1, 1, 2], [[1, 2]])
        [2]
    """
    # Use a dictionary to track the frequency of each color currently in the balls
    color_counts: dict[int, int] = {}
    
    # Initialize the frequency map with the starting colors
    for color in colors:
        color_counts[color] = color_counts.get(color, 0) + 1
        
    results: list[int] = []
    
    for index, new_color in queries:
        old_color = colors[index]
        
        # If the new color is different from the existing color at that index
        if old_color != new_color:
            # Decrement the count of the old color
            color_counts[old_color] -= 1
            # If the old color is no longer present, remove it from the map
            if color_counts[old_color] == 0:
                del color_counts[old_color]
            
            # Increment the count of the new color
            color_counts[new_color] = color_counts.get(new_color, 0) + 1
            
            # Update the balls array to reflect the change
            colors[index] = new_color
            
        # The number of distinct colors is simply the number of keys in our map
        results.append(len(color_counts))
        
    return results
