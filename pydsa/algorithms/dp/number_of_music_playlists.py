METADATA = {
    "id": 920,
    "name": "Number of Music Playlists",
    "slug": "number-of-music-playlists",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dynamic_programming", "math"],
    "difficulty": "hard",
    "time_complexity": "O(L * N)",
    "space_complexity": "O(L * N)",
    "description": "Calculate the number of ways to construct a playlist of length L using exactly N unique songs.",
}

def solve(songs: list[int], n: int, l: int) -> int:
    """
    Calculates the number of ways to create a playlist of length L using exactly N unique songs.

    The problem is solved using dynamic programming where dp[i][j] represents the 
    number of playlists of length i using exactly j unique songs.

    Args:
        songs: A list of song IDs (though the specific IDs don't matter, only the count N).
        n: The number of unique songs that must be included.
        l: The total length of the playlist.

    Returns:
        The number of valid playlists modulo 10^9 + 7.

    Examples:
        >>> solve([1, 2, 3], 3, 3)
        1
        >>> solve([1, 2], 2, 3)
        2
    """
    MOD = 1_000_000_007
    
    # dp[i][j] = number of playlists of length i using exactly j unique songs
    # i ranges from 0 to l, j ranges from 0 to n
    dp = [[0] * (n + 1) for _ in range(l + 1)]
    
    # Base case: A playlist of length 0 uses 0 unique songs in exactly 1 way
    dp[0][0] = 1
    
    for i in range(1, l + 1):
        for j in range(1, n + 1):
            # Case 1: The i-th song in the playlist is a new song.
            # We must have had j-1 unique songs in the previous i-1 positions.
            # There are (n - (j - 1)) choices for the new song.
            new_song_ways = dp[i - 1][j - 1] * (n - (j - 1))
            
            # Case 2: The i-th song in the playlist is a song already used.
            # We must have already had j unique songs in the previous i-1 positions.
            # There are j choices for which song to repeat.
            old_song_ways = dp[i - 1][j] * j
            
            # Sum the ways and apply modulo
            dp[i][j] = (new_song_ways + old_song_ways) % MOD
            
    return dp[l][n]
