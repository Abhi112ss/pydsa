METADATA = {
    "id": 966,
    "name": "Vowel Spellchecker",
    "slug": "vowel-spellchecker",
    "category": "Hash Table",
    "aliases": [],
    "tags": ["hash_map", "string", "string-matching"],
    "difficulty": "medium",
    "time_complexity": "O(L + Q)",
    "space_complexity": "O(L)",
    "description": "Implement a spellchecker that handles exact matches, case-insensitive matches, and vowel-insensitive matches using priority rules.",
}

def solve(wordlist: list[str], queries: list[str]) -> list[str]:
    """
    Implements a spellchecker with three levels of matching priority:
    1. Exact match (case-sensitive).
    2. Case-insensitive match.
    3. Vowel-insensitive match.

    Args:
        wordlist: A list of valid words.
        queries: A list of words to check against the wordlist.

    Returns:
        A list of strings where each element is the best match from wordlist 
        or an empty string if no match is found.

    Examples:
        >>> solve(["KiTe", "kite", "Kite"], ["kite", "Kite", "KiTe", "kete", "keet", "keti", "q"])
        ['kite', 'KiTe', 'KiTe', 'KiTe', 'KiTe', 'KiTe', '']
    """

    def get_vowel_pattern(word: str) -> str:
        """Converts a word to lowercase and replaces all vowels with a placeholder."""
        word = word.lower()
        return "".join('*' if char in "aeiou" else char for char in word)

    # exact_set: For O(1) exact match lookup
    exact_set = set(wordlist)
    
    # case_map: Maps lowercase version to the FIRST occurrence in wordlist
    case_map = {}
    
    # vowel_map: Maps vowel-masked version to the FIRST occurrence in wordlist
    vowel_map = {}

    for word in wordlist:
        lower_word = word.lower()
        vowel_pattern = get_vowel_pattern(word)

        # We only store the first occurrence for case and vowel patterns
        # to satisfy the requirement of returning the first match in wordlist.
        if lower_word not in case_map:
            case_map[lower_word] = word
        
        if vowel_pattern not in vowel_map:
            vowel_map[vowel_pattern] = word

    results = []
    for query in queries:
        # Priority 1: Exact match
        if query in exact_set:
            results.append(query)
            continue

        # Priority 2: Case-insensitive match
        lower_query = query.lower()
        if lower_query in case_map:
            results.append(case_map[lower_query])
            continue

        # Priority 3: Vowel-insensitive match
        vowel_query_pattern = get_vowel_pattern(query)
        if vowel_query_pattern in vowel_map:
            results.append(vowel_map[vowel_query_pattern])
            continue

        # No match found
        results.append("")

    return results
