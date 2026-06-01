METADATA = {
    "id": 3693,
    "name": "Climbing Stairs II",
    "slug": "climbing_stairs_ii",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dp", "math", "fibonacci"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Calculate the number of ways to climb n stairs where each step can be of varying lengths following a modified Fibonacci recurrence.",
}

def solve(n: int) -> int:
    """
    Calculates the number of ways to climb n stairs using a modified Fibonacci sequence.
    
    The problem follows a recurrence relation where the number of ways to reach 
    step i is the sum of ways to reach previous steps, adjusted by specific 
    base cases or step constraints. For the standard 'Climbing Stairs II' 
    variation, it typically implies a Fibonacci-like progression.

    Args:
        n: The total number of stairs to climb.

    Returns:
        The total number of distinct ways to reach the top.

    Examples:
        >>> solve(1)
        1
        >>> solve(2)
        2
        >>> solve(3)
        3
        >>> solve(4)
        5
    """
    if n <= 0:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 2

    # We use two variables to maintain the state of the previous two steps
    # to achieve O(1) space complexity.
    prev_two = 1  # Represents ways to reach step i-2
    prev_one = 2  # Represents ways to reach step i-1
    current = 0

    # Iterate from the 3rd step up to n
    for _ in range(3, n + 1):
        # The current step is the sum of the ways to reach the two previous steps
        current = prev_one + prev_two
        
        # Shift the window forward for the next iteration
        prev_two = prev_one
        prev_one = current

    return prev_one
