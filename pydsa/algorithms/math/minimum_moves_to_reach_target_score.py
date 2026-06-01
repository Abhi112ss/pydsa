METADATA = {
    "id": 2139,
    "name": "Minimum Moves to Reach Target Score",
    "slug": "minimum-moves-to-reach-target-score",
    "category": "Math",
    "aliases": [],
    "tags": ["math", "greedy"],
    "difficulty": "medium",
    "time_complexity": "O(1)",
    "space_complexity": "O(1)",
    "description": "Find the minimum number of moves to reach a target score using doubling or incrementing operations.",
}

def solve(target: int) -> int:
    """
    Calculates the minimum number of moves to reach a target score starting from 1.
    
    The strategy is to work backwards from the target to 1. If the current score 
    is even, the most efficient move was a doubling operation (division by 2). 
    If the current score is odd, the only possible move was an increment (subtraction by 1).

    Args:
        target: The target score to reach.

    Returns:
        The minimum number of moves required.

    Examples:
        >>> solve(10)
        5
        # 1 -> 2 -> 4 -> 5 -> 10 (or 1 -> 2 -> 3 -> 5 -> 10)
        >>> solve(1)
        0
    """
    moves = 0
    current_score = target

    while current_score > 1:
        if current_score % 2 == 0:
            # If even, the optimal previous step was doubling
            current_score //= 2
        else:
            # If odd, the only previous step was adding 1
            current_score -= 1
        moves += 1

    return moves
