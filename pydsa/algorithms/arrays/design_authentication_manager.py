METADATA = {
    "id": 1797,
    "name": "Design Authentication Manager",
    "slug": "design-authentication-manager",
    "category": "Design",
    "aliases": [],
    "tags": ["hash_map", "heap", "design"],
    "difficulty": "medium",
    "time_complexity": "O(log n) for generate/revoke, O(1) for validate",
    "space_complexity": "O(n)",
    "description": "Design a system to manage user authentication tokens with expiration times.",
}

import heapq

class AuthenticationManager:
    def __init__(self, time_lim: int):
        """
        Initializes the authentication manager.

        Args:
            time_lim (int): The duration for which a token is valid.
        """
        self.time_lim = time_lim
        # Maps token string to its absolute expiration time
        self.token_map: dict[str, int] = {}
        # Min-heap to store (expiration_time, token) for efficient cleanup
        self.expiry_heap: list[tuple[int, str]] = []

    def generate(self, token: str, time: int) -> None:
        """
        Generates a new token that expires at time + time_lim.

        Args:
            token (str): The token string.
            time (int): The current time.
        """
        expiry_time = time + self.time_lim
        self.token_map[token] = expiry_time
        # Push to heap to allow O(log n) insertion and O(1) access to earliest expiry
        heapq.heappush(self.expiry_heap, (expiry_time, token))

    def validate(self, token: str, time: int) -> bool:
        """
        Validates if a token is active and not expired.

        Args:
            token (str): The token to validate.
            time (int): The current time.

        Returns:
            bool: True if the token is valid, False otherwise.
        """
        # First, clean up any tokens that have expired by the current time
        self._cleanup(time)

        # Check if token exists in the map and its expiry is strictly greater than current time
        # Note: _cleanup handles the removal of expired tokens from the map
        return token in self.token_map

    def revoke(self, token: str, time: int) -> None:
        """
        Revokes a token, making it invalid.

        Args:
            token (str): The token to revoke.
            time (int): The current time.
        """
        # Remove from map to invalidate immediately
        if token in self.token_map:
            del self.token_map[token]
        
        # We don't remove from heap immediately to keep complexity O(1) for revoke.
        # The _cleanup method will handle the stale heap entries lazily.
        self._cleanup(time)

    def _cleanup(self, current_time: int) -> None:
        """
        Removes expired tokens from the internal data structures.

        Args:
            current_time (int): The current time.
        """
        # Remove tokens from the heap if their expiry time is <= current_time
        while self.expiry_heap and self.expiry_heap[0][0] <= current_time:
            expiry, token = heapq.heappop(self.expiry_heap)
            
            # Check if the token in the heap is still the current valid version
            # This handles cases where a token was revoked or re-generated
            if token in self.token_map and self.token_map[token] == expiry:
                del self.token_map[token]
            elif token in self.token_map and self.token_map[token] < expiry:
                # This case handles if a token was updated with a new expiry
                # but the old expiry is still in the heap
                pass 
            # If token is not in map, it was already revoked or cleaned up

def solve():
    """
    Example usage of the AuthenticationManager.
    """
    auth = AuthenticationManager(5)
    auth.generate("aaa", 2)
    print(auth.validate("aaa", 4))   # Expected: True
    auth.generate("bbb", 4)
    print(auth.validate("aaa", 7))   # Expected: False (2+5=7, expires at 7, invalid at 7)
    print(auth.validate("bbb", 7))   # Expected: True (4+5=9, valid at 7)
    auth.revoke("bbb", 7)
    print(auth.validate("bbb", 7))   # Expected: False
