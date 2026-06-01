METADATA = {
    "id": 2832,
    "name": "Maximal Range That Each Element Is Maximum in It",
    "slug": "maximal-range-that-each-element-is-maximum-in-it",
    "category": "Arrays",
    "aliases": [],
    "tags": ["monotonic_stack", "arrays"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Find the maximum length of a contiguous subarray where a specific element is the maximum value.",
}

def solve(nums: list[int]) -> int:
    """
    Finds the maximum length of a subarray where at least one element is the maximum.

    The problem asks for the maximum range [L, R] such that for some index i, 
    nums[i] is the maximum in nums[L...R]. This is equivalent to finding the 
    largest range for each element where it remains the maximum.

    Args:
        nums: A list of integers.

    Returns:
        The maximum length of such a range.

    Examples:
        >>> solve([1, 2, 3, 2, 1])
        5
        >>> solve([1, 1, 1, 1])
        4
        >>> solve([5, 4, 3, 2, 1])
        1
    """
    n = len(nums)
    if n == 0:
        return 0

    # left_boundary[i] will store the index of the first element to the left 
    # that is strictly greater than nums[i].
    left_boundary = [-1] * n
    # right_boundary[i] will store the index of the first element to the right 
    # that is strictly greater than nums[i].
    right_boundary = [n] * n

    # Monotonic stack to find the nearest larger element to the left
    stack: list[int] = []
    for i in range(n):
        while stack and nums[stack[-1]] <= nums[i]:
            stack.pop()
        if stack:
            left_boundary[i] = stack[-1]
        stack.append(i)

    # Clear stack to reuse for the right side
    stack.clear()

    # Monotonic stack to find the nearest larger element to the right
    for i in range(n - 1, -1, -1):
        while stack and nums[stack[-1]] <= nums[i]:
            stack.pop()
        if stack:
            right_boundary[i] = stack[-1]
        stack.append(i)

    # The range for which nums[i] is the maximum is (left_boundary[i], right_boundary[i])
    # The length of this range is (right_boundary[i] - 1) - (left_boundary[i] + 1) + 1
    # which simplifies to right_boundary[i] - left_boundary[i] - 1
    max_length = 0
    for i in range(n):
        current_range_length = right_boundary[i] - left_boundary[i] - 1
        if current_range_length > max_length:
            max_length = current_range_length

    return max_length
