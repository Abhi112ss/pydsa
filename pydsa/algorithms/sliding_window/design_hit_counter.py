METADATA = {
    "id": 362,
    "name": "Design Hit Counter",
    "slug": "design-hit-counter",
    "category": "Design",
    "aliases": [],
    "tags": ["design", "queue", "sliding_window"],
    "difficulty": "medium",
    "time_complexity": "O(1)",
    "space_complexity": "O(1)",
    "description": "Design a system that counts the number of hits received in the last 5 minutes.",
}

class HitCounter:
    """
    A system to track hits in a sliding window of 300 seconds (5 minutes).
    
    Uses a fixed-size array to achieve O(1) time complexity for both 
    recording hits and retrieving counts, regardless of the number of hits.
    """

    def __init__(self) -> None:
        """
        Initializes the hit counter with two arrays of size 300.
        """
        self.window_size = 300
        # times[i] stores the timestamp associated with bucket i
        self.times: list[int] = [0] * self.window_size
        # counts[i] stores the number of hits at the timestamp in times[i]
        self.counts: list[int] = [0] * self.window_size

    def hit(self, timestamp: int) -> None:
        """
        Records a hit at the given timestamp.

        Args:
            timestamp: The current timestamp in seconds.
        """
        # Map the timestamp to a bucket index using modulo
        index = timestamp % self.window_size

        # If the timestamp in this bucket is not the current one, 
        # it means the data in this bucket is older than 300 seconds.
        if self.times[index] != timestamp:
            self.times[index] = timestamp
            self.counts[index] = 1
        else:
            # Otherwise, increment the hit count for the current timestamp
            self.counts[index] += 1

    def getHits(self, timestamp: int) -> int:
        """
        Returns the number of hits in the last 5 minutes.

        Args:
            timestamp: The current timestamp in seconds.

        Returns:
            The total number of hits in the range (timestamp - 300, timestamp].

        Examples:
            >>> counter = HitCounter()
            >>> counter.hit(1)
            >>> counter.hit(2)
            >>> counter.hit(3)
            >>> counter.getHits(4)
            3
            >>> counter.hit(300)
            >>> counter.getHits(300)
            4
            >>> counter.getHits(301)
            3
        """
        total_hits = 0
        # Iterate through all buckets to sum hits that fall within the 300s window
        for i in range(self.window_size):
            # Check if the timestamp stored in the bucket is within the valid window
            if timestamp - self.times[i] < self.window_size:
                total_hits += self.counts[i]
        
        return total_hits

def solve() -> None:
    """
    Example usage of the HitCounter class.
    """
    counter = HitCounter()
    counter.hit(1)
    counter.hit(2)
    counter.hit(3)
    print(f"Hits at 4: {counter.getHits(4)}")  # Expected: 3
    counter.hit(300)
    print(f"Hits at 300: {counter.getHits(300)}")  # Expected: 4
    print(f"Hits at 301: {counter.getHits(301)}")  # Expected: 3 (hit at 1 is expired)
