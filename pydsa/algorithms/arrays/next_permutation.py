METADATA = {
    "id": 31,
    "name": "Next Permutation",
    "slug": "next_permutation",
    "category": "Arrays",
    "aliases": [],
    "tags": ["two_pointer", "arrays"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Finds the next lexicographically greater permutation of a sequence of numbers.",
}

def solve(nums: list[int]) -> None:
    """
    Modifies the input list in-place to the next lexicographical permutation.
    If no such permutation exists, it rearranges it as the lowest possible order (sorted ascending).

    Args:
        nums: A list of integers representing the current permutation.

    Returns:
        None. The list is modified in-place.

    Examples:
        >>> nums = [1, 2, 3]
        >>> solve(nums)
        >>> nums
        [1, 3, 2]

        >>> nums = [3, 2, 1]
        >>> solve(nums)
        >>> nums
        [1, 2, 3]

        >>> nums = [1, 1, 5]
        >>> solve(nums)
        >>> nums
        [1, 5, 1]
    """
    n = len(nums)
    if n <= 1:
        return

    # Step 1: Find the first pair from the right where nums[i] < nums[i + 1]
    # This index 'i' is the pivot that needs to be incremented to get the next permutation.
    pivot_index = -1
    for i in range(n - 2, -1, -1):
        if nums[i] < nums[i + 1]:
            pivot_index = i
            break

    # If no such index is found, the sequence is in descending order (last permutation).
    # We simply reverse the whole list to get the first permutation.
    if pivot_index == -1:
        nums.reverse()
        return

    # Step 2: Find the smallest element to the right of the pivot that is greater than nums[pivot_index].
    # Since the suffix is in descending order, the first element from the right 
    # that is greater than nums[pivot_index] is the smallest one we need.
    for i in range(n - 1, pivot_index, -1):
        if nums[i] > nums[pivot_index]:
            # Swap the pivot with this element
            nums[pivot_index], nums[i] = nums[i], nums[pivot_index]
            break

    # Step 3: Reverse the suffix starting from pivot_index + 1.
    # The suffix was in descending order; reversing it makes it ascending,
    # which is the smallest possible lexicographical order for that suffix.
    left, right = pivot_index + 1, n - 1
    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1
