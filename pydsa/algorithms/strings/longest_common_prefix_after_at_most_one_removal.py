METADATA = {
    "id": 3460,
    "name": "Longest Common Prefix After at Most One Removal",
    "slug": "longest-common-prefix-after-at-most-one-removal",
    "category": "String",
    "aliases": [],
    "tags": ["strings", "hash_map", "prefix", "suffix"],
    "difficulty": "hard",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Find the length of the longest common prefix between two strings after potentially removing at most one character from each string.",
}

def solve(s1: str, s2: str) -> int:
    """
    Finds the length of the longest common prefix possible by removing at most 
    one character from s1 and at most one character from s2.

    Args:
        s1: The first input string.
        s2: The second input string.

    Returns:
        The length of the longest common prefix after at most one removal from each.

    Examples:
        >>> solve("abcde", "abfde")
        4  # Remove 'c' from s1 and 'f' from s2 to get "abde" vs "abde" -> prefix "abde" (len 4)
        >>> solve("aaaaa", "aa")
        2
    """
    n1 = len(s1)
    n2 = len(s2)

    # Step 1: Find the length of the initial common prefix without any removals.
    common_prefix_len = 0
    min_len = min(n1, n2)
    while common_prefix_len < min_len and s1[common_prefix_len] == s2[common_prefix_len]:
        common_prefix_len += 1

    # If the strings are identical up to the end of the shorter string, 
    # the answer is simply the length of the shorter string.
    if common_prefix_len == min_len:
        return common_prefix_len

    # Step 2: We need to check the possibility of skipping one character in s1 or s2.
    # A skip can happen at the first point of mismatch.
    # Let the mismatch index be 'i'.
    # We can either:
    # 1. Skip s1[i] and see how many characters match starting from s1[i+1] and s2[i].
    # 2. Skip s2[i] and see how many characters match starting from s1[i] and s2[i+1].
    # 3. Skip both s1[i] and s2[i] and see how many characters match starting from s1[i+1] and s2[i+1].
    
    # However, the problem asks for the longest common prefix *after* removal.
    # This means the resulting strings must share a prefix.
    # If we remove s1[i], the new s1 starts with s1[0...i-1] + s1[i+1...].
    # If we remove s2[j], the new s2 starts with s2[0...j-1] + s2[j+1...].
    
    # The common prefix will always consist of the initial matching part s1[0...i-1].
    # After the mismatch at index i, we can try to "bridge" the gap.
    
    def get_match_after_skip(idx1: int, idx2: int) -> int:
        """Helper to count matching characters starting from specific indices."""
        count = 0
        while idx1 < n1 and idx2 < n2 and s1[idx1] == s2[idx2]:
            count += 1
            idx1 += 1
            idx2 += 1
        return count

    # Option A: Skip s1[common_prefix_len]
    # The prefix will be common_prefix_len + matches starting from (i+1, i)
    res_skip_s1 = common_prefix_len + get_match_after_skip(common_prefix_len + 1, common_prefix_len)

    # Option B: Skip s2[common_prefix_len]
    # The prefix will be common_prefix_len + matches starting from (i, i+1)
    res_skip_s2 = common_prefix_len + get_match_after_skip(common_prefix_len, common_prefix_len + 1)

    # Option C: Skip both s1[common_prefix_len] and s2[common_prefix_len]
    # The prefix will be common_prefix_len + matches starting from (i+1, i+1)
    res_skip_both = common_prefix_len + get_match_after_skip(common_prefix_len + 1, common_prefix_len + 1)

    # The result is the maximum of these possibilities, but we must ensure 
    # we don't exceed the length of the strings after removal.
    # Note: The logic above naturally handles the prefix length.
    
    # There is one more case: what if we skip a character much later?
    # But a skip later than the first mismatch won't increase the *prefix* length.
    # The prefix length is limited by the first point where the strings differ.
    
    return max(res_skip_s1, res_skip_s2, res_skip_both, common_prefix_len)
