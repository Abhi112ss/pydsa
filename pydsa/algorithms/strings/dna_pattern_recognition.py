METADATA = {
    "id": 3475,
    "name": "DNA Pattern Recognition",
    "slug": "dna_pattern_recognition",
    "category": "String",
    "aliases": [],
    "tags": ["kmp", "string_matching", "string"],
    "difficulty": "medium",
    "time_complexity": "O(n + m)",
    "space_complexity": "O(m)",
    "description": "Find all occurrences of a pattern in a DNA sequence using efficient string matching.",
}

def solve(sequence: str, pattern: str) -> list[int]:
    """
    Finds all starting indices of the pattern within the DNA sequence using 
    the Knuth-Morris-Pratt (KMP) algorithm.

    Args:
        sequence: The DNA sequence string to search within.
        pattern: The DNA pattern string to search for.

    Returns:
        A list of starting indices where the pattern is found in the sequence.

    Examples:
        >>> solve("GATTACA", "TTA")
        [2]
        >>> solve("AAAAA", "AA")
        [0, 1, 2, 3]
        >>> solve("GCTAGCTAGCTA", "GCTA")
        [0, 4, 8]
    """
    if not pattern:
        return []
    
    n = len(sequence)
    m = len(pattern)
    
    if m > n:
        return []

    # Step 1: Precompute the Longest Prefix Suffix (LPS) array
    # lps[i] stores the length of the longest proper prefix of pattern[0...i] 
    # that is also a suffix of pattern[0...i].
    lps = [0] * m
    length = 0  # length of the previous longest prefix suffix
    i = 1
    
    while i < m:
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1

    # Step 2: Perform the KMP search
    results = []
    seq_idx = 0  # index for sequence
    pat_idx = 0  # index for pattern
    
    while seq_idx < n:
        if pattern[pat_idx] == sequence[seq_idx]:
            seq_idx += 1
            pat_idx += 1
        
        if pat_idx == m:
            # Pattern found, record the starting index
            results.append(seq_idx - pat_idx)
            pat_idx = lps[pat_idx - 1]
        elif seq_idx < n and pattern[pat_idx] != sequence[seq_idx]:
            # Mismatch after pat_idx matches
            if pat_idx != 0:
                pat_idx = lps[pat_idx - 1]
            else:
                seq_idx += 1
                
    return results
