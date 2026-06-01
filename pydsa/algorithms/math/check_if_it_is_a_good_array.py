METADATA = {
    "id": 1250,
    "name": "Check If It Is a Good Array",
    "slug": "check-if-it-is-a-good-array",
    "category": "Math",
    "aliases": [],
    "tags": ["math", "number-theory", "gcd"],
    "difficulty": "medium",
    "time_complexity": "O(n log(max(nums)))",
    "space_complexity": "O(1)",
    "description": "Determine if there exists a subset of integers such that a linear combination of them equals 1 using Bezout's Identity.",
}

import math

def solve(nums: list[int]) -> bool:
    """
    Determines if a subset of the given array can form a linear combination equal to 1.
    
    According to Bezout's Identity, for a set of integers, the smallest positive 
    integer that can be expressed as a linear combination (sum of a_i * x_i) 
    is the Greatest Common Divisor (GCD) of the entire set. 
    Therefore, a 'good array' exists if and only if the GCD of all elements in 
    the array is 1.

    Args:
        nums: A list of positive integers.

    Returns:
        True if the GCD of all elements in the array is 1, False otherwise.

    Examples:
        >>> solve([6, 5, 4, 9, 7, 10])
        True
        >>> solve([2, 4, 6, 8])
        False
    """
    if not nums:
        return False

    # Initialize the running GCD with the first element
    current_gcd = nums[0]

    # Iterate through the array to find the cumulative GCD
    for i in range(1, len(nums)):
        current_gcd = math.gcd(current_gcd, nums[i])
        
        # Optimization: If GCD reaches 1, any further GCD operations 
        # will remain 1, so we can exit early.
        if current_gcd == 1:
            return True

    # If the final GCD of the entire set is 1, it is a good array
    return current_gcd == 1
