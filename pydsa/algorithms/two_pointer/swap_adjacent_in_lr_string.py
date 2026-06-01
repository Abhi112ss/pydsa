METADATA = {
    "id": 777,
    "name": "Swap Adjacent in LR String",
    "slug": "swap-adjacent-in-lr-string",
    "category": "String",
    "aliases": [],
    "tags": ["two_pointer", "strings"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Determine if one LR string can be transformed into another by swapping adjacent 'L' and 'R' characters.",
}

def solve(s1: str, s2: str) -> bool:
    """
    Determines if s1 can be transformed into s2 by swapping adjacent 'L' and 'R'.

    The transformation is possible if and only if:
    1. The sequence of 'L's and 'R's is identical in both strings.
    2. For every 'L', its index in s1 is greater than or equal to its index in s2 
       (since 'L' can only move left).
    3. For every 'R', its index in s1 is less than or equal to its index in s2 
       (since 'R' can only move right).
    Actually, a simpler way to view it: 'L' can only move to the left, and 'R' 
    can only move to the right. This is equivalent to saying that for every 
    k-th occurrence of 'L', its index in s1 must be >= its index in s2.

    Args:
        s1: The starting string.
        s2: The target string.

    Returns:
        True if s1 can be transformed into s2, False otherwise.

    Examples:
        >>> solve("RRL", "LRR")
        True
        >>> solve("RRL", "RLR")
        False
        >>> solve("LRLR", "LRRL")
        True
    """
    if len(s1) != len(s2):
        return False

    # We track the indices of 'L' characters in both strings.
    # Since 'L' can only move left, the index of the i-th 'L' in s1 
    # must be greater than or equal to the index of the i-th 'L' in s2.
    # Similarly, 'R' can only move right, so its index in s1 must be <= its index in s2.
    # However, if the counts and relative orders are the same, checking 'L' 
    # is sufficient to validate the entire string.

    l_indices_s1 = []
    l_indices_s2 = []
    
    # Count of R's encountered to ensure the total counts match
    r_count_s1 = 0
    r_count_s2 = 0

    for i in range(len(s1)):
        # Track 'L' positions
        if s1[i] == 'L':
            l_indices_s1.append(i)
        else:
            r_count_s1 += 1
            
        if s2[i] == 'L':
            l_indices_s2.append(i)
        else:
            r_count_s2 += 1

    # 1. Check if the number of 'L's (and thus 'R's) are the same
    if len(l_indices_s1) != len(l_indices_s2) or r_count_s1 != r_count_s2:
        return False

    # 2. Check if the relative order of 'L's allows the transformation.
    # An 'L' at index i in s1 can move to index j in s2 if i >= j.
    for idx1, idx2 in zip(l_indices_s1, l_indices_s2):
        if idx1 < idx2:
            return False

    return True
