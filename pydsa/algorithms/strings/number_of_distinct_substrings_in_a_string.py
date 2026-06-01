METADATA = {
    "id": 1698,
    "name": "Number of Distinct Substrings in a String",
    "slug": "number_of_distinct_substrings",
    "category": "String",
    "aliases": [],
    "tags": ["suffix_array", "suffix_automaton", "string"],
    "difficulty": "medium",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(n)",
    "description": "Count the number of unique substrings present in a given string using a Suffix Array and LCP array.",
}

def solve(s: str) -> int:
    """
    Calculates the total number of distinct substrings in a given string.
    
    The algorithm uses a Suffix Array and the Longest Common Prefix (LCP) array.
    The total number of substrings in a string of length n is n * (n + 1) // 2.
    Each entry in the LCP array represents a prefix shared between adjacent 
    suffixes in the sorted suffix array. These shared prefixes are duplicate 
    substrings. Subtracting the sum of LCP values from the total substrings 
    yields the count of distinct substrings.

    Args:
        s: The input string.

    Returns:
        The total number of distinct substrings.

    Examples:
        >>> solve("banana")
        15
        >>> solve("aaaaa")
        5
    """
    n = len(s)
    if n == 0:
        return 0

    # 1. Build Suffix Array in O(n log n)
    # sa[i] is the starting index of the i-th lexicographically smallest suffix
    sa = list(range(n))
    rank = [ord(c) for c in s]
    k = 1
    
    while k < n:
        # Key for sorting: (primary rank, secondary rank)
        # secondary rank is rank[i + k] if it exists, else -1
        def get_rank_tuple(i: int) -> tuple[int, int]:
            first = rank[i]
            second = rank[i + k] if i + k < n else -1
            return (first, second)

        sa.sort(key=get_rank_tuple)
        
        # Update ranks based on the sorted order
        new_rank = [0] * n
        for i in range(1, n):
            new_rank[sa[i]] = new_rank[sa[i - 1]]
            if get_rank_tuple(sa[i]) > get_rank_tuple(sa[i - 1]):
                new_rank[sa[i]] += 1
        rank = new_rank
        if rank[sa[n - 1]] == n - 1:
            break
        k *= 2

    # 2. Build LCP Array using Kasai's Algorithm in O(n)
    # lcp[i] is the length of the longest common prefix between sa[i] and sa[i-1]
    lcp = [0] * n
    inv_sa = [0] * n
    for i in range(n):
        inv_sa[sa[i]] = i
    
    h = 0
    for i in range(n):
        if inv_sa[i] > 0:
            j = sa[inv_sa[i] - 1]
            while i + h < n and j + h < n and s[i + h] == s[j + h]:
                h += 1
            lcp[inv_sa[i]] = h
            if h > 0:
                h -= 1

    # 3. Calculate distinct substrings
    # Total substrings = sum of lengths of all suffixes
    # Distinct substrings = Total - sum(LCP values)
    total_substrings = n * (n + 1) // 2
    duplicate_substrings = sum(lcp)
    
    return total_substrings - duplicate_substrings
