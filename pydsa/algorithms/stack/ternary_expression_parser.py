METADATA = {
    "id": 439,
    "name": "Ternary Expression Parser",
    "slug": "ternary-expression-parser",
    "category": "String",
    "aliases": [],
    "tags": ["stack", "string", "parsing"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Evaluate a nested ternary expression string by parsing it from right to left using a stack.",
}

def solve(expression: str) -> str:
    """
    Parses and evaluates a nested ternary expression.

    The expression follows the format 'condition ? true_value : false_value'.
    Nested expressions are handled by processing the string from right to left.

    Args:
        expression: A string representing the ternary expression.

    Returns:
        The evaluated result as a string.

    Examples:
        >>> solve("T?T:F")
        'T'
        >>> solve("T?T:F?F:T")
        'T'
        >>> solve("F?T:F?F:T")
        'T'
    """
    stack: list[str] = []
    n = len(expression)
    i = n - 1

    while i >= 0:
        char = expression[i]

        if char == ':':
            # When we hit a colon, we need to capture the 'false' value.
            # In a ternary 'cond ? true : false', the false value is to the right of ':'.
            # Since we are moving right-to-left, the false value is already on the stack.
            # We take the top element as the false value.
            false_val = stack.pop()
            i -= 1
            # Skip the '?' and the 'true' part to find the condition
            # But wait, the structure is: condition ? true_val : false_val
            # Moving right to left: false_val -> ':' -> true_val -> '?' -> condition
            # We need to find the '?' that corresponds to this ':'
            
            # Actually, a simpler way:
            # When we see ':', we know the next thing (to the left) is the 'true' part.
            # When we see '?', we know the next thing (to the left) is the 'condition'.
            pass 
        
        # Let's refine the logic:
        # We process right to left.
        # If we see 'T' or 'F', push to stack.
        # If we see ':', we are entering a ternary structure.
        # If we see '?', we have the condition.
        
        # Correct Right-to-Left Stack Logic:
        # 1. If char is 'T' or 'F', push to stack.
        # 2. If char is ':', we need to wait for the '?' to resolve.
        # 3. If char is '?', we have: [condition] ? [top_of_stack_as_true] : [next_top_as_false]
        #    Wait, the stack contains values. Let's trace: "T?T:F"
        #    i=4: 'F' -> stack=['F']
        #    i=3: ':' -> stack=['F', ':'] (marker)
        #    i=2: 'T' -> stack=['F', ':', 'T']
        #    i=1: '?' -> pop 'T' (true), pop ':' (marker), pop 'F' (false). 
        #              Evaluate 'T' (condition) with 'T' and 'F' -> push 'T'.
        #    i=0: 'T' -> stack=['T']
        
        # Let's implement this refined logic.
        i -= 1 # decrementing at end of loop

    # Re-implementing with a clean loop
    return _parse_logic(expression)

def _parse_logic(expression: str) -> str:
    stack: list[str] = []
    i = len(expression) - 1
    
    while i >= 0:
        char = expression[i]
        
        if char in ('T', 'F'):
            stack.append(char)
        elif char == ':':
            # Marker for the start of a ternary segment
            stack.append(':')
        elif char == '?':
            # We found a ternary operator. 
            # The stack currently looks like: [..., false_val, ':', true_val]
            # Note: because we are going right-to-left, the 'true_val' was pushed 
            # after the 'false_val' was pushed.
            
            true_val = stack.pop()
            # Pop the ':' marker
            if stack and stack[-1] == ':':
                stack.pop()
            
            false_val = stack.pop()
            
            # The condition is the character immediately to the left of '?'
            condition = expression[i-1]
            
            # Evaluate the ternary
            result = true_val if condition == 'T' else false_val
            stack.append(result)
            
            # Skip the condition character in the next iteration
            i -= 1
            
        i -= 1
        
    return stack[0]

# The solve function needs to be the entry point.
# Redefining solve to use the correct logic.

def solve_final(expression: str) -> str:
    """
    Evaluates the ternary expression using a right-to-left stack approach.
    """
    stack: list[str] = []
    i = len(expression) - 1
    
    while i >= 0:
        char = expression[i]
        
        if char == 'T' or char == 'F':
            stack.append(char)
        elif char == ':':
            # We use ':' as a delimiter to know we are inside a ternary
            stack.append(':')
        elif char == '?':
            # At this point, the stack contains: [..., false_val, ':', true_val]
            # We need to pop the true_val, the ':', and the false_val
            true_val = stack.pop()
            if stack and stack[-1] == ':':
                stack.pop()
            false_val = stack.pop()
            
            # The condition is the character at index i-1
            condition = expression[i-1]
            
            # Resolve the ternary and push back to stack
            resolved = true_val if condition == 'T' else false_val
            stack.append(resolved)
            
            # Skip the condition character
            i -= 1
        i -= 1
        
    return stack[0]

# Overwrite solve with the working implementation
solve = solve_final