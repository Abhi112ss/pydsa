METADATA = {
    "id": 2444,
    "name": "Count Subarrays With Fixed Bounds",
    "slug": "count-subarrays-with-fixed-bounds",
    "category": "Array",
    "aliases": [],
    "tags": ["sliding_window", "two_pointer"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Count the number of subarrays where the minimum element is equal to minK and the maximum element is equal to maxK.",
}

def solve(nums: list[int], minK: int, maxK: int) -> int:
    """
    Counts the number of subarrays where the minimum element is exactly minK 
    and the maximum element is exactly maxK.

    Args:
        nums: A list of integers.
        minK: The required minimum value in the subarray.
        maxK: The required maximum value in the subarray.

    Returns:
        The total count of valid subarrays.

    Examples:
        >>> solve([1, 3, 5, 2, 7, 5], 1, 5)
        2
        >>> solve([1, 1, 1], 1, 1)
        6
    """
    total_count = 0
    # last_invalid tracks the index of the most recent element that is out of [minK, maxK]
    last_invalid = -1
    # last_min_k tracks the index of the most recent occurrence of minK
    last_min_k = -1
    # last_max_k tracks the index of the most recent occurrence of maxK
    last_max_k = -1

    for current_index, num in enumerate(nums):
        # If the current number is outside the allowed range, it breaks any potential subarray
        if num < minK or num > maxK:
            last_invalid = current_index
        
        # Update the most recent positions of the required boundary values
        if num == minK:
            last_min_k = current_index
        if num == maxK:
            last_max_k = current_index

        # The valid subarrays ending at current_index must start after the last_invalid index
        # and must include at least one minK and one maxK.
        # The leftmost possible start index for a valid subarray ending here is (last_invalid + 1).
        # The rightmost possible start index that ensures both minK and maxK are included 
        # is the minimum of the last seen minK and maxK positions.
        
        # The number of valid start positions is max(0, min(last_min_k, last_max_k) - last_invalid)
        start_boundary = min(last_min_k, last_max_k)
        
        if start_boundary > last_invalid:
            total_count += (start_boundary - last_invalid)

    return total_count
