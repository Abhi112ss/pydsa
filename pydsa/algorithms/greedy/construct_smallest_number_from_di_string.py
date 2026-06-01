METADATA = {
    "id": 2375,
    "name": "Construct Smallest Number From DI String",
    "slug": "construct-smallest-number-from-di-string",
    "category": "Greedy",
    "aliases": [],
    "tags": ["stack", "greedy", "string", "monotonic stack"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Construct the smallest number possible from a given DI string using digits 0-9.",
}

def solve(pattern: str) -> str:
    """
    Constructs the smallest number possible from a given DI string.

    The algorithm uses a stack-based approach to handle the 'D' (decrease) 
    instructions. We iterate through the digits 0-9 and the pattern. 
    Whenever we encounter an 'I' (increase) or reach the end of the pattern, 
    we pop all digits currently in the stack to ensure the smallest 
    lexicographical order is maintained while satisfying the 'D' constraints.

    Args:
        pattern: A string consisting of 'I' and 'D' characters.

    Returns:
        A string representing the smallest number that satisfies the pattern.

    Raises:
        ValueError: If the pattern length is greater than 10.

    Examples:
        >>> solve("IDID")
        '013254'
        >>> solve("III")
        '0123'
        >>> solve("DDD")
        '3210'
    """
    if len(pattern) > 10:
        raise ValueError("Pattern length cannot exceed 10 as there are only 10 unique digits.")

    result = []
    stack = []
    
    # We iterate n + 1 times because a pattern of length n 
    # describes the relationship between n + 1 digits.
    for i in range(len(pattern) + 1):
        # Push the current digit (0, 1, 2...) onto the stack
        stack.append(i)
        
        # If we reach the end of the pattern or encounter an 'I',
        # it means the current sequence of 'D's has ended.
        # We pop everything from the stack to reverse the sequence 
        # of digits that were meant to be decreasing.
        if i == len(pattern) or pattern[i] == 'I':
            while stack:
                result.append(str(stack.pop()))
                
    return "".join(result)
