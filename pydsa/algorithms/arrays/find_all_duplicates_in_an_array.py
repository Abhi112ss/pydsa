METADATA = {
    "id": 442,
    "name": "Find All Duplicates in an Array",
    "slug": "find-all-duplicates-in-an-array",
    "category": "Array",
    "aliases": [],
    "tags": ["hash_map", "in_place"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Given an integer array nums of length n where all the integers of nums are in the range [1, n] and each integer appears once or twice, return an array of all the integers that appear twice.",
}

def solve(nums: list[int]) -> list[int]:
    """
    Finds all integers that appear twice in an array where elements are in range [1, n].

    The algorithm uses the input array itself as a hash table by treating the 
    values as indices. By negating the value at the index corresponding to 
    the current number, we can mark that the number has been seen.

    Args:
        nums: A list of integers where each integer is in the range [1, len(nums)].

    Returns:
        A list of integers that appear twice in the input array.

    Examples:
        >>> solve([1, 2, 2, 3])
        [2]
        >>> solve([4, 3, 2, 7, 8, 2, 3, 1])
        [2, 3]
    """
    duplicates = []

    for current_value in nums:
        # Use absolute value because the element at this index might have been negated
        index_to_check = abs(current_value) - 1

        # If the value at the target index is negative, we have seen this number before
        if nums[index_to_check] < 0:
            duplicates.append(abs(current_value))
        else:
            # Mark the number as seen by negating the value at its corresponding index
            nums[index_to_check] = -nums[index_to_check]

    return duplicates
