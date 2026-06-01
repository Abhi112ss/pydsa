METADATA = {
    "id": 293,
    "name": "Flip Game",
    "slug": "flip_game",
    "category": "String",
    "aliases": [],
    "tags": ["string_manipulation", "simulation"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Return all possible strings after flipping a single '++' to '--'.",
}


def solve(s: str) -> list[str]:
    """Generate all possible states of the game after one valid flip.

    Args:
        s: A string consisting only of '+' and '-' characters.

    Returns:
        A list of strings, each representing a board configuration after
        flipping exactly one occurrence of "++" to "--".

    Examples:
        >>> solve("++++")
        ['--++', '+--+', '++--']
        >>> solve("+-++")
        ['+---']
        >>> solve("----")
        []
    """
    possible_states: list[str] = []
    board_length: int = len(s)

    # Iterate over each pair of adjacent characters.
    for index in range(board_length - 1):
        # Check for a valid "++" that can be flipped.
        if s[index] == '+' and s[index + 1] == '+':
            # Build the new state by replacing the found "++" with "--".
            new_state = s[:index] + '--' + s[index + 2 :]
            possible_states.append(new_state)

    return possible_states