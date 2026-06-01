METADATA = {
    "id": 936,
    "name": "Stamping The Sequence",
    "slug": "stamping-the-sequence",
    "category": "String",
    "aliases": [],
    "tags": ["greedy", "string", "stack"],
    "difficulty": "medium",
    "time_complexity": "O(n * (n - m))",
    "space_complexity": "O(n)",
    "description": "Determine if a target sequence can be formed by stamping a pattern onto a sequence of question marks.",
}

def solve(target: str, pattern: str) -> bool:
    """
    Determines if the target string can be formed by stamping the pattern.
    
    The algorithm works backwards: instead of trying to place stamps on '?', 
    we try to 'un-stamp' the target string. We look for occurrences of the 
    pattern in the target and replace them with a wildcard character. 
    If we can eventually turn the entire target into wildcards, the answer is True.

    Args:
        target: The target string containing characters and '?'.
        pattern: The pattern string to be stamped.

    Returns:
        True if the target can be formed, False otherwise.

    Examples:
        >>> solve("??a?b", "ab")
        True
        >>> solve("??a?b", "ba")
        False
    """
    n = len(target)
    m = len(pattern)
    
    # Convert target to a list for mutability
    # We use a special character (e.g., '*') to represent a 'cleared' position
    current_state = list(target)
    
    # We iterate multiple times. In each pass, we look for matches of the pattern.
    # A match is valid if every character in the pattern either matches the 
    # current_state character OR the current_state character is a wildcard '*'.
    # We repeat this until no more changes can be made.
    changed = True
    while changed:
        changed = False
        # Slide the pattern across the current_state
        for i in range(n - m + 1):
            # Check if pattern matches the current window
            match = True
            for j in range(m):
                # If the target has a fixed char that doesn't match pattern, it's not a match
                # Note: '*' acts as a wildcard that matches anything in the pattern
                if current_state[i + j] != '*' and current_state[i + j] != pattern[j]:
                    match = False
                    break
            
            if match:
                # Check if this window actually contains any non-wildcard characters
                # to avoid infinite loops and redundant work
                has_non_wildcard = False
                for j in range(m):
                    if current_state[i + j] != '*':
                        has_non_wildcard = True
                        break
                
                if has_non_wildcard:
                    # "Un-stamp" this section by turning it into wildcards
                    for j in range(m):
                        current_state[i + j] = '*'
                    changed = True
                    
    # If the entire target has been converted to wildcards, the stamping is possible
    return all(char == '*' for char in current_state)
