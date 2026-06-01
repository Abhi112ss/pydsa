METADATA = {
    "id": 496,
    "name": "Next Greater Element I",
    "slug": "next_greater_element_i",
    "category": "Stack",
    "aliases": ["next greater element", "NGE"],
    "tags": ["stack", "hash_map", "monotonic_stack"],
    "difficulty": "easy",
    "time_complexity": "O(n + m)",
    "space_complexity": "O(n)",
    "description": "For each element in nums1, find the next greater element to its right in nums2.",
}


def solve(nums1: list[int], nums2: list[int]) -> list[int]:
    """Find the next greater element for each element in nums1 as it appears in nums2.

    Uses a monotonic decreasing stack to precompute the next greater element
    for every value in nums2, then looks up results for nums1.

    Args:
        nums1: A subset of nums2. All elements are unique.
        nums2: The superset array. All elements are unique.

    Returns:
        A list where result[i] is the next greater element of nums1[i] in nums2,
        or -1 if no such element exists.

    Examples:
        >>> solve([4, 1, 2], [1, 3, 4, 2])
        [-1, 3, -1]
        >>> solve([2, 4], [1, 2, 3, 4])
        [3, -1]
    """
    # Build a map from each value in nums2 to its next greater element
    next_greater: dict[int, int] = {}
    stack: list[int] = []  # monotonic decreasing stack of values

    for current in nums2:
        # Pop all elements smaller than current — current is their next greater
        while stack and stack[-1] < current:
            next_greater[stack.pop()] = current
        stack.append(current)

    # Remaining elements in the stack have no next greater element
    while stack:
        next_greater[stack.pop()] = -1

    # Build the result by looking up each element of nums1
    return [next_greater[val] for val in nums1]