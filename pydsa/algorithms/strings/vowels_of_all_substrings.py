METADATA = {
    "id": 2063,
    "name": "Vowels of All Substrings",
    "slug": "vowels-of-all-substrings",
    "category": "Math",
    "aliases": [],
    "tags": ["math", "strings", "prefix sum"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Calculate the total number of vowels in all possible substrings of a given string.",
}

def solve(word: str) -> int:
    """
    Calculates the total count of vowels across all possible substrings of the input word.

    The algorithm uses a mathematical approach to count the contribution of each vowel.
    For a vowel at index 'i' in a string of length 'n', the number of substrings 
    containing this specific vowel is (i + 1) * (n - i).

    Args:
        word: The input string containing lowercase English letters.

    Returns:
        The total sum of vowels in all substrings.

    Examples:
        >>> solve("ae")
        4
        >>> solve("leetcode")
        112
    """
    n = len(word)
    total_vowels_sum = 0
    vowels = {'a', 'e', 'i', 'o', 'u'}

    for index, char in enumerate(word):
        if char in vowels:
            # A vowel at index 'i' is part of (i + 1) possible starting positions
            # and (n - i) possible ending positions.
            # Total substrings containing this specific vowel = (i + 1) * (n - i)
            num_substrings_containing_vowel = (index + 1) * (n - index)
            total_vowels_sum += num_substrings_containing_vowel

    return total_vowels_sum
