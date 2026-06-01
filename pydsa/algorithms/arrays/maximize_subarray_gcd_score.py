METADATA = {
    "id": 3574,
    "name": "Maximize Subarray GCD Score",
    "slug": "maximize_subarray_gcd_score",
    "category": "Array",
    "aliases": [],
    "tags": ["sliding_window", "math", "gcd"],
    "difficulty": "medium",
    "time_complexity": "O(n log(max_val))",
    "space_complexity": "O(log(max_val))",
    "description": "Find the maximum GCD score of any subarray, where the score is defined by the GCD of the subarray elements.",
}

import math

def solve(nums: list[int]) -> int:
    """
    Finds the maximum GCD value possible for any subarray within the given list.
    
    Since the GCD of a subarray can only decrease or stay the same as elements 
    are added, and the number of distinct GCD values ending at any index is 
    at most O(log(max(nums))), we can track these values efficiently.

    Args:
        nums: A list of positive integers.

    Returns:
        The maximum GCD value found among all possible subarrays.

    Examples:
        >>> solve([12, 6, 9])
        12
        >>> solve([2, 4, 8])
        8
        >>> solve([1, 2, 3])
        3
    """
    if not nums:
        return 0

    max_gcd = 0
    # current_gcds stores a mapping of {gcd_value: count_of_subarrays_ending_here}
    # However, for this specific problem, we only need to track the distinct 
    # GCD values ending at the current index to find the global maximum.
    current_gcds: dict[int, int] = {}

    for num in nums:
        # Update the global maximum with the single element itself
        max_gcd = max(max_gcd, num)
        
        next_gcds: dict[int, int] = {num: 1}
        
        # For every GCD value ending at the previous index, 
        # calculate the new GCD with the current number.
        for prev_gcd in current_gcds:
            new_gcd = math.gcd(prev_gcd, num)
            # We use a dictionary to keep track of unique GCD values 
            # to maintain the O(log(max_val)) property.
            next_gcds[new_gcd] = next_gcds.get(new_gcd, 0) + 1
            max_gcd = max(max_gcd, new_gcd)
            
        current_gcds = next_gcds

    return max_gcd
