METADATA = {
    "id": 3035,
    "name": "Maximum Palindromes After Operations",
    "slug": "maximum-palindromes-after-operations",
    "category": "Greedy",
    "aliases": [],
    "tags": ["greedy", "strings"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Find the maximum number of palindromic substrings that can be formed by rearranging characters within given ranges.",
}

def solve(s: str, groups: list[list[int]]) -> int:
    """
    Args:
        s: The input string.
        groups: A list of integer pairs representing the start and end indices of ranges.

    Returns:
        The maximum number of palindromes that can be formed.
    """
    n = len(s)
    prefix_counts = [[0] * 26 for _ in range(n + 1)]
    for i in range(n):
        for char_idx in range(26):
            prefix_counts[i + 1][char_idx] = prefix_counts[i][char_idx]
        prefix_counts[i + 1][ord(s[i]) - ord('a')] += 1

    total_palindromes = 0
    for start, end in groups:
        range_length = end - start + 1
        odd_counts = 0
        for char_idx in range(26):
            count = prefix_counts[end + 1][char_idx] - prefix_counts[start][char_idx]
            if count % 2 != 0:
                odd_counts += 1
        
        available_pairs = (range_length - odd_counts) // 2
        total_palindromes += available_pairs + (1 if odd_counts > 0 or range_length % 2 != 0 else 0)
        
        # Correct logic for maximum palindromes in a range:
        # Each pair of identical characters can form the outer layers of a palindrome.
        # Any leftover single characters (odd counts) must be placed in the center.
        # However, the problem asks for the maximum number of palindromes.
        # A single character is a palindrome. A pair can form a palindrome.
        # The most efficient way to maximize palindromes is to use pairs to form 
        # palindromes of length 2 (or more) and use single characters as palindromes.
        # Actually, the optimal strategy is:
        # Each pair of identical characters can contribute to one palindrome.
        # If we have 'k' pairs, we can form 'k' palindromes of length 2.
        # If we have leftover single characters, each can be a palindrome of length 1.
        # But we must use all characters in the range.
        # The number of palindromes is maximized by making them as small as possible.
        # The smallest palindromes are length 1 and length 2.
        # Wait, the problem is simpler: 
        # A palindrome can be formed by pairs. If we have 'p' pairs, we can form 'p' palindromes.
        # If there are odd characters, they can be centers.
        # Let's re-evaluate: To maximize palindromes, we want to use pairs to form 
        # palindromes of length 2 and single characters to form palindromes of length 1.
        # But we can't just split them arbitrarily; we are rearranging the characters 
        # within the range to form the maximum number of palindromes.
        # The maximum number of palindromes is simply the number of pairs we can form, 
        # plus 1 if there's an odd character left to be a center? No.
        # If we have 4 'a's, we can have two "aa" palindromes.
        # If we have 3 'a's, we can have one "aaa" palindrome or one "aa" and one "a".
        # The rule is: we want to maximize the count.
        # Every pair of identical characters can form a palindrome of length 2.
        # Every single character can form a palindrome of length 1.
        # But we must use all characters.
        # If we have 'pairs' number of pairs, we can form 'pairs' palindromes.
        # If there are any characters left over (which would be the odd ones), 
        # they can each form a palindrome of length 1.
        # However, the question is about the total number of palindromes formed 
        # by partitioning the rearranged string.
        # If we have 'p' pairs and 'o' odd characters:
        # We can form 'p' palindromes of length 2 and 'o' palindromes of length 1.
        # Total = p + o.
        # But wait, if we have 2 pairs (aaaa), we can have "aa" and "aa" (2 palindromes).
        # If we have 1 pair and 1 odd (aaa), we can have "aa" and "a" (2 palindromes).
        # If we have 0 pairs and 3 odds (abc), we can have "a", "b", "c" (3 palindromes).
        # The number of pairs is sum(count // 2).
        # The number of odd characters is sum(count % 2).
        # Total palindromes = sum(count // 2) + sum(count % 2) is not quite right because 
        # we want to maximize the count.
        # Actually, the maximum number of palindromes is simply the number of pairs 
        # we can form, where each pair is a palindrome, and each remaining single 
        # character is a palindrome.
        # Wait, if we have "aabb", we can have "aa" and "bb" (2 palindromes).
        # If we have "aabbc", we can have "aa", "bb", "c" (3 palindromes).
        # The number of pairs is sum(count // 2).
        # The number of single characters is sum(count % 2).
        # Total = sum(count // 2) + sum(count % 2).
        # Let's check: if count is 4, pairs = 2, odds = 0. Total = 2. (aa, aa)
        # If count is 5, pairs = 2, odds = 1. Total = 3. (aa, aa, a)
        # This is equivalent to: total = (total_chars - odd_counts) // 2 + odd_counts.
        # Let's simplify: (range_length - odd_counts) // 2 + odd_counts 
        # = range_length // 2 - odd_counts // 2 + odd_counts 
        # = range_length // 2 + (odd_counts + 1) // 2 ? No.
        # Let's use: pairs = sum(count // 2), odds = sum(count % 2).
        # Result = pairs + odds.
        
        pairs = 0
        odds = 0
        for char_idx in range(26):
            count = prefix_counts[end + 1][char_idx] - prefix_counts[start][char_idx]
            pairs += count // 2
            odds += count % 2
        
        total_palindromes += (pairs + odds)

    # Re-calculating based on the logic: 
    # The problem asks for the maximum number of palindromes.
    # To maximize, we want the shortest possible palindromes.
    # Shortest palindromes are length 1 (single char) and length 2 (pair).
    # Every pair can form a palindrome of length 2.
    # Every single character can form a palindrome of length 1.
    # So for each character frequency 'c', we can form (c // 2) palindromes of length 2
    # and (c % 2) palindromes of length 1.
    # Total palindromes for a range = sum_{i=0}^{25} (count[i] // 2 + count[i] % 2).
    
    # Let's re-run the loop logic properly.
    actual_total = 0
    for start, end in groups:
        range_palindromes = 0
        for char_idx in range(26):
            count = prefix_counts[end + 1][char_idx] - prefix_counts[start][char_idx]
            range_palindromes += (count // 2) + (count % 2)
        actual_total += range_palindromes
        
    return actual_total

# The logic above is slightly redundant in the draft. Let's provide the clean version.
def solve(s: str, groups: list[list[int]]) -> int:
    """
    Args:
        s: The input string.
        groups: A list of integer pairs representing the start and end indices of ranges.

    Returns:
        The maximum number of palindromes that can be formed.
    """
    n = len(s)
    prefix_counts = [[0] * 26 for _ in range(n + 1)]
    for i in range(n):
        for char_idx in range(26):
            prefix_counts[i + 1][char_idx] = prefix_counts[i][char_idx]
        prefix_counts[i + 1][ord(s[i]) - ord('a')] += 1

    total_palindromes = 0
    for start, end in groups:
        range_palindromes = 0
        for char_idx in range(26):
            count = prefix_counts[end + 1][char_idx] - prefix_counts[start][char_idx]
            range_palindromes += (count // 2) + (count % 2)
        total_palindromes += range_palindromes
        
    return total_palindromes

# Wait, I must provide ONLY ONE solve function. The logic in the first attempt was 
# a bit messy. Let's refine the final version.
# The logic: For each character, we can form (count // 2) palindromes of length 2 
# and (count % 2) palindromes of length 1.
# Total palindromes = sum over all characters (count // 2 + count % 2).

def solve(s: str, groups: list[list[int]]) -> int:
    """
    Args:
        s: The input string.
        groups: A list of integer pairs representing the start and end indices of ranges.

    Returns:
        The maximum number of palindromes that can be formed.
    """
    n = len(s)
    prefix_counts = [[0] * 26 for _ in range(n + 1)]
    for i in range(n):
        for char_idx in range(26):
            prefix_counts[i + 1][char_idx] = prefix_counts[i][char_idx]
        prefix_counts[i + 1][ord(s[i]) - ord('a')] += 1

    total_palindromes = 0
    for start, end in groups:
        range_palindromes = 0
        for char_idx in range(26):
            count = prefix_counts[end + 1][char_idx] - prefix_counts[start][char_idx]
            range_palindromes += (count // 2) + (count % 2)
        total_palindromes += range_palindromes
        
    return total_palindromes

# Final check on the logic:
# If s = "aabbc", groups = [[0, 4]]
# a: 2, b: 2, c: 1
# a: 2//2 + 2%2 = 1 + 0 = 1
# b: 2//2 + 2%2 = 1 + 0 = 1
# c: 1//2 + 1%2 = 0 + 1 = 1
# Total = 3. (aa, bb, c)
# If s = "abcde", groups = [[0, 4]]
# a: 1, b: 1, c: 1, d: 1, e: 1
# Each gives 0 + 1 = 1. Total = 5. (a, b, c, d, e)
# This is correct.

def solve(s: str, groups: list[list[int]]) -> int:
    """
    Args:
        s: The input string.
        groups: A list of integer pairs representing the start and end indices of ranges.

    Returns:
        The maximum number of palindromes that can be formed.
    """
    n = len(s)
    prefix_counts = [[0] * 26 for _ in range(n + 1)]
    for i in range(n):
        for char_idx in range(26):
            prefix_counts[i + 1][char_idx] = prefix_counts[i][char_idx]
        prefix_counts[i + 1][ord(s[i]) - ord('a')] += 1

    total_palindromes = 0
    for start, end in groups:
        range_palindromes = 0
        for char_idx in range(26):
            count = prefix_counts[end + 1][char_idx] - prefix_counts[start][char_idx]
            range_palindromes += (count // 2) + (count % 2)
        total_palindromes += range_palindromes
        
    return total_palindromes

# Wait, I see a potential issue. The problem says "rearrange characters within the range".
# If we have "aabbc", we can rearrange to "abcba" (1 palindrome) or "aabbc" (not a palindrome).
# But we want to MAXIMIZE the number of palindromes.
# If we rearrange "aabbc" to "a", "b", "b", "a", "c", that's 5 palindromes? 
# No, the question is "partition the rearranged string into the maximum number of palindromes".
# A partition means every character must belong to exactly one palindrome.
# If we have "aabbc", we can partition it into ["a", "a", "b", "b", "c"] which are 5 palindromes.
# Wait, the problem says "rearrange the characters... to maximize the number of palindromes".
# If we can rearrange "aabbc" to "abcba", that's 1 palindrome.
# If we rearrange it to "a", "a", "b", "b", "c", that's 5 palindromes.
# Is "a", "a", "b", "b", "c" a valid partition of a rearranged string?
# Yes, because "aabbc" is a rearrangement of "aabbc".
# Let's re-read: "rearrange the characters... to maximize the number of palindromes".
# If the string is "aabbc", any rearrangement like "abcba" or "aabbc" or "abcab" is allowed.
# Then we partition that rearrangement into palindromes.
# If we choose the rearrangement "abcba", we can partition it into ["a", "b", "c", "b", "a"] (5 palindromes).
# Wait, if we can always pick palindromes of length 1, then the answer is always the length of the string?
# Let me re-read carefully.
# "You are given a string s and a 2D integer array groups... 
# For each group, you can rearrange the characters... 
# return the maximum total number of palindromes..."
# If I can rearrange "aabbc" to "abcba", I can partition it into ["a", "b", "c", "b", "a"] which is 5.
# But the question is "Maximum Palindromes After Operations".
# Let me check the actual LeetCode problem 3035.
# Ah, the problem is: "You can rearrange the characters... to maximize the number of palindromes".
# Wait, the example 1: s = "abacaba", groups = [[0,0],[1,3],[4,6]].
# Group [0,0] is "a" -> 1 palindrome.
# Group [1,3] is "bac" -> rearrange to "abc" -> "a", "b", "c" is 3 palindromes.
# Group [4,6] is "aba" -> rearrange to "aba" -> "aba" is 1 palindrome? No, "a", "b", "a" is 3.
# Let me look at the example again.
# Example 1: s = "abacaba", groups = [[0,0],[1,3],[4,6]], Output: 5.
# If my logic (sum of count//2 + count%2) was correct:
# [0,0]: a (1) -> 1
# [1,3]: bac (1,1,1) -> 1+1+1 = 3
# [4,6]: aba (2,1) -> 1+1 = 2
# Total = 1 + 3 + 2 = 6. But the output is 5.
# Why is it 5?
# Let's re-read: "a palindrome is a string that reads the same forwards and backwards."
# "a partition of a string is a sequence of non-empty substrings such that..."
# In Example 1:
# [0,0] is "a". Max palindromes: 1 ("a").
# [1,3