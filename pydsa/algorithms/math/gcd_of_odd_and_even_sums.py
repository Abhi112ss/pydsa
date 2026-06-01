METADATA = {
    "id": 3658,
    "name": "GCD of Odd and Even Sums",
    "slug": "gcd_of_odd_and_even_sums",
    "category": "Math",
    "aliases": [],
    "tags": ["math", "arrays"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Calculate the greatest common divisor of the sum of all odd numbers and the sum of all even numbers in an array.",
}

import math

def solve(nums: list[int]) -> int:
    """
    Calculates the greatest common divisor (GCD) of the sum of odd numbers 
    and the sum of even numbers in the provided list.

    Args:
        nums: A list of integers.

    Returns:
        The GCD of the sum of odd elements and the sum of even elements.
        If one of the sums is zero, returns the other sum.
        If both sums are zero, returns 0.

    Examples:
        >>> solve([1, 2, 3, 4])
        # odd_sum = 1+3=4, even_sum = 2+4=6, gcd(4, 6) = 2
        2
        >>> solve([1, 3, 5])
        # odd_sum = 9, even_sum = 0, gcd(9, 0) = 9
        9
    """
    odd_sum = 0
    even_sum = 0

    # Iterate through the array once to partition sums by parity
    for num in nums:
        if num % 2 == 0:
            even_sum += num
        else:
            odd_sum += num

    # math.gcd handles cases where one or both arguments are zero correctly
    # gcd(a, 0) = a; gcd(0, 0) = 0
    return math.gcd(odd_sum, even_sum)
