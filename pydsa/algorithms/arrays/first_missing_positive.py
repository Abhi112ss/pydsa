METADATA = {
    "id": 41,
    "name": "First Missing Positive",
    "slug": "first-missing-positive",
    "category": "Array",
    "aliases": [],
    "tags": ["hash_map", "array_manipulation", "cyclic_sort"],
    "difficulty": "hard",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Find the smallest positive integer that is not present in an unsorted integer array.",
}

def solve(nums: list[int]) -> int:
    """
    Finds the smallest positive integer missing from the array using cyclic sort.

    The algorithm treats the input array as a hash table where the value 'x' 
    is placed at index 'x - 1'. After rearranging, the first index 'i' 
    where nums[i] != i + 1 indicates that 'i + 1' is the missing number.

    Args:
        nums: A list of integers.

    Returns:
        The smallest positive integer not present in the list.

    Examples:
        >>> solve([1, 2, 0])
        3
        >>> solve([3, 4, -1, 1])
        2
        >>> solve([7, 8, 9, 11, 12])
        1
    """
    n = len(nums)

    # Cyclic Sort: Place each number x at its target index (x - 1)
    # We only care about numbers in the range [1, n]
    for i in range(n):
        # While the current number is in the valid range [1, n]
        # and it is not at its correct position (nums[i] != i + 1)
        # and the target position doesn't already have the correct number (to avoid infinite loop)
        while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
            # Swap nums[i] with the element at its target index
            target_idx = nums[i] - 1
            nums[i], nums[target_idx] = nums[target_idx], nums[i]

    # After sorting, the first index i where nums[i] != i + 1 
    # tells us that i + 1 is the missing positive integer
    for i in range(n):
        if nums[i] != i + 1:
            return i + 1

    # If all positions are correct, the missing number is n + 1
    return n + 1
