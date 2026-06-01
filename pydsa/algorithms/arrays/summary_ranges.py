METADATA = {
    "id": 228,
    "name": "Summary Ranges",
    "slug": "summary_ranges",
    "category": "Array",
    "aliases": [],
    "tags": ["arrays"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Given a sorted unique integer array, return the smallest sorted list of ranges that cover all the numbers exactly.",
}

def solve(nums: list[int]) -> list[str]:
    """Return the smallest sorted list of ranges covering all numbers in a sorted unique array.

    Args:
        nums: A sorted list of unique integers.

    Returns:
        A list of strings representing the summary ranges.

    Examples:
        >>> solve([0, 1, 2, 4, 5, 7])
        ['0->2', '4->5', '7']
        >>> solve([0, 2, 3, 4, 6, 8, 9])
        ['0', '2->4', '6', '8->9']
        >>> solve([])
        []
    """
    if not nums:
        return []

    result: list[str] = []
    range_start: int = nums[0]

    for index in range(1, len(nums)):
        # Check if current element breaks the contiguous sequence
        if nums[index] != nums[index - 1] + 1:
            # End the current range and format it
            if range_start == nums[index - 1]:
                result.append(str(range_start))
            else:
                result.append(f"{range_start}->{nums[index - 1]}")
            # Start a new range from the current element
            range_start = nums[index]

    # Handle the last range after the loop ends
    if range_start == nums[-1]:
        result.append(str(range_start))
    else:
        result.append(f"{range_start}->{nums[-1]}")

    return result