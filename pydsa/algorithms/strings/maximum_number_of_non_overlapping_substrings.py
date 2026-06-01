METADATA = {
    "id": 1520,
    "name": "Maximum Number of Non-Overlapping Substrings",
    "slug": "maximum-number-of-non-overlapping-substrings",
    "category": "Greedy",
    "aliases": [],
    "tags": ["greedy", "strings", "sorting"],
    "difficulty": "medium",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(n)",
    "description": "Find the maximum number of non-overlapping substrings such that each substring contains all occurrences of its characters within the original string.",
}

def solve(s: str) -> int:
    """
    Finds the maximum number of non-overlapping substrings where each substring 
    contains all occurrences of its constituent characters.

    Args:
        s: The input string.

    Returns:
        The maximum number of non-overlapping valid substrings.

    Examples:
        >>> solve("cababc")
        2
        >>> solve("abcabc")
        1
    """
    n = len(s)
    if n == 0:
        return 0

    # Step 1: Record the first and last occurrence of every character
    first_occurrence = {}
    last_occurrence = {}
    for index, char in enumerate(s):
        if char not in first_occurrence:
            first_occurrence[char] = index
        last_occurrence[char] = index

    # Step 2: Identify all "valid" candidate substrings.
    # A substring is valid if for every character in it, its entire range 
    # (from first to last occurrence) is contained within the substring.
    candidates = []
    unique_chars = list(first_occurrence.keys())
    
    for char in unique_chars:
        start = first_occurrence[char]
        end = last_occurrence[char]
        
        # Expand the range to include all occurrences of all characters found within [start, end]
        is_valid = True
        current_idx = start
        while current_idx <= end:
            char_at_idx = s[current_idx]
            # If a character's first occurrence is before our current start, 
            # this specific range cannot be a standalone valid substring for 'char'
            if first_occurrence[char_at_idx] < start:
                is_valid = False
                break
            # Expand the end boundary to include the last occurrence of the new character
            end = max(end, last_occurrence[char_at_idx])
            current_idx += 1
        
        if is_valid:
            candidates.append((start, end))

    if not candidates:
        return 0

    # Step 3: Solve the Interval Scheduling Maximization Problem.
    # Sort candidates by their end positions to greedily pick the earliest finishing intervals.
    candidates.sort(key=lambda x: x[1])

    count = 0
    last_end_time = -1
    for start, end in candidates:
        if start > last_end_time:
            count += 1
            last_end_time = end

    return count
