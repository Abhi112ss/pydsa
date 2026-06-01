METADATA = {
    "id": 2669,
    "name": "Count Artist Occurrences On Spotify Ranking List",
    "slug": "count-artist-occurrences-on-spotify-ranking-list",
    "category": "Hash Table",
    "aliases": [],
    "tags": ["hash_map", "array", "counting"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Count how many times each artist appears in a given list of songs.",
}

def solve(songs: list[list[str]]) -> dict[str, int]:
    """
    Counts the occurrences of each artist in a list of songs.

    Args:
        songs: A list of lists, where each inner list contains [song_name, artist_name].

    Returns:
        A dictionary where keys are artist names and values are their occurrence counts.

    Examples:
        >>> solve([["Song A", "Artist 1"], ["Song B", "Artist 2"], ["Song C", "Artist 1"]])
        {'Artist 1': 2, 'Artist 2': 1}
        >>> solve([["Song X", "Artist Z"]])
        {'Artist Z': 1}
    """
    artist_counts: dict[str, int] = {}

    for song_info in songs:
        # The problem structure implies song_info[1] is the artist name
        artist_name = song_info[1]
        
        # Increment the count for the artist in the frequency map
        if artist_name in artist_counts:
            artist_counts[artist_name] += 1
        else:
            artist_counts[artist_name] = 1

    return artist_counts
