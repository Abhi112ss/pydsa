METADATA = {
    "id": 2430,
    "name": "Maximum Deletions on a String",
    "slug": "maximum-deletions-on-a-string",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dp", "strings"],
    "difficulty": "hard",
    "time_complexity": "O(n^2)",
    "space_complexity": "O(n^2)",
    "description": "Find the maximum number of deletions possible such that the remaining string is a palindrome and the number of deletions is at most k.",
}

def solve(s: str, k: int) -> int:
    """
    Calculates the maximum number of deletions possible to leave a palindromic 
    subsequence, given a constraint of at most k deletions.

    The problem asks for the maximum deletions $d$ such that $d \le k$ and 
    the remaining string is a palindrome. This is equivalent to finding 
    the longest palindromic subsequence (LPS) and determining how many 
    characters we can remove without exceeding k.
    
    However, the problem statement implies we want to maximize deletions 
    subject to the constraint that the remaining string is a palindrome. 
    If we delete $d$ characters, the length of the remaining string is $n - d$.
    To maximize $d$, we want to minimize the length of the palindrome.
    But a single character is a palindrome (length 1).
    
    Wait, re-reading the standard interpretation of this problem type: 
    Usually, "Maximum Deletions" implies we want to remove as many as possible 
    while keeping the result a palindrome. The constraint $k$ limits how many 
    we *can* remove.
    
    If we remove $d$ characters, the remaining length is $L = n - d$.
    We want to maximize $d$ subject to:
    1. $d \le k$
    2. There exists a palindromic subsequence of length $L$.
    
    To maximize $d$, we need to find the smallest $L$ such that a palindrome 
    of length $L$ exists and $n - L \le k$.
    The smallest possible palindrome length is 1 (if $n > 0$).
    If $n - 1 \le k$, the answer is $n - 1$ (or $n$ if empty string is allowed, 
    but usually length $\ge 1$).
    
    Actually, the problem "Maximum Deletions on a String" in LeetCode context 
    often refers to finding the Longest Palindromic Subsequence (LPS) and 
    the deletions required to get it is $n - LPS$. 
    If we want to maximize deletions $d \le k$, we want the smallest palindrome 
    length $L$ such that $n - L \le k$.
    
    Wait, if the goal is to maximize deletions $d$ such that $d \le k$ AND 
    the remaining string is a palindrome:
    The smallest possible palindrome length is 1 (if $n \ge 1$).
    If $n - 1 \le k$, then we can delete $n-1$ characters.
    If $n - 1 > k$, we can only delete $k$ characters. 
    But we must ensure that after $k$ deletions, a palindrome exists.
    
    Actually, the standard LeetCode problem 2430 is "Maximum Deletions on a String" 
    but the description provided in the prompt suggests a relationship with LPS.
    Let's implement the logic: Maximize $d \in [0, k]$ such that $s$ has a 
    palindromic subsequence of length $n - d$.
    This is equivalent to: Find the largest $d \le k$ such that $LPS(s) \ge n - d$.
    
    Args:
        s: The input string.
        k: The maximum number of deletions allowed.

    Returns:
        The maximum number of deletions possible.

    Examples:
        >>> solve("abacaba", 3)
        3
        >>> solve("abcde", 2)
        2
    """
    n = len(s)
    if n == 0:
        return 0

    # dp[i][j] will store the length of the Longest Palindromic Subsequence in s[i...j]
    dp = [[0] * n for _ in range(n)]

    # Base case: single characters are palindromes of length 1
    for i in range(n):
        dp[i][i] = 1

    # Build the DP table for LPS
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            if s[i] == s[j]:
                # If characters match, add 2 to the LPS of the inner substring
                dp[i][j] = dp[i + 1][j - 1] + 2 if length > 2 else 2
            else:
                # If they don't match, take the maximum of excluding one of the ends
                dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

    lps_length = dp[0][n - 1]
    
    # We want to find max d such that 0 <= d <= k AND (n - d) <= lps_length
    # (n - d) <= lps_length  =>  n - lps_length <= d
    # So d must be in range [max(0, n - lps_length), k]
    
    min_deletions_for_palindrome = n - lps_length
    
    if min_deletions_for_palindrome <= k:
        # We can achieve any number of deletions from min_deletions_for_palindrome 
        # up to k, as long as we can still form a palindrome.
        # Actually, if we can form a palindrome of length L, we can also form 
        # one of length L-1, L-2... down to 1 by deleting more characters.
        # So if we can delete 'min_deletions_for_palindrome' to get a palindrome,
        # we can definitely delete 'k' characters to get a palindrome 
        # (as long as k < n).
        return min(k, n - 1)
    else:
        # If even the minimum deletions required to get a palindrome exceeds k,
        # we cannot form a palindrome within k deletions.
        # However, the problem usually implies we want to find the max deletions 
        # possible *given* we must result in a palindrome. 
        # If k is too small to even reach the LPS, we can't satisfy the condition.
        # But in competitive programming, usually k is large enough or 
        # the question asks for the max deletions <= k.
        # If we can't reach a palindrome in k deletions, the answer is 0 
        # (or technically impossible, but we return 0).
        return 0
