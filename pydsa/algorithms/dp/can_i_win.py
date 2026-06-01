METADATA = {
    "id": 464,
    "name": "Can I Win",
    "slug": "can-i-win",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["memoization", "bitmask", "dynamic_programming", "recursion"],
    "difficulty": "medium",
    "time_complexity": "O(2^n * n)",
    "space_complexity": "O(2^n)",
    "description": "Determine if the first player can win a game given a target sum and a set of available numbers.",
}

def solve(max_pick: int, target: int, available_numbers: list[int]) -> bool:
    """
    Determines if the first player can win the game.

    The game is played by two players. In each turn, a player chooses a number 
    from the available set that hasn't been used yet. The goal is to reach 
    or exceed the target sum.

    Args:
        max_pick: The maximum value of a number that can be picked.
        target: The target sum to reach.
        available_numbers: A list of integers available to be picked.

    Returns:
        True if the first player can win, False otherwise.

    Examples:
        >>> solve(10, 16, [1, 2, 3, 4, 5, 6, 7])
        True
        >>> solve(10, 16, [1, 2, 3, 4, 5, 6, 7]) # If target is impossible
        False
    """
    # If the sum of all available numbers is less than the target, no one can win.
    if sum(available_numbers) < target:
        return False

    # Memoization dictionary to store the result of each state.
    # The state is represented by a bitmask of used numbers.
    memo: dict[int, bool] = {}

    def can_win(current_target: int, mask: int) -> bool:
        """
        Recursive helper using bitmasking to represent the state of used numbers.

        Args:
            current_target: The remaining sum needed to win.
            mask: An integer bitmask where the i-th bit is 1 if available_numbers[i] is used.

        Returns:
            True if the current player can force a win from this state.
        """
        if current_target <= 0:
            return False
        
        if mask in memo:
            return memo[mask]

        # Try picking every available number
        for i in range(len(available_numbers)):
            # Check if the i-th number has already been used via bitmask
            if not (mask & (1 << i)):
                num = available_numbers[i]
                
                # If picking this number reaches the target, the current player wins.
                # Otherwise, the current player wins if the NEXT player cannot win.
                if num >= current_target or not can_win(current_target - num, mask | (1 << i)):
                    memo[mask] = True
                    return True

        # If no move leads to a win, the current player loses.
        memo[mask] = False
        return False

    return can_win(target, 0)
