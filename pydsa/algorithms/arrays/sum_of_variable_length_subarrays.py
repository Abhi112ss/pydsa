METADATA = {
    "id": 3427,
    "name": "Sum of Variable Length Subarrays",
    "slug": "sum_of_variable_length_subarrays",
    "category": "Array",
    "aliases": [],
    "tags": ["array", "prefix_sum"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Calculate the sum of all subarrays where each subarray starts at index i and has a length determined by the value at index i.",
}

def solve(nums: list[int]) -> int:
    """
    Calculates the sum of variable length subarrays defined by the input array.
    For each index i, a subarray is formed starting at i with length nums[i].
    The subarray is truncated if it exceeds the bounds of the array.

    Args:
        nums: A list of integers where nums[i] represents the length of the 
              subarray starting at index i.

    Returns:
        The total sum of all such subarrays.

    Examples:
        >>> solve([2, 3, 1])
        # Subarray 1: nums[0:2] -> [2, 3] (sum 5)
        # Subarray 2: nums[1:4] -> [3, 1] (sum 4)
        # Subarray 3: nums[2:3] -> [1] (sum 1)
        # Total: 5 + 4 + 1 = 10
        10
        >>> solve([1, 1, 1])
        3
    """
    n = len(nums)
    total_sum = 0
    
    # Precompute prefix sums to allow O(1) range sum queries.
    # prefix_sums[i] stores the sum of nums[0...i-1]
    prefix_sums = [0] * (n + 1)
    for i in range(n):
        prefix_sums[i + 1] = prefix_sums[i] + nums[i]
        
    for i in range(n):
        # The subarray starts at i and has length nums[i].
        # The end index (exclusive) is i + nums[i].
        # We must clamp the end index to the array length n.
        end_index = min(i + nums[i], n)
        
        # Calculate the sum of the range [i, end_index) using prefix sums.
        # sum(nums[i...end_index-1]) = prefix_sums[end_index] - prefix_sums[i]
        current_subarray_sum = prefix_sums[end_index] - prefix_sums[i]
        total_sum += current_subarray_sum
        
    return total_sum
