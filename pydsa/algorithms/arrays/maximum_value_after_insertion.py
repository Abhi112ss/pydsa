METADATA = {
    "id": 1881,
    "name": "Maximum Value after Insertion",
    "slug": "maximum-value-after-insertion",
    "category": "Array",
    "aliases": [],
    "tags": ["greedy", "arrays"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Find the maximum possible value of the sum of differences between adjacent elements after inserting exactly one element into an array.",
}

def solve(nums: list[int], x: int) -> int:
    """
    Args:
        nums: A list of integers.
        x: An integer to be inserted into the list.

    Returns:
        The maximum possible sum of absolute differences between adjacent elements.
    """
    n = len(nums)
    current_sum = 0
    for i in range(n - 1):
        current_sum += abs(nums[i] - nums[i + 1])

    max_additional_gain = -float('inf')

    for i in range(n - 1):
        gain = abs(nums[i] - x) + abs(x - nums[i + 1]) - abs(nums[i] - nums[i + 1])
        if gain > max_additional_gain:
            max_additional_gain = gain

    start_gain = abs(nums[0] - x)
    if start_gain > max_additional_gain:
        max_additional_gain = start_gain

    end_gain = abs(nums[n - 1] - x)
    if end_gain > max_additional_gain:
        max_additional_gain = end_gain

    return int(current_sum + max_additional_gain)