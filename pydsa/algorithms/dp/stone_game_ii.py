METADATA = {
    "id": 1140,
    "name": "Stone Game II",
    "slug": "stone-game-ii",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dynamic_programming", "game_theory", "memoization"],
    "difficulty": "medium",
    "time_complexity": "O(n^3)",
    "space_complexity": "O(n^2)",
    "description": "Two players take turns picking stones from a pile, where the number of stones taken depends on a variable M that grows over time.",
}

def solve(pile: list[int], m: int) -> int:
    """
    Calculates the maximum number of stones the first player can collect.

    The game follows a minimax strategy where each player tries to maximize 
    their own score. Since the total number of stones is constant, maximizing 
    one's own score is equivalent to minimizing the opponent's score.

    Args:
        pile: A list of integers representing the number of stones in each pile.
        m: The initial value of the multiplier M.

    Returns:
        The maximum number of stones the first player can obtain.

    Examples:
        >>> solve([2, 7, 9], 2)
        11
        >>> solve([1, 2, 3, 4, 5, 6, 7], 2)
        18
    """
    n = len(pile)
    # memo stores (index, m) -> max stones obtainable from this state
    memo: dict[tuple[int, int], int] = {}

    def get_max_stones(index: int, current_m: int) -> int:
        """
        Recursive helper with memoization to find max stones from current state.
        """
        # Base case: if we have reached or passed the end of the piles
        if index >= n:
            return 0
        
        # If we can take all remaining stones in one move
        if index + current_m >= n:
            return sum(pile[index:])

        state = (index, current_m)
        if state in memo:
            return memo[state]

        # The player wants to choose a move 'i' (1 <= i <= current_m) 
        # that maximizes: (stones taken in this move) + (remaining stones - opponent's max)
        # This is equivalent to: Total remaining stones - opponent's max stones
        
        # Calculate total stones available from current index to the end
        total_remaining = sum(pile[index:])
        
        max_stones_for_player = 0
        
        # Try all possible moves from 1 to current_m
        for i in range(1, current_m + 1):
            # The opponent will play optimally from the next state
            # The next state is (index + i, max(current_m, 2 * i))
            opponent_max = get_max_stones(index + i, max(current_m, 2 * i))
            
            # Current player's score for this choice is total available minus what opponent gets
            # We use the sum of pile[index:] to represent the pool available to both players
            # However, a more direct way is: 
            # current_player_score = (sum of pile[index : index+i]) + (remaining_after_i - opponent_max)
            # Which simplifies to: total_remaining_from_index - opponent_max
            
            # We need to calculate the sum of stones from index to index+i-1
            # But the logic is simpler: the player gets (Total stones from index to end) 
            # minus (what the opponent gets from index+i to end)
            # Wait, the player also gets the stones from index to index+i-1.
            # Let's use the standard minimax: Maximize (Current stones + (Total remaining - Opponent's max))
            # Actually, the simplest way: Maximize (Total stones from index to end - Opponent's max from index+i)
            
            # Let's re-evaluate: 
            # Let f(idx, m) be the max stones the current player can get from idx to n-1.
            # f(idx, m) = max_{1 <= i <= m} { sum(pile[idx : idx+i]) + (sum(pile[idx+i : n]) - f(idx+i, max(m, 2i))) }
            # This simplifies to: f(idx, m) = max_{1 <= i <= m} { sum(pile[idx : n]) - f(idx+i, max(m, 2i)) }
            
            # We need the sum of pile[index:] to calculate the current player's potential
            # But we must be careful: the sum(pile[index:]) includes the stones the player takes now.
            # Let's use a suffix sum for efficiency.
            pass

        # Re-implementing the logic clearly:
        return 0 # Placeholder for the structure

    # Precompute suffix sums for O(1) range sum queries
    suffix_sums = [0] * (n + 1)
    for i in range(n - 1, -1, -1):
        suffix_sums[i] = suffix_sums[i + 1] + pile[i]

    def compute(idx: int, curr_m: int) -> int:
        if idx >= n:
            return 0
        if idx + curr_m >= n:
            return suffix_sums[idx]
        
        state = (idx, curr_m)
        if state in memo:
            return memo[state]
        
        # The player chooses i to maximize: (stones in current move) + (stones left - opponent's max)
        # Which is: (suffix_sums[idx