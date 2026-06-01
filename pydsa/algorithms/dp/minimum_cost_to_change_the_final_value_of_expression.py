METADATA = {
    "id": 1896,
    "name": "Minimum Cost to Change the Final Value of Expression",
    "slug": "minimum-cost-to-change-the-final-value-of-expression",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dp", "strings", "greedy"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Find the minimum cost to change characters in an expression to make its final value equal to a target.",
}

def solve(expression: str, target: int) -> int:
    """
    Calculates the minimum cost to change characters in the expression to reach the target value.

    The expression consists of digits and operators ('+', '-'). The value is calculated
    from left to right. We use dynamic programming to track the minimum cost to reach
    each possible value at each step.

    Args:
        expression: A string representing the mathematical expression.
        target: The target integer value the expression should evaluate to.

    Returns:
        The minimum cost to modify the expression. Returns -1 if the target is unreachable.

    Examples:
        >>> solve("1+1-1+1", 3)
        1
        >>> solve("1-1+1", 1)
        0
        >>> solve("1+1-1+1", 10)
        -1
    """
    # The maximum possible value is 100 (10 digits * 10) and minimum is -100.
    # We use an offset of 100 to map range [-100, 100] to [0, 200].
    OFFSET = 100
    MAX_VAL = 200
    INF = float('inf')

    # dp[v] stores the minimum cost to achieve value (v - OFFSET)
    dp = [INF] * (MAX_VAL + 1)

    # Initial state: process the first number
    first_num_str = expression[:1]
    first_num_val = int(first_num_str)
    
    # We can change the first digit to any digit 0-9
    for digit in range(10):
        cost = 0 if digit == first_num_val else 1
        dp[digit + OFFSET] = min(dp[digit + OFFSET], cost)

    # Iterate through the rest of the expression in chunks of 2 (operator + digit)
    # expression[i] is the operator, expression[i+1] is the digit
    for i in range(1, len(expression), 2):
        operator = expression[i]
        digit_char = expression[i + 1]
        current_digit = int(digit_char)
        
        new_dp = [INF] * (MAX_VAL + 1)
        
        # Try all possible values reached in the previous step
        for val_idx in range(MAX_VAL + 1):
            if dp[val_idx] == INF:
                continue
            
            prev_val = val_idx - OFFSET
            
            # Try changing the current operator and current digit
            # Operators: '+' (cost 0 if same, 1 if different), '-' (cost 0 if same, 1 if different)
            # Digits: 0-9 (cost 0 if same, 1 if different)
            for op in ['+', '-']:
                op_cost = 0 if op == operator else 1
                
                for d in range(10):
                    digit_cost = 0 if d == current_digit else 1
                    
                    # Calculate the new value based on the operator
                    if op == '+':
                        new_val = prev_val + d
                    else:
                        new_val = prev_val - d
                    
                    # Check bounds and update the DP table
                    if -100 <= new_val <= 100:
                        total_cost = dp[val_idx] + op_cost + digit_cost
                        new_idx = new_val + OFFSET
                        if total_cost < new_dp[new_idx]:
                            new_dp[new_idx] = total_cost
        
        dp = new_dp

    result = dp[target + OFFSET]
    return int(result) if result != INF else -1
