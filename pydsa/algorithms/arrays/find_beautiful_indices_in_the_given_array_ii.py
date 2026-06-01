METADATA = {
    "id": 3008,
    "name": "Find Beautiful Indices in the Given Array II",
    "slug": "find-beautiful-indices-in-the-given-array-ii",
    "category": "String",
    "aliases": [],
    "tags": ["string_matching", "binary_search", "kmp"],
    "difficulty": "hard",
    "time_complexity": "O(n + m + k log k)",
    "space_complexity": "O(n + m)",
    "description": "Find all indices in an integer array where a pattern array occurs as a subarray, such that the index is within a specific range relative to a target value.",
}

def solve(nums: list[int], pattern: list[int], target: int, a: int, b: int) -> list[int]:
    """
    Finds all indices 'i' in 'nums' where 'pattern' occurs as a subarray,
    and there exists an index 'j' where 'pattern' occurs in 'nums' such that
    abs(i - j) <= a and abs(i - target) <= b.

    Wait, the problem definition for 3008 is:
    Find all indices 'i' such that:
    1. pattern occurs in nums starting at index i.
    2. There exists an index 'j' such that pattern occurs in nums starting at index j,
       and abs(i - target) <= a AND abs(j - target) <= b.
    Actually, the standard version of this problem (3008) is:
    Find all indices 'i' such that pattern occurs at 'i', and there exists 'j'
    where pattern occurs at 'j', and abs(i - target) <= a and abs(j - target) <= b.
    Wait, looking at the actual LeetCode 3008:
    Find all indices 'i' such that:
    1. pattern occurs at index i.
    2. There exists an index 'j' such that pattern occurs at index j,
       and abs(i - target) <= a and abs(j - target) <= b.
    Actually, the constraint is: abs(i - target) <= a AND there exists j such that
    pattern occurs at j and abs(j - target) <= b.
    Wait, let's re-read: "Find all indices i such that pattern occurs at i,
    and there exists an index j such that pattern occurs at j, and abs(i - target) <= a
    and abs(j - target) <= b."
    Actually, the problem is:
    Find all indices i such that:
    - pattern occurs at index i
    - abs(i - target) <= a
    - there exists an index j such that pattern occurs at index j and abs(j - target) <= b.

    Args:
        nums: The main integer array.
        pattern: The pattern array to search for.
        target: The target index to compare against.
        a: The tolerance for index i.
        b: The tolerance for index j.

    Returns:
        A sorted list of indices i that satisfy the conditions.

    Examples:
        >>> solve([1, 2, 1, 2, 1, 2], [1, 2], 1, 1, 1)
        [0, 2]
    """
    n = len(nums)
    m = len(pattern)

    if m == 0:
        return []

    # KMP algorithm to find all occurrences of pattern in nums
    def kmp_search(text: list[int], pat: list[int]) -> list[int]:
        """Standard KMP string matching algorithm for integer arrays."""
        occurrences = []
        m_len = len(pat)
        n_len = len(text)
        
        # Precompute the Longest Prefix Suffix (LPS) array
        lps = [0] * m_len
        length = 0
        i = 1
        while i < m_len:
            if pat[i] == pat[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length != 0:
                    length = lps[length - 1]
                else:
                    lps[i] = 0
                    i += 1
        
        # Perform the search
        i = 0  # index for text
        j = 0  # index for pat
        while i < n_len:
            if pat[j] == text[i]:
                i += 1
                j += 1
            
            if j == m_len:
                occurrences.append(i - j)
                j = lps[j - 1]
            elif i < n_len and pat[j] != text[i]:
                if j != 0:
                    j = lps[j - 1]
                else:
                    i += 1
        return occurrences

    # 1. Find all indices where pattern occurs
    all_indices = kmp_search(nums, pattern)
    if not all_indices:
        return []

    # 2. Find all indices j such that abs(j - target) <= b
    # This is equivalent to target - b <= j <= target + b
    # We can use binary search to check if any such j exists in all_indices
    import bisect
    
    lower_bound_j = target - b
    upper_bound_j = target + b
    
    # Find the first index in all_indices that is >= lower_bound_j
    idx_in_all = bisect.bisect_left(all_indices, lower_bound_j)
    
    # Check if this index exists and is <= upper_bound_j
    exists_j = False
    if idx_in_all < len(all_indices) and all_indices[idx_in_all] <= upper_bound_j:
        exists_j = True
        
    if not exists_j:
        return []

    # 3. Filter all_indices for i such that abs(i - target) <= a
    # This is equivalent to target - a <= i <= target + a
    result = []
    lower_bound_i = target - a
    upper_bound_i = target + a
    
    for i_idx in all_indices:
        if lower_bound_i <= i_idx <= upper_bound_i:
            result.append(i_idx)
            
    return result
