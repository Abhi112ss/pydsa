METADATA = {
    "id": 220,
    "name": "Contains Duplicate III",
    "slug": "contains_duplicate_iii",
    "category": "Array",
    "aliases": [],
    "tags": ["ordered_set", "bucket_sort", "sliding_window"],
    "difficulty": "hard",
    "time_complexity": "O(n)",
    "space_complexity": "O(min(n, k))",
    "description": "Given an integer array nums and two integers indexDiff and valueDiff, find two indices i and j such that abs(i - j) <= indexDiff and abs(nums[i] - nums[j]) <= valueDiff.",
}

def solve(nums: list[int], indexDiff: int, valueDiff: int) -> bool:
    """Determine if there exist two indices i and j such that abs(i - j) <= indexDiff and abs(nums[i] - nums[j]) <= valueDiff.

    Args:
        nums: The input array of integers.
        indexDiff: The maximum allowed difference between indices (k).
        valueDiff: The maximum allowed difference between values (t).

    Returns:
        True if such a pair exists, False otherwise.

    Examples:
        >>> solve([1, 2, 3, 1], 3, 0)
        True
        >>> solve([1, 5, 9, 1, 5, 9], 2, 3)
        False
    """
    if valueDiff < 0:
        return False

    bucket_width = valueDiff + 1
    buckets: dict[int, int] = {}

    for i, num in enumerate(nums):
        bucket_id = num // bucket_width

        # Check if current bucket already has a number
        if bucket_id in buckets:
            return True

        # Check adjacent buckets for numbers within valueDiff
        if bucket_id - 1 in buckets and abs(num - buckets[bucket_id - 1]) <= valueDiff:
            return True
        if bucket_id + 1 in buckets and abs(num - buckets[bucket_id + 1]) <= valueDiff:
            return True

        # Add current number to its bucket
        buckets[bucket_id] = num

        # Remove the number that falls outside the sliding window of size indexDiff
        if i >= indexDiff:
            old_bucket_id = nums[i - indexDiff] // bucket_width
            del buckets[old_bucket_id]

    return False