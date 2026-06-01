METADATA = {
    "id": 151,
    "name": "Reverse Words in a String",
    "slug": "reverse-words-in-a-string",
    "category": "String",
    "aliases": [],
    "tags": ["two_pointers", "string_manipulation"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Given an input string, reverse the order of the words in the string.",
}

def solve(s: str) -> str:
    """
    Reverses the order of words in a given string, handling multiple spaces.

    Args:
        s: The input string containing words separated by one or more spaces.

    Returns:
        A string where the order of words is reversed, with single spaces between words.

    Examples:
        >>> solve("the sky is blue")
        'blue is sky the'
        >>> solve("  hello world  ")
        'world hello'
        >>> solve("a good   example")
        'example good a'
    """
    # Step 1: Split the string into words. 
    # Python's split() without arguments automatically handles multiple spaces 
    # and trims leading/trailing whitespace.
    words = s.split()

    # Step 2: Reverse the list of words in place.
    # This changes the order of the words from [first, ..., last] to [last, ..., first].
    words.reverse()

    # Step 3: Join the reversed list of words with a single space.
    return " ".join(words)
