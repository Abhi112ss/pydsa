METADATA = {
    "id": 1414,
    "name": "Find the Minimum Number of Fibonacci Numbers Whose Sum Is K",
    "slug": "find-the-minimum-number-of-fibonacci-numbers-whose-sum-is-k",
    "category": "Math",
    "aliases": [],
    "tags": ["greedy", "math"],
    "difficulty": "medium",
    "time_complexity": "O(log k)",
    "space_complexity": "O(log k)",
    "description": "Find the minimum number of Fibonacci numbers that sum up to a given integer k using a greedy approach.",
}

def solve(k: int) -> int:
    """
    Finds the minimum number of Fibonacci numbers whose sum equals k.

    The problem can be solved greedily because the Fibonacci sequence 
    possesses a property similar to Zeckendorf's theorem, where any 
    positive integer can be uniquely represented as a sum of non-consecutive 
    Fibonacci numbers. Subtracting the largest possible Fibonacci number 
    at each step yields the minimum count.

    Args:
        k: The target integer sum.

    Returns:
        The minimum number of Fibonacci numbers required to sum to k.

    Examples:
        >>> solve(10)
        2  # 8 + 2
        >>> solve(11)
        3  # 8 + 2 + 1
        >>> solve(1)
        1  # 1
    """
    if k == 0:
        return 0

    # Generate all Fibonacci numbers up to k
    fibonacci_numbers: list[int] = [1, 2]
    while True:
        next_fib = fibonacci_numbers[-1] + fibonacci_numbers[-2]
        if next_fib > k:
            break
        fibonacci_numbers.append(next_fib)

    count = 0
    # Iterate backwards through the Fibonacci sequence (Greedy approach)
    # We always pick the largest Fibonacci number that is <= current k
    for i in range(len(fibonacci_numbers) - 1, -1, -1):
        if k <= 0:
            break
        
        current_fib = fibonacci_numbers[i]
        if current_fib <= k:
            # Calculate how many times this Fibonacci number fits into k
            # Note: In standard Zeckendorf representation, we use each once,
            # but for this problem, we just subtract and count.
            num_uses = k // current_fib
            count += num_uses
            k %= current_fib

    return count
