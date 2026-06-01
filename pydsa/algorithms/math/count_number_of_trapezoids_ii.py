METADATA = {
    "id": 3625,
    "name": "Count Number of Trapezoids II",
    "slug": "count-number-of-trapezoids-ii",
    "category": "math",
    "aliases": [],
    "tags": ["math", "combinatorics", "prefix_sum"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Count the number of trapezoids that can be formed given a set of parallel line segments of varying lengths.",
}

def solve(heights: list[int]) -> int:
    """
    Counts the number of trapezoids that can be formed using segments of given lengths.
    A trapezoid is defined by two parallel bases of different lengths and a height.
    In this specific problem context, we assume we are choosing two segments from 
    the provided list to act as bases.
    
    Note: The problem definition for 'Trapezoids II' typically implies we need to 
    count pairs (a, b) such that a != b from the given list of lengths.
    
    Args:
        heights: A list of integers representing the lengths of parallel segments.

    Returns:
        The total number of unique pairs of segments that can form a trapezoid.

    Examples:
        >>> solve([1, 2, 3])
        3
        >>> solve([2, 2, 2])
        0  # If bases must be of different lengths
    """
    MOD = 10**9 + 7
    n = len(heights)
    if n < 2:
        return 0

    # To form a trapezoid, we need two parallel bases of different lengths.
    # If the problem allows same-length bases (parallelograms), the answer is nC2.
    # However, standard trapezoid definitions in these competitive problems 
    # often require a != b.
    
    # Count frequencies of each length
    counts = {}
    for length in heights:
        counts[length] = counts.get(length, 0) + 1
    
    # Total possible pairs is n * (n - 1) / 2
    total_pairs = (n * (n - 1)) // 2
    
    # Subtract pairs where lengths are identical (these form parallelograms, not trapezoids)
    identical_pairs = 0
    for length in counts:
        freq = counts[length]
        if freq >= 2:
            identical_pairs += (freq * (freq - 1)) // 2
            
    # The number of trapezoids is total pairs minus pairs with equal lengths
    result = (total_pairs - identical_pairs) % MOD
    
    return result
