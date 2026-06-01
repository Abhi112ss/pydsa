METADATA = {
    "id": 1177,
    "name": "Can Make Palindrome from Substring",
    "slug": "can-make-palindrome-from-substring",
    "category": "Prefix Sum",
    "aliases": [],
    "tags": ["prefix_sum", "bit_manipulation"],
    "difficulty": "medium",
    "time_complexity": "O(n + q)",
    "space_complexity": "O(n)",
    "description": "Determine if a substring can be rearranged into a palindrome by checking if the number of characters with odd frequencies is within the allowed budget.",
}

def solve(s: str, queries: list[list[int]]) -> list[bool]:
    """
    Determines if substrings defined by queries can be rearranged into palindromes.
    
    A string can be rearranged into a palindrome if the number of characters 
    with odd frequencies is at most 1. Since we can change 'k' characters, 
    we can change 'k' odd frequencies into even ones (or vice versa), 
    effectively reducing the count of odd frequencies by up to 2*k.
    The condition becomes: (odd_count - 1) // 2 <= k, or more simply, 
    odd_count <= 2 * k + 1.

    Args:
        s: The input string consisting of lowercase English letters.
        queries: A list of queries where each query is [left, right].

    Returns:
        A list of booleans indicating if each substring can form a palindrome.

    Examples:
        >>> solve("abacaba", [[0, 2], [0, 3]])
        [True, False]
    """
    n = len(s)
    # We use a bitmask to represent the parity of character counts.
    # bitmask[i] stores the parity of all 26 characters for the prefix s[0...i-1].
    # The j-th bit is 1 if the j-th character has appeared an odd number of times.
    prefix_masks = [0] * (n + 1)
    current_mask = 0
    
    for i in range(n):
        # Map 'a'-'z' to bits 0-25
        char_idx = ord(s[i]) - ord('a')
        # Flip the bit corresponding to the current character
        current_mask ^= (1 << char_idx)
        prefix_masks[i + 1] = current_mask

    results = []
    for left, right in queries:
        # The parity of characters in s[left...right] is the XOR of 
        # prefix_masks[right + 1] and prefix_masks[left].
        # This works because (A ^ B) ^ A = B.
        range_mask = prefix_masks[right + 1] ^ prefix_masks[left]
        
        # Count how many bits are set to 1 (number of characters with odd frequency)
        # bin(x).count('1') is efficient in Python for this purpose.
        odd_count = bin(range_mask).count('1')
        
        # k is the number of characters we can change.
        # Each change can fix two odd counts (one odd becomes even, 
        # and another odd becomes even by changing it to match).
        # Actually, changing one char can reduce odd_count by 2.
        # The requirement is: odd_count - (2 * k) <= 1 (if we want a palindrome)
        # Or: odd_count <= 2 * k + 1
        k = (right - left + 1) // 2 # This is not k, k is provided in the problem.
        # Wait, the problem signature in LeetCode is actually:
        # canMakePalindrome(s, queries) where queries[i] = [left, right, k]
        # Let's adjust the logic to handle the actual query structure.
        pass

    # Re-implementing to match the actual LeetCode query format [left, right, k]
    return [] # Placeholder for the structure below

def can_make_palindrome(s: str, queries: list[list[int]]) -> list[bool]:
    """
    Correct implementation matching LeetCode's query format [left, right, k].

    Args:
        s: The input string.
        queries: A list of [left, right, k] queries.

    Returns:
        A list of booleans.
    """
    n = len(s)
    prefix_masks = [0] * (n + 1)
    current_mask = 0
    
    for i in range(n):
        char_idx = ord(s[i]) - ord('a')
        current_mask ^= (1 << char_idx)
        prefix_masks[i + 1] = current_mask

    results = []
    for left, right, k in queries:
        # XOR of prefix masks gives the parity of characters in the range [left, right]
        range_mask = prefix_masks[right + 1] ^ prefix_masks[left]
        
        # Count bits set to 1
        odd_count = bin(range_mask).count('1')
        
        # To form a palindrome, we can have at most one character with an odd count.
        # Each 'k' allows us to change a character, which can reduce the odd_count by 2.
        # (e.g., change one odd char to match another odd char).
        # The condition: odd_count - 2*k <= 1  => odd_count <= 2*k + 1
        results.append(odd_count <= 2 * k + 1)
        
    return results

# To satisfy the requirement of a single solve() function as requested:
def solve(s: str, queries: list[list[int]]) -> list[bool]:
    """
    Standardized solve function for the problem.
    
    Args:
        s: Input string.
        queries: List of [left, right, k].

    Returns:
        List of booleans.
    """
    n = len(s)
    prefix_masks = [0] * (n + 1)
    current_mask = 0
    
    # Precompute prefix XOR masks for character parity
    for i in range(n):
        current_mask ^= (1 << (ord(s[i]) - ord('a')))
        prefix_masks[i + 1] = current_mask

    results = []
    for left, right, k in queries:
        # Calculate parity of characters in the substring using XOR
        range_mask = prefix_masks[right + 1] ^ prefix_masks[left]
        
        # Count characters with odd frequencies
        odd_count = bin(range_mask).count('1')
        
        # Check if k changes can reduce odd_count to 0 or 1
        results.append(odd_count <= 2 * k + 1)
        
    return results