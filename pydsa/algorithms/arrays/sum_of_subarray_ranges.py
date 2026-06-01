METADATA = {
    "id": 2104,
    "name": "Sum of Subarray Ranges",
    "slug": "sum-of-subarray-ranges",
    "category": "Arrays",
    "aliases": [],
    "tags": ["monotonic_stack", "arrays", "dynamic_programming"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Calculate the sum of the difference between the maximum and minimum elements in every possible subarray.",
}

def solve(nums: list[int]) -> int:
    """
    Calculates the sum of (max(subarray) - min(subarray)) for all subarrays.
    
    The problem is equivalent to: Sum(max of all subarrays) - Sum(min of all subarrays).
    We use a monotonic stack to find the contribution of each element as a minimum 
    and a maximum in O(n) time.

    Args:
        nums: A list of integers.

    Returns:
        The total sum of subarray ranges.

    Examples:
        >>> solve([1, 2, 3])
        4
        >>> solve([-1, -2, -3])
        4
        >>> solve([4, 2, 1, 5])
        11
    """
    n = len(nums)

    def get_total_contribution(is_max: bool) -> int:
        """
        Calculates the sum of elements acting as either the max or min of subarrays.
        
        To handle duplicate values and avoid overcounting, we use a strict inequality 
        on one side and a non-strict inequality on the other when finding boundaries.
        """
        total_sum = 0
        # left[i] is the index of the nearest element to the left that violates the property
        # right[i] is the index of the nearest element to the right that violates the property
        left = [-1] * n
        right = [n] * n
        stack: list[int] = []

        # Find nearest boundary to the left
        for i in range(n):
            while stack:
                # If is_max is True, we look for elements > nums[i]
                # If is_max is False, we look for elements < nums[i]
                condition = nums[stack[-1]] < nums[i] if is_max else nums[stack[-1]] > nums[i]
                if condition:
                    stack.pop()
                else:
                    break
            if stack:
                left[i] = stack[-1]
            stack.append(i)

        stack.clear()

        # Find nearest boundary to the right
        # Note: We use >= or <= here to handle duplicates correctly (one side strict, one side not)
        for i in range(n - 1, -1, -1):
            while stack:
                condition = nums[stack[-1]] <= nums[i] if is_max else nums[stack[-1]] >= nums[i]
                if condition:
                    stack.pop()
                else:
                    break
            if stack:
                right[i] = stack[-1]
            stack.append(i)

        # The number of subarrays where nums[i] is the extreme is (i - left[i]) * (right[i] - i)
        for i in range(n):
            count = (i - left[i]) * (right[i] - i)
            total_sum += count * nums[i]
            
        return total_sum

    # Sum of Maxima - Sum of Minima
    return get_total_contribution(True) - get_total_contribution(False)
