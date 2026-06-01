METADATA = {
    "id": 3516,
    "name": "Find Closest Person",
    "slug": "find_closest_person",
    "category": "Binary Search",
    "aliases": [],
    "tags": ["binary_search", "two_pointer"],
    "difficulty": "medium",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(1)",
    "description": "Find the person whose position is closest to the target position in a sorted list of positions.",
}

def solve(positions: list[int], target: int) -> int:
    """
    Finds the position in the list that is closest to the target value.
    If two positions are equally close, the smaller position is returned.

    Args:
        positions: A list of integers representing the positions of people.
        target: The target position to find the closest person to.

    Returns:
        The position from the list that is closest to the target.

    Examples:
        >>> solve([1, 2, 4, 8, 10], 5)
        4
        >>> solve([1, 2, 4, 8, 10], 6)
        4
        >>> solve([1, 5, 10], 7)
        5
    """
    if not positions:
        raise ValueError("The positions list cannot be empty.")

    # Ensure the positions are sorted to enable binary search
    # Note: If the problem guarantees sorted input, this can be omitted for O(log n)
    # but based on the prompt's complexity requirement, we assume sorting is part of the process.
    sorted_positions = sorted(positions)
    
    n = len(sorted_positions)
    left = 0
    right = n - 1
    
    # Standard binary search to find the insertion point
    while left <= right:
        mid = (left + right) // 2
        if sorted_positions[mid] == target:
            return sorted_positions[mid]
        elif sorted_positions[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    # After the loop, 'right' is the index of the largest element < target
    # and 'left' is the index of the smallest element > target.
    
    # If target is smaller than all elements
    if left == 0:
        return sorted_positions[0]
    
    # If target is larger than all elements
    if left == n:
        return sorted_positions[n - 1]

    # Compare the two neighbors to find the closest one
    # We check the distance to the element at 'right' and 'left'
    dist_left = abs(sorted_positions[right] - target)
    dist_right = abs(sorted_positions[left] - target)

    # If distances are equal, return the smaller position (the one at 'right')
    if dist_left <= dist_right:
        return sorted_positions[right]
    else:
        return sorted_positions[left]
