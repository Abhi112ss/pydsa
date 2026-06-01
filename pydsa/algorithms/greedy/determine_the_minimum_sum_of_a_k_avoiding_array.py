METADATA = {
    "id": 2829,
    "name": "Determine the Minimum Sum of a k-avoiding Array",
    "slug": "determine-the-minimum-sum-of-a-k-avoiding-array",
    "category": "Greedy",
    "aliases": [],
    "tags": ["greedy", "math"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Find the minimum sum of an array where no two elements at distance k have the same value.",
}

def solve(nums: list[int], k: int) -> int:
    """
    Calculates the minimum sum of an array such that nums[i] != nums[i+k].
    
    The constraint is that for any index i, nums[i] cannot be equal to nums[i+k].
    To minimize the sum, for each residue class modulo k, we should alternate 
    between the two smallest possible positive integers: 1 and 2.

    Args:
        nums: A list of integers (though the values in the input are ignored, 
              only the length matters for the sum calculation).
        k: The distance constraint.

    Returns:
        The minimum possible sum of the array.

    Examples:
        >>> solve([0, 0, 0, 0], 2)
        6
        >>> solve([0, 0, 0], 1)
        3
    """
    n = len(nums)
    total_sum = 0
    
    # We process each residue class modulo k independently.
    # For a fixed residue r (0 <= r < k), the elements are at indices r, r+k, r+2k, ...
    # To minimize the sum, we alternate between 1 and 2.
    for remainder in range(k):
        # Count how many elements belong to this residue class
        # The indices are: remainder, remainder + k, remainder + 2k, ...
        # The number of elements is ceil((n - remainder) / k)
        if remainder < n:
            count = (n - 1 - remainder) // k + 1
            
            # In a sequence of length 'count', we alternate 1, 2, 1, 2...
            # Number of 1s: ceil(count / 2)
            # Number of 2s: floor(count / 2)
            num_ones = (count + 1) // 2
            num_twos = count // 2
            
            total_sum += (num_ones * 1) + (num_twos * 2)
            
    return total_sum
