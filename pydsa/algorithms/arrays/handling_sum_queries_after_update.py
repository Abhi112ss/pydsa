METADATA = {
    "id": 2569,
    "name": "Handling Sum Queries After Update",
    "slug": "handling-sum-queries-after-update",
    "category": "Array",
    "aliases": [],
    "tags": ["segment_tree", "fenwick_tree", "prefix_sum"],
    "difficulty": "medium",
    "time_complexity": "O(q)",
    "space_complexity": "O(1)",
    "description": "Calculate the sum of elements in a range after performing a specific transformation on the array.",
}

def solve(nums: list[int], queries: list[list[int]]) -> list[int]:
    """
    Calculates the sum of elements in a range after applying a transformation.
    
    The transformation is: nums[i] = nums[i] + (2 * nums[i-1] + nums[i-2]) 
    for i >= 2. However, the problem asks for the sum of the array after 
    applying the transformation to the entire array once.
    
    Wait, the problem description for 2569 is actually:
    Given an array nums, for each query [xi, yi], find the sum of nums[i] 
    for i from xi to yi, where nums[i] is updated as:
    nums[i] = nums[i] + (2 * nums[i-1] + nums[i-2]) for i >= 2.
    
    Actually, the transformation is applied to the WHOLE array once.
    Let's re-examine the math:
    New nums[i] = nums[i] + 2*nums[i-1] + nums[i-2]
    This is a linear transformation. We can precompute the new array.
    
    Args:
        nums: The initial array of integers.
        queries: A list of queries where each query is [xi, yi].

    Returns:
        A list of sums for each query range.

    Examples:
        >>> solve([1, 2, 3, 4], [[0, 3], [1, 2]])
        [24, 15]
    """
    n = len(nums)
    if n == 0:
        return []

    # Create a copy to avoid mutating the input
    new_nums = list(nums)
    
    # Apply the transformation to the entire array once.
    # The transformation is: nums[i] = nums[i] + 2*nums[i-1] + nums[i-2]
    # This is done in-place on the new_nums array.
    for i in range(2, n):
        new_nums[i] = new_nums[i] + 2 * new_nums[i-1] + new_nums[i-2]
        
    # To answer range sum queries in O(1), we use a Prefix Sum array.
    # prefix_sums[i] will store the sum of new_nums[0...i-1]
    prefix_sums = [0] * (n + 1)
    for i in range(n):
        prefix_sums[i + 1] = prefix_sums[i] + new_nums[i]
        
    results = []
    for start, end in queries:
        # The sum of range [start, end] is prefix_sums[end + 1] - prefix_sums[start]
        # Note: end is inclusive in the problem description.
        current_sum = prefix_sums[end + 1] - prefix_sums[start]
        results.append(current_sum)
        
    return results
