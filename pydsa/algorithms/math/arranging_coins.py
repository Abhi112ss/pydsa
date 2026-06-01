METADATA = {
    "id": 441,
    "name": "Arranging Coins",
    "slug": "arranging_coins",
    "category": "Math",
    "aliases": [],
    "tags": ["binary_search", "math"],
    "difficulty": "easy",
    "time_complexity": "O(log n)",
    "space_complexity": "O(1)",
    "description": "Find the number of complete rows of coins that can be arranged in a staircase shape given n coins.",
}

def solve(n: int) -> int:
    """Find the largest k such that k(k+1)/2 <= n using binary search.

    Args:
        n: The total number of coins available.

    Returns:
        The number of complete staircase rows that can be formed.

    Examples:
        >>> solve(5)
        2
        >>> solve(8)
        3
        >>> solve(1)
        1
        >>> solve(0)
        0
    """
    if n <= 0:
        return 0

    # Binary search for the largest k where k*(k+1)//2 <= n
    low = 1
    high = n

    while low <= high:
        mid = (low + high) // 2
        # Calculate the total coins needed for mid complete rows
        coins_needed = mid * (mid + 1) // 2

        if coins_needed == n:
            return mid
        elif coins_needed < n:
            # mid rows might be possible, try a larger k
            low = mid + 1
        else:
            # mid rows require too many coins, try a smaller k
            high = mid - 1

    # high is now the largest k where k*(k+1)//2 <= n
    return high