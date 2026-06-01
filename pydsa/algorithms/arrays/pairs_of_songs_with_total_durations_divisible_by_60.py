METADATA = {
    "id": 1010,
    "name": "Pairs of Songs With Total Durations Divisible by 60",
    "slug": "pairs-of-songs-with-total-durations-divisible-by-60",
    "category": "Hash Table",
    "aliases": [],
    "tags": ["hash_map", "math", "counting"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Count the number of pairs of songs whose total duration is a multiple of 60.",
}

def solve(duration: list[int]) -> int:
    """
    Counts the number of pairs of songs whose total duration is divisible by 60.

    Args:
        duration: A list of integers representing the duration of each song in seconds.

    Returns:
        The total number of pairs (i, j) such that i < j and (duration[i] + duration[j]) % 60 == 0.

    Examples:
        >>> solve([30, 20, 150, 100, 40])
        2
        >>> solve([60, 60, 60])
        3
    """
    # Since we only care about divisibility by 60, we only need to track 
    # the frequency of remainders when divided by 60.
    # There are only 60 possible remainders (0 to 59).
    remainder_counts = [0] * 60
    total_pairs = 0

    for time in duration:
        remainder = time % 60
        
        # To make the sum divisible by 60, the complement remainder needed is:
        # (60 - remainder) % 60. 
        # For example: if remainder is 20, we need 40. If remainder is 0, we need 0.
        target_remainder = (60 - remainder) % 60
        
        # If we have seen the target_remainder before, every occurrence 
        # forms a valid pair with the current song.
        total_pairs += remainder_counts[target_remainder]
        
        # Update the frequency of the current remainder for future songs.
        remainder_counts[remainder] += 1

    return total_pairs
