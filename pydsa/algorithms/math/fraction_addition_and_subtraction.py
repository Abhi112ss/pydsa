METADATA = {
    "id": 592,
    "name": "Fraction Addition and Subtraction",
    "slug": "fraction-addition-and-subtraction",
    "category": "Math",
    "aliases": [],
    "tags": ["string", "math", "gcd"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Evaluate a string expression containing fraction addition and subtraction and return the result as a simplified fraction.",
}

import math

def solve(expression: str) -> str:
    """
    Evaluates a string expression of fraction addition and subtraction.

    Args:
        expression: A string containing fractions separated by '+' or '-'.
            Example: "1/2-1/2+1/2"

    Returns:
        A string representing the simplified fraction in the form "numerator/denominator".

    Examples:
        >>> solve("1/2-1/2+1/2")
        '1/2'
        >>> solve("1/3+1/3+1/3")
        '1/1'
    """
    # current_numerator and current_denominator represent the running total
    current_numerator = 0
    current_denominator = 1
    
    # We use a pointer to traverse the string to handle multi-digit numbers
    i = 0
    n = len(expression)
    
    # The first number doesn't have a preceding sign, so we treat it as positive
    # We'll parse the expression by looking for the next sign
    while i < n:
        # 1. Parse the sign (if any)
        sign = 1
        if expression[i] == '+':
            sign = 1
            i += 1
        elif expression[i] == '-':
            sign = -1
            i += 1
            
        # 2. Parse the numerator
        num_start = i
        while i < n and expression[i].isdigit():
            i += 1
        numerator = int(expression[num_start:i])
        
        # Skip the '/'
        i += 1
        
        # 3. Parse the denominator
        den_start = i
        while i < n and expression[i].isdigit():
            i += 1
        denominator = int(expression[den_start:i])
        
        # 4. Perform fraction arithmetic:
        # a/b + c/d = (a*d + c*b) / (b*d)
        # We apply the sign to the numerator of the incoming fraction
        new_numerator = current_numerator * denominator + sign * numerator * current_denominator
        new_denominator = current_denominator * denominator
        
        # Simplify the fraction immediately to prevent integer overflow
        common_divisor = math.gcd(new_numerator, new_denominator)
        current_numerator = new_numerator // common_divisor
        current_denominator = new_denominator // common_divisor
        
    # Ensure the denominator is positive (though math.gcd handles signs, 
    # it's good practice for fraction normalization)
    if current_denominator < 0:
        current_numerator = -current_numerator
        current_denominator = -current_denominator
        
    return f"{current_numerator}/{current_denominator}"
