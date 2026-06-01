METADATA = {
    "id": 2490,
    "name": "Circular Sentence",
    "slug": "circular-sentence",
    "category": "String",
    "aliases": [],
    "tags": ["strings", "two_pointer"],
    "difficulty": "easy",
    "time_complexity": "O(N + M)",
    "space_complexity": "O(N + M)",
    "description": "Determine if one sentence can be transformed into another by rotating it circularly.",
}

def solve(sentence1: str, sentence2: str) -> bool:
    """
    Determines if sentence2 is a circular rotation of sentence1.

    A sentence is circular if it can be formed by taking a suffix of the 
    original sentence and prepending it to the prefix.

    Args:
        sentence1: The original sentence string.
        sentence2: The target sentence string to check against.

    Returns:
        True if sentence2 is a circular rotation of sentence1, False otherwise.

    Examples:
        >>> solve("a b c", "c a b")
        True
        >>> solve("a b c", "c a")
        False
        >>> solve("a b c", "b c a")
        True
    """
    # If lengths differ, they cannot be circular rotations of each other
    if len(sentence1) != len(sentence2):
        return False

    # A circular rotation of a string is always a substring of the string 
    # concatenated with itself.
    # Example: "a b c" + "a b c" = "a b c a b c"
    # "c a b" is a substring of "a b c a b c"
    doubled_sentence = sentence1 + " " + sentence1
    
    # We check if sentence2 exists within the doubled version.
    # Note: The space in the middle handles the edge case where the 
    # rotation might split a word incorrectly, though for standard 
    # circular rotation logic, sentence1 + sentence1 is sufficient.
    # However, to strictly follow the "circular sentence" definition 
    # where words are units, we check if sentence2 is in (sentence1 + " " + sentence1).
    # Actually, the simplest robust way is sentence1 + " " + sentence1.
    
    # Re-evaluating: The problem defines circularity based on word rotation.
    # If sentence1 = "a b c", possible rotations are "a b c", "c a b", "b c a".
    # All these are substrings of "a b c a b c".
    # We must ensure we don't match partial words (e.g., "a b" in "a b c").
    # But since len(sentence1) == len(sentence2), a substring match of 
    # the same length in the doubled string naturally respects word boundaries.
    
    combined = sentence1 + " " + sentence1
    
    # Check if sentence2 is a substring of the doubled sentence.
    # We use the 'in' operator which is highly optimized in Python (Boyer-Moore/Horspool variant).
    return sentence2 in combined
