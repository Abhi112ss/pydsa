METADATA = {
    "id": 2156,
    "name": "Find Substring With Given Hash Value",
    "slug": "find-substring-with-given-hash-value",
    "category": "String",
    "aliases": [],
    "tags": ["rolling_hash", "strings"],
    "difficulty": "hard",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Find all starting indices of substrings of length k that match a given hash value using a rolling hash.",
}

def solve(s: str, k: int, base: int, mod: int, target: int) -> list[int]:
    """
    Finds all starting indices of substrings of length k in s that have the given hash value.
    
    The hash function is defined as:
    hash(s[i..i+k-1]) = (s[i] * base^0 + s[i+1] * base^1 + ... + s[i+k-1] * base^{k-1}) % mod

    Args:
        s: The input string consisting of lowercase English letters.
        k: The length of the substring.
        base: The base used for the rolling hash.
        mod: The modulus used for the rolling hash.
        target: The target hash value to match.

    Returns:
        A list of starting indices of substrings that match the target hash value, 
        sorted in ascending order.

    Examples:
        >>> solve("leetcode", 3, 10, 1000, 123)
        [0, 1, 2] (hypothetical)
    """
    n = len(s)
    result = []
    
    # Convert characters to values (a=1, b=2, ..., z=26)
    def get_val(char: str) -> int:
        return ord(char) - ord('a') + 1

    current_hash = 0
    # Precompute base^(k-1) % mod to efficiently remove the leading term
    # in the rolling hash calculation.
    highest_power = pow(base, k - 1, mod)

    # The hash formula is: s[i]*base^0 + s[i+1]*base^1 + ... + s[i+k-1]*base^{k-1}
    # This is equivalent to processing from right to left:
    # hash = (...((s[i+k-1]*base + s[i+k-2])*base + s[i+k-3])...)
    # However, the powers are associated with the index relative to the start of the window.
    # To maintain O(1) updates, we process the string from right to left.
    
    # Step 1: Calculate the hash of the last window of size k
    for i in range(n - 1, n - k - 1, -1):
        current_hash = (current_hash * base + get_val(s[i])) % mod
    
    # Check if the last window matches the target
    if current_hash == target:
        result.append(n - k)

    # Step 2: Slide the window backwards from right to left
    # When moving from window starting at i+1 to window starting at i:
    # New_Hash = (Old_Hash - s[i+k]*base^{k-1}) / base + s[i]*base^0 ??? 
    # Actually, the formula is easier if we view it as:
    # Hash(i) = s[i]*base^0 + s[i+1]*base^1 + ... + s[i+k-1]*base^{k-1}
    # Hash(i-1) = s[i-1]*base^0 + s[i]*base^1 + ... + s[i+k-2]*base^{k-1}
    # Relationship: Hash(i-1) = (Hash(i) - s[i+k-1]*base^{k-1}) * base_inv + s[i-1]
    # But we don't want to use modular inverse.
    # Let's use the reverse definition:
    # Hash(i) = s[i]*base^0 + s[i+1]*base^1 + ...
    # If we process from right to left:
    # current_hash = (s[i]*base^0 + s[i+1]*base^1 + ... + s[i+k-1]*base^{k-1})
    # To get Hash(i-1):
    # current_hash_new = (current_hash - s[i+k-1]*base^{k-1}) * base + s[i-1] is WRONG.
    
    # Correct approach for the specific formula:
    # Hash(i) = (s[i] + base * Hash(i+1_without_last_element))
    # Let's re-evaluate:
    # Hash(i) = s[i]*base^0 + s[i+1]*base^1 + ... + s[i+k-1]*base^{k-1}
    # Hash(i-1) = s[i-1]*base^0 + s[i]*base^1 + ... + s[i+k-2]*base^{k-1}
    # Hash(i-1) = s[i-1] + base * (s[i]*base^0 + ... + s[i+k-2]*base^{k-2})
    # Hash(i-1) = s[i-1] + base * (Hash(i) - s[i+k-1]*base^{k-1})
    
    # Wait, the formula in the problem is:
    # hash(s[i..i+k-1]) = (s[i]*base^0 + s[i+1]*base^1 + ... + s[i+k-1]*base^{k-1}) % mod
    # Let's use the sliding window from right to left:
    # Start with the last window [n-k, n-1]
    # To get window [n-k-1, n-2]:
    # New_Hash = (s[n-k-1]*base^0 + s[n-k]*base^1 + ... + s[n-2]*base^{k-1})
    # New_Hash = s[n-k-1] + base * (s[n-k]*base^0 + ... + s[n-2]*base^{k-2})
    # The term in the parenthesis is (Old_Hash - s[n-1]*base^{k-1}) / base? No.
    
    # Let's use the standard rolling hash for this specific power structure:
    # We want to compute H(i) = sum_{j=0}^{k-1} s[i+j] * base^j
    # H(i-1) = s[i-1] + base * (H(i) - s[i+k-1] * base^{k-1})
    # This requires modular inverse of 'base'. 
    # BUT, if we process from right to left, we can avoid the inverse.
    # Let's define H'(i) = s[i]*base^{k-1} + s[i+1]*base^{k-2} + ... + s[i+k-1]*base^0
    # This is the standard polynomial rolling hash.
    # The problem's hash is the REVERSE of this.
    # Let's just use the property:
    # H(i) = s[i]*base^0 + s[i+1]*base^1 + ... + s[i+k-1]*base^{k-1}
    # H(i-1) = s[i-1] + base * (H(i) - s[i+k-1]*base^{k-1})
    # This is still problematic due to the division.
    
    # Let's use the "Right-to-Left" approach correctly:
    # We calculate the hash of the window [i, i+k-1] by iterating i from n-k down to 0.
    # For i = n-k: current_hash = sum_{j=0}^{k-1} s[n-k+j] * base^j
    # For i = n-k-1: current_hash = s[n-k-1] + base * (sum_{j=0}^{k-2} s[n-k+j] * base^j)
    # This is still not quite right.
    
    # Let's use the simplest O(n) approach:
    # The hash is H(i) = s[i] + base * s[i+1] + base^2 * s[i+2] ...
    # Let's compute the hash of the suffix starting at i:
    # SuffixHash(i) = s[i] + base * SuffixHash(i+1)
    # Then H(i) = (SuffixHash(i) - SuffixHash(i+k) * base^k) ... No, that's for a different formula.
    
    # Let's use the formula: H(i) = (s[i] + base * s[i+1] + ... + s[i+k-1] * base^{k-1})
    # We can compute this by:
    # 1. Compute H(n-k) = s[n-k]*base^0 + ... + s[n-1]*base^{k-1}
    # 2. To get H(i-1) from H(i):
    #    H(i-1) = s[i-1] + base * (H(i) - s[i+k-1]*base^{k-1})
    # This is only possible if we can divide by base.
    
    # ALTERNATIVE:
    # The hash is H(i) = sum_{j=0}^{k-1} s[i+j] * base^j
    # Let's compute the hash of the window [i, i+k-1] using the "reverse" polynomial:
    # P(i) = s[i]*base^{k-1} + s[i+1]*base^{k-2} + ... + s[i+k-1]*base^0
    # This is easy to roll: P(i-1) = (P(i) - s[i+k-1])*base + s[i-1]*base^k ... No.
    # P(i-1) = (P(i) - s[i+k-1]) * base_inv + s[i-1] * base^{k-1} ... No.
    
    # Let's go back to basics.
    # We want H(i) = s[i]*base^0 + s[i+1]*base^1 + ... + s[i+k-1]*base^{k-1}
    # Let's compute the hash of the window [i, i+k-1] by iterating i from n-k down to 0.
    # For the very first window (the rightmost one, starting at n-k):
    # current_hash = s[n-k]*base^0 + s[n-k+1]*base^1 + ... + s[n-1]*base^{k-1}
    # To get the window starting at n-k-1:
    # H(n-k-1) = s[n-k-1]*base^0 + s[n-k]*base^1 + ... + s[n-2]*base^{k-1}
    # H(n-k-1) = s[n-k-1] + base * (s[n-k]*base^0 + ... + s[n-2]*base^{k-2})
    # Notice that (s[n-k]*base^0 + ... + s[n-2]*base^{k-2}) is NOT H(n-k).
    # BUT, H(n-k) = (s[n-k]*base^0 + ... + s[n-2]*base^{k-2}) + s[n-1]*base^{k-1}
    # So, (s[n-k]*base^0 + ... + s[n-2]*base^{k-2}) = H(n-k) - s[n-1]*base^{k-1}
    # Therefore: H(n-k-1) = s[n-k-1] + base * (H(n-k) - s[n-1]*base^{k-1})
    
    # This works! We iterate i from n-k-1 down to 0.
    # The window is [i, i+k-1]. The next window to the right is [i+1, i+k].
    # H(i) = s[i] + base * (H(i+1) - s[i+k]*base^{k-1})
    
    # Let's re-implement.
    
    # Resetting logic for clean implementation
    result = []
    current_hash = 0
    # Precompute base^(k-1) % mod
    pk_1 = pow(base, k - 1, mod)
    
    # 1. Calculate hash for the last window [n-k, n-1]
    for i in range(n - k, n):
        # The power for s[i] in the window starting at n-k is base^(i - (n-k))
        current_hash = (current_hash + get_val(s[i]) * pow(base, i - (n - k), mod)) % mod
        
    if current_hash == target:
        result.append(n - k)
        
    # 2. Slide window from right to left
    # i is the start of the current window. We want to find H(i-1).
    # H(i) = s[i]*base^0 + s[i+1]*base^1 + ... + s[i+k-1]*base^{k-1}
    # H(i-1) = s[i-1]*base^0 + s[i]*base^1 + ... + s[i+k-2]*base^{k-1}
    # H(i-1) = s[i-1] + base * (H(i) - s[i+k-1]*base^{k-1})
    
    for i in range(n - k, 0, -1):
        # current_hash is H(i). We want to compute H(i-1).
        # The character to remove is s[i+k-1]
        # The character to add is s[i-1]
        
        # Remove the term s[i+k-1]*base^{k-1}
        term_to_remove = (get_val(s[i + k - 1]) * pk_1) % mod
        # H(i) - term_to_remove = s[i]*base^0 + ... + s[i+k-2]*base^{k-2}
        # Multiply by base: s[i]*base^1 + ... + s[i+k-2]*base^{k-1}
        # Add s[i-1]: s[i-1]*base^0 + s[i]*base^1 + ... + s[i+k-2]*base^{k-1}
        
        current_hash = (current_hash - term_to_remove) % mod
        current_hash = (current_hash * base + get_val(s[i - 1])) % mod
        
        # Wait, the logic above is slightly different. Let's re-trace.
        # If H(i) = s[i] + s[i+1]*b + ... + s[i+k-1]*b^{k-1}
        # Then H(i) - s[i+k-1]*b^{k-1} = s[i] + s[i+1]*b + ... + s[i+k-2]*b^{k-2}
        # Multiply by b: s[i]*b + s[i+1]*b^2 + ... + s[i+k-2]*b^{k-1}
        # Add s[i-1]: s[i-1] + s[i]*b + ... + s[i+k-2]*b^{k-1} = H(i-1)
        # This is correct.
        
        # However, the loop above calculates H(i-1) and then we check it.
        # Let's fix the loop and the index.
        pass

    # Let's rewrite the loop clearly.
    result = []
    current_hash = 0
    pk_1 = pow(base, k - 1, mod)
    
    # Initial window [n-k, n-1]
    # H(n-k) = s[n-k]*b^0 + s[n-k+1]*b^1 + ... + s[n-1]*b^{k-1}
    # We can compute this in O(k)
    p = 1
    for j in range(k):
        current_hash = (current_hash + get_val(s[n - k + j]) * p) % mod
        if j < k - 1:
            p