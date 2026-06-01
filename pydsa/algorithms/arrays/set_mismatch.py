METADATA = {
    "id": 645,
    "name": "Set Mismatch",
    "slug": "set-mismatch",
    "category": "Math",
    "aliases": [],
    "tags": ["hash_map", "math", "array"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Find the duplicate number and the missing number in an array containing numbers from 1 to n.",
}

def solve(nums: list[int]) -> list[int]:
    """
    Finds the duplicate and missing numbers in an array containing 1 to n.

    The algorithm uses the mathematical property of sums and sums of squares
    to solve the problem in O(n) time and O(1) space.
    
    Let S be the sum of numbers 1 to n, and S2 be the sum of squares 1 to n.
    Let A be the actual sum of nums, and A2 be the actual sum of squares of nums.
    Let x be the duplicate number and y be the missing number.
    
    A - S = x - y
    A2 - S2 = x^2 - y^2 = (x - y)(x + y)
    
    From these, we can derive:
    x - y = diff1
    x + y = diff2 / diff1
    x = (diff1 + (diff2 / diff1)) / 2
    y = x - diff1

    Args:
        nums: A list of integers representing the input array.

    Returns:
        A list of two integers [duplicate, missing].

    Examples:
        >>> solve([1, 2, 2, 4])
        [2, 3]
        >>> solve([1, 1])
        [1, 2]
    """
    n = len(nums)
    
    # Calculate expected sums for numbers 1 to n
    # Sum of first n natural numbers: n(n+1)/2
    # Sum of squares of first n natural numbers: n(n+1)(2n+1)/6
    expected_sum = n * (n + 1) // 2
    expected_sum_sq = n * (n + 1) * (2 * n + 1) // 6
    
    actual_sum = 0
    actual_sum_sq = 0
    
    # Calculate actual sums from the input array
    for num in nums:
        actual_sum += num
        actual_sum_sq += num * num
        
    # diff1 = x - y
    diff1 = actual_sum - expected_sum
    
    # diff2 = x^2 - y^2
    diff2 = actual_sum_sq - expected_sum_sq
    
    # Since x^2 - y^2 = (x - y)(x + y), then (x + y) = diff2 / diff1
    sum_xy = diff2 // diff1
    
    # Solving the system of linear equations:
    # x - y = diff1
    # x + y = sum_xy
    # 2x = diff1 + sum_xy
    duplicate = (diff1 + sum_xy) // 2
    missing = duplicate - diff1
    
    return [duplicate, missing]
