METADATA = {
    "id": 254,
    "name": "Factor Combinations",
    "slug": "factor-combinations",
    "category": "Backtracking",
    "aliases": [],
    "tags": ["recursion", "backtracking", "math"],
    "difficulty": "medium",
    "time_complexity": "O(2^n)",
    "space_complexity": "O(log n)",
    "description": "Given an integer n, return all possible combinations of its factors.",
}

def solve(n: int) -> list[list[int]]:
    """
    Finds all possible combinations of factors for a given integer n.

    Args:
        n: The target integer to factorize.

    Returns:
        A list of lists, where each inner list contains a unique combination 
        of factors that multiply to n.

    Examples:
        >>> solve(8)
        [[2, 4], [2, 2, 2]]
        >>> solve(12)
        [[2, 6], [2, 2, 3], [3, 4]]
    """
    if n <= 1:
        return []

    results: list[list[int]] = []

    def backtrack(target: int, start_factor: int, current_combination: list[int]) -> None:
        """
        Explores factor combinations using backtracking.

        Args:
            target: The remaining value to be factorized.
            start_factor: The minimum factor to consider (to avoid duplicates).
            current_combination: The list of factors found so far.
        """
        # Iterate from the last used factor up to the square root of the target
        # to find potential divisors.
        for factor in range(start_factor, int(target**0.5) + 1):
            if target % factor == 0:
                # Case 1: The factor and its quotient form a valid pair
                # We add [factor, target // factor] to the results
                results.append(current_combination + [factor, target // factor])
                
                # Case 2: Recurse to see if the quotient can be further factorized
                # We pass the current factor as the new start_factor to maintain non-decreasing order
                backtrack(target // factor, factor, current_combination + [factor])

    backtrack(n, 2, [])
    return results
