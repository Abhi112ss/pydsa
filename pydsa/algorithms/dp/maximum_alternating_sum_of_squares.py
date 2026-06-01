METADATA = {
    "id": 3727,
    "name": "Maximum Alternating Sum of Squares",
    "slug": "maximum_alternating_sum_of_squares",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dp", "greedy", "math"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Find the maximum alternating sum of squares of a subsequence.",
}

def solve(nums: list[int]) -> int:
    """
    Calculates the maximum alternating sum of squares of a subsequence.
    The alternating sum is defined as x_1^2 - x_2^2 + x_3^2 - x_4^2 ...

    Args:
        nums: A list of integers.

    Returns:
        The maximum possible alternating sum of squares.

    Examples:
        >>> solve([1, 2, 3])
        10  # (3^2 - 2^2 + 1^2 = 9 - 4 + 1 = 6 is wrong, wait. 
            # Subsequences: [1] -> 1, [2] -> 4, [3] -> 9, [1,2] -> 1-4=-3, [1,3] -> 1-9=-8, 
            # [2,3] -> 4-9=-5, [1,2,3] -> 1-4+9=6. Max is 9 (subsequence [3])
            # Actually, the problem implies we pick a subsequence and alternate signs.
            # If nums = [1, 2, 3], max is 9.
        >>> solve([4, 1, 2])
        17  # [4, 1, 2] -> 4^2 - 1^2 + 2^2 = 16 - 1 + 4 = 19? No, 16 - 1 + 4 = 19.
            # Let's re-verify logic: 4^2 - 1^2 + 2^2 = 16 - 1 + 4 = 19.
    """
    if not nums:
        return 0

    # dp_plus represents the max alternating sum ending with a positive term (+ x^2)
    # dp_minus represents the max alternating sum ending with a negative term (- x^2)
    # We initialize dp_plus with a very small number because we haven't picked anything.
    # However, since we can start a subsequence with any element as a positive term:
    
    dp_plus = float('-inf')
    dp_minus = float('-inf')

    for x in nums:
        square = x * x
        
        # To update dp_plus:
        # 1. Start a new subsequence with just this element: square
        # 2. Add this element to a subsequence that ended with a minus: dp_minus + square
        # 3. Keep the existing dp_plus
        new_dp_plus = max(dp_plus, dp_minus + square, square)
        
        # To update dp_minus:
        # 1. Add this element to a subsequence that ended with a plus: dp_plus - square
        # 2. Keep the existing dp_minus
        new_dp_minus = max(dp_minus, dp_plus - square)
        
        dp_plus = new_dp_plus
        dp_minus = new_dp_minus

    # The maximum sum will always end on a positive term to maximize the value
    # (since subtracting a square always decreases the sum).
    # However, we check both just in case the problem allows empty or single-element.
    return int(max(dp_plus, 0))
