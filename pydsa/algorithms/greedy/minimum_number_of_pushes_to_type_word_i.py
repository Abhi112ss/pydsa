METADATA = {
    "id": 3014,
    "name": "Minimum Number of Pushes to Type Word I",
    "slug": "minimum-number-of-pushes-to-type-word-i",
    "category": "Greedy",
    "aliases": [],
    "tags": ["greedy", "sorting", "string"],
    "difficulty": "easy",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(1)",
    "description": "Calculate the minimum number of key presses to type a word given a fixed keypad layout.",
}

from collections import Counter

def solve(word: str) -> int:
    """
    Calculates the minimum number of pushes required to type a given word.
    
    The strategy is to assign the most frequent characters in the word to the 
    keys that require the fewest number of presses (1 press, then 2, then 3).

    Args:
        word: The input string consisting of lowercase English letters.

    Returns:
        The minimum total number of key presses.

    Examples:
        >>> solve("akkb")
        6
        >>> solve("aaaaaaaabbbbbbbbcccc")
        13
    """
    # Count the frequency of each character in the word
    frequencies = Counter(word)
    
    # Sort frequencies in descending order to apply greedy approach
    # We want the most frequent characters to have the smallest number of pushes
    sorted_frequencies = sorted(frequencies.values(), reverse=True)
    
    total_pushes = 0
    current_key_index = 0
    
    # The keypad layout follows a pattern of 1, 2, 3, 4, 5, 6, 7, 8, 9, 10...
    # However, the keypad is structured as:
    # 1 press: 2, 3, 4, 5, 6, 7, 8, 9, a, b (10 characters)
    # 2 presses: c, d, e, f, g, h, i, j, k, l (10 characters)
    # 3 presses: m, n, o, p, q, r, s, t, u, v (10 characters)
    # 4 presses: w, x, y, z (4 characters)
    # Since we only care about the number of pushes per character, we can 
    # treat it as a sequence of 10 ones, 10 twos, 10 threes, etc.
    
    for freq in sorted_frequencies:
        # Determine how many pushes this specific character requires
        # (current_key_index // 10) + 1 gives the push count (1 for first 10, 2 for next 10...)
        pushes_per_char = (current_key_index // 10) + 1
        
        total_pushes += freq * pushes_per_char
        current_key_index += 1
        
    return total_pushes
