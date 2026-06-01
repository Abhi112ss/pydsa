METADATA = {
    "id": 164,
    "name": "Maximum Gap",
    "slug": "maximum-gap",
    "category": "Array",
    "aliases": [],
    "tags": ["bucket_sort", "sorting", "math"],
    "difficulty": "hard",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Find the maximum difference between successive elements in a sorted array of integers in linear time and space.",
}

def solve(nums: list[int]) -> int:
    """
    Finds the maximum gap between successive elements in a sorted version of the input array.
    
    Uses the Bucket Sort (Pigeonhole Principle) approach to achieve O(n) time complexity.
    The logic is that the maximum gap must be at least ceil((max - min) / (n - 1)).
    By setting bucket size to this minimum possible gap, we only need to compare 
    the distance between the maximum of one bucket and the minimum of the next non-empty bucket.

    Args:
        nums: A list of integers.

    Returns:
        The maximum gap between successive elements in the sorted array. 
        Returns 0 if the array has fewer than 2 elements.

    Examples:
        >>> solve([3, 6, 9, 1])
        3
        >>> solve([10])
        0
    """
    n = len(nums)
    if n < 2:
        return 0

    min_val = min(nums)
    max_val = max(nums)

    if min_val == max_val:
        return 0

    # Calculate the minimum possible maximum gap using Pigeonhole Principle
    # gap = ceil((max - min) / (n - 1))
    bucket_size = max(1, (max_val - min_val) // (n - 1))
    num_buckets = (max_val - min_val) // bucket_size + 1

    # We only need to track the min and max within each bucket
    bucket_mins = [float('inf')] * num_buckets
    bucket_maxs = [float('-inf')] * num_buckets
    bucket_used = [False] * num_buckets

    for x in nums:
        # Determine which bucket the number belongs to
        idx = (x - min_val) // bucket_size
        bucket_mins[idx] = min(bucket_mins[idx], x)
        bucket_maxs[idx] = max(bucket_maxs[idx], x)
        bucket_used[idx] = True

    max_gap = 0
    previous_max = min_val

    # Iterate through buckets to find the gap between the current bucket's min 
    # and the previous non-empty bucket's max.
    for i in range(num_buckets):
        if not bucket_used[i]:
            continue
        
        # The gap is the distance between the current bucket's minimum 
        # and the maximum value of the last seen non-empty bucket.
        max_gap = max(max_gap, bucket_mins[i] - previous_max)
        previous_max = bucket_maxs[i]

    return max_gap
