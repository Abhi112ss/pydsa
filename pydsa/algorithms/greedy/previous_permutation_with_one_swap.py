METADATA = {
    "id": 1053,
    "name": "Previous Permutation With One Swap",
    "slug": "previous_permutation_with_one_swap",
    "category": "Array",
    "aliases": [],
    "tags": ["greedy", "array_manipulation"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Find the largest lexicographically smaller permutation by performing exactly one swap.",
}

def solve(arr: list[int]) -> list[int]:
    """
    Finds the largest lexicographically smaller permutation by performing exactly one swap.

    The algorithm works by finding the first pair of adjacent elements (arr[i], arr[i+1]) 
    from the right such that arr[i] > arr[i+1]. This index 'i' is the pivot. 
    Then, we find the largest element to the right of 'i' that is strictly smaller 
    than arr[i] and swap them.

    Args:
        arr: A list of integers representing the current permutation.

    Returns:
        A list of integers representing the largest lexicographically smaller permutation.

    Examples:
        >>> solve([1, 2, 3])
        [1, 2, 3]
        >>> solve([3, 2, 1])
        [3, 1, 2]
        >>> solve([1, 9, 4, 6, 7])
        [1, 7, 4, 6, 9]
    """
    n = len(arr)
    if n <= 1:
        return arr

    # Step 1: Find the first index 'i' from the right such that arr[i] > arr[i+1]
    # This element is the one we need to swap to make the number smaller.
    pivot_index = -1
    for i in range(n - 2, -1, -1):
        if arr[i] > arr[i + 1]:
            pivot_index = i
            break

    # If no such index exists, the array is in non-decreasing order (smallest possible)
    if pivot_index == -1:
        return arr

    # Step 2: Find the largest element to the right of pivot_index that is smaller than arr[pivot_index]
    # To ensure we get the *largest* possible smaller permutation, we look for the 
    # largest value among those smaller than arr[pivot_index].
    # If there are duplicates, we pick the leftmost one among the largest candidates 
    # to maintain the largest possible value at the pivot position.
    swap_index = -1
    for j in range(n - 1, pivot_index, -1):
        if arr[j] < arr[pivot_index]:
            if swap_index == -1 or arr[j] >= arr[swap_index]:
                swap_index = j

    # Step 3: Perform the swap
    arr[pivot_index], arr[swap_index] = arr[swap_index], arr[pivot_index]

    return arr
