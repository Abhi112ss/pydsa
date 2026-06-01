METADATA = {
    "id": 216,
    "name": "Combination Sum III",
    "slug": "combination_sum_iii",
    "category": "Backtracking",
    "aliases": [],
    "tags": ["backtracking"],
    "difficulty": "medium",
    "time_complexity": "O(9! / (9-k)!)",
    "space_complexity": "O(k)",
    "description": "Find all valid combinations of k numbers that sum up to n using numbers 1-9, each used at most once.",
}

def solve(k: int, n: int) -> list[list[int]]:
    """
    Find all valid combinations of k distinct numbers from 1-9 that sum to n.

    Args:
        k: The number of elements in each combination.
        n: The target sum.

    Returns:
        A list of all valid combinations, each sorted in ascending order.

    Examples:
        >>> solve(3, 7)
        [[1, 2, 4]]
        >>> solve(3, 9)
        [[1, 2, 6], [1, 3, 5], [2, 3, 4]]
        >>> solve(4, 1)
        []
    """
    result = []

    def backtrack(start: int, remaining_k: int, remaining_sum: int, current: list[int]) -> None:
        # Base case: found a valid combination
        if remaining_k == 0 and remaining_sum == 0:
            result.append(current[:])
            return

        # Pruning: not enough digits left or sum already exceeded
        if remaining_k <= 0 or remaining_sum <= 0:
            return

        # Try each digit from start to 9
        for digit in range(start, 10):
            # Early termination: if current digit exceeds remaining sum, no need to continue
            if digit > remaining_sum:
                break

            current.append(digit)
            # Recurse with next digit, one fewer element needed, reduced sum
            backtrack(digit + 1, remaining_k - 1, remaining_sum - digit, current)
            current.pop()  # Backtrack: remove the last digit

    backtrack(1, k, n, [])
    return result