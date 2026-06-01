METADATA = {
    "id": 394,
    "name": "Decode String",
    "slug": "decode-string",
    "category": "String",
    "aliases": [],
    "tags": ["stack", "string", "recursion", "parsing"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Given an encoded string, return its decoded version by expanding repeated patterns within brackets.",
}

def solve(s: str) -> str:
    """
    Decodes an encoded string containing patterns like k[encoded_string].

    Args:
        s: The encoded string.

    Returns:
        The decoded string.

    Examples:
        >>> solve("3[a]2[bc]")
        'aaabcbc'
        >>> solve("3[a2[c]]")
        'accaccacc'
        >>> solve("2[abc]3[cd]ef")
        'abcabccdcdcdef'
    """
    # Stack to store the previous string context and the multiplier
    # string_stack stores the string built so far before entering a bracket
    # count_stack stores the multiplier (k) for the upcoming bracketed content
    string_stack: list[str] = []
    count_stack: list[int] = []
    
    current_string: str = ""
    current_num: int = 0

    for char in s:
        if char.isdigit():
            # Build the multi-digit number
            current_num = current_num * 10 + int(char)
        elif char == '[':
            # Entering a new nested level:
            # 1. Push the current multiplier to the count stack
            # 2. Push the string built so far to the string stack
            # 3. Reset current tracking variables
            count_stack.append(current_num)
            string_stack.append(current_string)
            current_num = 0
            current_string = ""
        elif char == ']':
            # Exiting a nested level:
            # 1. Pop the multiplier for the current segment
            # 2. Pop the string context from before the bracket
            # 3. Repeat the current segment and append to the context
            repeat_count = count_stack.pop()
            previous_string = string_stack.pop()
            current_string = previous_string + (current_string * repeat_count)
        else:
            # Regular character: append to the current working string
            current_string += char

    return current_string
