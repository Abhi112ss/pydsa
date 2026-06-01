METADATA = {
    "id": 282,
    "name": "Expression Add Operators",
    "slug": "expression-add-operators",
    "category": "Backtracking",
    "aliases": [],
    "tags": ["backtracking", "recursion", "math", "string"],
    "difficulty": "hard",
    "time_complexity": "O(4^n)",
    "space_complexity": "O(n)",
    "description": "Given a string containing only digits, return all possibilities to insert binary operators +, -, or * between the digits such that the resulting expression evaluates to a target value.",
}

def solve(num: str, target: int) -> list[str]:
    """
    Finds all possible expressions formed by inserting +, -, or * between digits 
    that evaluate to the target value.

    Args:
        num: A string of digits.
        target: The target integer value.

    Returns:
        A list of strings representing valid expressions.

    Examples:
        >>> solve("123", 6)
        ['1+2+3', '1*2*3']
        >>> solve("105", 5)
        ['1*0+5', '10-5']
    """
    results: list[str] = []
    n = len(num)

    def backtrack(index: int, current_expression: str, current_value: int, last_operand: int) -> None:
        """
        Recursive helper to explore all operator combinations.

        Args:
            index: Current position in the input string.
            current_expression: The expression string built so far.
            current_value: The evaluated result of the current expression.
            last_operand: The value of the last operand added (used to handle multiplication precedence).
        """
        if index == n:
            if current_value == target:
                results.append(current_expression)
            return

        for i in range(index, n):
            # Handle leading zeros: numbers like "05" are invalid, but "0" is valid.
            if i > index and num[index] == '0':
                break

            # Extract the current substring as an integer
            substring = num[index : i + 1]
            val = int(substring)

            if index == 0:
                # First number in the expression: no operator precedes it
                backtrack(i + 1, substring, val, val)
            else:
                # Addition
                backtrack(i + 1, f"{current_expression}+{substring}", current_value + val, val)
                
                # Subtraction
                backtrack(i + 1, f"{current_expression}-{substring}", current_value - val, -val)
                
                # Multiplication: To handle precedence, we undo the last operation 
                # and apply the multiplication to the last operand.
                # Example: 2 + 3 * 4 -> (2 + 3) - 3 + (3 * 4) = 14
                backtrack(
                    i + 1, 
                    f"{current_expression}*{substring}", 
                    (current_value - last_operand) + (last_operand * val), 
                    last_operand * val
                )

    backtrack(0, "", 0, 0)
    return results
