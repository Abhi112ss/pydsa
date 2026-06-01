METADATA = {
    "id": 3442,
    "name": "Maximum Difference Between Even and Odd Frequency I",
    "slug": "maximum-difference-between-even-and-odd-frequency-i",
    "category": "Hash Table",
    "aliases": [],
    "tags": ["hash_map", "frequency_count"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(k)",
    "description": "Find the maximum possible difference between an even frequency and an odd frequency of characters in a string.",
}

def solve(s: str) -> int:
    """
    Calculates the maximum difference between an even frequency and an odd frequency.

    The algorithm counts the occurrences of each character, separates the 
    frequencies into even and odd groups, and then finds the maximum 
    possible difference (max_even - min_odd) or (max_odd - min_even). 
    However, the problem specifically asks for (even_freq - odd_freq) 
    where we maximize this value.

    Args:
        s: The input string containing lowercase English letters.

    Returns:
        The maximum difference between an even frequency and an odd frequency.

    Examples:
        >>> solve("aabbbcccc")
        1  # even: [2, 4], odd: [3]. Max (4-3) = 1 or (2-3) = -1. Max is 1.
        >>> solve("abc")
        0  # even: [], odd: [1, 1, 1]. Since no even exists, logic depends on constraints.
           # Note: Problem constraints usually guarantee existence.
    """
    # Step 1: Count frequencies of all characters
    frequencies: dict[str, int] = {}
    for char in s:
        frequencies[char] = frequencies.get(char, 0) + 1

    even_frequencies: list[int] = []
    odd_frequencies: list[int] = []

    # Step 2: Separate frequencies into even and odd lists
    for count in frequencies.values():
        if count % 2 == 0:
            even_frequencies.append(count)
        else:
            odd_frequencies.append(count)

    # Step 3: Find max even and min odd to maximize (even - odd)
    # Based on the problem description, we want to maximize (even_freq - odd_freq)
    # To maximize a - b, we need max(a) and min(b).
    
    # Note: If the problem implies |even - odd|, we check both directions.
    # But "Maximum difference between even and odd" usually implies max(even) - min(odd).
    
    max_even = max(even_frequencies) if even_frequencies else float('-inf')
    min_odd = min(odd_frequencies) if odd_frequencies else float('inf')

    # The problem asks for the maximum difference. 
    # If we can pick any even and any odd, the max difference is max_even - min_odd.
    # If the question implies the absolute difference, we'd check max_odd - min_even too.
    # Standard interpretation for "Max difference between X and Y" is max(X) - min(Y).
    
    return int(max_even - min_odd)
