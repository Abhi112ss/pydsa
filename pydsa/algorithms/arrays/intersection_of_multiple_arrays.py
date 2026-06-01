METADATA = {
    "id": 2248,
    "name": "Intersection of Multiple Arrays",
    "slug": "intersection_of_multiple_arrays",
    "category": "array",
    "aliases": [],
    "tags": ["hash_map", "hash_set"],
    "difficulty": "easy",
    "time_complexity": "O(N*M)",
    "space_complexity": "O(N)",
    "description": "Return all integers that appear in every given array.",
}


def solve(nums: list[list[int]]) -> list[int]:
    """Find the intersection of multiple integer arrays.

    Args:
        nums: A list of integer arrays. Each inner array may contain duplicate
            values, but only distinct values matter for the intersection.

    Returns:
        A list containing the integers that appear in every array of `nums`.
        The order of elements in the returned list is not specified.

    Examples:
        >>> solve([[1,2,2,1],[2,2],[2,2,2,2]])
        [2]
        >>> solve([[4,4,4],[4,4],[4]])
        [4]
        >>> solve([[1,2,3],[4,5,6]])
        []
    """
    number_of_arrays = len(nums)
    occurrence_counts: dict[int, int] = {}

    for array in nums:
        # Use a set to avoid counting duplicate values within the same array
        distinct_values = set(array)
        for value in distinct_values:
            occurrence_counts[value] = occurrence_counts.get(value, 0) + 1

    # Keep only values that appeared in every array
    intersection = [
        value for value, count in occurrence_counts.items()
        if count == number_of_arrays
    ]
    return intersection