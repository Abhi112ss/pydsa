METADATA = {
    "id": 2232,
    "name": "Minimize Result by Adding Parentheses to Expression",
    "slug": "minimize-result-by-adding-parentheses-to-expression",
    "category": "Backtracking",
    "aliases": [],
    "tags": ["backtracking", "recursion"],
    "difficulty": "medium",
    "time_complexity": "O(n!)",
    "space_complexity": "O(n)",
    "description": "Minimize the result of an expression by adding parentheses to change the order of operations.",
}

def solve(expression: str) -> int:
    """
    Finds the minimum possible result of an expression by adding parentheses.

    The expression consists of digits and '+' or '-' operators. Adding parentheses
    effectively changes the order in which the operations are performed.

    Args:
        expression: A string representing the mathematical expression.

    Returns:
        The minimum integer result possible.

    Examples:
        >>> solve("1-2-3")
        4
        >>> solve("1+2-3-4+5*6")
        -23
    """
    # Convert string to a list of integers and operators for easier processing
    tokens: list[int | str] = []
    current_num = 0
    for char in expression:
        if char.isdigit():
            current_num = current_num * 10 + int(char)
        else:
            tokens.append(current_num)
            tokens.append(char)
            current_num = 0
    tokens.append(current_num)

    def compute_min(ops_indices: list[int]) -> int:
        """
        Recursive helper that evaluates the expression based on the order of operations.
        
        Args:
            ops_indices: A list of indices of the operators in the current expression.
            
        Returns:
            The minimum value for the current state of the expression.
        """
        if not ops_indices:
            # Base case: No more operators, return the only remaining number
            return tokens[0]

        min_val = float('inf')

        # Try every possible operator to be the "last" operation performed
        for i in range(len(ops_indices)):
            # The index of the operator in the 'tokens' list
            op_idx = ops_indices[i]
            
            # Split the current list of operators into left and right parts
            left_ops = ops_indices[:i]
            right_ops = ops_indices[i+1:]

            # Calculate the value of the left side and right side
            # We simulate the split by creating temporary token lists
            
            # Left side tokens: everything up to the operator
            left_tokens = tokens[:op_idx]
            # Right side tokens: everything after the operator
            right_tokens = tokens[op_idx + 1:]

            # To handle the recursion, we need to pass the state of the tokens.
            # However, a more efficient way is to pass the current tokens and 
            # the indices of operators available.
            
            # Since we need to modify the tokens list for the next level, 
            # we use a local copy or a way to reconstruct the expression.
            # A cleaner way for this specific problem is to pass the current 
            # list of numbers and operators.
            pass

        return int(min_val)

    # Redefining the recursive approach to be more robust with list slicing
    def backtrack(current_tokens: list[int | str]) -> int:
        # Find all operator indices in the current token list
        op_indices = [i for i, token in enumerate(current_tokens) if isinstance(token, str)]
        
        if not op_indices:
            return current_tokens[0]

        res = float('inf')
        
        # Try splitting the expression at every operator
        for i in range(len(op_indices)):
            idx = op_indices[i]
            
            # Split into left and right sub-expressions
            left_part = current_tokens[:idx]
            right_part = current_tokens[idx + 1:]
            
            # Recursively find the min/max of both sides. 
            # Note: To minimize (A - B), we need (min(A) - max(B)).
            # To minimize (A + B), we need (min(A) + min(B)).
            # This implies we actually need both min and max from the recursion.
            pass
        return 0

    # Corrected approach: Return both (min, max) to handle subtraction correctly
    def get_min_max(current_tokens: list[int | str]) -> tuple[int, int]:
        op_indices = [i for i, token in enumerate(current_tokens) if isinstance(token, str)]
        
        if not op_indices:
            val = current_tokens[0]
            return val, val

        min_res = float('inf')
        max_res = float('-inf')

        for i in range(len(op_indices)):
            idx = op_indices[i]
            op = current_tokens[idx]
            
            # Split the tokens into two sub-expressions
            left_min, left_max = get_min_max(current_tokens[:idx])
            right_min, right_max = get_min_max(current_tokens[idx + 1:])

            # Calculate all 4 possible combinations of min/max for the current operator
            if op == '+':
                vals = [
                    left_min + right_min,
                    left_min + right_max,
                    left_max + right_min,
                    left_max + right_max
                ]
            else:  # op == '-'
                vals = [
                    left_min - right_min,
                    left_min - right_max,
                    left_max - right_min,
                    left_max - right_max
                ]
            
            # Update the global min and max for this sub-expression
            min_res = min(min_res, min(vals))
            max_res = max(max_res, max(vals))

        return int(min_res), int(max_res)

    result_min, _ = get_min_max(tokens)
    return result_min
