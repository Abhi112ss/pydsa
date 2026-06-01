METADATA = {
    "id": 1244,
    "name": "Design A Leaderboard",
    "slug": "design-a-leaderboard",
    "category": "Design",
    "aliases": [],
    "tags": ["hash_map", "min_heap", "sorting"],
    "difficulty": "medium",
    "time_complexity": "O(N log K) for topK, where N is number of players",
    "space_complexity": "O(N) to store player scores",
    "description": "Design a leaderboard system that allows updating scores and retrieving the top K players.",
}

import heapq

class Leaderboard:
    """
    A leaderboard system that tracks player scores and allows retrieving top K scores.
    """

    def __init__(self) -> None:
        """
        Initializes the leaderboard with an empty player score map.
        """
        # Map to store player_id -> score
        self.scores: dict[int, int] = {}

    def addScore(self, player: int, score: int) -> None:
        """
        Adds a score to the player's current score.

        Args:
            player: The unique ID of the player.
            score: The score to add.
        """
        # Update existing score or initialize new player score
        self.scores[player] = self.scores.get(player, 0) + score

    def top(self, K: int) -> int:
        """
        Returns the sum of the top K players' scores.

        Args:
            K: The number of top players to sum.

        Returns:
            The sum of the scores of the top K players.

        Examples:
            >>> lb = Leaderboard()
            >>> lb.addScore(1, 75)
            >>> lb.addScore(2, 50)
            >>> lb.top(1)
            75
            >>> lb.addScore(2, 40)
            >>> lb.top(2)
            165
        """
        # Use a min-heap to maintain the top K elements efficiently.
        # This ensures O(N log K) time complexity.
        min_heap: list[int] = []
        
        for score in self.scores.values():
            heapq.heappush(min_heap, score)
            # If heap size exceeds K, remove the smallest element
            if len(min_heap) > K:
                heapq.heappop(min_heap)
        
        # The sum of elements in the heap represents the top K scores
        return sum(min_heap)

def solve():
    """
    Example usage of the Leaderboard class.
    """
    leaderboard = Leaderboard()
    leaderboard.addScore(1, 75)
    leaderboard.addScore(2, 50)
    print(leaderboard.top(1))  # Expected: 75
    leaderboard.addScore(2, 40)
    print(leaderboard.top(2))  # Expected: 165
