METADATA = {
    "id": 3389,
    "name": "Minimum Operations to Make Character Frequencies Equal",
    "slug": "minimum-operations-to-make-character-frequencies-equal",
    "category": "Greedy",
    "aliases": [],
    "tags": ["greedy", "hash_map", "strings"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Find the minimum number of operations to make all character frequencies in a string equal.",
}

def solve(s: str) -> int:
    """
    Calculates the minimum number of operations to make all character frequencies equal.
    An operation consists of changing one character to another.

    Args:
        s: The input string consisting of lowercase English letters.

    Returns:
        The minimum number of operations required.

    Examples:
        >>> solve("aabbcc")
        0
        >>> solve("aabbccc")
        1
        >>> solve("abcde")
        0
    """
    # Count the frequency of each character present in the string
    char_counts = {}
    for char in s:
        char_counts[char] = char_counts.get(char, 0) + 1
    
    # Extract the frequencies into a list
    frequencies = list(char_counts.values())
    n = len(s)
    num_unique_chars = len(frequencies)
    
    # The target frequency 'f' must be a divisor of the total length 'n'
    # because if all k characters have frequency f, then k * f = n.
    # However, the problem implies we can change characters, meaning we can 
    # change the number of unique characters present.
    # Actually, the problem asks to make all *existing* character frequencies equal? 
    # No, it asks to make the frequencies of all characters in the string equal.
    # This means if we decide on a target frequency 'f', the number of characters 
    # we will have is k = n // f. 
    # Note: n must be divisible by f for this to be possible without changing string length.
    
    min_operations = n  # Initialize with maximum possible operations
    
    # Iterate through all possible target frequencies 'f'
    # 'f' must be a divisor of n.
    for f in range(1, n + 1):
        if n % f == 0:
            k = n // f  # Number of characters that will have frequency 'f'
            
            # To minimize operations, we want to keep as many characters as possible.
            # We can keep at most 'k' distinct characters, and for each, 
            # we can keep at most 'f' occurrences.
            # However, we can only keep characters that already exist.
            # If we pick a character with count 'c', we can keep min(c, f) instances.
            # But wait, if we pick a character to be one of the 'k' characters, 
            # we can keep at most 'f' of its occurrences.
            # If we have more than 'k' characters, we must discard the extras.
            
            # Correct Greedy Strategy for a fixed 'f':
            # 1. We will have exactly k characters, each appearing f times.
            # 2. We want to pick k characters from the existing ones to maximize 
            #    the number of characters we "keep".
            # 3. For any character with frequency 'c', we can keep min(c, f) instances.
            # 4. We pick the top k characters that provide the maximum min(c, f).
            
            # Sort frequencies descending to pick the best characters to keep
            sorted_freqs = sorted(frequencies, reverse=True)
            
            kept_chars = 0
            # We can only pick up to k characters
            for i in range(min(k, len(sorted_freqs))):
                kept_chars += min(sorted_freqs[i], f)
            
            # Operations = Total length - characters we managed to keep
            current_ops = n - kept_chars
            if current_ops < min_operations:
                min_operations = current_ops
                
    return min_operations
