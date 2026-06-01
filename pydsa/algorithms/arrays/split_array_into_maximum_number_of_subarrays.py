METADATA = {
    "id": 2871,
    "name": "Split Array Into Maximum Number of Subarrays",
    "slug": "split-array-into-maximum-number-of-subarrays",
    "category": "Arrays",
    "aliases": [],
    "tags": ["arrays", "greedy"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Split the array into the maximum number of subarrays such that the maximum element in each subarray is at least the subarray's minimum element.",
}

def solve(nums: list[int]) -> int:
    """
    Args:
        nums: A list of integers.

    Returns:
        The maximum number of subarrays that can be formed.
    """
    subarray_count = 0
    current_min = float('inf')
    current_max = float('-inf')

    for number in nums:
        if number < current_min:
            current_min = number
        if number > current_max:
            current_max = number

        if current_max >= current_min:
            subarray_count += 1
            current_min = float('inf')
            current_max = float('-inf')

    return subarray_count