METADATA = {
    "id": 3708,
    "name": "Longest Fibonacci Subarray",
    "slug": "longest_fibonacci_subarray",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["two_pointer", "dynamic_programming", "hash-table"],
    "difficulty": "medium",
    "time_complexity": "O(n^2)",
    "space_complexity": "O(n)",
    "description": "Find the length of the longest subarray that follows the Fibonacci sequence property where each element is the sum of the two preceding elements.",
}

def solve(arr: list[int]) -> int:
    """
    Finds the length of the longest subarray that follows the Fibonacci sequence.
    
    A Fibonacci-like subarray is defined such that for all i >= 2, 
    arr[i] = arr[i-1] + arr[i-2].

    Args:
        arr: A list of integers.

    Returns:
        The length of the longest Fibonacci-like subarray. Returns 0 if no 
        such subarray of length >= 3 exists.

    Examples:
        >>> solve([1, 2, 3, 5, 8, 13, 21])
        7
        >>> solve([1, 2, 3, 10, 13, 23])
        3
        >>> solve([1, 1, 1, 1])
        0
    """
    n = len(arr)
    if n < 3:
        return 0

    max_length = 0
    
    # We iterate through every possible starting pair (i, i+1)
    # and try to extend the Fibonacci sequence as far as possible.
    for start_index in range(n - 2):
        # Check if the first three elements form a Fibonacci sequence
        if arr[start_index] + arr[start_index + 1] == arr[start_index + 2]:
            current_length = 3
            prev_val = arr[start_index + 1]
            curr_val = arr[start_index + 2]
            
            # Extend the sequence greedily
            for next_index in range(start_index + 3, n):
                if arr[next_index] == prev_val + curr_val:
                    current_length += 1
                    prev_val = curr_val
                    curr_val = arr[next_index]
                else:
                    # The sequence is broken
                    break
            
            max_length = max(max_length, current_length)
            
    # The problem typically defines a Fibonacci sequence as having length >= 3
    return max_length if max_length >= 3 else 0
