METADATA = {
    "id": 1006,
    "name": "Clumsy Factorial",
    "slug": "clumsy_factorial",
    "category": "Math",
    "aliases": [],
    "tags": ["math", "simulation"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Calculate the result of a clumsy factorial expression involving multiplication, division, addition, and subtraction.",
}

def solve(n: int) -> int:
    """
    Calculates the result of the clumsy factorial expression.
    
    The expression follows the pattern: n! = n * (n-1) / (n-2) + (n-3) - (n-4) * (n-5) / (n-6) + (n-7) ...
    The key insight is that the operations repeat in a cycle of 4:
    1. Multiplication and Division: (n-1) / (n-2)
    2. Addition: + (n-3)
    3. Subtraction: - (n-4)
    Wait, the pattern is actually:
    n * (n-1) / (n-2) + (n-3) - (n-4) * (n-5) / (n-6) + (n-7) ...
    
    Actually, the pattern of signs for terms (n-1), (n-2), (n-3), (n-4)... is:
    n * (n-1) / (n-2) + (n-3) - (n-4) * (n-5) / (n-6) + (n-7) ...
    
    Let's re-evaluate the sequence of operations:
    Term 0: n
    Term 1: * (n-1)
    Term 2: / (n-2)
    Term 3: + (n-3)
    Term 4: - (n-4)
    Term 5: * (n-5)
    Term 6: / (n-6)
    Term 7: + (n-7)
    Term 8: - (n-8)
    
    The cycle of operators is [*, /, +, -] repeating every 4 terms.
    
    Args:
        n: The integer to start the factorial from.

    Returns:
        The integer result of the clumsy factorial.

    Examples:
        >>> solve(10)
        7182
        >>> solve(2)
        2
        >>> solve(4)
        6
    """
    if n <= 1:
        return n

    # We start with the first term 'n'
    result = n
    current_val = n
    
    # We track the current index being processed (starting from n-1)
    # and the current operator in the cycle [*, /, +, -]
    # However, a simpler way is to simulate the operations using a stack 
    # or by observing the pattern of the 4-step cycle.
    
    # Let's use the pattern approach:
    # The sequence of operations applied to the next number is:
    # n * (n-1) / (n-2) + (n-3) - (n-4) * (n-5) / (n-6) + (n-7) ...
    # The operators are: *, /, +, -
    
    # We can use a stack to handle precedence (multiplication and division first)
    # But since the pattern is fixed, we can just simulate it.
    
    # Let's use a stack-based approach for clarity and correctness.
    # We treat the expression as: n [op1] (n-1) [op2] (n-2) ...
    # Operators: 0:*, 1:/, 2:+, 3:-
    
    stack = [n]
    operators = [0, 1, 2, 3] # indices for *, /, +, -
    
    current_num = n - 1
    op_idx = 0
    
    while current_num > 0:
        op = operators[op_idx % 4]
        
        if op == 0: # Multiplication
            stack.append(current_num)
        elif op == 1: # Division
            # Pop the last element, divide it by current_num, and push back
            last_val = stack.pop()
            stack.append(int(last_val / current_num))
        elif op == 2: # Addition
            stack.append(current_num)
        elif op == 3: # Subtraction
            stack.append(-current_num)
            
        current_num -= 1
        op_idx += 1
        
    # Sum everything in the stack to get the final result
    # Addition and subtraction are handled by pushing positive or negative numbers
    return sum(stack)
