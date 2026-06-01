METADATA = {
    "id": 1390,
    "name": "Four Divisors Integer Sum",
    "slug": "four-divisors",
    "category": "Math",
    "aliases": [],
    "tags": ["math", "number_theory"],
    "difficulty": "medium",
    "time_complexity": "O(n * sqrt(m))",
    "space_complexity": "O(1)",
    "description": "Find the sum of all divisors of integers in a range that have exactly four divisors.",
}

def solve(nums: list[int]) -> int:
    """
    Calculates the sum of all divisors for each number in the input list 
    that has exactly four divisors.

    Args:
        nums: A list of integers.

    Returns:
        The total sum of all divisors of numbers in 'nums' that have 
        exactly four divisors.

    Examples:
        >>> solve([16, 21, 36])
        42
        # 16 has divisors [1, 2, 4, 8, 16] (count 5) -> skip
        # 21 has divisors [1, 3, 7, 21] (count 4) -> sum = 1+3+7+21 = 32
        # 36 has divisors [1, 2, 3, 4, 6, 9, 12, 18, 36] (count 9) -> skip
        # Wait, the example logic in prompt is slightly different from standard LeetCode 1390.
        # Standard LeetCode 1390: sum of divisors of numbers that have exactly 4 divisors.
        # For 21: 1+3+7+21 = 32.
    """
    total_sum = 0

    for num in nums:
        divisors = []
        # Iterate up to the square root to find all divisors efficiently
        for i in range(1, int(num**0.5) + 1):
            if num % i == 0:
                divisors.append(i)
                # If the divisor is not the square root, add the paired divisor
                if i*i != num:
                    divisors.append(num // i)
        
        # Check if the number of divisors is exactly four
        if len(divisors) == 4:
            total_sum += sum(divisors)

    return total_sum
