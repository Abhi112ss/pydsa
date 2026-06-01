METADATA = {
    "id": 1950,
    "name": "Maximum of Minimum Values in All Subarrays",
    "slug": "maximum-of-minimum-values-in-all-subarrays",
    "category": "Array",
    "aliases": [],
    "tags": ["monotonic_stack", "greedy", "array"],
    "difficulty": "hard",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Find the maximum of the minimum values for all possible subarray lengths from 1 to n.",
}

def solve(arr: list[int]) -> list[int]:
    """
    Calculates the maximum of minimum values for all subarray lengths from 1 to n.

    The algorithm uses a monotonic stack to determine the largest window in which 
    each element acts as the minimum value. It then uses a dynamic programming 
    approach to propagate these maximums to smaller window sizes.

    Args:
        arr: A list of integers representing the input array.

    Returns:
        A list of integers where the i-th element (0-indexed) is the maximum 
        minimum value for all subarrays of length i + 1.

    Examples:
        >>> solve([1, 2, 3, 4, 5])
        [5, 4, 3, 2, 1]
        >>> solve([3, 1, 3, 4, 2])
        [4, 3, 2, 1, 1]
    """
    n = len(arr)
    if n == 0:
        return []

    # left[i] stores the index of the first element to the left of i that is smaller than arr[i]
    # right[i] stores the index of the first element to the right of i that is smaller than arr[i]
    left = [-1] * n
    right = [n] * n
    stack: list[int] = []

    # Find the nearest smaller element to the left using a monotonic stack
    for i in range(n):
        while stack and arr[stack[-1]] >= arr[i]:
            stack.pop()
        if stack:
            left[i] = stack[-1]
        stack.append(i)

    stack.clear()

    # Find the nearest smaller element to the right using a monotonic stack
    for i in range(n - 1, -1, -1):
        while stack and arr[stack[-1]] >= arr[i]:
            stack.pop()
        if stack:
            right[i] = stack[-1]
        stack.append(i)

    # ans[len] will store the maximum minimum value for a subarray of length 'len'
    # We use 1-based indexing for length to match problem logic easily
    ans = [0] * (n + 1)

    # For each element, calculate the length of the largest subarray where it is the minimum
    # The length is (right_index - left_index - 1)
    for i in range(n):
        window_len = right[i] - left[i] - 1
        ans[window_len] = max(ans[window_len], arr[i])

    # Some window lengths might not have been filled. 
    # If a value is the minimum for a window of size k, it is also a candidate 
    # for a window of size k-1. We propagate the maximums backwards.
    for i in range(n - 1, 0, -1):
        ans[i] = max(ans[i], ans[i + 1])

    # Return results from length 1 to n
    return ans[1:]
