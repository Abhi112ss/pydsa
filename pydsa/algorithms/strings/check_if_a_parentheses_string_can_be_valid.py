METADATA = {
    "id": 2116,
    "name": "Check if a Parentheses String Can Be Valid",
    "slug": "check-if-a-parentheses-string-can-be-valid",
    "category": "String",
    "aliases": [],
    "tags": ["greedy", "string", "stack"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Determine if a string of parentheses and characters can be made valid by assigning each character to either an open or close parenthesis, provided the string length is even.",
}

def solve(s: str, locked: list[int]) -> bool:
    """
    Checks if a string of parentheses can be made valid given a list of locked indices.

    A string is valid if:
    1. Every open parenthesis '(' has a corresponding close parenthesis ')'.
    2. Every close parenthesis ')' has a corresponding open parenthesis '('.
    3. Open parentheses are closed in the correct order.
    Locked indices (locked[i] == 1) cannot be changed. Unlocked indices (locked[i] == 0)
    can be changed to either '(' or ')'.

    Args:
        s: The input string containing '(' and ')'.
        locked: A list of integers where 1 means the character is locked and 0 means it is flexible.

    Returns:
        True if the string can be made valid, False otherwise.

    Examples:
        >>> solve("(*)", [0, 1, 0])
        True
        >>> solve("]())", [0, 1, 2, 3])
        False
    """
    n = len(s)
    
    # A valid parentheses string must have an even length.
    if n % 2 != 0:
        return False

    # Left-to-right pass: Ensure we never have more ')' than available '(' and flexible chars.
    # We treat flexible characters as '(' to see if we can satisfy all ')' requirements.
    balance = 0
    for i in range(n):
        if locked[i] == 0 or s[i] == '(':
            balance += 1
        else:
            balance -= 1
        
        # If balance is negative, we have too many ')' that cannot be compensated.
        if balance < 0:
            return False

    # Right-to-left pass: Ensure we never have more '(' than available ')' and flexible chars.
    # We treat flexible characters as ')' to see if we can satisfy all '(' requirements.
    balance = 0
    for i in range(n - 1, -1, -1):
        if locked[i] == 0 or s[i] == ')':
            balance += 1
        else:
            balance -= 1
            
        # If balance is negative, we have too many '(' that cannot be compensated.
        if balance < 0:
            return False

    return True
