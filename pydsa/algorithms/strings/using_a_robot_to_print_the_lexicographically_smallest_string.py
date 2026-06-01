METADATA = {
    "id": 2434,
    "name": "Using a Robot to Print the Lexicographically Smallest String",
    "slug": "using-a-robot-to-print-the-lexicographically-smallest-string",
    "category": "Greedy",
    "aliases": [],
    "tags": ["greedy", "stack", "string"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Use a robot to move characters from a source string to a stack and then to a result string to form the lexicographically smallest possible string.",
}

def solve(s: str) -> str:
    """
    Constructs the lexicographically smallest string possible using a robot 
    that moves characters from a source string to a stack and then to a result.

    Args:
        s: The input source string.

    Returns:
        The lexicographically smallest string that can be formed.

    Examples:
        >>> solve("acdb")
        "abcd"
        >>> solve("bac")
        "abc"
    """
    n = len(s)
    # Precompute the smallest character available from index i to the end of the string.
    # This allows us to know if a smaller character exists later in the source.
    min_char_ahead = [None] * n
    current_min = '{'  # Character lexicographically larger than 'z'
    
    for i in range(n - 1, -1, -1):
        if s[i] < current_min:
            current_min = s[i]
        min_char_ahead[i] = current_min

    stack: list[str] = []
    result_chars: list[str] = []
    
    for i in range(n):
        # Push current character from source to stack
        stack.append(s[i])
        
        # Check if the top of the stack is smaller than or equal to any 
        # character remaining in the source string.
        # If it is, it's safe to move it to the result immediately.
        next_min_in_source = min_char_ahead[i + 1] if i + 1 < n else '{'
        
        while stack and stack[-1] <= next_min_in_source:
            result_chars.append(stack.pop())
            
    # After processing all characters in source, empty the stack into the result
    while stack:
        result_chars.append(stack.pop())
        
    return "".join(result_chars)
