METADATA = {
    "id": 682,
    "name": "Baseball Game",
    "slug": "baseball_game",
    "category": "Stack",
    "aliases": [],
    "tags": ["stack", "simulation"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Calculate the total points after applying a sequence of baseball game operations.",
}


def solve(operations: list[str]) -> int:
    """Calculate the total score after processing baseball game operations.

    Args:
        operations: A list of strings where each string is either an integer
            representing a new score, or one of the commands:
            "C" – invalidate the previous score,
            "D" – double the previous score,
            "+" – sum of the previous two scores.

    Returns:
        The sum of all valid scores after applying all operations.

    Examples:
        >>> solve(["5","2","C","D","+"])
        30
        >>> solve(["5","-2","4","C","D","9","+","+"])
        27
    """
    valid_scores: list[int] = []

    for record in operations:
        if record == "C":
            # Remove the last valid score
            valid_scores.pop()
        elif record == "D":
            # Double the previous score and store it
            valid_scores.append(2 * valid_scores[-1])
        elif record == "+":
            # Sum of the previous two scores
            valid_scores.append(valid_scores[-1] + valid_scores[-2])
        else:
            # New integer score
            valid_scores.append(int(record))

    # Return the total of all valid scores
    return sum(valid_scores)