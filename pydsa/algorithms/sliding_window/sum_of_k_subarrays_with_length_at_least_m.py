METADATA = {
    "id": 3473,
    "name": "Sum of K Subarrays With Length at Least M",
    "slug": "sum_of_k_subarrays_with_length_at_least_m",
    "category": "Array",
    "aliases": [],
    "tags": ["sliding_window", "prefix_sum"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Calculate the sum of all subarrays that have a length of at least M.",
}

def solve(nums: list[int], m: int) -> int:
    """
    Calculates the sum of all subarrays in 'nums' that have a length of at least 'm'.

    The algorithm uses prefix sums to calculate subarray sums in O(1) and 
    mathematically determines how many times each element contributes to 
    the total sum based on the constraints of the subarray length.

    Args:
        nums: A list of integers.
        m: The minimum length required for a subarray.

    Returns:
        The total sum of all subarrays with length >= m.

    Examples:
        >>> solve([1, 2, 3], 2)
        # Subarrays: [1, 2], [2, 3], [1, 2, 3]
        # Sums: 3 + 5 + 6 = 14
        14
        >>> solve([1, 1, 1], 1)
        # Subarrays: [1], [1], [1], [1,1], [1,1], [1,1,1]
        # Sums: 1+1+1+2+2+3 = 10
        10
    """
    n = len(nums)
    if m > n:
        return 0

    # prefix_sums[i] stores the sum of nums[0...i-1]
    prefix_sums = [0] * (n + 1)
    for i in range(n):
        prefix_sums[i + 1] = prefix_sums[i] + nums[i]

    total_sum = 0
    
    # We want to find the sum of (prefix_sums[j] - prefix_sums[i]) 
    # for all pairs (i, j) such that j - i >= m.
    # This can be rewritten as: Sum(prefix_sums[j]) - Sum(prefix_sums[i])
    # for all valid j and i.
    
    # Let's iterate through each possible end index 'j' of a subarray.
    # For a fixed 'j', the valid start indices 'i' are 0, 1, ..., j - m.
    # The contribution to the total sum for a fixed 'j' is:
    # sum_{i=0}^{j-m} (prefix_sums[j] - prefix_sums[i])
    # = (j - m + 1) * prefix_sums[j] - sum_{i=0}^{j-m} (prefix_sums[i])

    running_prefix_sum_of_prefixes = 0
    
    for j in range(m, n + 1):
        # The new valid 'i' index that becomes available as 'j' increases is 'j - m'
        new_i = j - m
        running_prefix_sum_of_prefixes += prefix_sums[new_i]
        
        # Calculate contribution of all subarrays ending at index j-1 (length >= m)
        # Number of such subarrays is (j - m + 1)
        count = j - m + 1
        current_contribution = (count * prefix_sums[j]) - running_prefix_sum_of_prefixes
        total_sum += current_contribution

    return total_sum
