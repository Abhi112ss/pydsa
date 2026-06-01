METADATA = {
    "id": 287,
    "name": "Find the Duplicate Number",
    "slug": "find-the-duplicate-number",
    "category": "Array",
    "aliases": [],
    "tags": ["floyds_cycle_detection", "binary_search", "two_pointer"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Find the duplicate number in an array of n+1 integers where each integer is between 1 and n inclusive.",
}

def solve(nums: list[int]) -> int:
    """
    Finds the duplicate number in an array using Floyd's Cycle-Finding Algorithm.
    
    The array is treated as a linked list where the value at each index points 
    to the next index. Since there is a duplicate, a cycle must exist.

    Args:
        nums: A list of n+1 integers where each integer is in the range [1, n].

    Returns:
        The duplicate integer found in the list.

    Examples:
        >>> solve([1, 3, 4, 2, 2])
        2
        >>> solve([3, 1, 3, 4, 2])
        3
    """
    # Phase 1: Finding the intersection point in the cycle
    # We use two pointers: slow moves one step, fast moves two steps.
    slow_pointer = nums[0]
    fast_pointer = nums[0]

    while True:
        slow_pointer = nums[slow_pointer]
        fast_pointer = nums[nums[fast_pointer]]
        if slow_pointer == fast_pointer:
            break

    # Phase 2: Finding the entrance to the cycle (the duplicate)
    # Reset one pointer to the start; move both at the same speed.
    # The point where they meet is the start of the cycle.
    slow_pointer = nums[0]
    while slow_pointer != fast_pointer:
        slow_pointer = nums[slow_pointer]
        fast_pointer = nums[fast_pointer]

    return slow_pointer
