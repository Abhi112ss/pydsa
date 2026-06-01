METADATA = {
    "id": 3094,
    "name": "Guess the Number Using Bitwise Questions II",
    "slug": "guess-the-number-using-bitwise-questions-ii",
    "category": "Binary Search",
    "aliases": [],
    "tags": ["binary_search", "bit_manipulation"],
    "difficulty": "medium",
    "time_complexity": "O(log n)",
    "space_complexity": "O(1)",
    "description": "Find a hidden number in a range [1, n] using bitwise AND queries.",
}

class GuessGame:
    """
    A helper class to simulate the game environment.
    Note: In LeetCode, this is provided by the system.
    """
    def __init__(self, target: int):
        self.target = target

    def query(self, x: int) -> int:
        return x & self.target

class Solution:
    def guessNumber(self, n: int, game: GuessGame) -> int:
        """
        Finds the target number using bitwise AND queries.

        The core idea is to determine the target bit by bit. For each bit position 'i',
        we check if the target has that bit set by querying a number that has only 
        that bit set (or a combination of bits). However, since the query is (x & target),
        if we query a power of 2 (e.g., 1, 2, 4, 8...), the result will be either 
        that power of 2 (if the bit is set) or 0 (if the bit is not set).

        Args:
            n: The upper bound of the range [1, n].
            game: An instance of GuessGame providing the query method.

        Returns:
            The hidden target number.

        Examples:
            >>> class MockGame:
            ...     def __init__(self, target): self.target = target
            ...     def query(self, x): return x & self.target
            >>> sol = Solution()
            >>> sol.guessNumber(10, MockGame(6))
            6
        """
        target = 0
        
        # We iterate through each bit position from 0 up to the maximum possible bit for n.
        # Since n can be up to 10^9, 30 bits are sufficient (2^30 > 10^9).
        for bit_index in range(31):
            # Create a mask representing the current bit position (1, 2, 4, 8...)
            bit_mask = 1 << bit_index
            
            # If the bit_mask exceeds n, we can stop early if we only care about bits within n,
            # but checking all 31 bits is safe and constant time.
            if bit_mask > n:
                # We must check if this bit is actually part of the target.
                # However, if bit_mask > n, the target cannot have this bit set 
                # unless the target itself is larger than n, which contradicts the problem.
                # But to be safe and handle all bits, we continue or break.
                if bit_mask > 2**31: # Safety break
                    break
            
            # Perform the bitwise AND query.
            # If (bit_mask & target) == bit_mask, then the bit is set in the target.
            # Because the query returns (bit_mask & target), if the bit is set, 
            # the result will be exactly bit_mask.
            if game.query(bit_mask) == bit_mask:
                target |= bit_mask
                
        return target

# Example usage for local testing
