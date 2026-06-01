METADATA = {
    "id": 1769,
    "name": "Minimum Number of Operations to Move All Balls to Each Box",
    "slug": "minimum-number-of-operations-to-move-all-balls-to-each-box",
    "category": "Array",
    "aliases": [],
    "tags": ["prefix_sum", "array", "two_pointers"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Calculate the total number of moves required to move all balls to each box using two passes.",
}

def solve(boxes: list[str]) -> list[int]:
    """
    Calculates the minimum number of operations to move all balls to each box.
    
    The algorithm uses a two-pass approach (left-to-right and right-to-left) 
    to accumulate the total distance in O(n) time.

    Args:
        boxes: A list of strings where '1' represents a ball and '0' represents an empty box.

    Returns:
        A list of integers where the i-th integer is the total moves to move all balls to box i.

    Examples:
        >>> solve(["1","0","0","0","1"])
        [4, 3, 2, 3, 4]
        >>> solve(["0","1"])
        [1, 0]
    """
    n = len(boxes)
    result = [0] * n
    
    # First pass: Left to Right
    # Calculate moves required to bring all balls from the left side to the current box
    balls_count = 0
    current_moves = 0
    for i in range(n):
        result[i] += current_moves
        if boxes[i] == '1':
            balls_count += 1
        # Every ball encountered so far will need 1 more move to reach the next box
        current_moves += balls_count
        
    # Second pass: Right to Left
    # Calculate moves required to bring all balls from the right side to the current box
    balls_count = 0
    current_moves = 0
    for i in range(n - 1, -1, -1):
        result[i] += current_moves
        if boxes[i] == '1':
            balls_count += 1
        # Every ball encountered so far will need 1 more move to reach the previous box
        current_moves += balls_count
        
    return result
