METADATA = {
    "id": 3087,
    "name": "Find Trending Hashtags",
    "slug": "find-trending-hashtags",
    "category": "Hash Table",
    "aliases": [],
    "tags": ["strings", "hash_map", "sorting"],
    "difficulty": "medium",
    "time_complexity": "O(N log N)",
    "space_complexity": "O(N)",
    "description": "Find the top K most frequent hashtags, sorted by frequency descending and lexicographically ascending.",
}

def solve(hashtags: list[str], k: int) -> list[str]:
    """
    Finds the top k most frequent hashtags from a given list.
    
    The results are ordered primarily by frequency in descending order, 
    and secondarily by the hashtag string in ascending lexicographical order 
    in case of ties in frequency.

    Args:
        hashtags: A list of strings representing the hashtags.
        k: The number of top trending hashtags to return.

    Returns:
        A list of the top k trending hashtags.

    Examples:
        >>> solve(["#python", "#coding", "#python", "#algo", "#coding"], 2)
        ['#coding', '#python']
        >>> solve(["#a", "#b", "#a", "#c", "#b"], 3)
        ['#a', '#b', '#c']
    """
    if not hashtags or k <= 0:
        return []

    # Step 1: Count the frequency of each hashtag using a hash map
    frequency_map: dict[str, int] = {}
    for tag in hashtags:
        frequency_map[tag] = frequency_map.get(tag, 0) + 1

    # Step 2: Convert the map to a list of tuples (hashtag, frequency)
    # We need to sort by frequency (descending) and then by hashtag (ascending)
    # To achieve this in one sort, we can use a custom key.
    # Python's sort is stable, but a single sort with a tuple key is more efficient.
    unique_tags = list(frequency_map.keys())

    # Sorting logic:
    # -x[1] makes the frequency descending
    # x[0] makes the string ascending (lexicographical)
    unique_tags.sort(key=lambda tag: (-frequency_map[tag], tag))

    # Step 3: Return the top k elements
    return unique_tags[:k]
