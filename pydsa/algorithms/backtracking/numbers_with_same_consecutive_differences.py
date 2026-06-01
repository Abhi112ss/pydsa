METADATA = {
    "id": 967,
    "name": "Numbers With Same Consecutive Differences",
    "slug": "numbers-with-same-consecutive-differences",
    "category": "Breadth-First Search",
    "aliases": [],
    "tags": ["dfs", "bfs", "math"],
    "difficulty": "medium",
    "time_complexity": "O(2^n)",
    "space_complexity": "O(2^n)",
    "description": "Find all numbers of length n where the absolute difference between every two consecutive digits is exactly k.",
}

def solve(n: int, k: int) -> list[int]:
    """
    Finds all numbers of length n where the absolute difference between 
    consecutive digits is exactly k.

    Args:
        n: The number of digits in the target numbers.
        k: The required absolute difference between consecutive digits.

    Returns:
        A sorted list of all valid numbers.

    Examples:
        >>> solve(2, 3)
        [14, 25, 30, 36, 41, 47, 52, 58, 63, 69, 74, 85, 96]
        >>> solve(3, 5)
        [161, 505]
    """
    if n == 1:
        return list(range(1, 10))

    # We use a queue for BFS to build numbers digit by digit.
    # Each element in the queue is the number formed so far.
    queue: list[int] = list(range(1, 10))
    
    # Process the queue level by level until we reach length n.
    # Each level represents adding one more digit to the numbers.
    for _ in range(n - 1):
        next_level: list[int] = []
        for current_num in queue:
            # Get the last digit to determine valid next digits.
            last_digit = current_num % 10
            
            # Option 1: The next digit is last_digit + k
            digit_plus = last_digit + k
            if digit_plus <= 9:
                next_level.append(current_num * 10 + digit_plus)
            
            # Option 2: The next digit is last_digit - k
            # If k is 0, we only process this once to avoid duplicates.
            digit_minus = last_digit - k
            if k > 0 and digit_minus >= 0:
                next_level.append(current_num * 10 + digit_minus)
        
        queue = next_level

    # The problem requires the result to be sorted.
    return sorted(queue)
