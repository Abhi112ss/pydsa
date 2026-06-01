METADATA = {
    "id": 2140,
    "name": "Solving Questions With Brainpower",
    "slug": "solving-questions-with-brainpower",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dp", "array"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Find the maximum points you can earn by solving questions given specific brainpower requirements for each question.",
}

def solve(brainpower: list[int], points: list[int]) -> int:
    """
    Calculates the maximum points achievable given the brainpower constraints.

    For each question i, if you solve it, you must skip the next brainpower[i] questions.
    This is a variation of the House Robber problem where the 'jump' distance varies.

    Args:
        brainpower: A list of integers where brainpower[i] is the number of 
            questions to skip after solving question i.
        points: A list of integers where points[i] is the points gained from 
            solving question i.

    Returns:
        The maximum total points possible.

    Examples:
        >>> solve([1, 1, 1, 1], [1, 1, 1, 1])
        2
        >>> solve([0, 1, 1, 1, 1], [1, 1, 1, 1, 1])
        3
    """
    n = len(brainpower)
    # dp[i] stores the maximum points we can get starting from index i to the end.
    # We use n + 1 to handle the base case of index n easily.
    dp = [0] * (n + 1)

    # We iterate backwards from the last question to the first.
    # This allows us to build the solution using previously computed optimal subproblems.
    for i in range(n - 1, -1, -1):
        # Option 1: Skip the current question.
        # The max points will be whatever we could get starting from the next question.
        skip_current = dp[i + 1]

        # Option 2: Solve the current question.
        # We get points[i] plus the max points from the question after the skip range.
        next_available_index = i + brainpower[i] + 1
        
        # If the next available index is within bounds, add its DP value.
        if next_available_index < n:
            solve_current = points[i] + dp[next_available_index]
        else:
            # If the skip range goes beyond the array, we just get the current points.
            solve_current = points[i]

        # The optimal choice for index i is the maximum of the two options.
        dp[i] = max(skip_current, solve_current)

    return dp[0]
