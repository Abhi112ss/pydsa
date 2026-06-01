METADATA = {
    "id": 1852,
    "name": "Distinct Numbers in Each Subarray",
    "slug": "distinct-numbers-in-each-subarray",
    "category": "Array",
    "aliases": [],
    "tags": ["sliding_window", "hash_map", "array"],
    "difficulty": "medium",
    "time_complexity": "O(n^2)",
    "space_complexity": "O(n)",
    "description": "Given an integer array nums and an integer k, return an array of size n-k+1 where each element is the number of distinct integers in every subarray of length k.",
}

def solve(nums: list[int], k: int) -> list[int]:
    """
    Calculates the number of distinct elements in every contiguous subarray of length k.

    Args:
        nums: A list of integers.
        k: The size of the sliding window.

    Returns:
        A list of integers representing the count of distinct elements in each window.

    Examples:
        >>> solve([1, 2, 1, 3, 4, 2, 3], 3)
        [2, 3, 3, 3, 3]
        >>> solve([1, 2, 1, 2, 1], 2)
        [2, 2, 2, 2]
    """
    n = len(nums)
    if n == 0 or k == 0:
        return []

    result = []
    # Frequency map to track counts of elements in the current window
    frequency_map: dict[int, int] = {}
    distinct_count = 0

    # Initialize the first window of size k
    for i in range(k):
        val = nums[i]
        if val not in frequency_map or frequency_map[val] == 0:
            distinct_count += 1
            frequency_map[val] = 1
        else:
            frequency_map[val] += 1
    
    result.append(distinct_count)

    # Slide the window from index 1 to n-k
    for i in range(k, n):
        # Element entering the window
        new_val = nums[i]
        if new_val not in frequency_map or frequency_map[new_val] == 0:
            distinct_count += 1
            frequency_map[new_val] = 1
        else:
            frequency_map[new_val] += 1

        # Element leaving the window
        old_val = nums[i - k]
        frequency_map[old_val] -= 1
        if frequency_map[old_val] == 0:
            distinct_count -= 1

        result.append(distinct_count)

    return result
