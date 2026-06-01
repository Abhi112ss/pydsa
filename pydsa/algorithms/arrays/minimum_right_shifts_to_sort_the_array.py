METADATA = {
    "id": 2855,
    "name": "Minimum Right Shifts to Sort the Array",
    "slug": "minimum-right-shifts-to-sort-the-array",
    "category": "Arrays",
    "aliases": [],
    "tags": ["arrays", "sorting"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Find the minimum number of right shifts required to make a circularly sorted array sorted in non-decreasing order.",
}

def solve(nums: list[int]) -> int:
    """
    Calculates the minimum number of right shifts to make the array sorted.

    A circularly sorted array is an array that was originally sorted and then 
    rotated some number of times. If the array is already sorted, 0 shifts 
    are needed. Otherwise, the number of shifts is the count of elements 
    from the point of decrease to the end of the array.

    Args:
        nums: A list of integers representing the circularly sorted array.

    Returns:
        The minimum number of right shifts required to sort the array. 
        Returns -1 if it is impossible to sort the array with shifts.

    Examples:
        >>> solve([3, 4, 5, 1, 2])
        2
        >>> solve([2, 1, 3, 4])
        -1
        >>> solve([1, 2, 3])
        0
    """
    n = len(nums)
    decrease_count = 0
    decrease_index = -1

    for i in range(n):
        # Check if the current element is greater than the next element (circularly)
        # We use (i + 1) % n to compare the last element with the first element
        if nums[i] > nums[(i + 1) % n]:
            decrease_count += 1
            decrease_index = i

    # If there is more than one point where the order decreases, 
    # it's not a circularly sorted array.
    if decrease_count > 1:
        return -1

    # If there are no decreases, the array is already sorted.
    if decrease_count == 0:
        return 0

    # If there is exactly one decrease, the number of right shifts needed 
    # to bring the smallest element to the front is the number of elements 
    # after the decrease point.
    # In a right shift, the element at index (i+1) moves to index i.
    # To make the array sorted, the element at (decrease_index + 1) must move to index 0.
    # The number of elements to the right of the decrease point is n - 1 - decrease_index.
    # However, since we are looking for the number of right shifts to make it 
    # [nums[i+1], ..., nums[n-1], nums[0], ..., nums[i]], 
    # the number of shifts is actually (n - 1 - decrease_index).
    # Wait, let's re-verify: [3, 4, 5, 1, 2]. i=2 (nums[2]=5 > nums[3]=1). 
    # n=5, i=2. Shifts = 5 - 1 - 2 = 2. Correct.
    return n - 1 - decrease_index
