METADATA = {
    "id": 2983,
    "name": "Palindrome Rearrangement Queries",
    "slug": "palindrome_rearrangement_queries",
    "category": "Hash Table",
    "aliases": [],
    "tags": ["prefix_sum", "hash_map", "string_manipulation", "bitmask"],
    "difficulty": "medium",
    "time_complexity": "O(n + q)",
    "space_complexity": "O(n)",
    "description": "Determine if a substring can be rearranged into a palindrome using bitmask prefix sums.",
}

def solve(s: str, queries: list[list[int]]) -> list[bool]:
    """
    Determines if substrings defined by queries can be rearranged into palindromes.
    
    A substring can be rearranged into a palindrome if and only if at most one 
    character in that substring appears an odd number of times. This is 
    efficiently checked using a bitmask where the i-th bit represents the 
    parity of the i-th character in the alphabet.

    Args:
        s: The input string consisting of lowercase English letters.
        queries: A list of queries, where each query is [left, right] (0-indexed).

    Returns:
        A list of booleans indicating if each query substring can form a palindrome.

    Examples:
        >>> solve("aabb", [[0, 1], [0, 3]])
        [True, True]
        >>> solve("abcde", [[0, 2]])
        [False]
    """
    n = len(s)
    # prefix_masks[i] stores the bitmask of character parities for s[0...i-1]
    # A bitmask is an integer where the k-th bit is 1 if character (ord('a') + k) 
    # has appeared an odd number of times, and 0 otherwise.
    prefix_masks = [0] * (n + 1)
    current_mask = 0
    
    for i in range(n):
        # Calculate bit position for current character (0-25)
        char_bit = 1 << (ord(s[i]) - ord('a'))
        # XOR the current mask with the bit to flip the parity
        current_mask ^= char_bit
        prefix_masks[i + 1] = current_mask

    results = []
    for left, right in queries:
        # The parity mask for substring s[left...right] is the XOR sum 
        # of prefix_masks[right + 1] and prefix_masks[left].
        # This effectively cancels out all characters that appeared an even number of times.
        substring_mask = prefix_masks[right + 1] ^ prefix_masks[left]
        
        # A substring can form a palindrome if at most one bit is set in the mask.
        # (substring_mask & (substring_mask - 1)) == 0 is a trick to check if 
        # an integer has zero or exactly one bit set.
        is_palindrome_possible = (substring_mask & (substring_mask - 1)) == 0
        results.append(is_palindrome_possible)

    return results
