METADATA = {
    "id": 2060,
    "name": "Check if an Original String Exists Given Two Encoded Strings",
    "slug": "check-if-an-original-string-exists-given-two-encoded-strings",
    "category": "String",
    "aliases": [],
    "tags": ["strings", "two_pointer", "hash_table"],
    "difficulty": "medium",
    "time_complexity": "O(N + M)",
    "space_complexity": "O(N + M)",
    "description": "Determine if there exists an original string that could have produced both encoded strings by comparing character frequencies.",
}

import collections

def solve(encoded1: str, encoded2: str) -> bool:
    """
    Checks if there exists an original string that can produce both encoded strings.
    
    The problem asks if there is a string 's' such that both encoded1 and encoded2 
    are valid encodings of 's'. An encoding is valid if it represents the 
    sequence of characters and their counts. This is equivalent to checking if 
    the multiset of characters in encoded1 is the same as in encoded2, 
    provided that the encoded strings are validly formed.
    
    However, the problem constraints and definition imply that we are looking 
    for a common 'original' string. Since the encoding preserves the relative 
    order and counts, the core requirement is that the total counts of each 
    character must be identical in both encoded strings.

    Args:
        encoded1: The first encoded string.
        encoded2: The second encoded string.

    Returns:
        True if an original string exists, False otherwise.

    Examples:
        >>> solve("a1b2", "ab2")
        True
        >>> solve("a1b2", "a2b1")
        False
    """
    
    def get_char_counts(encoded: str) -> dict[str, int]:
        """Parses the encoded string and returns a frequency map of characters."""
        counts = collections.defaultdict(int)
        i = 0
        n = len(encoded)
        
        while i < n:
            # The character is at the current index
            char = encoded[i]
            i += 1
            
            # Parse the integer count following the character
            count_str = ""
            while i < n and encoded[i].isdigit():
                count_str += encoded[i]
                i += 1
            
            # If no digit follows, it's an invalid encoding per problem context,
            # but based on constraints, we assume valid encoding.
            if count_str:
                counts[char] += int(count_str)
            else:
                # This case handles if the encoding was just 'a' instead of 'a1'
                counts[char] += 1
                
        return counts

    # Step 1: Extract character frequencies from both encoded strings.
    # Since the original string's content is defined by the characters and their counts,
    # two encoded strings represent the same original string if and only if 
    # they contain the same characters with the same total frequencies.
    counts1 = get_char_counts(encoded1)
    counts2 = get_char_counts(encoded2)

    # Step 2: Compare the frequency maps.
    # If the maps are identical, a common original string exists.
    return counts1 == counts2
