METADATA = {
    "id": 351,
    "name": "Android Unlock Patterns",
    "slug": "android-unlock-patterns",
    "category": "Backtracking",
    "aliases": [],
    "tags": ["dfs", "backtracking"],
    "difficulty": "medium",
    "time_complexity": "O(9!)",
    "space_complexity": "O(1)",
    "description": "Find the number of valid unlock patterns on a 3x3 keypad given the number of allowed steps.",
    "note": "Note: This problem is often presented as 'Android Unlock Patterns' on LeetCode, but the standard version is 'Android Unlock Patterns' (LeetCode 351 is actually 'Android Unlock Patterns' in some contexts, but the logic follows the keypad rules)."
}

def solve(n_steps: int) -> int:
    """
    Calculates the number of valid Android unlock patterns for a given number of steps.
    
    A pattern is valid if:
    1. Each step moves to a new digit.
    2. If a move jumps over a digit (e.g., 1 to 3), the jumped digit (2) must 
       have been visited previously.

    Args:
        n_steps: The number of digits to be included in the pattern.

    Returns:
        The total number of valid patterns.

    Examples:
        >>> solve(1)
        9
        >>> solve(2)
        36
    """
    # jump_table[i][j] stores the digit that must be visited before moving from i to j.
    # The keypad is indexed 1-9. 0 is used as a placeholder for 'no jump'.
    jump_table = [[0] * 10 for _ in range(10)]
    
    jump_table[1][3] = jump_table[3][1] = 2
    jump_table[4][6] = jump_table[6][4] = 5
    jump_table[7][9] = jump_table[9][7] = 8
    jump_table[1][7] = jump_table[7][1] = 4
    jump_table[2][8] = jump_table[8][2] = 5
    jump_table[3][9] = jump_table[9][3] = 6
    jump_table[1][9] = jump_table[9][1] = 5
    jump_table[3][7] = jump_table[7][3] = 5

    visited = [False] * 10

    def backtrack(current_digit: int, remaining_steps: int) -> int:
        """
        Recursive DFS to explore all valid paths.
        """
        if remaining_steps == 0:
            return 1
        
        count = 0
        for next_digit in range(1, 10):
            if not visited[next_digit]:
                # Check if the jump required to reach next_digit is already visited
                middle_digit = jump_table[current_digit][next_digit]
                if middle_digit == 0 or visited[middle_digit]:
                    visited[next_digit] = True
                    count += backtrack(next_digit, remaining_steps - 1)
                    visited[next_digit] = False
        return count

    total_patterns = 0
    # Start the pattern from every possible digit 1-9
    for start_digit in range(1, 10):
        visited[start_digit] = True
        total_patterns += backtrack(start_digit, n_steps - 1)
        visited[start_digit] = False
        
    return total_patterns
