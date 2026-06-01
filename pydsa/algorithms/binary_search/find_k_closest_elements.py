METADATA = {
    "id": 658,
    "name": "Find K Closest Elements",
    "slug": "find-k-closest-elements",
    "category": "Binary Search",
    "aliases": [],
    "tags": ["binary_search", "two_pointer", "sorting"],
    "difficulty": "medium",
    "time_complexity": "O(log(n - k) + k)",
    "space_complexity": "O(1)",
    "description": "Find k closest integers to x in a sorted array.",
}

def solve(arr: list[int], k: int, x: int) -> list[int]:
    """
    Finds the k closest elements to x in a sorted array using binary search.

    The algorithm performs a binary search on the possible starting indices 
    of the k-length window. For a window starting at index 'mid', we compare 
    the distance of the element at 'mid' and the element at 'mid + k' to 
    determine if the window should shift left or right.

    Args:
        arr: A sorted list of integers.
        k: The number of elements to return.
        x: The target integer.

    Returns:
        A list of k integers that are closest to x, sorted in ascending order.

    Examples:
        >>> solve([1, 2, 3, 4, 5], 4, 3)
        [1, 2, 3, 4]
        >>> solve([1, 2, 3, 4, 5], 4, -1)
        [1, 2, 3, 4]
        >>> solve([1, 1, 1, 10, 10, 10], 1, 9)
        [10]
    """
    # The range of possible starting indices for a window of size k
    # is from 0 to len(arr) - k.
    low = 0
    high = len(arr) - k

    while low < high:
        mid = (low + high) // 2
        
        # We compare the element at mid with the element just outside 
        # the window on the right (mid + k).
        # If x is closer to arr[mid + k] than to arr[mid], 
        # then the window must start at an index greater than mid.
        # Note: The condition (x - arr[mid] > arr[mid + k] - x) 
        # handles the tie-breaking rule (prefer smaller element).
        if x - arr[mid] > arr[mid + k] - x:
            low = mid + 1
        else:
            high = mid

    # The binary search converges on the optimal starting index.
    return arr[low : low + k]
