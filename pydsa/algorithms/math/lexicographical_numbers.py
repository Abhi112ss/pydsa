METADATA = {
    "id": 386,
    "name": "Lexicographical Numbers",
    "slug": "lexicographical-numbers",
    "category": "Math",
    "aliases": [],
    "tags": ["dfs", "recursion", "math", "simulation"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Return 1 to n in lexicographical order.",
}

def solve(n: int) -> list[int]:
    """
    Generates numbers from 1 to n in lexicographical order using a 
    simulated pre-order traversal of a 10-ary tree.

    Args:
        n: The upper bound (inclusive) of the numbers to generate.

    Returns:
        A list of integers from 1 to n sorted lexicographically.

    Examples:
        >>> solve(13)
        [1, 10, 11, 12, 13, 2, 3, 4, 5, 6, 7, 8, 9]
        >>> solve(2)
        [1, 2]
    """
    result: list[int] = []
    current_number = 1

    for _ in range(n):
        result.append(current_number)
        
        # Try to go deeper in the tree (append a digit 0-9)
        if current_number * 10 <= n:
            current_number *= 10
        else:
            # If we can't go deeper, try to go sideways (increment digit)
            # or go up and then sideways if we hit the limit n or a trailing 9
            while current_number % 10 == 9 or current_number + 1 > n:
                current_number //= 10
            
            # Increment to the next sibling in the tree
            current_number += 1
            
    return result
