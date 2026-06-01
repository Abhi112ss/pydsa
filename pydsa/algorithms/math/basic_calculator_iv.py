METADATA = {
    "id": 770,
    "name": "Basic Calculator IV",
    "slug": "basic-calculator-iv",
    "category": "Math",
    "aliases": [],
    "tags": ["hash_map", "recursion", "strings", "math"],
    "difficulty": "hard",
    "time_complexity": "O(2^n)",
    "space_complexity": "O(2^n)",
    "description": "Evaluate a mathematical expression involving variables and return the result as a simplified polynomial.",
}

from collections import defaultdict

def solve(expression: str) -> list[str]:
    """
    Evaluates a mathematical expression and returns the simplified polynomial.

    The polynomial is represented as a dictionary where keys are sorted tuples 
    of variable names (representing the monomial) and values are their coefficients.

    Args:
        expression: A string containing variables, numbers, and operators (+, -, *, (, )).

    Returns:
        A list of strings representing the simplified polynomial in descending order 
        of degree, then lexicographical order.

    Examples:
        >>> solve("a + b")
        ['a', 'b']
        >>> solve("a + b - (a + b)")
        []
        >>> solve("a * b + b * a")
        ['ab']
    """

    def parse_expression(expr: str) -> dict[tuple[str, ...], int]:
        """
        Parses the expression using a recursive descent approach.
        Returns a dictionary mapping sorted variable tuples to coefficients.
        """
        # Remove whitespace
        expr = expr.replace(" ", "")
        
        def get_polynomial(s: str) -> dict[tuple[str, ...], int]:
            # Handle addition and subtraction at the top level
            # We find the top-level + or - (not inside parentheses)
            balance = 0
            for i in range(len(s) - 1, -1, -1):
                if s[i] == ')':
                    balance += 1
                elif s[i] == '(':
                    balance -= 1
                elif balance == 0 and s[i] in '+-':
                    # Split into left and right parts
                    left_poly = get_polynomial(s[:i])
                    right_poly = get_polynomial(s[i+1:])
                    
                    res = defaultdict(int, left_poly)
                    sign = 1 if s[i] == '+' else -1
                    for term, coeff in right_poly.items():
                        res[term] += sign * coeff
                    return {k: v for k, v in res.items() if v != 0}

            # Handle multiplication at the top level
            balance = 0
            for i in range(len(s) - 1, -1, -1):
                if s[i] == ')':
                    balance += 1
                elif s[i] == '(':
                    balance -= 1
                elif balance == 0 and s[i] == '*':
                    left_poly = get_polynomial(s[:i])
                    right_poly = get_polynomial(s[i+1:])
                    
                    res = defaultdict(int)
                    # Multiply every term in left by every term in right
                    for term_l, coeff_l in left_poly.items():
                        for term_r, coeff_r in right_poly.items():
                            # Combine and sort variable tuples to maintain canonical form
                            combined_term = tuple(sorted(term_l + term_r))
                            res[combined_term] += coeff_l * coeff_r
                    return {k: v for k, v in res.items() if v != 0}

            # Handle parentheses
            if s.startswith('(') and s.endswith(')'):
                # Check if the parentheses actually wrap the whole expression
                balance = 0
                is_wrapped = True
                for i in range(len(s) - 1):
                    if s[i] == '(': balance += 1
                    elif s[i] == ')': balance -= 1
                    if balance == 0 and i < len(s) - 1:
                        is_wrapped = False
                        break
                if is_wrapped:
                    return get_polynomial(s[1:-1])

            # Base case: single term (variable or constant)
            if s.isdigit():
                return {(): int(s)}
            elif s.isalpha():
                # Handle single variable or multiple variables like 'abc'
                return {tuple(sorted(list(s))): 1}
            
            return {}

        return get_polynomial(expr)

    # 1. Parse the expression into a canonical polynomial representation
    poly_map = parse_expression(expression)
    
    if not poly_map:
        return []

    # 2. Convert the map into the required list of strings format
    # Sort by degree (length of tuple) descending, then lexicographically
    sorted_terms = sorted(
        poly_map.items(),
        key=lambda item: (-len(item[0]), item[0])
    )

    result = []
    for term_tuple, coeff in sorted_terms:
        # Handle coefficient
        term_str = ""
        if coeff == 1 and term_tuple:
            term_str = "".join(term_tuple)
        elif coeff == -1 and term_tuple:
            term_str = "-" + "".join(term_tuple)
        elif not term_tuple:
            term_str = str(coeff)
        else:
            term_str = str(coeff) + "".join(term_tuple)
        
        result.append(term_str)

    return result
