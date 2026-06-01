METADATA = {
    "id": 1440,
    "name": "Evaluate Boolean Expression",
    "slug": "evaluate-boolean-expression",
    "category": "Stack",
    "aliases": [],
    "tags": ["stack", "strings", "parsing"],
    "difficulty": "hard",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Evaluate a boolean expression consisting of '!', '&', '|', and '?' operators using a stack-based approach.",
}

def solve(expression: str) -> bool:
    """
    Evaluates a boolean expression containing operators '!', '&', '|', and '?'.

    The expression follows a specific format:
    - '?' : returns the value of its single argument.
    - '!' : returns the negation of its single argument.
    - '&' : returns true if all its arguments are true.
    - '|' : returns true if any of its arguments are true.

    Args:
        expression: A string representing the boolean expression.

    Returns:
        The boolean result of the evaluated expression.

    Examples:
        >>> solve("?(|(T,F))")
        True
        >>> solve("!(&(T,T,F))")
        True
        >>> solve("&(&(T,T),|(F,T))")
        True
    """
    stack: list[str | bool] = []

    for char in expression:
        # Skip commas and closing parentheses as they are handled by the operator logic
        if char in (",", ")"):
            continue
        
        # Push operators and values onto the stack
        if char in ("!", "&", "|", "?", "T", "F"):
            # We store 'T' and 'F' as booleans for easier computation
            if char == "T":
                stack.append(True)
            elif char == "F":
                stack.append(False)
            else:
                stack.append(char)
        
        # When we encounter a closing parenthesis, it signals the end of an expression block
        # We need to look back to find the operator and its arguments
        if char == ")":
            # This part is actually handled by the logic above if we treat ')' as a trigger.
            # However, the problem structure implies ')' follows the arguments.
            # Let's refine the loop to handle the trigger correctly.
            pass

    # Re-implementing the loop logic to correctly handle the trigger ')'
    # The previous loop was a draft; let's use a robust stack-based parser.
    
    stack: list[str | bool] = []
    
    for char in expression:
        if char == ",":
            continue
        elif char == ")":
            # 1. Pop arguments until we hit the opening parenthesis '('
            # Note: The problem format is 'op(arg1,arg2...)'. 
            # We need to find the operator which is just before the '('
            # But in the string, the operator is at the start of the block.
            # Let's use a different approach: find the operator and its arguments.
            pass

    # Corrected Stack Implementation
    stack: list[str | bool] = []
    
    for char in expression:
        if char == ",":
            continue
        elif char == ")":
            # Collect all arguments until we find the '('
            args = []
            while stack and stack[-1] != "(":
                args.append(stack.pop())
            
            # Pop the '('
            if stack and stack[-1] == "(":
                stack.pop()
            
            # The operator is the character immediately before the '('
            operator = stack.pop()
            
            # Evaluate based on the operator
            if operator == "?":
                result = args[0]
            elif operator == "!":
                result = not args[0]
            elif operator == "&":
                result = all(args)
            elif operator == "|":
                result = any(args)
            else:
                raise ValueError("Invalid operator")
            
            stack.append(result)
            
        elif char == "(":
            stack.append("(")
        elif char == "T":
            stack.append(True)
        elif char == "F":
            stack.append(False)
        elif char in ("!", "&", "|", "?"):
            stack.append(char)
        # Note: The input format is 'op(args)'. The operator is NOT inside the parens.
        # Example: &(T,F) -> stack: ['&', '(', True, False]
        # When ')' is hit: args=[False, True], pop '(', pop '&', result=False, stack=[False]
        # Wait, the operator is BEFORE the '('. So when we see '(', the operator is already on stack.
        # Let's trace: '&' -> stack=['&']; '(' -> stack=['&', '(']; 'T' -> stack=['&', '(', True]...
        # This works.
        
    # The final result is the only item left in the stack
    return stack[0]

# Redefining solve to be cleaner and strictly follow the logic
def solve(expression: str) -> bool:
    """
    Evaluates a boolean expression using a stack.
    
    Complexity:
        Time: O(n) - Each character is processed a constant number of times.
        Space: O(n) - Stack stores up to n characters.
    """
    stack: list[str | bool] = []
    
    for char in expression:
        if char == ",":
            continue
        elif char == ")":
            # 1. Extract arguments from the stack until '(' is found
            args = []
            while stack and stack[-1] != "(":
                args.append(stack.pop())
            
            # 2. Remove the '(' from the stack
            if stack and stack[-1] == "(":
                stack.pop()
            
            # 3. The operator is the element immediately preceding '('
            operator = stack.pop()
            
            # 4. Compute the result of the sub-expression
            if operator == "?":
                res = args[0]
            elif operator == "!":
                res = not args[0]
            elif operator == "&":
                res = all(args)
            elif operator == "|":
                res = any(args)
            else:
                res = False
            
            stack.append(res)
            
        elif char == "(":
            stack.append("(")
        elif char == "T":
            stack.append(True)
        elif char == "F":
            stack.append(False)
        elif char in ("!", "&", "|", "?"):
            stack.append(char)
            
    return stack[0]
