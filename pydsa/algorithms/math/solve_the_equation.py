METADATA = {
    "id": 640,
    "name": "Solve the Equation",
    "slug": "solve-the-equation",
    "category": "Math",
    "aliases": [],
    "tags": ["math", "string", "parsing"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Solve a linear equation represented as a string and return the integer solution for x.",
}

import re

def solve(equation: str) -> int:
    """
    Parses a linear equation string and solves for x.

    The equation is in the form 'ax+b=cx+d' where 'a', 'b', 'c', and 'd' 
    are integers. The solution is guaranteed to be a single integer.

    Args:
        equation: A string representing the linear equation.

    Returns:
        The integer value of x that satisfies the equation.

    Raises:
        ValueError: If no solution exists or if the solution is not an integer.

    Examples:
        >>> solve("x+6=2x+4")
        2
        >>> solve("x+0=0+x")
        0
        >>> solve("2x+5=5x-7")
        4
    """
    # Split the equation into left and right sides
    left_side, right_side = equation.split('=')

    def parse_side(side: str) -> tuple[int, int]:
        """
        Parses one side of the equation to find the coefficient of x and the constant.
        
        Returns:
            A tuple (x_coefficient, constant)
        """
        x_coeff = 0
        constant = 0
        
        # Replace '-' with '+-' to make splitting by '+' easier, 
        # then handle the edge case of a leading '-'
        normalized_side = side.replace('-', '+-')
        terms = normalized_side.split('+')

        for term in terms:
            if not term:
                continue
            
            if 'x' in term:
                # Handle cases like 'x', '-x', '2x', '-2x'
                coeff_str = term.replace('x', '')
                if coeff_str == '' or coeff_str == '+':
                    x_coeff += 1
                elif coeff_str == '-':
                    x_coeff -= 1
                else:
                    x_coeff += int(coeff_str)
            else:
                # It's a pure constant term
                constant += int(term)
                
        return x_coeff, constant

    # Extract coefficients and constants from both sides
    left_x, left_const = parse_side(left_side)
    right_x, right_const = parse_side(right_side)

    # The equation is: left_x * x + left_const = right_x * x + right_const
    # Rearrange to: (left_x - right_x) * x = (right_const - left_const)
    # This is in the form: A * x = B
    final_x_coeff = left_x - right_x
    final_constant = right_const - left_const

    # If final_x_coeff is 0, then final_constant must be 0 for infinite solutions,
    # but the problem guarantees a single integer solution.
    if final_x_coeff == 0:
        raise ValueError("No unique solution exists.")

    # Solve for x: x = B / A
    # Since the problem guarantees an integer solution, we use integer division
    return final_constant // final_x_coeff
