METADATA = {
    "id": 2785,
    "name": "Sort Vowels in a String",
    "slug": "sort-vowels-in-a-string",
    "category": "String",
    "aliases": [],
    "tags": ["string", "sorting"],
    "difficulty": "medium",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(n)",
    "description": "Sort all vowels in a string in ascending order based on their ASCII values while keeping consonants in their original positions.",
}

def solve(s: str) -> str:
    """
    Sorts the vowels in a string in ascending order of their ASCII values.

    Args:
        s: The input string containing lowercase and uppercase English letters.

    Returns:
        A new string where the vowels are sorted and consonants remain in place.

    Examples:
        >>> solve("lEetcOde")
        'lEetCode'
        >>> solve("lEetcOde") # Note: 'E' (69) < 'O' (79) < 'e' (101)
        'lEetCode'
        >>> solve("lEetcOde") # Corrected logic: E, O, e -> E, O, e (already sorted)
        >>> solve("leetcode")
        'aeeecodt' # Wait, example: 'leetcode' -> vowels: e, e, o, e -> sorted: e, e, e, o -> 'leeeocde'
    """
    vowels_set = set("aeiouAEIOU")
    
    # Step 1: Extract all vowels present in the string
    extracted_vowels = [char for char in s if char in vowels_set]
    
    # Step 2: Sort the extracted vowels based on ASCII values
    extracted_vowels.sort()
    
    # Step 3: Reconstruct the string
    # We iterate through the original string; if we hit a vowel, we pop from our sorted list
    result_chars = []
    vowel_index = 0
    for char in s:
        if char in vowels_set:
            result_chars.append(extracted_vowels[vowel_index])
            vowel_index += 1
        else:
            result_chars.append(char)
            
    return "".join(result_chars)
