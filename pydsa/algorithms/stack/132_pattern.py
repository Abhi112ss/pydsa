METADATA = {
    "id": 456,
    "name": "132 Pattern",
    "slug": "132-pattern",
    "category": "Stack",
    "aliases": [],
    "tags": ["stack", "monotonic_stack", "greedy"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Find if there exists a subsequence of three indices i < j < k such that nums[i] < nums[k] < nums[j].",
}

def solve(nums: list[int]) -> bool:
    """
    Determines if there exists a 132 pattern in the given list of integers.
    
    A 132 pattern is a subsequence of three elements nums[i], nums[j], nums[k] 
    such that i < j < k and nums[i] < nums[k] < nums[j].

    Args:
        nums: A list of integers.

    Returns:
        True if a 132 pattern exists, False otherwise.

    Examples:
        >>> solve([1, 2, 3, 4])
        False
        >>> solve([3, 1, 4, 2])
        True
        >>> solve([-1, 3, 2, 0])
        True
    """
    if len(nums) < 3:
        return False

    # 'second_largest' represents the 'k' in the 132 pattern (nums[k]).
    # We want to find the largest possible 'k' that is smaller than some 'j' (nums[j]).
    # By maximizing 'k', we make it easier to find an 'i' (nums[i]) such that nums[i] < k.
    second_largest = float('-inf')
    stack: list[int] = []

    # Iterate backwards to treat the current element as a potential 'j' (the peak).
    # The stack will maintain potential 'k' values in a monotonic decreasing order.
    for i in range(len(nums) - 1, -1, -1):
        # If we find an element smaller than our best 'k', we found the 'i' in 132.
        if nums[i] < second_largest:
            return True

        # If the current element is greater than the top of the stack, 
        # the stack top is a candidate for 'k' and the current element is 'j'.
        # We pop elements to ensure 'second_largest' is the largest possible 'k' 
        # that is still smaller than the current 'j'.
        while stack and nums[i] > stack[-1]:
            second_largest = stack.pop()

        # Push the current element onto the stack as a potential 'j' for future iterations.
        stack.append(nums[i])

    return False
