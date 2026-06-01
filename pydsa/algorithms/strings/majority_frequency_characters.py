METADATA = {
    "id": 3692,
    "name": "Majority Frequency Characters",
    "slug": "majority_frequency_characters",
    "category": "String",
    "aliases": [],
    "tags": ["hash_map", "strings"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Find all characters in a string that appear with a frequency greater than a given threshold.",
}

def solve(s: str, threshold: int) -> list[str]:
    """
    Finds all characters in the string 's' that appear more than 'threshold' times.

    Args:
        s: The input string containing lowercase English letters.
        threshold: The frequency threshold that a character must exceed.

    Returns:
        A list of characters that appear more than 'threshold' times, 
        sorted in alphabetical order.

    Examples:
        >>> solve("aabbbc", 1)
        ['a', 'b']
        >>> solve("abcde", 0)
        ['a', 'b', 'c', 'd', 'e']
        >>> solve("aaaaa", 5)
        []
    """
    # Use a fixed-size array for O(1) space (26 lowercase English letters)
    counts = [0] * 26
    
    # Count occurrences of each character
    for char in s:
        # Map 'a'-'z' to indices 0-25
        index = ord(char) - ord('a')
        counts[index] += 1
        
    result = []
    
    # Iterate through the counts to find characters exceeding the threshold
    for i in range(26):
        if counts[i] > threshold:
            # Convert index back to character
            result.append(chr(ord('a') + i))
            
    return result
