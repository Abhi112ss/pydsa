METADATA = {
    "id": 686,
    "name": "Repeated String Match",
    "slug": "repeated-string-match",
    "category": "String",
    "aliases": [],
    "tags": ["string_matching", "kmp", "string"],
    "difficulty": "medium",
    "time_complexity": "O(N + M)",
    "space_complexity": "O(N + M)",
    "description": "Find the minimum number of times string 'a' must be repeated such that 'b' is a substring of the repeated 'a'.",
}

def solve(a: str, b: str) -> int:
    """
    Finds the minimum number of times string 'a' must be repeated so that 'b' is a substring.

    Args:
        a: The base string to be repeated.
        b: The target string to search for.

    Returns:
        The minimum number of repetitions required, or -1 if 'b' cannot be found.

    Examples:
        >>> solve("abcd", "cdabcdab")
        3
        >>> solve("a", "aa")
        2
        >>> solve("abc", "d")
        -1
    """
    
    def compute_lps(pattern: str) -> list[int]:
        """Computes the Longest Prefix Suffix array for KMP."""
        length = 0
        lps = [0] * len(pattern)
        i = 1
        while i < len(pattern):
            if pattern[i] == pattern[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length != 0:
                    length = lps[length - 1]
                else:
                    lps[i] = 0
                    i += 1
        return lps

    def kmp_search(text: str, pattern: str) -> bool:
        """Performs KMP string matching algorithm."""
        if not pattern:
            return True
        lps = compute_lps(pattern)
        i = 0  # index for text
        j = 0  # index for pattern
        while i < len(text):
            if pattern[j] == text[i]:
                i += 1
                j += 1
            if j == len(pattern):
                return True
            elif i < len(text) and pattern[j] != text[i]:
                if j != 0:
                    j = lps[j - 1]
                else:
                    i += 1
        return False

    # Calculate the minimum number of repetitions needed to match or exceed length of b
    # We use math.ceil(len(b) / len(a))
    min_repeats = (len(b) + len(a) - 1) // len(a)
    
    # Case 1: Check if b is in a repeated min_repeats times
    # Case 2: Check if b is in a repeated min_repeats + 1 times (to handle wrap-around)
    # We only need to check up to min_repeats + 1 because if it's not there, 
    # adding more 'a's won't help as the pattern would just repeat.
    
    current_string = a * min_repeats
    if kmp_search(current_string, b):
        return min_repeats
    
    current_string += a
    if kmp_search(current_string, b):
        return min_repeats + 1
    
    return -1
