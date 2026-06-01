METADATA = {
    "id": 2677,
    "name": "Chunk Array",
    "slug": "chunk_array",
    "category": "Array",
    "aliases": [],
    "tags": ["Array", "Simulation"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Split the input array into subarrays of a given size.",
}


def solve(nums: list[int], size: int) -> list[list[int]]:
    """Split an array into chunks of a given size.

    Args:
        nums: List of integers to be chunked.
        size: Desired maximum size of each chunk (size > 0).

    Returns:
        A list of sublists where each sublist contains at most `size` elements
        from `nums` in the original order.

    Examples:
        >>> solve([1, 2, 3, 4, 5], 2)
        [[1, 2], [3, 4], [5]]
        >>> solve([7, 8, 9], 3)
        [[7, 8, 9]]
    """
    # Iterate over the array with a step equal to the chunk size and slice.
    chunked: list[list[int]] = []
    for start_index in range(0, len(nums), size):
        chunked.append(nums[start_index:start_index + size])
    return chunked