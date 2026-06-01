METADATA = {
    "id": 775,
    "name": "Global and Local Inversions",
    "slug": "global-and-local-inversions",
    "category": "Arrays",
    "aliases": [],
    "tags": ["arrays", "math"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Determine if all global inversions in an array are also local inversions.",
}

def solve(arr: list[int]) -> bool:
    """
    Determines if all global inversions in the array are also local inversions.
    
    A global inversion is a pair (i, j) such that i < j and arr[i] > arr[j].
    A local inversion is a pair (i, i + 1) such that arr[i] > arr[i + 1].
    
    The key insight is that a global inversion that is NOT local occurs if 
    arr[i] > arr[j] where j > i + 1. This can only happen if there is an 
    element at index i that is greater than an element at index i + 2 or further.
    Specifically, if arr[i] > arr[i + 2], then (i, i + 2) is a global inversion 
    that is not local.

    Args:
        arr: A list of integers representing the permutation.

    Returns:
        True if all global inversions are local, False otherwise.

    Examples:
        >>> solve([1, 0, 2, 3, 4])
        True
        >>> solve([1, 2, 0, 3])
        False
    """
    # A global inversion is not local if arr[i] > arr[j] for some j > i + 1.
    # This is equivalent to checking if there exists any i such that 
    # arr[i] > arr[i + 2]. If such a pair exists, we have a non-local global inversion.
    
    # We only need to check elements at distance 2.
    # If arr[i] > arr[i+2], then (i, i+2) is a global inversion but not a local one.
    for index in range(len(arr) - 2):
        if arr[index] > arr[index + 2]:
            return False
            
    return True
