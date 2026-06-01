METADATA = {
    "id": 2928,
    "name": "Distribute Candies Among Children I",
    "slug": "distribute-candies-among-children-i",
    "category": "Math",
    "aliases": [],
    "tags": ["combinatorics", "math"],
    "difficulty": "medium",
    "time_complexity": "O(1)",
    "space_complexity": "O(1)",
    "description": "Calculate the number of ways to distribute n identical candies among k distinct children using the stars and bars theorem.",
}

import math

def solve(n: int, k: int) -> int:
    """
    Calculates the number of ways to distribute n identical candies among k distinct children.
    
    This problem is a classic application of the 'Stars and Bars' theorem. 
    The number of ways to put n identical items into k distinct bins is equivalent 
    to finding the number of non-negative integer solutions to the equation:
    x_1 + x_2 + ... + x_k = n
    
    The formula for this is C(n + k - 1, k - 1) or C(n + k - 1, n).

    Args:
        n: The number of identical candies.
        k: The number of distinct children.

    Returns:
        The total number of ways to distribute the candies.

    Examples:
        >>> solve(3, 2)
        4
        # Ways: (0,3), (1,2), (2,1), (3,0)
        >>> solve(2, 3)
        6
        # Ways: (2,0,0), (0,2,0), (0,0,2), (1,1,0), (1,0,1), (0,1,1)
    """
    # According to Stars and Bars theorem:
    # We have n stars and we need to place k-1 bars to create k partitions.
    # Total positions = n + (k - 1)
    # We choose (k - 1) positions for the bars.
    
    # Total items to choose from
    total_positions = n + k - 1
    # Number of bars to place
    bars_to_place = k - 1
    
    # Using math.comb for efficient calculation of combinations C(n, r)
    # This handles the large integer arithmetic internally.
    return math.comb(total_positions, bars_to_place)
