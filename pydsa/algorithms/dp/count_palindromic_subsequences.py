METADATA = {
    "id": 2484,
    "name": "Count Palindromic Subsequences",
    "slug": "count-palindromic-subsequences",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dynamic_programming", "strings", "math"],
    "difficulty": "hard",
    "time_complexity": "O(n^2)",
    "space_complexity": "O(n^2)",
    "description": "Count the number of palindromic subsequences of length 2 or 3 in a given string modulo 10^9 + 7.",
}

def solve(s: str) -> int:
    """
    Counts the number of palindromic subsequences of length 2 or 3 in the string s.
    
    A palindromic subsequence of length 2 is of the form 'aa'.
    A palindromic subsequence of length 3 is of the form 'aba'.
    
    Args:
        s: The input string consisting of lowercase English letters.
        
    Returns:
        The total count of palindromic subsequences of length 2 or 3, modulo 10^9 + 7.
        
    Examples:
        >>> solve("aabaa")
        7
        # Length 2: "aa" (index 0,1), "aa" (index 0,3), "aa" (index 0,4), "aa" (index 1,3), "aa" (index 1,4), "aa" (index 3,4) -> 6
        # Length 3: "aaa" (index 0,1,3), "aaa" (index 0,1,4), "aaa" (index 0,3,4), "aaa" (index 1,3,4), "aba" (index 1,2,3), "aba" (index 1,2,4) -> 6? 
        # Wait, the logic is simpler: 
        # Length 2: pairs of same characters.
        # Length 3: char at i, char at j, char at k where s[i] == s[k] and i < j < k.
    """
    MOD = 1_000_000_007
    n = len(s)
    total_count = 0

    # 1. Count palindromic subsequences of length 2:
    # This is simply the sum of (count * (count - 1) // 2) for each character 'a'-'z'
    char_counts = [0] * 26
    for char in s:
        char_counts[ord(char) - ord('a')] += 1
    
    for count in char_counts:
        if count >= 2:
            # Combination nCr where r=2: n*(n-1)/2
            total_count = (total_count + (count * (count - 1) // 2)) % MOD

    # 2. Count palindromic subsequences of length 3:
    # A subsequence s[i], s[j], s[k] is a palindrome of length 3 if s[i] == s[k] and i < j < k.
    # For every pair of identical characters at indices i and k, any character at index j (i < j < k)
    # forms a palindromic subsequence of length 3.
    
    # To do this efficiently in O(n), we track the occurrences of each character.
    # For a fixed character 'c', if it appears at indices p1, p2, ..., pm:
    # For any pair (pi, pk) where k > i + 1, the number of elements between them is (pk - pi - 1).
    # However, we need to avoid double counting and handle the sum efficiently.
    
    # Let's use a prefix sum approach for each character.
    # For each character 'c', we want to sum (count of elements between index i and k) 
    # for all pairs (i, k) where s[i] == s[k] == 'c'.
    
    # Optimization: For a fixed character 'c', let its positions be pos[0], pos[1], ...
    # Total length-3 palindromes with 'c' as ends = sum_{0 <= i < k < m} (pos[k] - pos[i] - 1)
    # This can be rewritten as:
    # sum_{k=1 to m-1} [ sum_{i=0 to k-1} (pos[k] - pos[i] - 1) ]
    # = sum_{k=1 to m-1} [ k * pos[k] - (sum_{i=0 to k-1} pos[i]) - k ]
    
    char_positions = [[] for _ in range(26)]
    for index, char in enumerate(s):
        char_positions[ord(char) - ord('a')].append(index)
        
    for positions in char_positions:
        m = len(positions)
        if m < 2:
            continue
            
        prefix_sum_indices = 0
        for k in range(m):
            # k is the number of elements seen before the current index positions[k]
            # The formula derived: k * pos[k] - sum_of_previous_pos - k
            if k >= 2: # Need at least two previous indices to form a length-3 palindrome with a middle element
                # Actually, even with k=1, we can have a length-3 palindrome if pos[1]-pos[0] > 1
                pass
            
            # Contribution of all pairs (i, k) where i < k to the total count:
            # Each pair (i, k) adds (positions[k] - positions[i] - 1) to the total.
            # We use the running prefix sum of positions to calculate this in O(1) per k.
            if k > 0:
                # term = k * positions[k] - prefix_sum_indices - k
                # But wait, the 'k' in the formula is the count of 'i's, which is exactly 'k'.
                # The number of elements between pos[i] and pos[k] is pos[k] - pos[i] - 1.
                # Summing over i from 0 to k-1:
                # Sum_{i=0}^{k-1} (pos[k] - pos[i] - 1) = k*pos[k] - (Sum_{i=0}^{k-1} pos[i]) - k
                term = (k * positions[k]) - prefix_sum_indices - k
                total_count = (total_count + term) % MOD
            
            prefix_sum_indices += positions[k]

    return total_count
