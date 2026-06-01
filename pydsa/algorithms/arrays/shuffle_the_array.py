METADATA = {
    "id": 1470,
    "name": "Shuffle the Array",
    "slug": "shuffle_the_array",
    "category": "array",
    "aliases": [],
    "tags": ["array"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Rearrange a 2n-length array by interleaving its two halves.",
}


def solve(nums: list[int], n: int) -> list[int]:
    """Shuffle the array by interleaving its two halves.

    Args:
        nums: A list of length 2 * n containing the elements to shuffle.
        n: The size of each half of the array.

    Returns:
        A new list where elements from the first half and second half are
        interleaved: [x1, y1, x2, y2, ..., xn, yn].

    Examples:
        >>> solve([2,5,1,3,4,7], 3)
        [2, 3, 5, 4, 1, 7]
        >>> solve([1,2,3,4,4,3,2,1], 4)
        [1, 4, 2, 3, 3, 2, 4, 1]
    """
    shuffled: list[int] = [0] * (2 * n)  # allocate result list

    # Place elements from the first half at even indices and second half at odd indices
    for index in range(n):
        shuffled[2 * index] = nums[index]          # element from first half
        shuffled[2 * index + 1] = nums[n + index]  # element from second half

    return shuffled