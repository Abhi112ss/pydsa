METADATA = {
    "id": 1170,
    "name": "Compare Strings by Frequency of the Smallest Character",
    "slug": "compare-strings-by-frequency-of-the-smallest-character",
    "category": "String",
    "aliases": [],
    "tags": ["sorting", "binary_search", "string"],
    "difficulty": "medium",
    "time_complexity": "O(n + m log m)",
    "space_complexity": "O(m)",
    "description": "Compare two strings based on the frequency of their lexicographically smallest character.",
}

import bisect

def solve(s1: str, s2: str, queries: list[list[int]]) -> list[int]:
    """
    Compares two strings based on the frequency of their smallest characters.

    For each query [i, j], we compare the frequency of the smallest character 
    in s1[i:j+1] with the frequency of the smallest character in s2[i:j+1].
    The comparison rules are:
    1. If freq1 > freq2, return 1.
    2. If freq1 < freq2, return -1.
    3. If freq1 == freq2, compare the smallest characters lexicographically.
       If char1 < char2, return 1. Else return -1.

    Args:
        s1: The first string.
        s2: The second string.
        queries: A list of queries where each query is [i, j].

    Returns:
        A list of integers representing the result of each query.

    Examples:
        >>> solve("aba", "aba", [[0, 2]])
        [1]
        >>> solve("aba", "aba", [[0, 0]])
        [-1]
    """
    
    def get_char_info(s: str) -> tuple[list[list[int]], list[list[int]]]:
        """
        Precalculates prefix sums for each character 'a'-'z'.
        Returns:
            A tuple containing:
            - prefix_counts: A 2D list where prefix_counts[char_idx][i] is the 
              count of char_idx in s[:i].
            - smallest_char_indices: A list of lists where each sublist contains 
              the indices where each character appears.
        """
        n = len(s)
        # prefix_counts[c][i] stores count of character c in s[0...i-1]
        prefix_counts = [[0] * (n + 1) for _ in range(26)]
        # char_indices[c] stores all indices where character c appears
        char_indices = [[] for _ in range(26)]
        
        for idx, char in enumerate(s):
            char_idx = ord(char) - ord('a')
            char_indices[char_idx].append(idx)
            for c in range(26):
                prefix_counts[c][idx + 1] = prefix_counts[c][idx]
            prefix_counts[char_idx][idx + 1] += 1
            
        return prefix_counts, char_indices

    # Precompute prefix sums and character positions for both strings
    # This allows O(1) frequency lookup and O(log N) smallest char lookup
    p1, indices1 = get_char_info(s1)
    p2, indices2 = get_char_info(s2)
    
    results = []
    
    for left, right in queries:
        # Find the smallest character present in s1[left:right+1]
        # and its frequency
        best_char1 = -1
        freq1 = 0
        for c in range(26):
            # Check if character c exists in the range [left, right]
            # using the precomputed prefix sums
            count = p1[c][right + 1] - p1[c][left]
            if count > 0:
                best_char1 = c
                freq1 = count
                break
        
        # Find the smallest character present in s2[left:right+1]
        # and its frequency
        best_char2 = -1
        freq2 = 0
        for c in range(26):
            count = p2[c][right + 1] - p2[c][left]
            if count > 0:
                best_char2 = c
                freq2 = count
                break
        
        # Comparison logic
        if freq1 > freq2:
            results.append(1)
        elif freq1 < freq2:
            results.append(-1)
        else:
            # Frequencies are equal, compare characters lexicographically
            # Note: The problem states if char1 < char2, return 1
            char1_val = ord('a') + best_char1
            char2_val = ord('a') + best_char2
            if char1_val < char2_val:
                results.append(1)
            else:
                results.append(-1)
                
    return results
