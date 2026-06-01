METADATA = {
    "id": 3504,
    "name": "Longest Palindrome After Substring Concatenation II",
    "slug": "longest-palindrome-after-substring-concatenation-ii",
    "category": "String",
    "aliases": [],
    "tags": ["string_matching", "hashing", "dynamic_programming"],
    "difficulty": "hard",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(n)",
    "description": "Find the length of the longest palindrome formed by concatenating two substrings from a given string.",
}

def solve(s: str) -> int:
    """
    Args:
        s: The input string.

    Returns:
        The length of the longest palindrome formed by concatenating two substrings.
    """
    n = len(s)
    if n == 0:
        return 0

    def get_manacher(text: str) -> list[int]:
        t = "#" + "#".join(text) + "#"
        m = len(t)
        p = [0] * m
        center = 0
        right = 0
        for i in range(m):
            mirror = 2 * center - i
            if i < right:
                p[i] = min(right - i, p[mirror])
            
            while i + 1 + p[i] < m and i - 1 - p[i] >= 0 and t[i + 1 + p[i]] == t[i - 1 - p[i]]:
                p[i] += 1
            
            if i + p[i] > right:
                center = i
                right = i + p[i]
        return p

    p_radii = get_manacher(s)
    
    def get_max_pal_at_index(radii: list[int], length: int) -> list[int]:
        max_p = [0] * length
        for i in range(len(radii)):
            original_idx = (i - 1) // 2
            if i % 2 == 0:
                radius = radii[i] // 2
                if radius > 0:
                    start = i // 2 - radius
                    end = i // 2 + radius - 1
                    max_p[start] = max(max_p[start], end - start + 1)
                    max_p[end] = max(max_p[end], end - start + 1)
            else:
                radius = radii[i] // 2
                start = (i - 1) // 2 - radius
                end = (i - 1) // 2 + radius
                max_p[start] = max(max_p[start], end - start + 1)
                max_p[end] = max(max_p[end], end - start + 1)
        return max_p

    max_len_ending_at = [0] * n
    max_len_starting_at = [0] * n

    for i in range(len(p_radii)):
        radius = p_radii[i]
        if radius == 0:
            continue
        
        if i % 2 == 0:
            length = radius
            start = (i // 2) - (radius // 2)
            end = (i // 2) + (radius // 2) - 1
            if start <= end:
                max_len_starting_at[start] = max(max_len_starting_at[start], length)
                max_len_ending_at[end] = max(max_len_ending_at[end], length)
        else:
            length = radius
            start = (i - 1) // 2 - (radius // 2)
            end = (i - 1) // 2 + (radius // 2)
            if start <= end:
                max_len_starting_at[start] = max(max_len_starting_at[start], length)
                max_len_ending_at[end] = max(max_len_ending_at[end], length)

    for i in range(1, n):
        max_len_ending_at[i] = max(max_len_ending_at[i], max_len_ending_at[i-1] - 2)
    for i in range(n - 2, -1, -1):
        max_len_starting_at[i] = max(max_len_starting_at[i], max_len_starting_at[i+1] - 2)

    ans = 0
    for i in range(n - 1):
        ans = max(ans, max_len_ending_at[i] + max_len_starting_at[i+1])
    
    for i in range(n):
        ans = max(ans, p_radii[2*i+1])

    return ans