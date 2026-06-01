METADATA = {
    "id": 3016,
    "name": "Minimum Number of Pushes to Type Word II",
    "slug": "minimum-number-of-pushes-to-type-word-ii",
    "category": "Greedy",
    "aliases": [],
    "tags": ["greedy", "sorting", "string"],
    "difficulty": "medium",
    "time_complexity": "O(N log N)",
    "space_complexity": "O(1)",
    "description": "Calculate the minimum number of key presses to type a word given a specific keypad layout.",
}

def solve(word: str) -> int:
    """
    Calculates the minimum number of pushes required to type a given word
    using a keypad where characters are distributed across keys to minimize pushes.

    The strategy is to count the frequency of each character, sort them in 
    descending order, and greedily assign the most frequent characters to 
    the keys that require the fewest pushes (1 push, then 2, then 3, etc.).

    Args:
        word: The input string consisting of lowercase English letters.

    Returns:
        The minimum number of pushes required to type the word.

    Examples:
        >>> solve("akkb")
        6
        >>> solve("aaaa")
        4
    """
    # Count frequency of each character
    char_counts = {}
    for char in word:
        char_counts[char] = char_counts.get(char, 0) + 1

    # Sort frequencies in descending order to apply greedy approach
    frequencies = sorted(char_counts.values(), reverse=True)

    total_pushes = 0
    current_frequency_index = 0
    num_frequencies = len(frequencies)
    
    # The keypad layout follows a pattern:
    # 1st set of 4 keys: 1 push each
    # 2nd set of 4 keys: 2 pushes each
    # 3rd set of 4 keys: 3 pushes each, and so on.
    # However, the problem implies we can choose the layout. 
    # To minimize, we use 4 keys for 1 push, 4 keys for 2 pushes, etc.
    # Wait, the standard layout is 4 keys per 'level' of pushes.
    # Level 1: 4 keys (1 push)
    # Level 2: 4 keys (2 pushes)
    # Level 3: 4 keys (3 pushes)
    # ...
    
    pushes_per_key = 1
    keys_at_current_level = 0
    
    while current_frequency_index < num_frequencies:
        # Assign the current most frequent character to the current push level
        total_pushes += frequencies[current_frequency_index] * pushes_per_key
        current_frequency_index += 1
        keys_at_current_level += 1
        
        # If we have used up 4 keys for the current push level, move to the next level
        if keys_at_current_level == 4:
            pushes_per_key += 1
            keys_at_current_level = 0
            
    return total_pushes
