METADATA = {
    "id": 2452,
    "name": "Words Within Two Edits of Dictionary",
    "slug": "words-within-two-edits-of-dictionary",
    "category": "Strings",
    "aliases": [],
    "tags": ["strings", "hash_set", "brute_force"],
    "difficulty": "medium",
    "time_complexity": "O(n * m^2)",
    "space_complexity": "O(m)",
    "description": "Determine if each word in a list can be transformed into any word in a dictionary using at most two edits (insert, delete, or replace).",
}

def solve(dictionary: list[str], words: list[str]) -> list[bool]:
    """
    Determines if each word in the 'words' list is within two edits of any word in 'dictionary'.

    Args:
        dictionary: A list of strings representing the target dictionary.
        words: A list of strings to check against the dictionary.

    Returns:
        A list of booleans where each element indicates if the corresponding word 
        is within two edits of a dictionary word.

    Examples:
        >>> solve(["apple", "banana"], ["aple", "banan", "apple", "bana"])
        [True, True, True, True]
        >>> solve(["a", "b", "c"], ["abc", "def"])
        [False, False]
    """
    dictionary_set = set(dictionary)
    results = []

    for word in words:
        found = False
        
        # Case 0: Exact match
        if word in dictionary_set:
            results.append(True)
            continue

        # Case 1: One edit away
        # We generate all possible strings with 1 edit and check existence
        if _check_one_edit(word, dictionary_set):
            results.append(True)
            continue

        # Case 2: Two edits away
        # We generate all possible strings with 2 edits and check existence
        if _check_two_edits(word, dictionary_set):
            results.append(True)
            continue

        results.append(False)

    return results

def _check_one_edit(word: str, dictionary_set: set[str]) -> bool:
    """Checks if any string one edit away from 'word' exists in 'dictionary_set'."""
    chars = "abcdefghijklmnopqrstuvwxyz"
    n = len(word)

    # Deletion
    for i in range(n):
        if word[:i] + word[i+1:] in dictionary_set:
            return True

    # Replacement
    for i in range(n):
        original_char = word[i]
        for char in chars:
            if char != original_char:
                if word[:i] + char + word[i+1:] in dictionary_set:
                    return True

    # Insertion
    for i in range(n + 1):
        for char in chars:
            if word[:i] + char + word[i:] in dictionary_set:
                return True

    return False

def _check_two_edits(word: str, dictionary_set: set[str]) -> bool:
    """Checks if any string two edits away from 'word' exists in 'dictionary_set'."""
    chars = "abcdefghijklmnopqrstuvwxyz"
    
    # To avoid redundant calculations, we can think of this as:
    # A word is 2 edits away if it can reach a dictionary word via 1 edit 
    # from a word that is already 1 edit away from the original.
    # However, for simplicity and to follow the prompt's logic:
    # We generate all 1-edit variations and for each, check if its 1-edit variations exist.
    
    # Optimization: Instead of generating all 2-edit strings (which is huge),
    # we check if any word in the dictionary is within 2 edits of 'word'.
    # But the prompt suggests generating variations. 
    # Given the constraints and the "O(n * m)" hint (which usually implies 
    # m is the length and n is the number of words), we use a more direct approach.
    
    # Let's use the property: if word is 2 edits from dict_word, 
    # then there exists a word 'mid' such that 
    # distance(word, mid) == 1 AND distance(mid, dict_word) == 1.
    
    # We generate all 1-edit variations of 'word'
    one_edit_variations = set()
    n = len(word)
    
    # Deletions
    for i in range(n):
        one_edit_variations.add(word[:i] + word[i+1:])
    # Replacements
    for i in range(n):
        for char in chars:
            if char != word[i]:
                one_edit_variations.add(word[:i] + char + word[i+1:])
    # Insertions
    for i in range(n + 1):
        for char in chars:
            one_edit_variations.add(word[:i] + char + word[i:])

    # Now check if any variation in one_edit_variations is 1 edit away from a dictionary word
    # Or if any variation is in the dictionary (already covered by 1-edit check)
    for variation in one_edit_variations:
        if variation in dictionary_set:
            return True
        if _check_one_edit(variation, dictionary_set):
            return True
            
    return False

# Note: The complexity O(n * m) in the prompt is likely a simplification 
# or refers to specific constraints. The actual complexity for 2 edits 
# involves the alphabet size (26) and word length (m).
# The approach above is the standard way to handle "within K edits" for small K.