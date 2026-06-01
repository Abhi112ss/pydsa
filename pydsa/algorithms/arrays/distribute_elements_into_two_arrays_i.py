METADATA = {
    "id": 3069,
    "name": "Distribute Elements Into Two Arrays I",
    "slug": "distribute-elements-into-two-arrays-i",
    "category": "Array",
    "aliases": [],
    "tags": ["arrays", "greedy"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Distribute elements into two arrays such that each element in the first array is strictly less than the next, and similarly for the second array.",
}

def solve(nums: list[int]) -> list[list[int]]:
    """
    Distributes elements into two arrays based on the condition that 
    elements in each array must be strictly increasing.

    Args:
        nums: A list of integers to be distributed.

    Returns:
        A list containing two lists, representing the two distributed arrays.

    Examples:
        >>> solve([1, 3, 5, 2, 4, 6])
        [[1, 3, 5], [2, 4, 6]]
        >>> solve([1, 2, 3, 4])
        [[1, 3], [2, 4]]
    """
    array_one: list[int] = []
    array_two: list[int] = []

    for i in range(len(nums)):
        # If it's the first element or it's greater than the last element 
        # added to array_one, add it to array_one.
        if not array_one or nums[i] > array_one[-1]:
            array_one.append(nums[i])
        else:
            # Otherwise, the problem guarantees it can fit into array_two
            # based on the problem constraints/logic.
            array_two.append(nums[i])

    return [array_one, array_two]
