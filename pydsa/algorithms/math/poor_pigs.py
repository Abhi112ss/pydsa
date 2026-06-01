METADATA = {
    "id": 458,
    "name": "Poor Pigs",
    "slug": "poor-pigs",
    "category": "Math",
    "aliases": [],
    "tags": ["math", "combinatorics"],
    "difficulty": "medium",
    "time_complexity": "O(log(smell_count))",
    "space_complexity": "O(1)",
    "description": "Find the minimum number of pigs needed to identify the smell of a specific food among many given a limited number of tests.",
}

import math

def solve(smell_count: int, test_limit: int) -> int:
    """
    Calculates the minimum number of pigs required to identify the smell.
    
    The problem can be modeled as finding the minimum number of pigs (p) 
    such that the number of possible outcomes (test_limit + 1) raised to the 
    power of the number of pigs (p) is greater than or equal to the number 
    of food items (smell_count).
    
    Mathematically: (test_limit + 1) ** pigs >= smell_count
    Taking the logarithm on both sides:
    pigs * log(test_limit + 1) >= log(smell_count)
    pigs >= log(smell_count) / log(test_limit + 1)

    Args:
        smell_count: The number of food items that could potentially smell.
        test_limit: The maximum number of tests allowed.

    Returns:
        The minimum number of pigs required.

    Examples:
        >>> solve(7, 3)
        2
        >>> solve(10, 1)
        4
        >>> solve(1, 1)
        0
    """
    # If there is only one food item, no pigs are needed because 
    # we already know which one it is (or there's no "other" to find).
    if smell_count <= 1:
        return 0

    # Each pig can represent a dimension in a coordinate system.
    # The number of possible states for each pig is (test_limit + 1),
    # representing the test results (e.g., test 1, test 2, ..., test N, or no test).
    # The total number of unique outcomes with 'p' pigs is (test_limit + 1) ** p.
    
    # We need to find the smallest integer p such that (test_limit + 1) ** p >= smell_count.
    # Using the change of base formula for logarithms:
    # p = ceil( log(smell_count) / log(test_limit + 1) )
    
    base = test_limit + 1
    
    # Using math.log with base can sometimes lead to precision issues with very large numbers,
    # but for LeetCode constraints, it is generally safe. 
    # To be robust, we can use a loop or math.log with a small epsilon.
    
    pigs = math.ceil(math.log(smell_count) / math.log(base))
    
    # Double check for floating point precision errors
    if (base ** (pigs - 1)) >= smell_count:
        pigs -= 1
        
    return pigs
