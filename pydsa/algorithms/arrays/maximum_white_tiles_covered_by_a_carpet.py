METADATA = {
    "id": 2271,
    "name": "Maximum White Tiles Covered by a Carpet",
    "slug": "maximum-white-tiles-covered-by-a-carpet",
    "category": "Array",
    "aliases": [],
    "tags": ["sliding_window", "prefix_sum"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Find the maximum number of white tiles covered by a carpet of length k placed anywhere on a row of tiles.",
}

def solve(tiles: list[int], carpet_length: int) -> int:
    """
    Calculates the maximum number of white tiles covered by a carpet of a given length.

    The problem is solved using a prefix sum array to allow O(1) range sum queries,
    combined with a sliding window approach to find the optimal placement.

    Args:
        tiles: A list of integers where 0 represents a black tile and 1 represents a white tile.
        carpet_length: The length of the carpet.

    Returns:
        The maximum number of white tiles that can be covered.

    Examples:
        >>> solve([0, 1, 0, 1, 0, 1], 3)
        2
        >>> solve([1, 1, 1, 1, 1, 1], 3)
        3
        >>> solve([0, 0, 0, 0], 3)
        0
    """
    n = len(tiles)
    
    # Create a prefix sum array to store the cumulative count of white tiles.
    # prefix_sums[i] will store the number of white tiles in tiles[0...i-1].
    prefix_sums = [0] * (n + 1)
    for i in range(n):
        prefix_sums[i + 1] = prefix_sums[i] + tiles[i]

    max_white_tiles = 0
    
    # We use a sliding window approach. For each starting position 'left',
    # we find the furthest position 'right' that the carpet can reach.
    right = 0
    for left in range(n):
        # Expand the right boundary of the carpet as far as possible.
        # The carpet covers tiles from index 'left' to 'left + carpet_length - 1'.
        # We cap the right boundary at the end of the tiles array.
        right = min(left + carpet_length, n)
        
        # The number of white tiles in the range [left, right-1] is 
        # calculated in O(1) using the prefix sum array.
        current_white_tiles = prefix_sums[right] - prefix_sums[left]
        
        if current_white_tiles > max_white_tiles:
            max_white_tiles = current_white_tiles
            
        # Optimization: If we have already covered all possible white tiles, we can exit early.
        if max_white_tiles == prefix_sums[n]:
            break

    return max_white_tiles
