METADATA = {
    "id": 1465,
    "name": "Maximum Area of a Piece of Cake After Horizontal and Vertical Cuts",
    "slug": "maximum-area-of-a-piece-of-cake-after-horizontal-and-vertical-cuts",
    "category": "Array",
    "aliases": [],
    "tags": ["array", "greedy"],
    "difficulty": "medium",
    "time_complexity": "O(m + n)",
    "space_complexity": "O(1)",
    "description": "Find the maximum area of a cake piece by multiplying the largest horizontal gap by the largest vertical gap.",
}

def solve(horizontalCuts: list[int], verticalCuts: list[int], n: int, m: int) -> int:
    """
    Calculates the maximum area of a piece of cake after making horizontal and vertical cuts.

    The maximum area is obtained by finding the largest gap between consecutive horizontal 
    cuts (including the boundaries 0 and n) and multiplying it by the largest gap 
    between consecutive vertical cuts (including the boundaries 0 and m).

    Args:
        horizontalCuts: A list of integers representing the positions of horizontal cuts.
        verticalCuts: A list of integers representing the positions of vertical cuts.
        n: The total height of the cake.
        m: The total width of the cake.

    Returns:
        The maximum area of a single piece of cake.

    Examples:
        >>> solve([1, 3, 4, 10], [1, 2, 3, 4], 13, 5)
        4
        >>> solve([1, 3, 4, 10], [1, 2, 3, 4], 13, 5)
        4
    """

    def get_max_gap(cuts: list[int], boundary: int) -> int:
        """Helper to find the maximum distance between consecutive cuts."""
        # Start with the gap between the first cut and the 0 boundary
        max_gap = cuts[0]
        
        # Calculate gaps between consecutive cuts
        for i in range(1, len(cuts)):
            max_gap = max(max_gap, cuts[i] - cuts[i - 1])
            
        # Finally, check the gap between the last cut and the boundary
        max_gap = max(max_gap, boundary - cuts[-1])
        
        return max_gap

    # The problem guarantees cuts are sorted, so we can find gaps in O(len(cuts))
    max_h_gap = get_max_gap(horizontalCuts, n)
    max_v_gap = get_max_gap(verticalCuts, m)

    # The maximum area is the product of the two largest dimensions
    return max_h_gap * max_v_gap
