METADATA = {
    "id": 1389,
    "name": "Create Target Array in the Given Order",
    "slug": "create_target_array_in_the_given_order",
    "category": "array",
    "aliases": [],
    "tags": ["array", "simulation"],
    "difficulty": "easy",
    "time_complexity": "O(n^2)",
    "space_complexity": "O(n)",
    "description": "Construct target array by inserting elements at specified positions.",
}


def solve(nums: list[int], index: list[int]) -> list[int]:
    """Create target array by inserting each element of ``nums`` at the
    corresponding position from ``index``.

    Args:
        nums: List of integers to be placed into the target array.
        index: List of positions where each element of ``nums`` should be inserted.

    Returns:
        A new list representing the target array after all insertions.

    Examples:
        >>> solve([0,1,2,3,4], [0,1,2,2,1])
        [0,4,1,3,2]
        >>> solve([1,2,3,4,0], [0,1,2,3,0])
        [0,1,2,3,4]
    """
    target: list[int] = []
    # Iterate over paired values and positions; list.insert shifts elements rightward.
    for value, position in zip(nums, index):
        target.insert(position, value)
    return target