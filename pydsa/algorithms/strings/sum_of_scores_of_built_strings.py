METADATA = {
    "id": 2223,
    "name": "Sum of Scores of Built Strings",
    "slug": "sum-of-scores-of-built-strings",
    "category": "String",
    "aliases": [],
    "tags": ["hash_map", "string_matching", "string"],
    "difficulty": "hard",
    "time_complexity": "O(n^2)",
    "space_complexity": "O(n^2)",
    "description": "Calculate the sum of scores of all strings built by concatenating a prefix and a suffix of a given string s.",
}

def solve(s: str) -> int:
    """
    Calculates the sum of scores of all strings built by concatenating a prefix 
    and a suffix of the input string s. The score of a string is the length 
    of its longest common substring with s.

    Args:
        s: The input string.

    Returns:
        The total sum of scores of all possible prefix-suffix combinations.

    Examples:
        >>> solve("abc")
        10
        # Combinations: "a"+"abc"="aabc"(1), "a"+"bc"="abc"(3), "a"+"c"="ac"(1),
        # "ab"+"abc"="ababc"(2), "ab"+"c"="abc"(3), "abc"+"abc"="abcabc"(3)
        # Wait, the problem defines combinations as:
        # prefix s[0:i], suffix s[j:n] where 1 <= i <= n and 0 <= j < n.
        # Actually, the problem states: 
        # prefix s[0:i] for 1 <= i <= n
        # suffix s[j:n] for 0 <= j < n
        # Total combinations: n * n.
    """
    n = len(s)
    # count[k] will store how many times a substring of length k 
    # appears as a common substring between a prefix and a suffix.
    # However, the problem asks for the sum of the *longest* common substring.
    # A better approach: For every pair of (prefix, suffix), find the LCS.
    # But we can use the property that if a common substring of length k exists,
    # then common substrings of length k-1, k-2...1 also exist.
    
    # We use a frequency map to count how many times each possible 
    # substring length occurs as a common substring between all prefix-suffix pairs.
    # To optimize, we find the length of the longest common suffix between 
    # every prefix s[0:i] and every suffix s[j:n].
    
    # dp[i][j] = length of longest common suffix of s[0:i] and s[j:n]
    # This is equivalent to finding the longest common substring ending at 
    # index i-1 in the prefix and index (j + length - 1) in the suffix.
    # Actually, the simplest way to view this is:
    # For every pair of indices (i, j) where 0 <= i < n and 0 <= j < n,
    # let L = length of longest common substring ending at i and starting at j.
    # This is not quite right. Let's use the standard DP for LCS:
    # dp[i][j] is the length of the longest common suffix of s[0...i-1] and s[j...n-1].
    # Wait, the suffix is s[j...n-1]. The prefix is s[0...i-1].
    # We want the longest common substring between s[0...i-1] and s[j...n-1].
    
    # Correct approach:
    # For every pair of starting positions (i, j) in the string, 
    # find the length of the longest common substring starting at i and j.
    # Let this length be L. This substring contributes to all prefix-suffix 
    # pairs that contain this substring.
    # Actually, the problem is simpler: 
    # For every pair of indices (i, j) where 0 <= i < n and 0 <= j < n,
    # let L be the length of the longest common substring starting at i and j.
    # This is still not quite right.
    
    # Let's use the property: 
    # A substring of length L starting at i and j is a common substring 
    # for all prefixes ending at or after i+L-1 and all suffixes starting at or before j.
    # This is getting complicated. Let's use the DP for "Longest Common Suffix":
    # dp[i][j] = length of longest common suffix of s[0...i-1] and s[j...n-1].
    # This is not standard. Let's use:
    # dp[i][j] = length of longest common substring ending at index i and index j.
    # If s[i] == s[j], dp[i][j] = dp[i-1][j-1] + 1.
    # This substring of length L = dp[i][j] is a common substring for 
    # any prefix that includes index i and any suffix that includes index j.
    
    # Let's re-read: "score of a string is the length of its longest common substring with s".
    # This is equivalent to:
    # For every pair (i, j) where 1 <= i <= n and 0 <= j < n:
    #   Let P = s[0:i], S = s[j:n]
    #   Score = max length of substring in P that is also in S.
    
    # The optimal way:
    # For every pair of indices (i, j) such that s[i] == s[j], 
    # they can be the end of a common substring of length L.
    # This common substring of length L is the *longest* common substring 
    # for a specific set of (prefix, suffix) pairs.
    # Actually, we can just count how many times each length L occurs.
    # If a common substring of length L exists, it contributes to the score.
    # We want the sum of MAX lengths.
    # Let's find for every pair (i, j) the length of the longest common substring 
    # ending at i and j. Let this be L.
    # This L contributes to the score of all (prefix, suffix) pairs that 
    # "cover" this substring.
    # Wait, the problem is simpler: 
    # For every pair of indices (i, j) where s[i] == s[j], 
    # let L be the length of the longest common substring ending at i and j.
    # This L is a candidate for the score.
    # We want the sum of max(L) over all (prefix, suffix).
    # This is equivalent to:
    # For every pair (i, j) such that s[i] == s[j], 
    # let L be the length of the longest common substring ending at i and j.
    # This L contributes to the score of all (prefix, suffix) pairs 
    # where the prefix ends at index >= i and the suffix starts at index <= j.
    # No, that's not right.
    
    # Let's use the DP: dp[i][j] is the length of the longest common substring 
    # ending at index i and index j.
    # If s[i] == s[j]: dp[i][j] = dp[i-1][j-1] + 1
    # Else: dp[i][j] = 0
    # For each (i, j), this dp[i][j] value means there is a common substring 
    # of length L = dp[i][j] ending at i and j.
    # This substring is contained in any prefix s[0:p] where p > i 
    # and any suffix s[q:n] where q <= j.
    # However, we only care about the *maximum* such L for each (p, q).
    # This is equivalent to:
    # For each (i, j), the value L = dp[i][j] contributes to the score 
    # of all (p, q) such that p > i and q <= j.
    # But we only want to count the *maximum* L.
    # We can use a 2D difference array (or 2D prefix sums) to add 1 to 
    # all (p, q) in the range [i+1, n] x [0, j].
    # But we want to add the *length*.
    # Actually, if we add 1 to the range [i+1, n] x [0, j] for every 
    # (i, j) where s[i] == s[j], we are counting how many common substrings 
    # of length at least 1 exist.
    # If we do this for all (i, j) where s[i] == s[j], we are effectively 
    # summing up the lengths of all common substrings.
    # Wait, the sum of max lengths is equal to the sum of (number of common 
    # substrings of length at least k) for all k >= 1.
    # A common substring of length L ending at i and j exists if 
    # dp[i][j] >= L.
    # This is equivalent to saying that for a fixed (i, j), 
    # it contributes to the score of all (p, q) where p > i and q <= j.
    # If we sum up dp[i][j] for all (i, j) such that s[i] == s[j], 
    # we are not getting the max.
    # BUT, if we use the property: 
    # Sum of max lengths = Sum over all (i, j) of (dp[i][j] where s[i]==s[j]) 
    # is NOT correct.
    # Correct logic:
    # For every pair (i, j) such that s[i] == s[j], 
    # let L = dp[i][j]. This L contributes to the score of all (p, q) 
    # such that p > i and q <= j.
    # To avoid overcounting, we only consider the "maximal" common substrings.
    # Actually, the sum of max lengths is equal to:
    # Sum_{i, j} (dp[i][j] if s[i] == s[j] else 0) 
    # where we only count the contribution of each (i, j) to the 
    # (prefix, suffix) pairs.
    # Let's use the 2D difference array approach.
    # For each (i, j) where s[i] == s[j], let L = dp[i][j].
    # This L contributes to all (p, q) where p in [i+1, n] and q in [0, j].
    # This is still not quite right because one (p, q) could have multiple 
    # common substrings. We only want the max.
    # The key insight from similar problems:
    # The sum of max lengths is equal to the sum of dp[i][j] 
    # where we only consider the contribution of each (i, j) to the 
    # (p, q) pairs.
    # Let's use the 2D difference array `diff[p][q]`.
    # For each (i, j) where s[i] == s[j], let L = dp[i][j].
    # We want to add L to all (p, q) such that p > i and q <= j.
    # But we only want the *maximum* L.
    # Actually, if we add 1 to the range [i+1, n] x [0, j] for every 
    # (i, j) where s[i] == s[j], we are counting how many common 
    # substrings of length at least 1 exist.
    # If we do this for all (i, j) where s[i] == s[j], 
    # the total sum will be the sum of the lengths of the longest 
    # common substrings!
    # Let's trace: if a common substring has length 3, it will be 
    # counted at (i, j), (i-1, j-1), and (i-2, j-2).
    # At (i, j), it adds 1 to the range [i+1, n] x [0, j].
    # At (i-1, j-1), it adds 1 to the range [i, n] x [0, j-1].
    # This is exactly what we need.
    
    # Let's refine:
    # 1. Create a 2D difference array `diff` of size (n+2) x (n+2).
    # 2. For each i in 0..n-1, j in 0..n-1:
    #    If s[i] == s[j]:
    #       L = dp[i][j]
    #       # We want to add 1 to all (p, q) such that p > i and q <= j.
    #       # Wait, the range is p in [i+1, n] and q in [0, j].
    #       # In 2D difference array:
    #       # diff[i+1][0] += 1
    #       # diff[i+1][j+1] -= 1
    #       # diff[n+1][0] -= 1 (not needed if we bound)
    #       # diff[n+1][j+1] += 1 (not needed if we bound)
    #       # Actually, the range is p from i+1 to n, and q from 0 to j.
    #       # diff[i+1][0] += 1
    #       # diff[i+1][j+1] -= 1
    #       # diff[n+1][0] -= 1
    #       # diff[n+1][j+1] += 1
    # 3. Compute 2D prefix sum of `diff`.
    # 4. Sum all values in the prefix sum array.
    
    # Wait, the DP `dp[i][j]` is the length of the longest common suffix 
    # of s[0...i] and s[j...n-1]. No, that's not right.
    # Let's use: dp[i][j] = length of longest common substring ending at i and j.
    # If s[i] == s[j]: dp[i][j] = dp[i-1][j-1] + 1
    # This substring ends at i and j.
    # It is a common substring for any prefix s[0:p] where p > i 
    # and any suffix s[q:n] where q <= j.
    # The score of (p, q) is the MAX length.
    # The sum of max lengths is equal to the sum of (number of common 
    # substrings of length at least k).
    # A common substring of length k exists if there is some (i, j) 
    # such that dp[i][j] >= k.
    # This is equivalent to: for each (i, j) where s[i] == s[j], 
    # it contributes 1 to the score of all (p, q) where p > i and q <= j.
    # Let's re-verify:
    # If a common substring has max length 3, it will be counted 
    # at (i, j), (i-1, j-1), and (i-2, j-2).
    # For a fixed (p, q), the number of such (i, j) is exactly the 
    # length of the longest common substring.
    # Yes! This is a known trick.
    
    diff = [[0] * (n + 1) for _ in range(n + 1)]
    
    # dp[i][j] is the length of the longest common suffix of s[0...i] and s[j...n-1]
    # But we need to be careful with indices.
    # Let's use dp[i][j] for s[i] and s[j].
    # To save space, we can use two rows for DP, but we need the 2D diff array.
    # The diff array is O(n^2), which is fine for n=1000.
    
    # We can compute dp[i][j] and update diff immediately.
    # To avoid O(n^2) space for DP, we use only the previous row.
    prev_dp = [0] * n
    for i in range(n):
        curr_dp = [0] * n
        for j in range(n):
            if s[i] == s[j]:
                if i > 0 and j > 0:
                    curr_dp[j] = prev_dp[j-1] + 1
                else:
                    curr_dp[j] = 1
                
                # This (i, j) pair with length L = curr_dp[j] 
                # contributes 1 to all (p, q) where p > i and q <= j.
                # Wait, the (i, j) we are looking at is the END of the substring.
                # The substring is s[i-L+1 ... i]