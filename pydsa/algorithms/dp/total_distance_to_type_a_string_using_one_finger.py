METADATA = {
    "id": 3846,
    "name": "Total Distance to Type a String Using One Finger",
    "slug": "total-distance-to-type-a-string-using-one-finger",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dp", "string", "greedy"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Calculate the minimum total distance to type a string using one finger on a keyboard layout.",
}

def solve(keyboard: list[list[int]], target: str) -> int:
    """
    Calculates the minimum total distance to type a target string using one finger.
    
    The finger moves between characters on a keyboard layout. The distance between 
    two characters is the Manhattan distance between their coordinates.
    
    Args:
        keyboard: A 2D list representing the keyboard layout where each element 
                  is the character at that position.
        target: The string to be typed.

    Returns:
        The minimum total Manhattan distance required to type the string.

    Examples:
        >>> keyboard = [['a', 'b'], ['c', 'd']]
        >>> target = "ac"
        >>> solve(keyboard, target)
        2
    """
    # Map each character to its (row, col) coordinates for O(1) lookup
    char_to_pos: dict[str, tuple[int, int]] = {}
    rows = len(keyboard)
    cols = len(keyboard[0])
    
    for r in range(rows):
        for c in range(cols):
            char_to_pos[keyboard[r][c]] = (r, c)

    # Convert target string to a list of coordinates
    target_coords = [char_to_pos[char] for char in target]
    n = len(target_coords)
    
    if n <= 1:
        return 0

    # dp[i] represents the minimum distance to have typed up to target_coords[i]
    # Since we only use one finger, the state is simply the cumulative distance.
    # The problem implies we start at the first character of the target string.
    # If the problem implies starting at (0,0), the logic would adjust, 
    # but standard "typing" problems assume the first char is the starting point.
    
    total_distance = 0
    for i in range(1, n):
        prev_r, prev_c = target_coords[i - 1]
        curr_r, curr_c = target_coords[i]
        
        # Manhattan distance: |x1 - x2| + |y1 - y2|
        dist = abs(prev_r - curr_r) + abs(prev_c - curr_c)
        total_distance += dist
        
    return total_distance
