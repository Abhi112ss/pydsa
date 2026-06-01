METADATA = {
    "id": 3025,
    "name": "Find the Number of Ways to Place People I",
    "slug": "find-the-number-of-ways-to-place-people-i",
    "category": "Math",
    "aliases": [],
    "tags": ["sorting", "two_pointer", "geometry"],
    "difficulty": "medium",
    "time_complexity": "O(n^2)",
    "space_complexity": "O(1)",
    "description": "Count the number of pairs of points that can form a valid rectangle containing no other points.",
}

def solve(points: list[list[int]]) -> int:
    """
    Finds the number of ways to choose two people such that one is at the top-left 
    and the other is at the bottom-right of a rectangle containing no other people.

    Args:
        points: A list of [x, y] coordinates representing the positions of people.

    Returns:
        The number of valid pairs (Alice at top-left, Bob at bottom-right).

    Examples:
        >>> solve([[1, 1], [2, 2], [3, 3]])
        2
        >>> solve([[0, 0], [1, 1], [0, 1], [1, 0]])
        4
    """
    # Sort points primarily by x ascending, and secondarily by y descending.
    # This ensures that for any pair (i, j) where i < j, point i is to the left 
    # of point j (or on the same x-line but higher up).
    points.sort(key=lambda p: (p[0], -p[1]))
    
    n = len(points)
    valid_count = 0

    for i in range(n):
        x_alice, y_alice = points[i]
        
        # We need to find a Bob (points[j]) such that:
        # 1. x_alice <= x_bob and y_alice >= y_bob
        # 2. No other point k is inside the rectangle defined by Alice and Bob.
        
        # To satisfy the "no other point inside" condition, as we iterate through 
        # potential Bobs (j > i), we keep track of the highest y-coordinate 
        # seen so far that is less than or equal to y_alice.
        max_y_seen_for_bob = float('-inf')
        
        for j in range(i + 1, n):
            x_bob, y_bob = points[j]
            
            # Condition 1: Bob must be at or below Alice's y-level.
            # (x_bob >= x_alice is guaranteed by sorting).
            if y_bob <= y_alice:
                # Condition 2: To ensure no point is inside the rectangle,
                # the current y_bob must be greater than the y of any 
                # previously valid Bob we encountered in this inner loop.
                # This is because any point between the current Bob and the 
                # previous Bob would have been "inside" if its y was higher.
                if y_bob > max_y_seen_for_bob:
                    valid_count += 1
                    max_y_seen_for_bob = y_bob
                    
    return valid_count
