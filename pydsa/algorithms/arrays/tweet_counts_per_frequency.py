METADATA = {
    "id": 1348,
    "name": "Tweet Counts Per Frequency",
    "slug": "tweet-counts-per-frequency",
    "category": "Design",
    "aliases": [],
    "tags": ["hash_map", "sorting", "design", "binary_search"],
    "difficulty": "medium",
    "time_complexity": "O(log N) per count call",
    "space_complexity": "O(N) where N is total tweets",
    "description": "Design a system that tracks tweet timestamps and returns the number of tweets within specific time intervals.",
}

import bisect

class TweetScheduler:
    """
    A system to track tweet timestamps and query counts within time intervals.
    """

    def __init__(self) -> None:
        """
        Initializes the scheduler with an empty mapping of user to timestamps.
        """
        # Maps user_id (int) to a sorted list of timestamps (int)
        self.user_tweets: dict[int, list[int]] = {}

    def post_tweet(self, user_id: int, timestamp: int) -> None:
        """
        Records a tweet for a specific user at a given timestamp.

        Args:
            user_id: The unique identifier for the user.
            timestamp: The time at which the tweet was posted.
        """
        if user_id not in self.user_tweets:
            self.user_tweets[user_id] = []
        
        # Since timestamps are guaranteed to be increasing in the problem context,
        # we can simply append. If not, we would use bisect.insort.
        self.user_tweets[user_id].append(timestamp)

    def tweet_count(self, user_id: int, start_time: int, end_time: int, period: int) -> list[int]:
        """
        Returns the number of tweets for a user in consecutive time intervals.

        Args:
            user_id: The unique identifier for the user.
            start_time: The beginning of the first interval.
            end_time: The end of the last interval.
            period: The length of each interval.

        Returns:
            A list of integers representing the tweet counts for each interval.

        Examples:
            >>> scheduler = TweetScheduler()
            >>> scheduler.post_tweet(1, 5)
            >>> scheduler.post_tweet(1, 10)
            >>> scheduler.tweet_count(1, 5, 15, 5)
            [1, 1]
        """
        if user_id not in self.user_tweets:
            # Calculate how many intervals exist even if no tweets exist
            num_intervals = (end_time - start_time) // period + 1
            return [0] * num_intervals

        timestamps = self.user_tweets[user_id]
        results = []

        # Iterate through each period starting from start_time
        for current_start in range(start_time, end_time + 1, period):
            current_end = current_start + period - 1
            
            # Use binary search (bisect) to find the range of timestamps 
            # falling within [current_start, current_end]
            # bisect_left finds the first index >= current_start
            # bisect_right finds the first index > current_end
            left_idx = bisect.bisect_left(timestamps, current_start)
            right_idx = bisect.bisect_right(timestamps, current_end)
            
            # The number of elements in the range is the difference between indices
            results.append(right_idx - left_idx)

        return results

def solve() -> None:
    """
    Example usage of the TweetScheduler class.
    """
    scheduler = TweetScheduler()
    scheduler.post_tweet(1, 5)
    scheduler.post_tweet(1, 10)
    scheduler.post_tweet(1, 15)
    
    # Interval 1: [5, 9] -> [5] -> count 1
    # Interval 2: [10, 14] -> [10] -> count 1
    # Interval 3: [15, 19] -> [15] -> count 1
    print(scheduler.tweet_count(1, 5, 15, 5))
