METADATA = {
    "id": 2543,
    "name": "Check if Point Is Reachable",
    "slug": "check-if-point-is-reachable",
    "category": "Math",
    "aliases": [],
    "tags": ["math", "greedy"],
    "difficulty": "medium",
    "time_complexity": "O(log(max(x, y)))",
    "space_complexity": "O(1)",
    "description": "Determine if a target point (x, y) can be reached from (1, 1) using specific jump rules.",
}

def solve(x: int, y: int) -> bool:
    """
    Determines if the point (x, y) is reachable from (1, 1) using the given jump rules.
    
    The rules allow jumping from (x, y) to (x + 2*x*k, y + 2*y*k) or (x + 2*y*k, y + 2*x*k).
    Working backwards from (x, y) to (1, 1), we greedily reduce the larger coordinate
    using the modulo operator to simulate multiple jumps at once.

    Args:
        x: The x-coordinate of the target point.
        y: The y-coordinate of the target point.

    Returns:
        True if the point (x, y) is reachable from (1, 1), False otherwise.

    Examples:
        >>> solve(5, 7)
        True
        >>> solve(1, 2)
        False
        >>> solve(1, 1)
        True
    """
    # Base case: if we are already at (1, 1), it is reachable.
    if x == 1 and y == 1:
        return True

    while x > 1 and y > 1:
        if x > y:
            # If x is larger, we reduce x using the jump rule: x_new = x - 2 * y * k
            # We want to find the largest k such that x - 2 * y * k >= 1.
            # This is equivalent to (x - 1) // (2 * y).
            # We use modulo to jump directly to the smallest possible positive x.
            if y == 0: return False # Safety check, though constraints say x,y >= 1
            
            # The jump size is 2 * y. We need to ensure we don't jump below 1.
            # We use (x - 1) % (2 * y) to find the remainder relative to the jump step.
            # However, the jump is specifically 2*y*k. 
            # So x_new = x - 2 * y * k. We want x_new to be 1 or more.
            # Let's use the property: x_new = x % (2 * y). 
            # If x % (2 * y) == 0, the smallest positive value is 2 * y.
            # But we must ensure we don't go below 1.
            
            # Correct greedy step:
            # We need to subtract multiples of (2 * y) from x.
            # To keep x >= 1, we calculate how many 2*y we can subtract.
            # k = (x - 1) // (2 * y)
            # If k == 0, we can't reduce x further while keeping it > 1 and x > y.
            k = (x - 1) // (2 * y)
            if k == 0:
                break
            x -= k * (2 * y)
        elif y > x:
            # Symmetric case for when y is larger.
            k = (y - 1) // (2 * x)
            if k == 0:
                break
            y -= k * (2 * x)
        else:
            # If x == y and they are not 1, they can never be reduced to 1 
            # because the jump rule requires one coordinate to be strictly larger 
            # or the jump would result in (x + 2xk, x + 2xk), which doesn't help 
            # reach (1, 1) unless x=1.
            break

    return x == 1 and y == 1