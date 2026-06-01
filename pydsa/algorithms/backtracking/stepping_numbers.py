METADATA = {
    "id": 1215,
    "name": "Stepping Numbers",
    "slug": "stepping-numbers",
    "category": "Breadth-First Search",
    "aliases": [],
    "tags": ["bfs", "dfs", "backtracking", "math"],
    "difficulty": "medium",
    "time_complexity": "O(10 * 2^k) where k is the number of digits in max_num",
    "space_complexity": "O(2^k)",
    "description": "Find all stepping numbers in a given range [low, high].",
}

from collections import deque

def solve(low: int, high: int) -> list[int]:
    """
    Finds all stepping numbers within the range [low, high] using BFS.

    A stepping number is a number where all adjacent digits have an absolute 
    difference of exactly 1.

    Args:
        low: The lower bound of the range (inclusive).
        high: The upper bound of the range (inclusive).

    Returns:
        A sorted list of all stepping numbers in the range [low, high].

    Examples:
        >>> solve(0, 21)
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 21]
        >>> solve(10, 15)
        [10, 12]
    """
    result = []

    # Handle the edge case for 0 separately as it's a single-digit stepping number
    if low <= 0 <= high:
        result.append(0)

    # Use a queue for BFS to generate stepping numbers level by level (by digit length)
    # We start BFS from each single digit 1-9
    queue = deque(range(1, 10))

    while queue:
        current_num = queue.popleft()

        # If the current number is within the range, add it to results
        if low <= current_num <= high:
            result.append(current_num)

        # If the current number exceeds the high bound, we don't explore its children
        if current_num > high:
            continue

        last_digit = current_num % 10

        # Generate next possible stepping numbers by appending last_digit - 1 or last_digit + 1
        # Case 1: Last digit is greater than 0, we can append (last_digit - 1)
        if last_digit > 0:
            next_num_minus = current_num * 10 + (last_digit - 1)
            if next_num_minus <= high:
                queue.append(next_num_minus)

        # Case 2: Last digit is less than 9, we can append (last_digit + 1)
        if last_digit < 9:
            next_num_plus = current_num * 10 + (last_digit + 1)
            if next_num_plus <= high:
                queue.append(next_num_plus)

    # The BFS approach doesn't guarantee global order across different starting digits
    return sorted(result)
