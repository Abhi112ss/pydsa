METADATA = {
    "id": 873,
    "name": "Length of Longest Fibonacci Subsequence",
    "slug": "length-of-longest-fibonacci-subsequence",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["hash_map", "dynamic_programming"],
    "difficulty": "medium",
    "time_complexity": "O(n^2)",
    "space_complexity": "O(n^2)",
    "description": "Find the length of the longest subsequence that follows the Fibonacci rule where each term is the sum of the two preceding terms.",
}

def solve(arr: list[int]) -> int:
    """
    Finds the length of the longest Fibonacci-like subsequence in a given array.

    A subsequence is Fibonacci-like if for all i > 1, seq[i] = seq[i-1] + seq[i-2].

    Args:
        arr: A strictly increasing list of integers.

    Returns:
        The length of the longest Fibonacci-like subsequence. Returns 0 if no such 
        subsequence exists with length >= 3.

    Examples:
        >>> solve([1, 2, 3, 4, 5, 6, 7, 8])
        5
        >>> solve([1, 2, 3, 4, 5, 6, 7, 8]) # Sequence: 1, 2, 3, 5, 8
        >>> solve([1, 3, 7, 11, 12, 14, 18])
        0
    """
    n = len(arr)
    # Map value to its index for O(1) lookup
    index_map = {val: i for i, val in enumerate(arr)}
    
    # dp[j, i] stores the length of the Fibonacci sequence ending with arr[j] and arr[i]
    # where j < i.
    dp: dict[tuple[int, int], int] = {}
    max_len = 0

    # Iterate through all possible pairs (j, i) as the last two elements of a sequence
    for i in range(n):
        for j in range(i):
            # We need to find if there exists an element 'prev_val' such that
            # prev_val + arr[j] == arr[i] => prev_val = arr[i] - arr[j]
            prev_val = arr[i] - arr[j]
            
            # The sequence must be strictly increasing, so prev_val must be < arr[j]
            if prev_val < arr[j] and prev_val in index_map:
                k = index_map[prev_val]
                
                # If a sequence ending in (k, j) exists, extend it to (j, i)
                # Otherwise, the sequence (k, j, i) has length 3
                current_len = dp.get((k, j), 2) + 1
                dp[(j, i)] = current_len
                max_len = max(max_len, current_len)

    return max_len if max_len >= 3 else 0
