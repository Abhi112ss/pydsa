METADATA = {
    "id": 1,
    "name": "Two Sum",
    "slug": "two_sum",
    "category": "Array",
    "aliases": [],
    "tags": ["hash_map", "array"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Given an array of integers and an integer target, return indices of the two numbers such that they add up to target.",
}


def solve(nums: list[int], target: int) -> list[int]:
    """
    Finds two numbers in an array that add up to a specific target.

    This function iterates through the array, and for each number, it calculates
    the complement needed to reach the target. It then checks if this complement
    has already been seen and stored in a hash map. If found, it returns the
    indices of the two numbers. If not, it stores the current number and its
    index in the hash map for future lookups.

    Args:
        nums: A list of integers.
        target: The integer target sum.

    Returns:
        A list of two integers, representing the 0-based indices of the two
        numbers that sum up to the target. It is guaranteed that exactly one
        solution exists.

    Examples:
        >>> solve([2, 7, 11, 15], 9)
        [0, 1]
        >>> solve([3, 2, 4], 6)
        [1, 2]
        >>> solve([3, 3], 6)
        [0, 1]
    """
    # A hash map (dictionary in Python) to store numbers and their indices.
    # Key: number, Value: index
    num_map: dict[int, int] = {}

    for current_index, number in enumerate(nums):
        # Calculate the complement needed to reach the target sum.
        complement = target - number

        # Check if the complement already exists in our hash map.
        # If it does, we've found the two numbers that sum to the target.
        if complement in num_map:
            # Return the index of the complement and the current number's index.
            return [num_map[complement], current_index]

        # If the complement is not found, add the current number and its index
        # to the hash map for future lookups.
        num_map[number] = current_index

    # The problem guarantees that exactly one solution exists, so this line
    # should theoretically not be reached.
    return []