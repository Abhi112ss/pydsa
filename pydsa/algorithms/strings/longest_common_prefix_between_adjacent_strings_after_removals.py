METADATA = {
    "id": 3598,
    "name": "Longest Common Prefix Between Adjacent Strings After Removals",
    "slug": "longest-common-prefix-between-adjacent-strings-after-removals",
    "category": "Strings",
    "aliases": [],
    "tags": ["strings", "sliding_window", "dynamic_programming"],
    "difficulty": "medium",
    "time_complexity": "O(n * L)",
    "space_complexity": "O(n)",
    "description": "Find the maximum length of the longest common prefix between any two adjacent strings in an array after performing a specific number of character removals.",
}

def solve(strings: list[str], k: int) -> int:
    """
    Args:
        strings: A list of strings to process.
        k: The maximum number of total character removals allowed across all strings.

    Returns:
        The maximum length of the longest common prefix between any two adjacent strings.
    """
    n = len(strings)
    if n < 2:
        return 0

    max_lcp = 0

    for i in range(n - 1):
        s1 = strings[i]
        s2 = strings[i + 1]
        len1 = len(s1)
        len2 = len(s2)
        
        lcp_candidates = []
        
        match_count = 0
        ptr1 = 0
        ptr2 = 0
        
        while ptr1 < len1 and ptr2 < len2:
            if s1[ptr1] == s2[ptr2]:
                match_count += 1
                ptr1 += 1
                ptr2 += 1
            else:
                lcp_candidates.append(match_count)
                match_count = 0
                ptr1 += 1
                ptr2 += 1
        
        lcp_candidates.append(match_count)

        for length in range(min(len1, len2), 0, -1):
            if length <= max_lcp:
                break
            
            needed_removals = 0
            found_valid_lcp = False
            
            for start1 in range(len1 - length + 1):
                sub1 = s1[start1 : start1 + length]
                removals_s1 = len1 - length
                
                for start2 in range(len2 - length + 1):
                    sub2 = s2[start2 : start2 + length]
                    removals_s2 = len2 - length
                    
                    if sub1 == sub2:
                        if removals_s1 + removals_s2 <= k:
                            found_valid_lcp = True
                            break
                if found_valid_lcp:
                    break
            
            if found_valid_lcp:
                max_lcp = max(max_lcp, length)
                break

    return max_lcp

def solve_optimized(strings: list[str], k: int) -> int:
    """
    Args:
        strings: A list of strings to process.
        k: The maximum number of total character removals allowed across all strings.

    Returns:
        The maximum length of the longest common prefix between any two adjacent strings.
    """
    n = len(strings)
    if n < 2:
        return 0

    ans = 0
    for i in range(n - 1):
        s1 = strings[i]
        s2 = strings[i + 1]
        n1 = len(s1)
        n2 = len(s2)

        for length in range(min(n1, n2), ans, -1):
            possible = False
            removals_needed_base = (n1 - length) + (n2 - length)
            if removals_needed_base > k:
                continue

            for start1 in range(n1 - length + 1):
                sub1 = s1[start1 : start1 + length]
                for start2 in range(n2 - length + 1):
                    if s2[start2 : start2 + length] == sub1:
                        if (n1 - length) + (n2 - length) <= k:
                            possible = True
                            break
                if possible:
                    break
            
            if possible:
                ans = max(ans, length)
                break
    return ans

def solve(strings: list[str], k: int) -> int:
    """
    Args:
        strings: A list of strings to process.
        k: The maximum number of total character removals allowed across all strings.

    Returns:
        The maximum length of the longest common prefix between any two adjacent strings.
    """
    n = len(strings)
    if n < 2:
        return 0

    max_lcp = 0
    for i in range(n - 1):
        s1, s2 = strings[i], strings[i+1]
        len1, len2 = len(s1), len(s2)
        
        for length in range(min(len1, len2), max_lcp, -1):
            if (len1 - length) + (len2 - length) > k:
                continue
            
            found = False
            for start1 in range(len1 - length + 1):
                target = s1[start1 : start1 + length]
                for start2 in range(len2 - length + 1):
                    if s2[start2 : start2 + length] == target:
                        found = True
                        break
                if found:
                    break
            
            if found:
                max_lcp = max(max_lcp, length)
                break
                
    return max_lcp