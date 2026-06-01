METADATA = {
    "id": 2563,
    "name": "Count the Number of Fair Pairs",
    "slug": "count-the-number-of-fair-pairs",
    "category": "Array",
    "aliases": [],
    "tags": ["binary_search", "two_pointer", "sorting"],
    "difficulty": "medium",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(1)",
    "description": "Count pairs (i, j) such that the difference between the minimum and maximum of the combined elements falls within a given range [lower, upper].",
}

def solve(nums: list[int], lower: int, upper: int) -> int:
    """
    Counts the number of fair pairs (i, j) where 0 <= i < j < n and
    lower <= max(nums[i], nums[j]) - min(nums[i], nums[j]) <= upper.

    The condition max(a, b) - min(a, b) is equivalent to abs(a - b).
    By sorting the array, for any pair (i, j) with i < j, the condition 
    becomes lower <= nums[j] - nums[i] <= upper.

    Args:
        nums: A list of integers.
        lower: The lower bound of the difference.
        upper: The upper bound of the difference.

    Returns:
        The total number of fair pairs.

    Examples:
        >>> solve([1, 2, 3, 4, 5], 1, 2)
        6
        >>> solve([1, 1, 1], 0, 0)
        3
    """
    nums.sort()
    n = len(nums)

    def count_pairs_with_max_diff(threshold: int) -> int:
        """
        Counts pairs (i, j) such that nums[j] - nums[i] <= threshold.
        Uses a two-pointer approach.
        """
        count = 0
        left = 0
        # For each right index, find the leftmost index 'left' such that
        # nums[right] - nums[left] <= threshold.
        # All indices between 'left' and 'right-1' will satisfy the condition.
        for right in range(n):
            while nums[right] - nums[left] > threshold:
                left += 1
            count += (right - left)
        return count

    # The number of pairs in [lower, upper] is:
    # (pairs with diff <= upper) - (pairs with diff <= lower - 1)
    return count_pairs_with_max_diff(upper) - count_pairs_with_max_diff(lower - 1)
