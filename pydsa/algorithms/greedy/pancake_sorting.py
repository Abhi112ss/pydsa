METADATA = {
    "id": 969,
    "name": "Pancake Sorting",
    "slug": "pancake-sorting",
    "category": "Sorting",
    "aliases": [],
    "tags": ["sorting", "greedy"],
    "difficulty": "medium",
    "time_complexity": "O(n^2)",
    "space_complexity": "O(n)",
    "description": "Sort an array using only prefix reversals (flips) by repeatedly moving the largest unsorted element to its correct position.",
}

def solve(arr: list[int]) -> list[list[int]]:
    """
    Sorts the array using the pancake sorting algorithm.

    The algorithm works by finding the largest element in the unsorted portion,
    flipping it to the front of the array, and then flipping it to its 
    target position at the end of the unsorted portion.

    Args:
        arr: A list of integers representing the unsorted array.

    Returns:
        A list of lists, where each inner list contains the k-th flip (1-indexed).

    Examples:
        >>> solve([3, 2, 4, 1])
        [[3, 4], [1, 2], [3, 4]]
    """
    flips = []
    n = len(arr)

    def flip(k: int) -> None:
        """Helper to reverse the prefix of the array up to index k (0-indexed)."""
        left, right = 0, k
        while left < right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1

    # Iterate from the end of the array to the beginning
    for current_size in range(n, 1, -1):
        # Find the index of the maximum element in the unsorted prefix [0...current_size-1]
        max_idx = 0
        for i in range(1, current_size):
            if arr[i] > arr[max_idx]:
                max_idx = i

        # If the max element is already at its correct position, skip
        if max_idx == current_size - 1:
            continue

        # Step 1: If the max element is not at the front, flip it to the front
        if max_idx != 0:
            flip(max_idx)
            flips.append([max_idx + 1])

        # Step 2: Flip the max element from the front to its target position
        flip(current_size - 1)
        flips.append([current_size])

    return flips
