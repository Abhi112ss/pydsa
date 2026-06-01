METADATA = {
    "id": 265,
    "name": "Paint House II",
    "slug": "paint-house-ii",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dynamic programming", "array"],
    "difficulty": "hard",
    "time_complexity": "O(n * k)",
    "space_complexity": "O(1)",
    "description": "Find the minimum cost to paint n houses with k colors such that no two adjacent houses have the same color.",
}

def solve(costs: list[list[int]], k: int) -> int:
    """
    Calculates the minimum cost to paint n houses with k colors such that 
    no two adjacent houses have the same color.

    Args:
        costs: A 2D list where costs[i][j] is the cost of painting house i with color j.
        k: The number of available colors.

    Returns:
        The minimum total cost to paint all houses.

    Examples:
        >>> solve([[1, 5, 3], [2, 9, 4]], 3)
        3
        >>> solve([[1, 10, 10], [10, 1, 10], [10, 10, 1]], 3)
        3
    """
    if not costs or not costs[0]:
        return 0

    num_houses = len(costs)
    num_colors = k

    # We only need to track the minimum cost and the second minimum cost 
    # from the previous house to decide the current house's cost in O(1) per color.
    # prev_min_val: the absolute minimum cost to paint the previous house.
    # prev_min_idx: the color index that resulted in prev_min_val.
    # prev_second_min_val: the second best cost for the previous house.
    prev_min_val = 0
    prev_min_idx = -1
    prev_second_min_val = 0

    for house_idx in range(num_houses):
        current_min_val = float('inf')
        current_second_min_val = float('inf')
        current_min_idx = -1

        for color_idx in range(num_colors):
            # If the current color is the same as the previous house's best color,
            # we must use the second best cost from the previous house.
            if color_idx == prev_min_idx:
                cost_for_this_color = costs[house_idx][color_idx] + prev_second_min_val
            else:
                cost_for_this_color = costs[house_idx][color_idx] + prev_min_val

            # Update the current house's minimum and second minimum values
            if cost_for_this_color < current_min_val:
                current_second_min_val = current_min_val
                current_min_val = cost_for_this_color
                current_min_idx = color_idx
            elif cost_for_this_color < current_second_min_val:
                current_second_min_val = cost_for_this_color

        # Prepare for the next house iteration
        prev_min_val = current_min_val
        prev_min_idx = current_min_idx
        prev_second_min_val = current_second_min_val

    return int(prev_min_val)
