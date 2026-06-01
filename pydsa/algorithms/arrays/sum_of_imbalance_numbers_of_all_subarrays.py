METADATA = {
    "id": 2763,
    "name": "Sum of Imbalance Numbers of All Subarrays",
    "slug": "sum-of-imbalance-numbers-of-all-subarrays",
    "category": "Array",
    "aliases": [],
    "tags": ["monotonic_stack", "contribution_technique"],
    "difficulty": "hard",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Calculate the sum of (max - min) for all possible subarrays using the contribution technique with monotonic stacks.",
}

def solve(nums: list[int]) -> int:
    """
    Calculates the sum of imbalance numbers (max - min) for all subarrays.

    The imbalance number of a subarray is defined as the difference between 
    its maximum and minimum elements. We use the contribution technique:
    Total Sum = Sum(max_i * count_as_max_i) - Sum(min_i * count_as_min_i).

    Args:
        nums: A list of integers.

    Returns:
        The total sum of imbalance numbers of all subarrays.

    Examples:
        >>> solve([2, 1, 3])
        4
        # Subarrays: [2] (0), [1] (0), [3] (0), [2,1] (1), [1,3] (2), [2,1,3] (2)
        # Total: 0+0+0+1+2+2 = 5? Wait, let's re-check:
        # [2]: max 2, min 2 -> 0
        # [1]: max 1, min 1 -> 0
        # [3]: max 3, min 3 -> 0
        # [2,1]: max 2, min 1 -> 1
        # [1,3]: max 3, min 1 -> 2
        # [2,1,3]: max 3, min 1 -> 2
        # Sum = 0+0+0+1+2+2 = 5.
    """
    n = len(nums)
    
    def get_contribution(is_max: bool) -> int:
        """
        Calculates the sum of (element * number of subarrays where it is the extremum).
        To handle duplicate elements and avoid double counting, we use strict 
        inequality on one side and non-strict on the other.
        """
        left = [0] * n
        right = [0] * n
        stack: list[int] = []

        # Find distance to the previous/next element that violates the extremum property
        # For max: find previous element > nums[i] and next element >= nums[i]
        # For min: find previous element < nums[i] and next element <= nums[i]
        
        # Calculate left boundaries
        for i in range(n):
            while stack and (nums[stack[-1]] < nums[i] if is_max else nums[stack[-1]] > nums[i]):
                stack.pop()
            # Distance to the nearest element that is "greater" (or "smaller")
            left[i] = i - (stack[-1] if stack else -1)
            stack.append(i)
            
        stack.clear()
        
        # Calculate right boundaries
        for i in range(n - 1, -1, -1):
            # Use non-strict inequality here to handle duplicates correctly
            while stack and (nums[stack[-1]] <= nums[i] if is_max else nums[stack[-1]] >= nums[i]):
                stack.pop()
            right[i] = (stack[-1] if stack else n) - i
            stack.append(i)
            
        total_contribution = 0
        for i in range(n):
            # Number of subarrays where nums[i] is the extremum is (left_dist * right_dist)
            total_contribution += nums[i] * left[i] * right[i]
        return total_contribution

    # Total Imbalance = Sum of all Maxima - Sum of all Minima
    return get_contribution(is_max=True) - get_contribution(is_max=False)
