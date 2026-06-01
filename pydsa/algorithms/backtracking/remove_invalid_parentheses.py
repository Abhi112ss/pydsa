METADATA = {
    "id": 301,
    "name": "Remove Invalid Parentheses",
    "slug": "remove-invalid-parentheses",
    "category": "String",
    "aliases": [],
    "tags": ["bfs", "dfs", "backtracking", "string"],
    "difficulty": "hard",
    "time_complexity": "O(2^n)",
    "space_complexity": "O(2^n)",
    "description": "Remove the minimum number of invalid parentheses to make the input string valid.",
}

from collections import deque

def solve(s: str) -> list[str]:
    """
    Finds all possible results of removing the minimum number of invalid parentheses.

    Args:
        s: The input string containing '(' , ')' and potentially other characters.

    Returns:
        A list of unique valid strings after minimum removals.

    Examples:
        >>> solve("()())()")
        ['(())()', '()()()']
        >>> solve("(a)())()")
        ['(a)()()', '(a())()']
        >>> solve(")(")
        ['']
    """
    def is_valid(string: str) -> bool:
        """Checks if the parentheses in the string are balanced."""
        balance = 0
        for char in string:
            if char == '(':
                balance += 1
            elif char == ')':
                balance -= 1
                if balance < 0:
                    return False
        return balance == 0

    if not s:
        return [""]

    # BFS approach to find the minimum number of removals
    # We explore level by level (number of removals)
    queue = deque([s])
    visited = {s}
    found = False
    results = []

    while queue:
        # Process current level
        level_size = len(queue)
        current_level_nodes = set()
        
        for _ in range(level_size):
            current_str = queue.popleft()
            
            if is_valid(current_str):
                results.append(current_str)
                found = True
            
            # If we haven't found a valid string yet, generate next level
            if not found:
                for i in range(len(current_str)):
                    # Only attempt to remove parentheses, skip other characters
                    if current_str[i] not in ('(', ')'):
                        continue
                    
                    # Create a new string by removing the character at index i
                    next_str = current_str[:i] + current_str[i+1:]
                    if next_str not in visited:
                        visited.add(next_str)
                        queue.append(next_str)
        
        # If we found valid strings at this level, we stop exploring deeper levels
        # because we are looking for the MINIMUM number of removals.
        if found:
            break

    return results if results else [""]
