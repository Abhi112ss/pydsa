METADATA = {
    "id": 259,
    "name": "3Sum Smaller",
    "slug": "3sum-smaller",
    "category": "Array",
    "aliases": [],
    "tags": ["sorting", "two_pointer"],
    "difficulty": "medium",
    "time_complexity": "O(n^2)",
    "space_complexity": "O(1)",
    "description": "Find the number of index triplets (i, j, k) such that i < j < k and nums[i] + nums[j] + nums[k] < target.",
}

def solve(nums: list[int], target: int) -> int:
    """
    Calculates the number of triplets in the array whose sum is strictly less than the target.

    Args:
        nums: A list of integers.
        target: The integer threshold for the sum of the triplet.

    Returns:
        The total count of triplets (i, j, k) where i < j < k and nums[i] + nums[j] + nums[k] < target.

    Examples:
        >>> solve([-2, 0, 1, 3], 2)
        2
        >>> solve([-1, 0, 1, 2], 1)
        1
    """
    n = len(nums)
    count = 0
    
    # Sorting allows us to use the two-pointer approach effectively
    nums.sort()

    # Iterate through each element as the first element of the triplet
    for i in range(n - 2):
        left = i + 1
        right = n - 1
        
        # Use two pointers to find pairs (left, right) such that nums[i] + nums[left] + nums[right] < target
        while left < right:
            current_sum = nums[i] + nums[left] + nums[right]
            
            if current_sum < target:
                # If the sum is less than target, then all elements between 'left' and 'right'
                # will also satisfy the condition when paired with nums[i] and nums[left]
                # because the array is sorted.
                count += (right - left)
                left += 1
            else:
                # If the sum is too large, decrease the right pointer to reduce the sum
                right -= 1
                
    return count
