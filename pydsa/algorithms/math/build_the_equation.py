METADATA = {
    "id": 2118,
    "name": "Build the Equation",
    "slug": "build-the-equation",
    "category": "Math",
    "aliases": [],
    "tags": ["math", "string", "hash_map"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Determine if a given equation string is valid by parsing coefficients and constants for each variable.",
}

import re

def solve(equation: str) -> bool:
    """
    Parses an equation string and checks if the sum of terms equals zero.
    
    The equation is in the format 'var1=var2+var3-var4...'. 
    Each term can be a variable with a coefficient (e.g., '2x') or a constant.
    
    Args:
        equation: A string representing the equation.
        
    Returns:
        True if the equation is valid (sum of all terms is zero), False otherwise.
        
    Examples:
        >>> solve("x+y-z=0")
        True
        >>> solve("2x+3y-5z=0")
        True
        >>> solve("x+y=z")
        False
    """
    # Split the equation into the left-hand side and right-hand side
    lhs_str, rhs_str = equation.split('=')
    
    # We want to move everything to one side to check if sum == 0.
    # We treat the RHS as being subtracted from the LHS.
    # We'll use a dictionary to store the net coefficient of each variable.
    # A separate variable will track the net constant term.
    coefficients: dict[str, float] = {}
    constant_sum: float = 0.0

    def parse_side(side_str: str, multiplier: float) -> None:
        """
        Parses a side of the equation and updates the global coefficients and constant.
        
        Args:
            side_str: The string part of the equation (LHS or RHS).
            multiplier: 1.0 for LHS, -1.0 for RHS.
        """
        nonlocal constant_sum
        
        # Replace '-' with '+-' to easily split by '+' while keeping the sign
        # Then split by '+' to get individual terms
        normalized_side = side_str.replace('-', '+-')
        terms = normalized_side.split('+')
        
        for term in terms:
            if not term:
                continue
            
            # Use regex to separate the coefficient/sign from the variable name
            # Pattern: optional sign and digits, followed by optional variable name
            # Example: '-2x' -> group 1: '-2', group 2: 'x'
            # Example: 'x' -> group 1: '', group 2: 'x'
            # Example: '5' -> group 1: '5', group 2: ''
            match = re.match(r'([+-]?\d*)([a-z]*)', term)
            if not match:
                continue
                
            coeff_str, var_name = match.groups()
            
            # Determine the numeric coefficient
            if coeff_str == "" or coeff_str == "+":
                coeff = 1.0
            elif coeff_str == "-":
                coeff = -1.0
            else:
                coeff = float(coeff_str)
            
            # Apply the side multiplier (LHS is positive, RHS is negative)
            coeff *= multiplier
            
            if var_name:
                # It's a variable term
                coefficients[var_name] = coefficients.get(var_name, 0.0) + coeff
            else:
                # It's a constant term
                constant_sum += coeff

    # Process both sides
    parse_side(lhs_str, 1.0)
    parse_side(rhs_str, -1.0)

    # The equation is valid if all variable coefficients are 0 
    # and the net constant sum is 0.
    # We use a small epsilon for float comparison, though integers/simple floats 
    # should be exact in this specific problem context.
    epsilon = 1e-9
    
    for val in coefficients.values():
        if abs(val) > epsilon:
            return False
            
    return abs(constant_sum) < epsilon
