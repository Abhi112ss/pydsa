METADATA = {
    "id": 956,
    "name": "Tallest Billboard",
    "slug": "tallest-billboard",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dynamic_programming", "knapsack"],
    "difficulty": "hard",
    "time_complexity": "O(n * sum(rods))",
    "space_complexity": "O(sum(rods))",
    "description": "Find the maximum height of a billboard consisting of two parallel supports of equal height using a subset of given rods.",
}

def solve(rods: list[int]) -> int:
    """
    Finds the maximum height of a billboard with two equal-height supports.

    The problem can be modeled as finding two disjoint subsets of rods such that 
    the sum of elements in the first subset equals the sum of elements in the second.
    We use dynamic programming where dp[diff] represents the maximum height of 
    the shorter support when the difference between the two supports is 'diff'.

    Args:
        rods: A list of integers representing the lengths of available rods.

    Returns:
        The maximum height of the two equal supports.

    Examples:
        >>> solve([1, 2, 3, 4, 5, 6])
        6
        >>> solve([1, 2, 3, 4, 5, 6, 7, 8, 9])
        15
        >>> solve([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])
        30
    """
    # dp[diff] = max height of the shorter support for a given difference 'diff'
    # between the two supports.
    # We use a dictionary to handle the sparse nature of the differences.
    dp = {0: 0}

    for rod in rods:
        # Create a copy to avoid modifying the dictionary while iterating
        new_dp = dp.copy()
        
        for diff, shorter_height in dp.items():
            # Option 1: Add the rod to the taller support
            # New difference: diff + rod
            # Shorter height remains the same
            new_diff_plus = diff + rod
            new_dp[new_diff_plus] = max(new_dp.get(new_diff_plus, 0), shorter_height)

            # Option 2: Add the rod to the shorter support
            # If rod <= diff, the rod becomes part of the shorter side, 
            # and the new difference is (diff - rod).
            # The new shorter height is (shorter_height + rod).
            if rod <= diff:
                new_diff_minus = diff - rod
                new_dp[new_diff_minus] = max(new_dp.get(new_diff_minus, 0), shorter_height + rod)
            else:
                # If rod > diff, the rod becomes the new taller side.
                # The new difference is (rod - diff).
                # The new shorter height is the old taller height (shorter_height + diff).
                # Wait, a simpler way to think: 
                # The new shorter height is the old taller height, which is (shorter_height + diff).
                # But we track 'shorter_height'. The old taller height was (shorter_height + diff).
                # After adding rod to the shorter side, the new shorter height is (shorter_height + diff).
                # The new difference is (rod - diff).
                new_diff_minus = rod - diff
                new_dp[new_diff_minus] = max(new_dp.get(new_diff_minus, 0), shorter_height + diff)

        dp = new_dp

    # The answer is the max height when the difference is 0
    return dp.get(0, 0)
