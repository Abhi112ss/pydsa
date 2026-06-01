METADATA = {
    "id": 2019,
    "name": "The Score of Students Solving Math Expression",
    "slug": "the-score-of-students-solving-math-expression",
    "category": "Simulation",
    "aliases": [],
    "tags": ["math", "simulation", "string"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Calculate the total score of students based on their answers to mathematical expressions involving addition and subtraction.",
}

def solve(expression: str, answers: list[str]) -> int:
    """
    Calculates the total score of students based on their answers to math expressions.
    
    The scoring rules are:
    - If the expression is 'a + b' and the student answers 'a + b', they get 2 points.
    - If the expression is 'a - b' and the student answers 'a - b', they get 1 point.
    - Otherwise, they get 0 points.
    
    Note: This implementation assumes the input follows the standard format 
    'operand operator operand' as per the problem description.

    Args:
        expression: A string representing the mathematical expression (e.g., "1 + 2").
        answers: A list of strings representing the students' answers.

    Returns:
        The total score accumulated by all students.

    Examples:
        >>> solve("1 + 2", ["1 + 2", "1 - 2"])
        2
        >>> solve("5 - 3", ["5 - 3", "5 + 3"])
        1
    """
    # Split the expression into components: [operand1, operator, operand2]
    # Since the expression is fixed format "a + b", we can split by space.
    expr_parts = expression.split()
    if len(expr_parts) != 3:
        return 0
        
    operator = expr_parts[1]
    total_score = 0

    for answer in answers:
        # Check if the answer matches the expression exactly
        if answer == expression:
            # If it's addition, the student gets 2 points
            if operator == "+":
                total_score += 2
            # If it's subtraction, the student gets 1 point
            elif operator == "-":
                total_score += 1
        # If the answer is incorrect, they get 0 points (no action needed)
                
    return total_score
