METADATA = {
    "id": 256,
    "name": "Paint House",
    "slug": "paint-house",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dynamic_programming", "array"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Find the minimum cost to paint n houses such that no two adjacent houses have the same color.",
}

def solve(costs: list[list[int]]) -> int:
    """
    Calculates the minimum cost to paint all houses such that no two adjacent 
    houses have the same color using dynamic programming.

    Args:
        costs: A list of lists where costs[i][j] is the cost of painting 
               house i with color j (0, 1, or 2).

    Returns:
        The minimum total cost to paint all houses.

    Examples:
        >>> solve([[17, 2, 17], [16, 16, 5], [14, 3, 19]])
        10
        >>> solve([[1, 1, 1], [1, 1, 1], [1, 1, 1]])
        3
    """
    if not costs:
        return 0

    # We use three variables to track the minimum cost to paint the 
    # current house with color 0, 1, or 2. This allows O(1) space.
    prev_red, prev_blue, prev_green = costs[0]

    for i in range(1, len(costs)):
        # For the current house, the cost of choosing a color is the 
        # current color's cost plus the minimum cost of the previous 
        # house using a DIFFERENT color.
        curr_red = costs[i][0] + min(prev_blue, prev_green)
        curr_blue = costs[i][1] + min(prev_red, prev_green)
        curr_green = costs[i][2] + min(prev_red, prev_blue)

        # Update previous values for the next iteration
        prev_red, prev_blue, prev_green = curr_red, curr_blue, curr_green

    # The answer is the minimum of the three possible final color choices
    return min(prev_red, prev_blue, prev_green)
