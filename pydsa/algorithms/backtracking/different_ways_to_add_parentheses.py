METADATA = {
    "id": 241,
    "name": "Different Ways to Add Parentheses",
    "slug": "different-ways-to-add-parentheses",
    "category": "Divide and Conquer",
    "aliases": [],
    "tags": ["divide_and_conquer", "recursion", "memoization", "dynamic_programming"],
    "difficulty": "medium",
    "time_complexity": "O(2^n)",
    "space_complexity": "O(2^n)",
    "description": "Given a string of numbers and operators, return all possible results from computing all the different ways to group numbers and operators with parentheses.",
}

from typing import Dict, List


def solve(expression: str) -> List[int]:
    """
    Computes all possible results from grouping the expression with parentheses.

    Uses a divide and conquer approach: for every operator found in the string,
    split the expression into left and right parts, recursively solve both,
    and combine the results using the operator.

    Args:
        expression: A string containing digits and operators ('+', '-', '*').

    Returns:
        A list of all possible integer results.

    Examples:
        >>> solve("2-1-1")
        [2, 0]
        >>> solve("2*3-4*5")
        [-34, -14, -10, -10, 10]
    """
    memo: Dict[str, List[int]] = {}

    def compute_ways(expr: str) -> List[int]:
        # Return cached result if available to avoid redundant computations
        if expr in memo:
            return memo[expr]

        results: List[int] = []
        is_number_only = True

        # Iterate through the expression to find operators
        for index, char in enumerate(expr):
            if char in "+-*":
                is_number_only = False
                
                # Divide: Split the expression at the operator
                left_results = compute_ways(expr[:index])
                right_results = compute_ways(expr[index + 1:])

                # Conquer: Combine results from left and right sub-expressions
                for left_val in left_results:
                    for right_val in right_results:
                        if char == '+':
                            results.append(left_val + right_val)
                        elif char == '-':
                            results.append(left_val - right_val)
                        elif char == '*':
                            results.append(left_val * right_val)

        # Base Case: If no operator was found, the expression is a single number
        if is_number_only:
            results.append(int(expr))

        memo[expr] = results
        return results

    return compute_ways(expression)
