METADATA = {
    "id": 3064,
    "name": "Guess the Number Using Bitwise Questions I",
    "slug": "guess-the-number-using-bitwise-questions-i",
    "category": "Binary Search",
    "aliases": [],
    "tags": ["binary_search", "bit_manipulation"],
    "difficulty": "medium",
    "time_complexity": "O(log n)",
    "space_complexity": "O(1)",
    "description": "Find a hidden number within a range by asking bitwise questions to determine if specific bits are set.",
}

class GuessGame:
    """
    A helper class to simulate the game environment.
    In a real LeetCode scenario, this is provided by the judge.
    """
    def __init__(self, target: int):
        self.target = target

    def query(self, bit_index: int) -> bool:
        """Returns True if the bit_index-th bit of target is 1, else False."""
        return bool((self.target >> bit_index) & 1)

def solve(game: GuessGame, n: int) -> int:
    """
    Finds the hidden number using bitwise queries.

    Args:
        game: An instance of GuessGame providing the query method.
        n: The upper bound of the range [1, n].

    Returns:
        The hidden number.

    Examples:
        >>> game = GuessGame(5)
        >>> solve(game, 10)
        5
    """
    hidden_number = 0
    
    # Determine the maximum number of bits needed to represent n.
    # Since n can be up to 10^9, we check up to 30 bits (2^30 > 10^9).
    # We iterate through each bit position from 0 upwards.
    for bit_index in range(31):
        # If the current bit position exceeds the range of n, 
        # we can stop early if we know the number is within [1, n].
        # However, checking all 31 bits is O(1) constant time.
        
        if game.query(bit_index):
            # If the query returns True, the bit at bit_index is set in the target.
            # We use bitwise OR to set this bit in our reconstructed number.
            hidden_number |= (1 << bit_index)
            
    return hidden_number
