METADATA = {
    "id": 3335,
    "name": "Total Characters in String After Transformations I",
    "slug": "total-characters-in-string-after-transformations-i",
    "category": "Math",
    "aliases": [],
    "tags": ["math", "hash_map", "string"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Calculate the total number of characters in a string after applying a specific character transformation rule to each character.",
}

def solve(s: str, transformations: list[dict[str, int]]) -> int:
    """
    Calculates the total number of characters in the string after transformations.
    
    Each character in the string is transformed based on the provided rules.
    The transformation rule for a character 'c' is defined by a dictionary 
    where keys are characters and values are the number of times that character 
    appears after transformation.

    Args:
        s: The initial string.
        transformations: A list of dictionaries where transformations[i] 
            defines the transformation for the character with ASCII value i + 97.
            (i.e., transformations[0] is for 'a', transformations[1] for 'b', etc.)

    Returns:
        The total count of characters after all transformations are applied.

    Examples:
        >>> solve("abc", [{"a": 2, "b": 1}, {"a": 1}, {"b": 3}])
        # 'a' -> 2+1=3, 'b' -> 1, 'c' -> 3. Total: 3+1+3 = 7? 
        # Wait, the rule is: each char in s is replaced by the set of chars in its rule.
        # If s="a", and transformations[0] is {"a": 2, "b": 1}, total is 3.
    """
    # Count the frequency of each character in the original string
    # Since we only deal with lowercase English letters, a fixed size array works
    char_counts = [0] * 26
    for char in s:
        char_counts[ord(char) - ord('a')] += 1

    total_length = 0
    
    # Iterate through each character type present in the original string
    for i in range(26):
        if char_counts[i] > 0:
            # The transformation rule for character (ord('a') + i) 
            # is stored in transformations[i]
            rule = transformations[i]
            
            # Calculate how many characters one instance of this char produces
            chars_produced_per_instance = sum(rule.values())
            
            # Total characters contributed by all instances of this character
            total_length += char_counts[i] * chars_produced_per_instance

    return total_length
