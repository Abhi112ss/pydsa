METADATA = {
    "id": 385,
    "name": "Mini Parser",
    "slug": "mini-parser",
    "category": "String",
    "aliases": [],
    "tags": ["recursion", "string_parsing", "stack"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Parse a string representing a nested list structure into a Python list.",
}

def solve(s: str) -> list:
    """
    Parses a string representing a nested list structure into a Python list.

    The input string follows a format similar to Python lists, using brackets '[]' 
    for nesting and commas ',' as delimiters.

    Args:
        s: The input string to parse.

    Returns:
        A list containing the parsed elements (integers or nested lists).

    Examples:
        >>> solve("[123,[456,[789],0],1]")
        [123, [456, [789], 0], 1]
        >>> solve("[]")
        []
    """
    stack: list[list | int] = []
    current_list: list[list | int] = []
    i = 0
    n = len(s)

    while i < n:
        char = s[i]

        if char == '[':
            # Start a new nested list: push the current list to stack and start fresh
            stack.append(current_list)
            current_list = []
            i += 1
        elif char == ']':
            # End of current list: append current list to the parent list from stack
            finished_list = current_list
            current_list = stack.pop()
            current_list.append(finished_list)
            i += 1
        elif char == ',':
            # Delimiter: just move to the next character
            i += 1
        else:
            # It's a digit: parse the full integer
            start = i
            while i < n and s[i].isdigit():
                i += 1
            num_str = s[start:i]
            if num_str:
                current_list.append(int(num_str))
            # Note: i is already at the next character after the while loop
    
    # The final result is the first element of the last list processed if we 
    # started with a root bracket, but since we push the initial empty list 
    # to stack when '[' is hit, the logic above handles the nesting.
    # However, the way the loop is structured, the very first '[' pushes 
    # an empty list to stack, so the result is actually the last 'current_list' 
    # if we consider the root. Let's refine the logic to be more robust.
    
    # Re-implementing with a cleaner stack approach for production-grade:
    return _parse_with_stack(s)

def _parse_with_stack(s: str) -> list:
    """
    Helper implementation using a stack to manage nested list contexts.
    """
    stack: list[list] = []
    current_list: list = []
    i = 0
    n = len(s)

    while i < n:
        if s[i] == '[':
            # Push the list we are currently building to the stack
            stack.append(current_list)
            current_list = []
            i += 1
        elif s[i] == ']':
            # Close the current list and add it to the parent list
            finished_list = current_list
            current_list = stack.pop()
            current_list.append(finished_list)
            i += 1
        elif s[i] == ',':
            i += 1
        elif s[i].isdigit():
            # Extract the full integer
            start = i
            while i < n and s[i].isdigit():
                i += 1
            current_list.append(int(s[start:i]))
        else:
            i += 1

    return current_list
