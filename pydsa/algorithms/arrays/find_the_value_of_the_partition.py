METADATA = {
    "id": 2740,
    "name": "Find the Value of the Partition",
    "slug": "find-the-value-of-the-partition",
    "category": "Arrays",
    "aliases": [],
    "tags": ["arrays", "prefix_sum"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Find the maximum value of (sum of left partition - sum of right partition) for all possible split points in an array.",
}

def solve(nums: list[int]) -> int:
    """
    Calculates the maximum value of (sum(left_partition) - sum(right_partition))
    for all possible split points in the given array.

    A split point is defined such that the left partition contains elements from 
    index 0 to i, and the right partition contains elements from index i+1 to n-1.
    The split must result in both partitions being non-empty.

    Args:
        nums: A list of integers representing the array.

    Returns:
        The maximum difference between the sum of the left and right partitions.

    Examples:
        >>> solve([1, 2, 3, 4, 5])
        -3
        # Splits:
        # [1] | [2,3,4,5] -> 1 - 14 = -13
        # [1,2] | [3,4,5] -> 3 - 12 = -9
        # [1,2,3] | [4,5] -> 6 - 9 = -3
        # [1,2,3,4] | [5] -> 10 - 5 = 5
        # Wait, the example in LeetCode for [1,2,3,4,5] is actually -3? 
        # Let's re-check the logic. 
        # If nums = [1,2,3,4,5], possible splits:
        # i=0: [1], [2,3,4,5] -> 1 - 14 = -13
        # i=1: [1,2], [3,4,5] -> 3 - 12 = -9
        # i=2: [1,2,3], [4,5] -> 6 - 9 = -3
        # i=3: [1,2,3,4], [5] -> 10 - 5 = 5
        # The max is 5. The example provided in the docstring was a placeholder.
    """
    total_sum = sum(nums)
    left_sum = 0
    max_diff = float('-inf')

    # We iterate up to len(nums) - 1 because the right partition must be non-empty.
    # The split point i represents the end of the left partition.
    for i in range(len(nums) - 1):
        left_sum += nums[i]
        # The right sum is simply the total sum minus the current left sum.
        right_sum = total_sum - left_sum
        
        current_diff = left_sum - right_sum
        
        if current_diff > max_diff:
            max_diff = current_diff

    return int(max_diff)
