METADATA = {
    "id": 3224,
    "name": "Minimum Array Changes to Make Differences Equal",
    "slug": "minimum-array-changes-to-make-differences-equal",
    "category": "Arrays",
    "aliases": [],
    "tags": ["arrays", "greedy"],
    "difficulty": "medium",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(n)",
    "description": "Find the minimum number of changes to make all adjacent differences in an array equal.",
}

def solve(nums: list[int]) -> int:
    """
    Args:
        nums: A list of integers.

    Returns:
        The minimum number of changes required to make all adjacent differences equal.
    """
    n = len(nums)
    if n <= 2:
        return 0

    differences = []
    for i in range(n - 1):
        differences.append(abs(nums[i + 1] - nums[i]))

    diff_counts = {}
    for diff in differences:
        diff_counts[diff] = diff_counts.get(diff, 0) + 1

    max_frequency = 0
    for count in diff_counts.values():
        if count > max_frequency:
            max_frequency = count

    return (n - 1) - max_frequency