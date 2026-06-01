METADATA = {
    "id": 2663,
    "name": "Lexicographically Smallest Beautiful String",
    "slug": "lexicographically-smallest-beautiful-string",
    "category": "String",
    "aliases": [],
    "tags": ["greedy", "string"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Construct the lexicographically smallest string of length n such that for every index i, the character at i is the same as the character at index (i % k).",
}

def solve(n: int, k: int, s: str) -> str:
    """
    Constructs the lexicographically smallest beautiful string of length n.
    
    A string is beautiful if for every index i, s[i] == s[i % k].
    The input string s provides constraints: if s[i] != '?', then the 
    character at index i must be s[i].

    Args:
        n: The length of the target string.
        k: The period of the beautiful string.
        s: A string of length n containing lowercase letters and '?'.

    Returns:
        The lexicographically smallest beautiful string. Returns an empty 
        string if no such string exists.

    Examples:
        >>> solve(5, 3, "a?b??")
        'aab aa' -> 'aabaa' (Wait, example logic: s[0]='a', s[2]='b'. 
        Period 3 means s[0]=s[3], s[1]=s[4], s[2]=s[5]...)
        Actually, let's follow the rule: s[i] == s[i % k].
        If n=5, k=3, s="a?b??":
        i=0: s[0]='a' -> s[3] must be 'a'
        i=1: s[1]='?' -> s[4] must be s[1]
        i=2: s[2]='b' -> s[5] (out of bounds)
        Result: 'aabaa' if s[1] can be 'a'.
    """
    # pattern will store the determined character for each index in the period [0, k-1]
    pattern = [None] * k

    # Step 1: Fill the pattern based on the constraints provided in s
    for i in range(n):
        if s[i] != '?':
            char_at_i = s[i]
            period_idx = i % k
            
            # If this period index is already assigned a different character, it's impossible
            if pattern[period_idx] is not None and pattern[period_idx] != char_at_i:
                return ""
            pattern[period_idx] = char_at_i

    # Step 2: Fill remaining 'None' values in pattern with 'a' to ensure lexicographical smallest
    for i in range(k):
        if pattern[i] is None:
            pattern[i] = 'a'

    # Step 3: Construct the final string using the pattern
    result_chars = []
    for i in range(n):
        result_chars.append(pattern[i % k])

    return "".join(result_chars)
