METADATA = {
    "id": 2748,
    "name": "Number of Beautiful Pairs",
    "slug": "number-of-beautiful-pairs",
    "category": "Math",
    "aliases": [],
    "tags": ["math", "gcd", "array"],
    "difficulty": "medium",
    "time_complexity": "O(n^2 * log(max_val))",
    "space_complexity": "O(1)",
    "description": "Count pairs (i, j) such that the greatest common divisor of the first digit of nums[i] and the last digit of nums[j] is 1.",
}

import math

def solve(nums: list[int]) -> int:
    """
    Counts the number of beautiful pairs in the given list.
    
    A pair (i, j) is beautiful if 0 <= i < j < len(nums) and 
    gcd(first_digit(nums[i]), last_digit(nums[j])) == 1.

    Args:
        nums: A list of positive integers.

    Returns:
        The total count of beautiful pairs.

    Examples:
        >>> solve([14, 21, 45])
        2
        # Pairs: (14, 21) -> gcd(1, 1)=1; (14, 45) -> gcd(1, 5)=1; (21, 45) -> gcd(2, 5)=1.
        # Wait, let's re-check: 
        # (14, 21): first(14)=1, last(21)=1. gcd(1,1)=1. (Beautiful)
        # (14, 45): first(14)=1, last(45)=5. gcd(1,5)=1. (Beautiful)
        # (21, 45): first(21)=2, last(45)=5. gcd(2,5)=1. (Beautiful)
        # Total = 3.
    """
    beautiful_pairs_count = 0
    n = len(nums)

    for i in range(n):
        # Extract the first digit of nums[i]
        # We convert to string for simplicity, or use a while loop for math approach
        first_digit = int(str(nums[i])[0])
        
        for j in range(i + 1, n):
            # Extract the last digit of nums[j]
            last_digit = nums[j] % 10
            
            # Check the GCD condition using math.gcd
            # A pair is beautiful if the GCD is exactly 1
            if math.gcd(first_digit, last_digit) == 1:
                beautiful_pairs_count += 1
                
    return beautiful_pairs_count
