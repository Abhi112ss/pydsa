METADATA = {
    "id": 1535,
    "name": "Find the Winner of an Array Game",
    "slug": "find-the-winner-of-an-array-game",
    "category": "Simulation",
    "aliases": [],
    "tags": ["array", "simulation"],
    "difficulty": "medium",
    "time_complexity": "O(n^2)",
    "space_complexity": "O(1)",
    "description": "Simulate a game where elements are compared and replaced until a certain number of rounds are completed or only one element remains.",
}

def solve(nums: list[int], k: int) -> int:
    """
    Simulates the array game to find the winner.

    In each round, the first two elements are compared. The smaller element 
    is replaced by the larger one. This continues for k rounds or until 
    only one element remains.

    Args:
        nums: A list of integers representing the initial state of the game.
        k: The number of rounds to simulate.

    Returns:
        The integer that remains after k rounds or when only one element is left.

    Examples:
        >>> solve([1, 3, 5, 2, 4], 2)
        5
        >>> solve([2, 1, 3, 4], 3)
        4
    """
    n = len(nums)
    # We use a pointer to simulate the 'current' winner of the previous comparison
    # to avoid unnecessary list slicing or modifications, keeping space O(1).
    current_winner = nums[0]
    rounds_completed = 0

    for i in range(1, n):
        # Compare the current winner with the next element in the array
        if nums[i] > current_winner:
            current_winner = nums[i]
        
        # Every comparison counts as a round
        rounds_completed += 1
        
        # If we have completed k rounds, the current winner is the final answer
        if rounds_completed == k:
            return current_winner

    # If we finish the loop without reaching k rounds, the maximum element found is the winner
    return current_winner
