METADATA = {
    "id": 1862,
    "name": "Sum of Floored Pairs",
    "slug": "sum-of-floored-pairs",
    "category": "Math",
    "aliases": [],
    "tags": ["math", "binary_search", "prefix_sum"],
    "difficulty": "medium",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(n)",
    "description": "Calculate the sum of floor(nums1[i] / nums2[j]) for all pairs (i, j) modulo 10^9 + 7.",
}

def solve(nums1: list[int], nums2: list[int]) -> int:
    """
    Calculates the sum of floor(nums1[i] / nums2[j]) for all pairs (i, j).

    The algorithm uses a frequency array and prefix sums to count how many 
    elements in nums1 fall into specific ranges defined by multiples of 
    elements in nums2. This avoids the O(n^2) brute force approach.

    Args:
        nums1: A list of integers.
        nums2: A list of integers.

    Returns:
        The sum of floor(nums1[i] / nums2[j]) modulo 10^9 + 7.

    Examples:
        >>> solve([10, 20, 30], [2, 3])
        35
        >>> solve([1, 2, 3, 4, 5], [1, 2])
        18
    """
    MOD = 1_000_000_007
    if not nums1 or not nums2:
        return 0

    max_val = max(max(nums1), max(nums2))
    
    # Create a frequency array for nums1
    # count[v] will store how many times value 'v' appears in nums1
    count = [0] * (max_val + 1)
    for x in nums1:
        count[x] += 1
        
    # Transform count into a prefix sum array
    # prefix_sum[i] will store the number of elements in nums1 <= i
    prefix_sum = [0] * (max_val + 2)
    for i in range(max_val + 1):
        prefix_sum[i + 1] = prefix_sum[i] + count[i]

    total_sum = 0
    for divisor in nums2:
        # For a fixed divisor, we iterate through multiples: 
        # [divisor, 2*divisor-1], [2*divisor, 3*divisor-1], etc.
        # All elements in the range [k*divisor, (k+1)*divisor - 1] 
        # will have floor(x / divisor) == k.
        current_divisor_sum = 0
        for k in range(1, (max_val // divisor) + 1):
            lower_bound = k * divisor
            upper_bound = min((k + 1) * divisor - 1, max_val)
            
            # Number of elements in nums1 that fall in [lower_bound, upper_bound]
            # using the prefix sum array in O(1)
            num_elements_in_range = prefix_sum[upper_bound + 1] - prefix_sum[lower_bound]
            
            current_divisor_sum += num_elements_in_range * k
            
        total_sum = (total_sum + current_divisor_sum) % MOD

    return total_sum
