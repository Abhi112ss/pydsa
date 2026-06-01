METADATA = {
    "id": 1683,
    "name": "Invalid Tweets",
    "slug": "invalid_tweets",
    "category": "Database",
    "aliases": [],
    "tags": ["string_length"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Return the IDs of tweets whose content exceeds 140 characters.",
}


def solve(tweets: list[dict]) -> list[int]:
    """Identify tweets with content longer than 140 characters.

    Args:
        tweets: A list of dictionaries, each representing a tweet with keys
            "tweet_id" (int) and "content" (str).

    Returns:
        A list of tweet IDs (int) whose content length is greater than 140.

    Examples:
        >>> tweets = [
        ...     {"tweet_id": 1, "content": "short"},
        ...     {"tweet_id": 2, "content": "a" * 150},
        ... ]
        >>> solve(tweets)
        [2]
    """
    invalid_ids: list[int] = []
    for tweet in tweets:
        # If the tweet's content length exceeds 140 characters, record its ID.
        if len(tweet["content"]) > 140:
            invalid_ids.append(tweet["tweet_id"])
    return invalid_ids