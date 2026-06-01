METADATA = {
    "id": 1003,
    "name": "Check If Word Is Valid After Substitutions",
    "slug": "check-if-word-is-valid-after-substitutions",
    "category": "String",
    "aliases": [],
    "tags": ["stack", "string_manipulation"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Determine if a string is valid by checking if it can be formed by repeatedly replacing 'abc' with an empty string.",
}

def solve(s: str) -> bool:
    """
    Checks if a string is valid by simulating the reverse of the substitution process.
    
    The problem states that a string is valid if it can be formed by repeatedly 
    inserting 'abc' into an empty string. This is equivalent to saying we can 
    repeatedly remove 'abc' from the string until it is empty.

    Args:
        s: The input string to validate.

    Returns:
        True if the string is valid, False otherwise.

    Examples:
        >>> solve("دقabc") # Note: This is a placeholder for logic, actual example below
        >>> solve("aabcbc")
        True
        >>> solve("abacaba")
        False
    """
    stack: list[str] = []

    for character in s:
        stack.append(character)
        
        # If the last three characters added to the stack form 'abc',
        # they represent a valid substitution that can be "undone".
        if len(stack) >= 3:
            if stack[-3] == 'a' and stack[-2] == 'b' and stack[-1] == 'c':
                # Pop the three characters to simulate removal
                stack.pop()
                stack.pop()
                stack.pop()

    # If the string was valid, the stack should be completely empty
    return len(stack) == 0
