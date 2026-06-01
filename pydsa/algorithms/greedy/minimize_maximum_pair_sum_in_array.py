METADATA = {
    "id": 1877,
    "name": "Minimize Maximum Pair Sum in Array",
    "slug": "minimize-maximum-pair-sum-in-array",
    "category": "Greedy",
    "aliases": [],
    "tags": ["greedy", "sorting"],
    "difficulty": "easy",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(1)",
    "description": "Minimize the maximum pair sum by pairing the smallest elements with the largest elements after sorting.",
}

def solve(nums: list[int]) -> int:
    """
    Finds the minimum possible value of the maximum pair sum by pairing elements.

    The optimal strategy is to sort the array and pair the smallest available 
    element with the largest available element. This greedy approach balances 
    the sums to prevent any single pair from becoming excessively large.

    Args:
        nums: A list of integers representing the array.

    Returns:
        The minimum possible maximum pair sum.

    Examples:
        >>> solve([3, 5, 2, 3])
        8
        >>> solve([1, 1, 1, 1])
        2
        >>> solve([10, 1, 2, 7, 1, 3])
        11
    """
    # Sort the array to allow pairing smallest with largest
    nums.sort()
    
    n = len(nums)
    max_pair_sum = 0
    
    # Use two pointers: one starting from the beginning, one from the end
    # Pair nums[i] with nums[n - 1 - i]
    for i in range(n // 2):
        current_pair_sum = nums[i] + nums[n - 1 - i]
        
        # Track the maximum sum encountered among all pairs
        if current_pair_sum > max_pair_sum:
            max_pair_sum = current_pair_sum
            
    return max_pair_sum
