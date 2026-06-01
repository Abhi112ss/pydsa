METADATA = {
    "id": 345,
    "name": "Reverse Vowels of a String",
    "slug": "reverse_vowels_of_a_string",
    "category": "Two Pointers",
    "aliases": [],
    "tags": ["two_pointer", "string"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Reverse only the vowels in a given string while keeping consonants in their original positions.",
}


def solve(s: str) -> str:
    """Reverse only the vowels in the given string using a two-pointer approach.

    Vowels are 'a', 'e', 'i', 'o', 'u' (both lowercase and uppercase).
    The algorithm scans from both ends simultaneously, swapping vowels
    when both pointers land on one.

    Args:
        s: The input string to process.

    Returns:
        A new string with vowels reversed and consonants unchanged.

    Examples:
        >>> solve("hello")
        'holle'
        >>> solve("leetcode")
        'leotcede'
        >>> solve("aA")
        'Aa'
        >>> solve("xyz")
        'xyz'
    """
    vowels = set("aeiouAEIOU")
    chars = list(s)  # Strings are immutable, so convert to list for in-place swaps
    left = 0
    right = len(chars) - 1

    while left < right:
        # Advance left pointer until it points to a vowel
        while left < right and chars[left] not in vowels:
            left += 1
        # Retreat right pointer until it points to a vowel
        while left < right and chars[right] not in vowels:
            right -= 1
        # Swap the vowels found at both pointers
        if left < right:
            chars[left], chars[right] = chars[right], chars[left]
            left += 1
            right -= 1

    return "".join(chars)