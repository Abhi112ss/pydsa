METADATA = {
    "id": 1958,
    "name": "Check if Move is Legal",
    "slug": "check_if_move_is_legal",
    "category": "math",
    "aliases": [],
    "tags": ["math"],
    "difficulty": "easy",
    "time_complexity": "O(1)",
    "space_complexity": "O(1)",
    "description": "Determine whether a chess piece can legally move from a start square to an end square on an empty board.",
}

import sys

def solve() -> None:
    """Read test cases and output whether each move is legal.

    Args:
        Input is read from standard input.
        The first line contains an integer t, the number of test cases.
        Each of the next t lines contains:
            piece_name start_row start_col end_row end_col
        piece_name is one of: rook, bishop, queen, knight, king (case‑insensitive).

    Returns:
        For each test case, prints "true" if the move is legal for the given piece,
        otherwise prints "false".

    Examples:
        >>> # example input
        >>> # 3
        >>> # rook 1 1 1 8
        >>> # bishop 4 4 6 6
        >>> # knight 2 1 3 3
        >>> # corresponding output:
        >>> # true
        >>> # true
        >>> # false
    """
    data = sys.stdin.read().strip().split()
    if not data:
        return
    t = int(data[0])
    index = 1
    outputs: list[str] = []
    for _ in range(t):
        piece_name = data[index].lower()
        start_row = int(data[index + 1])
        start_col = int(data[index + 2])
        end_row = int(data[index + 3])
        end_col = int(data[index + 4])
        index += 5

        delta_row = abs(end_row - start_row)
        delta_col = abs(end_col - start_col)

        if piece_name == "rook":
            legal = (start_row == end_row) or (start_col == end_col)
        elif piece_name == "bishop":
            # bishop moves diagonally; must change both coordinates equally
            legal = delta_row == delta_col and delta_row != 0
        elif piece_name == "queen":
            # queen combines rook and bishop moves
            legal = (start_row == end_row) or (start_col == end_col) or (delta_row == delta_col and delta_row != 0)
        elif piece_name == "knight":
            # L‑shaped move: (2,1) or (1,2)
            legal = (delta_row == 2 and delta_col == 1) or (delta_row == 1 and delta_col == 2)
        elif piece_name == "king":
            # one square in any direction
            legal = max(delta_row, delta_col) == 1 and (delta_row != 0 or delta_col != 0)
        else:
            legal = False  # unknown piece

        outputs.append("true" if legal else "false")
    sys.stdout.write("\n".join(outputs))
