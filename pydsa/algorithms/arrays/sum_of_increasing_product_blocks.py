METADATA = {
    "id": 3792,
    "name": "Sum of Increasing Product Blocks",
    "slug": "sum_of_increasing_product_blocks",
    "category": "Arrays",
    "aliases": [],
    "tags": ["arrays", "sliding_window", "math"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Calculate the sum of products of all contiguous increasing subarrays.",
}

def solve(nums: list[int]) -> int:
    """
    Calculates the sum of products of all contiguous increasing subarrays.
    
    An increasing subarray is a subarray where each element is strictly greater 
    than the previous one. For each such maximal increasing segment, we 
    calculate the sum of products of all its possible subarrays.

    Args:
        nums: A list of integers.

    Returns:
        The sum of products of all increasing subarrays. Since the result 
        can be very large, the problem context usually implies modulo 10^9 + 7, 
        but here we return the raw sum as per standard algorithmic practice 
        unless specified.

    Examples:
        >>> solve([1, 2, 3])
        # Subarrays: [1], [2], [3], [1,2], [2,3], [1,2,3]
        # Products: 1 + 2 + 3 + 2 + 6 + 6 = 20
        >>> solve([3, 2, 1])
        # Subarrays: [3], [2], [1]
        # Products: 3 + 2 + 1 = 6
    """
    if not nums:
        return 0

    MOD = 10**9 + 7
    total_sum = 0
    n = len(nums)
    
    i = 0
    while i < n:
        # Identify the boundaries of the maximal increasing segment
        start = i
        while i + 1 < n and nums[i + 1] > nums[i]:
            i += 1
        end = i
        
        # Current segment is nums[start...end]
        # We need the sum of products of all subarrays within this segment.
        # Let segment be [a, b, c]. Subarrays: [a], [b], [c], [a,b], [b,c], [a,b,c]
        # We can use dynamic programming to find the sum of products of all 
        # subarrays ending at each position within the segment.
        
        # current_ending_sum stores the sum of products of all increasing 
        # subarrays ending at the current index.
        current_ending_sum = 0
        for j in range(start, end + 1):
            # If we are at index j, the subarrays ending at j are:
            # [nums[j]], [nums[j-1], nums[j]], ..., [nums[start], ..., nums[j]]
            # The sum of their products is:
            # nums[j] + (nums[j-1]*nums[j]) + (nums[j-2]*nums[j-1]*nums[j]) ...
            # Which simplifies to: nums[j] * (1 + sum_of_products_ending_at_j-1)
            
            current_ending_sum = (nums[j] * (1 + current_ending_sum)) % MOD
            total_sum = (total_sum + current_ending_sum) % MOD
            
        # Move to the next segment
        i += 1
        
    return total_sum
