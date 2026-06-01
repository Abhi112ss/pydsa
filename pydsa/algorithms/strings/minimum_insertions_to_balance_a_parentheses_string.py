METADATA = {
    "id": 1541,
    "name": "Minimum Insertions to Balance a Parentheses String",
    "slug": "minimum-insertions-to-balance-a-parentheses-string",
    "category": "Greedy",
    "aliases": [],
    "tags": ["greedy", "string", "stack"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Calculate the minimum number of insertions needed to make a parentheses string balanced where one '(' must be followed by exactly two consecutive ')'.",
}

def solve(s: str) -> int:
    """
    Calculates the minimum number of insertions required to balance the string.
    
    A string is balanced if every '(' is followed by exactly two consecutive ')'.
    
    Args:
        s: The input string consisting of '(' and ')'.
        
    Returns:
        The minimum number of insertions needed to balance the string.
        
    Examples:
        >>> solve("(()))")
        0
        >>> solve("())")
        0
        >>> solve(")())(")
        4
        >>> solve("(((((")
        10
    """
    insertions = 0
    needed_closing = 0
    index = 0
    n = len(s)

    while index < n:
        char = s[index]
        
        if char == '(':
            # Each '(' requires two ')'
            needed_closing += 2
            
            # If we have an odd number of needed closing parentheses, it means
            # the previous '(' was only followed by one ')'. We must insert 
            # one ')' to complete that pair before starting a new '(' group.
            if needed_closing % 2 != 0:
                insertions += 1
                needed_closing -= 1
        else:
            # We encountered a ')'
            if index + 1 < n and s[index + 1] == ')':
                # We found a pair of '))'
                needed_closing -= 2
                index += 1  # Skip the next ')' as we processed it as a pair
            else:
                # We found a single ')', we need to insert one ')' to make it a pair
                insertions += 1
                needed_closing -= 2
            
            # If needed_closing becomes negative, it means we have more ')' 
            # than '(' can support. We must insert a '(' to balance it.
            if needed_closing < 0:
                insertions += 1
                needed_closing += 2
        
        index += 1

    # Any remaining needed_closing must be added to insertions
    return insertions + needed_closing
