METADATA = {
    "id": 34,
    "name": "Find First and Last Position of Element in Sorted Array",
    "slug": "find-first-and-last-position-of-element-in-sorted-array",
    "category": "Arrays",
    "aliases": [],
    "tags": ["binary_search", "arrays"],
    "difficulty": "medium",
    "time_complexity": "O(log n)",
    "space_complexity": "O(1)",
    "description": "Find the starting and ending position of a given target value in a sorted array using binary search.",
}

def solve(nums: list[int], target: int) -> list[int]:
    """
    Finds the starting and ending position of a given target value in a sorted array.

    Args:
        nums: A sorted list of integers.
        target: The integer value to search for.

    Returns:
        A list of two integers [start_index, end_index]. 
        If target is not found, returns [-1, -1].

    Examples:
        >>> solve([5, 7, 7, 8, 8, 10], 8)
        [3, 4]
        >>> solve([5, 7, 7, 8, 8, 10], 6)
        [-1, -1]
        >>> solve([], 0)
        [-1, -1]
    """
    def find_bound(is_first: bool) -> int:
        low, high = 0, len(nums) - 1
        bound = -1
        
        while low <= high:
            mid = (low + high) // 2
            
            if nums[mid] == target:
                bound = mid
                # If searching for the first occurrence, narrow search to the left half
                if is_first:
                    high = mid - 1
                # If searching for the last occurrence, narrow search to the right half
                else:
                    low = mid + 1
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return bound

    # Perform two separate binary searches to find the boundaries
    start_index = find_bound(is_first=True)
    
    # If the start index is -1, the target doesn't exist, so no need to search for end
    if start_index == -1:
        return [-1, -1]
        
    end_index = find_bound(is_first=False)
    
    return [start_index, end_index]
