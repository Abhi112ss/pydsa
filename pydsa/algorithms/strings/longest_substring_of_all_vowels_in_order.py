METADATA = {
    "id": 1839,
    "name": "Longest Substring Of All Vowels in Order",
    "slug": "longest-substring-of-all-vowels-in-order",
    "category": "String",
    "aliases": [],
    "tags": ["sliding_window", "strings"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Find the length of the longest substring that contains all five vowels in alphabetical order.",
}

def solve(s: str) -> int:
    """
    Finds the length of the longest substring containing all vowels 'a', 'e', 'i', 'o', 'u' 
    in alphabetical order.

    Args:
        s: The input string containing lowercase English letters.

    Returns:
        The length of the longest valid substring. Returns 0 if no such substring exists.

    Examples:
        >>> solve("aeiouu")
        6
        >>> solve("aeiauo")
        0
        >>> solve("aeiouuauioe")
        6
    """
    vowels = "aeiou"
    vowel_count = 0
    max_length = 0
    current_length = 0
    vowel_idx = 0

    for char in s:
        # Check if the current character is the next expected vowel in the sequence
        if vowel_idx < 5 and char == vowels[vowel_idx]:
            vowel_count += 1
            vowel_idx += 1
            current_length += 1
        # Check if the current character is the same as the current vowel (allowing repeats)
        elif vowel_idx > 0 and char == vowels[vowel_idx - 1]:
            current_length += 1
        else:
            # Reset if we encounter a non-vowel or a vowel out of order
            vowel_count = 0
            vowel_idx = 0
            current_length = 0
            
            # Re-evaluate the current character in case it's the start of a new sequence
            if char == vowels[0]:
                vowel_count = 1
                vowel_idx = 1
                current_length = 1

        # If we have successfully found all 5 vowels in order, update max_length
        if vowel_count == 5:
            max_length = max(max_length, current_length)

    return max_length
