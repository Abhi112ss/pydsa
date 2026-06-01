METADATA = {
    "id": 1856,
    "name": "Maximum Subarray Min-Product",
    "slug": "maximum-subarray-min-product",
    "category": "Array",
    "aliases": [],
    "tags": ["monotonic_stack", "array", "prefix_sum"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Find the maximum value of the minimum element in a subarray multiplied by the sum of that subarray.",
}

def solve(nums: list[int]) -> int:
    """
    Calculates the maximum min-product of any subarray in the given list.

    The min-product is defined as the minimum element of a subarray multiplied 
    by the sum of all elements in that subarray.

    Args:
        nums: A list of positive integers.

    Returns:
        The maximum min-product found among all possible subarrays, modulo 10^9 + 7.

    Examples:
        >>> solve([1, 2, 3, 4])
        12
        >>> solve([1, 2, 3, 4, 5])
        15
    """
    MOD = 10**9 + 7
    n = len(nums)
    
    # Precompute prefix sums to calculate subarray sums in O(1)
    # prefix_sums[i] stores the sum of nums[0...i-1]
    prefix_sums = [0] * (n + 1)
    for i in range(n):
        prefix_sums[i + 1] = prefix_sums[i] + nums[i]

    # left_boundary[i] will store the index of the first element to the left 
    # that is strictly smaller than nums[i].
    left_boundary = [-1] * n
    # right_boundary[i] will store the index of the first element to the right 
    # that is strictly smaller than nums[i].
    right_boundary = [n] * n

    # Use a monotonic increasing stack to find the left boundaries
    stack = []
    for i in range(n):
        while stack and nums[stack[-1]] >= nums[i]:
            stack.pop()
        if stack:
            left_boundary[i] = stack[-1]
        stack.append(i)

    # Clear stack to reuse for right boundaries
    stack = []
    # Use a monotonic increasing stack to find the right boundaries
    for i in range(n - 1, -1, -1):
        while stack and nums[stack[-1]] >= nums[i]:
            stack.pop()
        if stack:
            right_boundary[i] = stack[-1]
        stack.append(i)

    max_min_product = 0

    # For each element, treat it as the minimum element of a subarray.
    # The largest such subarray extends from (left_boundary + 1) to (right_boundary - 1).
    for i in range(n):
        left = left_boundary[i] + 1
        right = right_boundary[i] - 1
        
        # Calculate sum of subarray nums[left...right] using prefix sums
        current_sum = prefix_sums[right + 1] - prefix_sums[left]
        current_min_product = nums[i] * current_sum
        
        if current_min_product > max_min_product:
            max_min_product = current_min_product

    return max_min_product % MOD
