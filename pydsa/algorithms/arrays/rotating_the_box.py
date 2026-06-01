METADATA = {
    "id": 1861,
    "name": "Rotating the Box",
    "slug": "rotating-the-box",
    "category": "Simulation",
    "aliases": [],
    "tags": ["matrix", "simulation"],
    "difficulty": "medium",
    "time_complexity": "O(m * n)",
    "space_complexity": "O(1)",
    "description": "Rotate a 2D matrix 90 degrees clockwise and simulate gravity for stones in each row.",
}

def solve(box: list[list[int]]) -> list[list[int]]:
    """
    Rotates the box 90 degrees clockwise and simulates gravity for stones.

    Args:
        box: A 2D list of integers representing the box where 1 is a stone and 0 is empty.

    Returns:
        A 2D list of integers representing the box after rotation and gravity simulation.

    Examples:
        >>> solve([[1,1,0],[0,0,0],[0,3,1]])
        [[0,0,1],[0,0,1],[1,3,0]]
    """
    if not box or not box[0]:
        return box

    rows = len(box)
    cols = len(box[0])

    # Step 1: Rotate the box 90 degrees clockwise.
    # The new dimensions will be (cols x rows).
    # A cell at (r, c) in the original box moves to (c, rows - 1 - r) in the rotated box.
    rotated_box = [[0 for _ in range(rows)] for _ in range(cols)]
    for r in range(rows):
        for c in range(cols):
            rotated_box[c][rows - 1 - r] = box[r][c]

    # Step 2: Simulate gravity for each row in the rotated box.
    # We iterate through each row and use a pointer to track the lowest available empty position.
    new_rows = len(rotated_box)
    new_cols = len(rotated_box[0])

    for r in range(new_rows):
        # 'empty_slot' tracks the rightmost position a stone can fall into.
        empty_slot = new_cols - 1
        for c in range(new_cols - 1, -1, -1):
            if rotated_box[r][c] == 0:
                # If we find an empty space, it becomes a potential landing spot.
                empty_slot = c
            elif rotated_box[r][c] > 0:
                # If we find a stone, move it to the 'empty_slot' if they are different.
                # We use a temporary variable to hold the stone value.
                stone_value = rotated_box[r][c]
                rotated_box[r][c] = 0
                rotated_box[r][empty_slot] = stone_value
                # The next stone must land above the current empty_slot.
                empty_slot -= 1

    return rotated_box
