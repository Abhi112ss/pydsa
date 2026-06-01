METADATA = {
    "id": 70,
    "name": "Climbing Stairs",
    "slug": "climbing-stairs",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dynamic_programming", "math", "fibonacci"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Find the number of distinct ways to climb to the top of a staircase with n steps, where you can take either 1 or 2 steps at a time.",
}

def solve(n: int) -> int:
    """
    Calculates the number of distinct ways to climb n stairs using 1 or 2 steps.
    
    The problem follows the Fibonacci sequence recurrence relation:
    ways(n) = ways(n-1) + ways(n-2), because to reach step n, 
    you must have come from either step n-1 or step n-2.

    Args:
        n: The total number of steps to reach the top.

    Returns:
        The total number of distinct ways to reach the top.

    Examples:
        >>> solve(2)
        2
        >>> solve(3)
        3
        >>> solve(5)
        8
    """
    # Base cases: if there are 0 or 1 steps, there is only 1 way (staying put or 1 step).
    # For n=2, the result is 2 (1+1 or 2).
    if n <= 2:
        return n

    # We only need to keep track of the previous two values to calculate the current one.
    # This allows us to achieve O(1) space complexity.
    first_step_back = 1  # Represents ways(i-2)
    second_step_back = 2 # Represents ways(i-1)

    # Iterate from the 3rd step up to n.
    for _ in range(3, n + 1):
        # The current number of ways is the sum of the previous two.
        current_ways = first_step_back + second_step_back
        
        # Shift the window forward for the next iteration.
        first_step_back = second_step_back
        second_step_back = current_ways

    return second_step_back
