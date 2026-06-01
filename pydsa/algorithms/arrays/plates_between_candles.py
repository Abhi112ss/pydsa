METADATA = {
    "id": 2055,
    "name": "Plates Between Candles",
    "slug": "plates-between-candles",
    "category": "Arrays",
    "aliases": [],
    "tags": ["arrays", "prefix_sum"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Count the number of plates between any two candles for each query using precomputed prefix sums and nearest candle positions.",
}

def solve(s: str, queries: list[list[int]]) -> list[int]:
    """
    Calculates the number of plates between candles for each query.

    Args:
        s: A string consisting of '*' (plates) and '|' (candles).
        queries: A list of queries where each query is [left, right] indices.

    Returns:
        A list of integers representing the number of plates between candles for each query.

    Examples:
        >>> solve("***|**|***|", [[1, 3], [5, 9]])
        [0, 2]
    """
    n = len(s)
    
    # prefix_plates[i] stores the total number of plates from index 0 to i-1
    prefix_plates = [0] * (n + 1)
    for i in range(n):
        prefix_plates[i + 1] = prefix_plates[i] + (1 if s[i] == '*' else 0)
        
    # left_candle[i] stores the index of the nearest candle to the left of or at index i
    left_candle = [-1] * n
    last_candle_idx = -1
    for i in range(n):
        if s[i] == '|':
            last_candle_idx = i
        left_candle[i] = last_candle_idx
        
    # right_candle[i] stores the index of the nearest candle to the right of or at index i
    right_candle = [-1] * n
    last_candle_idx = -1
    for i in range(n - 1, -1, -1):
        if s[i] == '|':
            last_candle_idx = i
        right_candle[i] = last_candle_idx
        
    results = []
    for left, right in queries:
        # Find the first candle within the range [left, right] from the left side
        first_candle = right_candle[left]
        # Find the first candle within the range [left, right] from the right side
        last_candle = left_candle[right]
        
        # If both candles exist and the first candle is to the left of the last candle
        if first_candle != -1 and last_candle != -1 and first_candle < last_candle:
            # The number of plates is the difference in prefix sums between these two candles
            results.append(prefix_plates[last_candle] - prefix_plates[first_candle])
        else:
            results.append(0)
            
    return results
