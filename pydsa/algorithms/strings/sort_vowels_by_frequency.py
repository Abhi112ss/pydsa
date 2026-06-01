METADATA = {
    "id": 3913,
    "name": "Sort Vowels by Frequency",
    "slug": "sort-vowels-by-frequency",
    "category": "String",
    "aliases": [],
    "tags": ["hash_map", "sorting", "strings"],
    "difficulty": "medium",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(n)",
    "description": "Sort the vowels in a string based on their frequency in descending order, using their ASCII value as a tie-breaker.",
}

def solve(s: str) -> str:
    """
    Sorts the vowels in the given string based on their frequency in descending order.
    If two vowels have the same frequency, the one with the higher ASCII value comes first.

    Args:
        s: The input string containing vowels and consonants.

    Returns:
        A new string where the vowels are rearranged according to the frequency 
        and ASCII rules, while consonants remain in their original positions.

    Examples:
        >>> solve("leetcode")
        'eeoecdt' (Note: This is a conceptual example; actual output depends on vowel counts)
        >>> solve("aeiou")
        'uoiea'
    """
    vowels_set = set("aeiouAEIOU")
    vowel_counts = {}

    # Step 1: Count the frequency of each vowel present in the string
    for char in s:
        if char in vowels_set:
            vowel_counts[char] = vowel_counts.get(char, 0) + 1

    # Step 2: Collect all vowels present in the string into a list
    # We need to know which vowels were actually in the string to re-insert them
    vowels_in_string = []
    for char in s:
        if char in vowels_set:
            vowels_in_string.append(char)

    # Step 3: Sort the collected vowels
    # Primary key: frequency (descending -> -vowel_counts[x])
    # Secondary key: ASCII value (descending -> -ord(x))
    vowels_in_string.sort(key=lambda x: (-vowel_counts[x], -ord(x)))

    # Step 4: Reconstruct the string
    # Iterate through the original string; if it's a vowel, take the next sorted vowel
    result = []
    vowel_idx = 0
    for char in s:
        if char in vowels_set:
            result.append(vowels_in_string[vowel_idx])
            vowel_idx += 1
        else:
            result.append(char)

    return "".join(result)
