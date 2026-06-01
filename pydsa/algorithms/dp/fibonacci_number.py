METADATA = {
    "id": 509,
    "name": "Fibonacci Number",
    "slug": "fibonacci_number",
    "category": "Dynamic Programming",
    "aliases": ["fib"],
    "tags": ["math", "recursion", "memoization"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Given n, calculate F(n) where F(0)=0, F(1)=1, and F(n)=F(n-1)+F(n-2) for n>1.",
}


def solve(n: int) -> int:
    """Calculate the n-th Fibonacci number using iterative DP with constant space.

    Args:
        n: A non-negative integer (0 <= n <= 30 per LeetCode constraints).

    Returns:
        The n-th Fibonacci number F(n).

    Examples:
        >>> solve(0)
        0
        >>> solve(1)
        1
        >>> solve(2)
        1
        >>> solve(5)
        5
        >>> solve(10)
        55
    """
    if n <= 1:
        return n

    # Only need to track the previous two values at each step.
    prev_two = 0  # F(i-2)
    prev_one = 1  # F(i-1)

    for _ in range(2, n + 1):
        # Compute current Fibonacci number as sum of the two preceding ones.
        current = prev_one + prev_two
        # Shift the window forward for the next iteration.
        prev_two = prev_one
        prev_one = current

    return prev_one