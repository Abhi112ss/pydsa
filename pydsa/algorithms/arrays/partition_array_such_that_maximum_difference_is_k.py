METADATA = {
    "id": 2294,
    "name": "Partition Array Such That Maximum Difference Is K",
    "slug": "partition-array-such-that-maximum-difference-is-k",
    "category": "Greedy",
    "aliases": [],
    "tags": ["greedy", "sorting"],
    "difficulty": "medium",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(1)",
    "description": "Partition an array into the minimum number of subarrays such that the difference between the maximum and minimum element in each subarray is at most k.",
}

def solve(nums: list[int], k: int) -> int:
    """
    Partitions the array into the minimum number of subarrays where the 
    difference between the max and min element in each subarray is <= k.

    Args:
        nums: A list of integers to be partitioned.
        k: The maximum allowed difference between the max and min in a subarray.

    Returns:
        The minimum number of subarrays required.

    Examples:
        >>> solve([1, 4, 10, 11, 12, 13, 15], 3)
        4
        >>> solve([1, 2, 3, 4, 5], 1)
        3
    """
    if not nums:
        return 0

    # Sorting allows us to group elements greedily. 
    # In a sorted array, the difference between max and min of a contiguous 
    # subarray is simply the difference between the last and first element.
    nums.sort()

    subarrays_count = 1
    current_subarray_start_val = nums[0]

    for i in range(1, len(nums)):
        # If the current element exceeds the allowed range relative to 
        # the start of the current subarray, we must start a new subarray.
        if nums[i] - current_subarray_start_val > k:
            subarrays_count += 1
            current_subarray_start_val = nums[i]

    return subarrays_count
