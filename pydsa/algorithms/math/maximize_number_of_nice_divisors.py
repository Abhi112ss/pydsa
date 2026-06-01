METADATA = {
    "id": 1808,
    "name": "Maximize Number of Nice Divisors",
    "slug": "maximize-number-of-nice-divisors",
    "category": "Math",
    "aliases": [],
    "tags": ["math", "greedy"],
    "difficulty": "medium",
    "time_complexity": "O(n * sqrt(n))",
    "space_complexity": "O(1)",
    "description": "Find the maximum number of divisors for any number in the range [n, n + 10].",
}

def solve(n: int) -> int:
    """
    Calculates the maximum number of divisors for any integer in the range [n, n + 10].

    Args:
        n: The starting integer of the range.

    Returns:
        The maximum number of divisors found in the range [n, n + 10].

    Examples:
        >>> solve(1)
        1
        >>> solve(4)
        3
        >>> solve(10)
        4
    """
    def count_divisors(num: int) -> int:
        """Helper function to count divisors of a number using the sqrt method."""
        if num == 1:
            return 1
        
        count = 0
        divisor = 1
        # Iterate up to the square root of the number
        while divisor * divisor <= num:
            if num % divisor == 0:
                # If divisor is a perfect square root, count it once
                if divisor * divisor == num:
                    count += 1
                else:
                    # Otherwise, count both the divisor and its complement
                    count += 2
            divisor += 1
        return count

    max_divisors = 0
    # The problem constraints specify checking the range [n, n + 10]
    for current_num in range(n, n + 11):
        current_divisors = count_divisors(current_num)
        if current_divisors > max_divisors:
            max_divisors = current_divisors
            
    return max_divisors
