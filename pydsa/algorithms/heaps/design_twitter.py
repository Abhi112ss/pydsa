METADATA = {
    "id": 355,
    "name": "Design Twitter",
    "slug": "design-twitter",
    "category": "Design",
    "aliases": [],
    "tags": ["design", "hash_map", "heap", "queue"],
    "difficulty": "medium",
    "time_complexity": "O(k log n) for getNewsFeed, where k is number of followees",
    "space_complexity": "O(U + T) where U is users and T is total tweets",
    "description": "Design a Twitter-like system to post tweets, follow/unfollow users, and retrieve a news feed of the most recent tweets.",
}

import heapq
from collections import defaultdict, deque

class Twitter:
    """
    A class representing a simplified Twitter system.
    
    Attributes:
        timestamp (int): A global counter to simulate chronological order.
        user_tweets (dict): Maps user_id to a deque of (timestamp, tweet_id) tuples.
        following (dict): Maps user_id to a set of user_ids they follow.
    """

    def __init__(self) -> None:
        self.timestamp: int = 0
        # Stores tweets as: {user_id: deque([(timestamp, tweet_id), ...])}
        self.user_tweets: dict[int, deque] = defaultdict(deque)
        # Stores following as: {user_id: set(followed_user_ids)}
        self.following: dict[int, set[int]] = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        """
        Generates a new tweet by a user.

        Args:
            userId (int): The ID of the user posting the tweet.
            tweetId (int): The ID of the tweet.
        """
        self.timestamp += 1
        # We use a deque to store tweets; newest tweets are appended to the right.
        # To make merging easier, we treat the deque as a list where the end is the most recent.
        self.user_tweets[userId].append((self.timestamp, tweetId))

    def getNewsFeed(self, userId: int) -> list[int]:
        """
        Retrieves the 10 most recent tweet IDs in the user's news feed.
        The news feed contains the user's tweets and tweets from people they follow.

        Args:
            userId (int): The ID of the user requesting the feed.

        Returns:
            list[int]: A list of up to 10 most recent tweet IDs.
        """
        # The user follows themselves implicitly for the feed
        followees = self.following[userId] | {userId}
        
        # Max-heap to merge k sorted lists (one list per followee).
        # Python's heapq is a min-heap, so we use negative timestamps to simulate a max-heap.
        # Heap stores: (-timestamp, tweet_id, user_id, index_in_user_tweets_deque)
        max_heap: list[tuple[int, int, int, int]] = []

        for followee_id in followees:
            tweets = self.user_tweets[followee_id]
            if tweets:
                # Start with the very last (most recent) tweet of each followee
                last_idx = len(tweets) - 1
                ts, t_id = tweets[last_idx]
                heapq.heappush(max_heap, (-ts, t_id, followee_id, last_idx))

        feed: list[int] = []
        while max_heap and len(feed) < 10:
            neg_ts, t_id, followee_id, idx = heapq.heappop(max_heap)
            feed.append(t_id)

            # If this followee has more tweets, push the next most recent one into the heap
            if idx > 0:
                next_idx = idx - 1
                next_ts, next_t_id = self.user_tweets[followee_id][next_idx]
                heapq.heappush(max_heap, (-next_ts, next_t_id, followee_id, next_idx))

        return feed

    def follow(self, followerId: int, followeeId: int) -> None:
        """
        Causes user to follow another user.

        Args:
            followerId (int): The ID of the user following.
            followeeId (int): The ID of the user being followed.
        """
        if followerId != followeeId:
            self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        """
        Causes user to unfollow another user.

        Args:
            followerId (int): The ID of the user unfollowing.
            followeeId (int): The ID of the user being unfollowed.
        """
        if followeeId in self.following[followerId]:
            self.following[followerId].remove(followeeId)

def solve():
    """
    Example usage and test driver.
    """
    twitter = Twitter()
    twitter.postTweet(1, 5)
    twitter.postTweet(2, 6)
    twitter.follow(1, 2)
    print(f"Feed 1: {twitter.getNewsFeed(1)}")  # Expected: [6, 5]
    twitter.unfollow(1, 2)
    print(f"Feed 1 after unfollow: {twitter.getNewsFeed(1)}")  # Expected: [5]
