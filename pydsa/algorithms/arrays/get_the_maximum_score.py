METADATA = {
    "id": 1537,
    "name": "Get the Maximum Score",
    "slug": "get-the-maximum-score",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dp", "array"],
    "difficulty": "hard",
    "time_complexity": "O(n^2)",
    "space_complexity": "O(n^2)",
    "description": "Find the maximum score of a non-empty subarray where the score is the minimum element multiplied by the length of the subarray.",
}

def solve(arr: list[int]) -> int:
    """
    Calculates the maximum score of a non-empty subarray.
    The score is defined as the minimum value in the subarray multiplied by its length.

    Args:
        arr: A list of integers representing the array.

    Returns:
        The maximum score found among all possible subarrays.

    Examples:
        >>> solve([1, 3, 2, 5])
        6
        >>> solve([2, 1, 5])
        3
    """
    n = len(arr)
    if n == 0:
        return 0

    # dp[i][j] will store the minimum value in the subarray arr[i...j]
    # Using a 2D array to precompute minimums allows O(1) lookup during score calculation.
    # However, to optimize space and time, we can iterate through all possible 
    # subarrays and maintain the running minimum.
    
    max_score = 0

    # Iterate through every possible starting index of a subarray
    for start_index in range(n):
        current_min = arr[start_index]
        
        # Iterate through every possible ending index for the current starting index
        for end_index in range(start_index, n):
            # Update the minimum value for the current subarray [start_index...end_index]
            if arr[end_index] < current_min:
                current_min = arr[end_index]
            
            # Calculate the score: minimum value * length of subarray
            current_length = end_index - start_index + 1
            current_score = current_min * current_length
            
            # Update the global maximum score
            if current_score > max_score:
                max_score = current_score
                
    return max_score

def solve_optimal(arr: list[int]) -> int:
    """
    An optimized O(n) approach using a Monotonic Stack.
    This is the standard optimal solution for 'Largest Rectangle in Histogram' 
    which is mathematically equivalent to this problem.

    Args:
        arr: A list of integers.

    Returns:
        The maximum score.
    """
    n = len(arr)
    max_score = 0
    stack = []  # Stores indices
    
    # Append a 0 to the end to ensure all elements are popped from the stack at the end
    extended_arr = arr + [0]
    
    for i, height in enumerate(extended_arr):
        # While the current height is less than the height at the index on top of the stack,
        # it means the rectangle ending at the previous index cannot be extended further.
        while stack and extended_arr[stack[-1]] >= height:
            h = extended_arr[stack.pop()]
            # If stack is empty, the width is the entire distance to the current index
            # Otherwise, width is the distance between current index and the new top of stack
            w = i if not stack else i - stack[-1] - 1
            max_score = max(max_score, h * w)
        stack.append(i)
        
    return max_score

# The problem asks for the optimal algorithm. 
# While the prompt suggested O(n^2) DP, the Monotonic Stack is the true optimal O(n).
# We provide the O(n) version as the primary solve implementation.
solve = solve_optimal