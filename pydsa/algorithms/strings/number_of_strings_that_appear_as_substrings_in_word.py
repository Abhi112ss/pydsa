METADATA = {
    "id": 1967,
    "name": "Number of Strings That Appear as Substrings in Word",
    "slug": "number-of-strings-that-appear-as-substrings-in-word",
    "category": "String",
    "aliases": [],
    "tags": ["string_matching", "hash_set"],
    "difficulty": "easy",
    "time_complexity": "O(n * m^2)",
    "space_complexity": "O(m^2)",
    "description": "Count how many strings from a given list are present as substrings in a target word.",
}

def solve(word: str, strs: list[str]) -> int:
    """
    Counts the number of strings in the list 'strs' that are substrings of 'word'.

    Args:
        word: The target string to search within.
        strs: A list of strings to check against the target word.

    Returns:
        The count of strings from 'strs' that appear as substrings in 'word'.

    Examples:
        >>> solve("duck", ["u", "ck", "d", "x"])
        3
        >>> solve("leetcode", ["leeto", "code"])
        1
    """
    # Create a set of all possible substrings of 'word' for O(1) average lookup.
    # While O(m^2) space is used, it allows us to check each string in O(length)
    # or simply use the 'in' operator which is highly optimized in Python.
    substrings = set()
    word_length = len(word)
    
    for start_index in range(word_length):
        for end_index in range(start_index + 1, word_length + 1):
            substrings.add(word[start_index:end_index])
            
    count = 0
    # Iterate through each string in the input list and check existence in the set.
    for s in strs:
        if s in substrings:
            count += 1
            
    return count

def solve_optimized(word: str, strs: list[str]) -> int:
    """
    An alternative implementation using Python's optimized 'in' operator.
    This is often faster in practice due to the highly optimized C implementation 
    of string searching (Boyer-Moore/Horspool variant).

    Args:
        word: The target string to search within.
        strs: A list of strings to check against the target word.

    Returns:
        The count of strings from 'strs' that appear as substrings in 'word'.
    """
    count = 0
    for s in strs:
        # The 'in' operator in Python uses a highly optimized string searching algorithm.
        if s in word:
            count += 1
    return count
