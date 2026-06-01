METADATA = {
    "id": 16,
    "name": "3Sum Closest",
    "slug": "3sum-closest",
    "category": "Array",
    "aliases": [],
    "tags": ["two_pointer", "array", "sorting"],
    "difficulty": "medium",
    "time_complexity": "O(n^2)",
    "space_complexity": "O(1)",
    "description": "Find three integers in an array such that the sum is closest to a given target number.",
}

def solve(nums: list[int], target: int) -> int:
    """
    Finds the sum of three integers in the array that is closest to the target.

    Args:
        nums: A list of integers.
        target: The target integer to approach.

    Returns:
        The sum of the three integers that is closest to the target.

    Examples:
        >>> solve([-1, 2, 1, -4], 1)
        2
        >>> solve([0, 0, 0], 1)
        0
    """
    # Sorting allows us to use the two-pointer technique effectively
    nums.sort()
    n = len(nums)
    
    # Initialize closest_sum with the sum of the first three elements
    closest_sum = nums[0] + nums[1] + nums[2]

    for i in range(n - 2):
        # Optimization: Skip duplicate values for the first element to reduce redundant checks
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        left = i + 1
        right = n - 1

        while left < right:
            current_sum = nums[i] + nums[left] + nums[right]

            # If we found the exact target, return immediately
            if current_sum == target:
                return current_sum

            # Update closest_sum if the current_sum is closer to target than previous best
            if abs(current_sum - target) < abs(closest_sum - target):
                closest_sum = current_sum

            # Move pointers based on whether current_sum is smaller or larger than target
            if current_sum < target:
                left += 1
            else:
                right -= 1

    return closest_sum
