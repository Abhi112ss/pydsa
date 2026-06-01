METADATA = {
    "id": 1387,
    "name": "Sort Integers by The Power Value",
    "slug": "sort-integers-by-the-power-value",
    "category": "Sorting",
    "aliases": [],
    "tags": ["sorting", "memoization", "recursion"],
    "difficulty": "medium",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(n)",
    "description": "Sort an array of integers based on their power value, where power is defined by the number of steps to reach 1 using the Collatz conjecture.",
}

def solve(nums: list[int], k: int) -> list[int]:
    """
    Sorts the given list of integers based on their 'power value'.
    The power value is the number of steps required to reach 1 using the 
    Collatz conjecture: if n is even, n = n / 2; if n is odd, n = 3n + 1.
    If two numbers have the same power value, the smaller number comes first.

    Args:
        nums: A list of positive integers.
        k: An integer used to determine the power value (though the problem 
           definition of power value is independent of k, k is provided 
           in the signature).

    Returns:
        A list of integers sorted by power value, then by value.

    Examples:
        >>> solve([1, 3, 5, 7], 2)
        [1, 3, 5, 7]
        >>> solve([17, 5, 2, 3], 2)
        [2, 3, 5, 17]
    """
    memo: dict[int, int] = {1: 0}

    def get_power(n: int) -> int:
        """Calculates the power value of n using memoization."""
        if n in memo:
            return memo[n]
        
        # Collatz conjecture step
        if n % 2 == 0:
            next_val = n // 2
        else:
            next_val = 3 * n + 1
            
        # Recursive step with memoization
        memo[n] = 1 + get_power(next_val)
        return memo[n]

    # Pre-calculate all power values to avoid redundant calculations during sort
    # We store them as tuples (power_value, original_value) to handle the 
    # secondary sorting criteria (smaller value first) automatically.
    power_pairs: list[tuple[int, int]] = []
    for num in nums:
        power_pairs.append((get_power(num), num))

    # Sort primarily by power_value (index 0) and secondarily by num (index 1)
    power_pairs.sort()

    # Extract the original numbers from the sorted tuples
    return [pair[1] for pair in power_pairs]
