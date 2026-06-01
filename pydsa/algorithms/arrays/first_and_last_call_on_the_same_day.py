METADATA = {
    "id": 1972,
    "name": "First and Last Call On the Same Day",
    "slug": "first-and-last-call-on-the-same-day",
    "category": "Binary Search",
    "aliases": [],
    "tags": ["binary_search", "array"],
    "difficulty": "medium",
    "time_complexity": "O(log n)",
    "space_complexity": "O(1)",
    "description": "Find the first and last index of a target day in a sorted array of call days.",
}

def solve(callDay: list[int], target: int) -> list[int]:
    """
    Finds the first and last occurrence of a target day in a sorted list.

    Args:
        callDay: A sorted list of integers representing the day of each call.
        target: The specific day to search for.

    Returns:
        A list of two integers [first_index, last_index]. 
        If the target is not found, returns [-1, -1].

    Examples:
        >>> solve([1, 2, 2, 2, 3], 2)
        [1, 3]
        >>> solve([1, 2, 2, 2, 3], 4)
        [-1, -1]
    """
    def find_first(arr: list[int], val: int) -> int:
        low, high = 0, len(arr) - 1
        first_idx = -1
        while low <= high:
            mid = (low + high) // 2
            if arr[mid] == val:
                first_idx = mid
                # Continue searching left to find the earliest occurrence
                high = mid - 1
            elif arr[mid] < val:
                low = mid + 1
            else:
                high = mid - 1
        return first_idx

    def find_last(arr: list[int], val: int) -> int:
        low, high = 0, len(arr) - 1
        last_idx = -1
        while low <= high:
            mid = (low + high) // 2
            if arr[mid] == val:
                last_idx = mid
                # Continue searching right to find the latest occurrence
                low = mid + 1
            elif arr[mid] < val:
                low = mid + 1
            else:
                high = mid - 1
        return last_idx

    # Perform two independent binary searches to find the boundaries
    first_occurrence = find_first(callDay, target)
    
    # If the first occurrence doesn't exist, the target isn't in the list
    if first_occurrence == -1:
        return [-1, -1]
        
    last_occurrence = find_last(callDay, target)
    
    return [first_occurrence, last_occurrence]
