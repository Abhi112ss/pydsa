METADATA = {
    "id": 2210,
    "name": "Count Hills and Valleys in an Array",
    "slug": "count_hills_and_valleys_in_an_array",
    "category": "array",
    "aliases": [],
    "tags": ["array", "two_pointer"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Count the number of hills and valleys in an array after removing consecutive duplicates.",
}


def solve(nums: list[int]) -> int:
    """Count hills and valleys in the given integer array.

    Args:
        nums: List of integers representing the original array.

    Returns:
        The total number of hills and valleys after removing consecutive
        duplicate elements.

    Examples:
        >>> solve([1,2,2,3,2,2,1])
        2
        >>> solve([2,4,1,1,6,5])
        2
        >>> solve([1,1,1,1])
        0
    """
    # Remove consecutive duplicates in-place to keep O(1) extra space.
    unique = []
    for value in nums:
        if not unique or unique[-1] != value:
            unique.append(value)

    # A hill or valley requires three distinct consecutive points.
    if len(unique) < 3:
        return 0

    hill_valley_count = 0
    # Iterate over the middle elements and compare with neighbours.
    for index in range(1, len(unique) - 1):
        left = unique[index - 1]
        middle = unique[index]
        right = unique[index + 1]
        if middle > left and middle > right:
            hill_valley_count += 1  # hill
        elif middle < left and middle < right:
            hill_valley_count += 1  # valley

    return hill_valley_count