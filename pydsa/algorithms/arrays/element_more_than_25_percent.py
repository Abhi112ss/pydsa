METADATA = {
    "id": 1287,
    "name": "Element Appearing More Than 25% In Sorted Array",
    "slug": "element-appearing-more-than-25-in-sorted-array",
    "category": "Arrays",
    "aliases": [],
    "tags": ["arrays", "binary_search"],
    "difficulty": "medium",
    "time_complexity": "O(log n)",
    "space_complexity": "O(1)",
    "description": "Find all elements in a sorted array that appear more than 25% of the time.",
}

def solve(nums: list[int]) -> list[int]:
    """
    Finds all elements in a sorted array that appear more than 25% of the time.

    Since the array is sorted, any element appearing more than 25% must occupy
    at least one of the indices at 1/4, 2/4, or 3/4 of the array's length.
    We can use binary search to find the first and last occurrence of these
    candidates to verify their frequency.

    Args:
        nums: A sorted list of integers.

    Returns:
        A list of integers that appear more than 25% of the time, sorted ascending.

    Examples:
        >>> solve([1, 2, 2, 2, 3])
        [2]
        >>> solve([1, 1, 1, 3, 3, 3, 4, 4, 4, 4])
        [4]
    """
    n = len(nums)
    threshold = n // 4
    candidates = set()

    # The elements that appear > 25% must be at these specific indices
    # because the array is sorted and the element spans more than 1/4 of the array.
    check_indices = [n // 4, n // 2, (3 * n) // 4]
    
    for idx in check_indices:
        if idx < n:
            candidates.add(nums[idx])

    def find_first(target: int, start: int, end: int) -> int:
        """Finds the first occurrence of target using binary search."""
        res = -1
        low, high = start, end
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                res = mid
                high = mid - 1
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return res

    def find_last(target: int, start: int, end: int) -> int:
        """Finds the last occurrence of target using binary search."""
        res = -1
        low, high = start, end
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                res = mid
                low = mid + 1
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return res

    result = []
    for candidate in sorted(list(candidates)):
        # For each candidate, find the range [first, last]
        first_idx = find_first(candidate, 0, n - 1)
        last_idx = find_last(candidate, 0, n - 1)
        
        # Check if the count (last - first + 1) exceeds the 25% threshold
        if (last_idx - first_idx + 1) > threshold:
            result.append(candidate)

    return result
