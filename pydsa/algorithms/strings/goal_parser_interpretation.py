METADATA = {
    "id": 1678,
    "name": "Goal Parser Interpretation",
    "slug": "goal-parser-interpretation",
    "category": "String",
    "aliases": [],
    "tags": ["string_manipulation"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Interpret a given string containing specific patterns into their corresponding mapped values.",
}

def solve(command: str) -> str:
    """
    Parses the input command string based on specific pattern rules.

    Rules:
    - "G" -> "G"
    - "()" -> "o"
    - "(al)" -> "al"

    Args:
        command: The input string containing the encoded patterns.

    Returns:
        The interpreted string after replacing patterns.

    Examples:
        >>> solve("G()()()()(al)")
        'Gooooal'
        >>> solve("(al)G(al)")
        'alGal'
    """
    result_chars: list[str] = []
    index = 0
    n = len(command)

    while index < n:
        # Case 1: Pattern is 'G'
        if command[index] == 'G':
            result_chars.append('G')
            index += 1
        
        # Case 2: Pattern starts with '('
        elif command[index] == '(':
            # Check if it is '()'
            if index + 1 < n and command[index + 1] == ')':
                result_chars.append('o')
                index += 2
            # Check if it is '(al)'
            elif index + 3 < n and command[index:index + 4] == '(al)':
                result_chars.append('al')
                index += 4
            else:
                # This part handles unexpected input gracefully, 
                # though problem constraints guarantee valid input.
                index += 1
        else:
            # Skip any other characters if they exist
            index += 1

    return "".join(result_chars)
