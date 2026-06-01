METADATA = {
    "id": 975,
    "name": "Odd Even Jump",
    "slug": "odd-even-jump",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dynamic programming", "sorting", "greedy", "monotonic stack"],
    "difficulty": "hard",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(n)",
    "description": "Determine if it is possible to reach the last index of an array following specific odd and even jump rules.",
}

def solve(arr: list[int]) -> bool:
    """
    Determines if it is possible to reach the last index of the array.

    The rules are:
    - Odd jumps: Jump to the smallest index j > i such that arr[j] >= arr[i].
    - Even jumps: Jump to the largest index j > i such that arr[j] <= arr[i].

    Args:
        arr: A list of integers representing the values at each index.

    Returns:
        True if the last index is reachable, False otherwise.

    Examples:
        >>> solve([10, 13, 2, 1, 20])
        True
        >>> solve([10, 13, 2, 1, 20, 2, 1])
        False
    """
    n = len(arr)
    if n <= 1:
        return True

    def get_next_indices(indices: list[int]) -> list[int]:
        """
        Uses a monotonic stack to find the next index for each element 
        based on the sorted order of values.
        """
        # Sort indices by value, then by index to handle duplicates correctly
        # For odd jumps (arr[j] >= arr[i]): we want smallest arr[j] where j > i
        # For even jumps (arr[j] <= arr[i]): we want largest arr[j] where j > i
        sorted_indices = sorted(indices, key=lambda i: (arr[i], i))
        
        next_indices = [-1] * n
        stack = []
        
        # Monotonic stack approach to find the 'next greater' index in the sorted sequence
        for idx in sorted_indices:
            while stack and idx > stack[-1]:
                # The current index 'idx' is the first index to the right of 
                # stack[-1] in the sorted value order.
                next_indices[stack.pop()] = idx
            stack.append(idx)
        return next_indices

    # odd_next[i] is the index we jump to on an odd jump from i
    # To find smallest arr[j] >= arr[i] with j > i:
    # Sort by value ascending, then index ascending. 
    # The next index in this sorted list that has a larger original index is our target.
    odd_next = get_next_indices(list(range(n)))

    # even_next[i] is the index we jump to on an even jump from i
    # To find largest arr[j] <= arr[i] with j > i:
    # Sort by value descending, then index ascending.
    # The next index in this sorted list that has a larger original index is our target.
    # We achieve this by negating values or reversing the sort logic.
    def get_even_next_indices(indices: list[int]) -> list[int]:
        # Sort by value descending, then index ascending
        sorted_indices = sorted(indices, key=lambda i: (-arr[i], i))
        next_indices = [-1] * n
        stack = []
        for idx in sorted_indices:
            while stack and idx > stack[-1]:
                next_indices[stack.pop()] = idx
            stack.append(idx)
        return next_indices

    even_next = get_even_next_indices(list(range(n)))

    # dp_odd[i] is True if we can reach the end starting from index i on an odd jump
    # dp_even[i] is True if we can reach the end starting from index i on an even jump
    dp_odd = [False] * n
    dp_even = [False] * n

    # Base case: the last index is the destination
    dp_odd[n - 1] = True
    dp_even[n - 1] = True

    # Fill DP tables backwards
    for i in range(n - 2, -1, -1):
        # Odd jump from i leads to an even jump from odd_next[i]
        if odd_next[i] != -1:
            dp_odd[i] = dp_even[odd_next[i]]
        
        # Even jump from i leads to an odd jump from even_next[i]
        if even_next[i] != -1:
            dp_even[i] = dp_odd[even_next[i]]

    # The problem starts with an odd jump from index 0
    return dp_odd[0]
