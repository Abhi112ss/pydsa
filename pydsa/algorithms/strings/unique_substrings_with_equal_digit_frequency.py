METADATA = {
    "id": 2168,
    "name": "Unique Substrings With Equal Digit Frequency",
    "slug": "unique-substrings-with-equal-digit-frequency",
    "category": "String",
    "aliases": [],
    "tags": ["string", "hash_map", "sliding_window"],
    "difficulty": "medium",
    "time_complexity": "O(n^2)",
    "space_complexity": "O(n)",
    "description": "Find the number of unique substrings where all present digits appear with the same frequency.",
}

def solve(s: str) -> int:
    """
    Calculates the number of unique substrings where all digits present in the 
    substring appear with the same frequency.

    Args:
        s: A string consisting of digits.

    Returns:
        The count of unique substrings satisfying the condition.

    Examples:
        >>> solve("122")
        4
        # Substrings: "1", "2", "22", "122" is invalid because '1' freq=1, '2' freq=2.
        # Wait, "122" is invalid. Substrings: "1", "2", "2", "12", "22", "122".
        # Valid: "1" (1), "2" (1), "2" (1), "22" (2), "12" (1,1).
        # Unique valid: "1", "2", "22", "12". Total 4.
    """
    n = len(s)
    unique_valid_substrings = set()

    # Iterate through every possible starting position of a substring
    for start in range(n):
        # Frequency map for digits in the current substring starting at 'start'
        digit_counts = {}
        
        # Expand the substring by moving the end pointer
        for end in range(start, n):
            digit = s[end]
            digit_counts[digit] = digit_counts.get(digit, 0) + 1
            
            # To check if all present digits have the same frequency,
            # we extract the values from the frequency map.
            # Since the number of unique digits is at most 10, this is O(1).
            counts = list(digit_counts.values())
            
            # Check if all values in the counts list are identical
            # We use the first count as a reference
            first_count = counts[0]
            is_equal = True
            for i in range(1, len(counts)):
                if counts[i] != first_count:
                    is_equal = False
                    break
            
            if is_equal:
                # Add the substring to the set to ensure uniqueness
                unique_valid_substrings.add(s[start : end + 1])
                
    return len(unique_valid_substrings)
