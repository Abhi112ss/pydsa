METADATA = {
    "id": 911,
    "name": "Online Election",
    "slug": "online-election",
    "category": "Design",
    "aliases": [],
    "tags": ["binary_search", "hash_map", "design"],
    "difficulty": "medium",
    "time_complexity": "O(log n) per query",
    "space_complexity": "O(n)",
    "description": "Design a system that tracks votes in real-time and returns the winner at a specific timestamp.",
}

class OnlineElection:
    def __init__(self, votes: list[int]):
        """
        Initializes the election system with a sequence of votes.
        
        Args:
            votes: A list of integers representing the candidate ID of each vote.
        """
        # timestamps stores the time at which a change in winner occurred
        # winners stores the candidate ID who was leading at that timestamp
        self.timestamps: list[int] = []
        self.winners: list[int] = []
        
        if not votes:
            return

        # vote_counts tracks the current tally of votes for each candidate
        vote_counts: dict[int, int] = {}
        current_leader: int = -1
        max_votes: int = 0

        for timestamp, candidate in enumerate(votes):
            # Update the vote count for the current candidate
            vote_counts[candidate] = vote_counts.get(candidate, 0) + 1
            
            # Check if the current candidate has overtaken the leader
            # Note: In case of a tie, the existing leader remains the leader
            if vote_counts[candidate] > max_votes:
                max_votes = vote_counts[candidate]
                current_leader = candidate
                
                # Only record the timestamp if the leader actually changes
                # This allows us to use binary search on a strictly increasing sequence
                if not self.timestamps or self.timestamps[-1] != timestamp:
                    self.timestamps.append(timestamp)
                    self.winners.append(current_leader)
            elif not self.timestamps:
                # Handle the very first vote case
                self.timestamps.append(timestamp)
                self.winners.append(candidate)
                max_votes = vote_counts[candidate]
                current_leader = candidate

    def query(self, timestamp: int) -> int:
        """
        Returns the winner at the given timestamp.
        
        Args:
            timestamp: The time at which to query the winner.
            
        Returns:
            The candidate ID of the winner at that timestamp.
            
        Examples:
            >>> sol = OnlineElection([3, 7, 7, 3])
            >>> sol.query(2)
            7
            >>> sol.query(3)
            7
        """
        if not self.timestamps:
            return -1

        # Perform binary search to find the largest timestamp <= query timestamp
        # We want the rightmost index in self.timestamps such that self.timestamps[idx] <= timestamp
        left: int = 0
        right: int = len(self.timestamps) - 1
        best_idx: int = 0

        while left <= right:
            mid: int = (left + right) // 2
            if self.timestamps[mid] <= timestamp:
                best_idx = mid
                left = mid + 1
            else:
                right = mid - 1
                
        return self.winners[best_idx]

def solve():
    """
    Example usage of the OnlineElection class.
    """
    # Example 1
    election = OnlineElection([3, 7, 7, 3])
    print(election.query(2))  # Expected: 7
    print(election.query(3))  # Expected: 7
