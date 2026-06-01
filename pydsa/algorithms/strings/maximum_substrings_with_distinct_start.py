METADATA = {
    "id": 3760,
    "name": "Maximum Substrings With Distinct Start",
    "slug": "maximum_substrings_with_distinct_start",
    "category": "Greedy",
    "aliases": [],
    "tags": ["sliding_window", "hash_map", "greedy"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Find the maximum number of non-overlapping substrings such that each substring starts with a unique character.",
}

def solve(s: str) -> int:
    """
    Calculates the maximum number of non-overlapping substrings where each 
    substring starts with a unique character.

    The problem asks for the maximum number of substrings we can pick such that 
    no two substrings start with the same character. Since we want to maximize 
    the count, we should greedily pick the shortest possible substring for each 
    available starting character. However, the constraint is actually simpler: 
    we just need to find if a character can be a starting character of *some* 
    substring that doesn't overlap with others. 

    Actually, the optimal strategy is to identify the first occurrence of each 
    character and see if we can partition the string. But since the problem 
    implies we want to maximize the count of *distinct* starting characters, 
    the maximum possible answer is the number of unique characters present in 
    the string, provided we can pick them without overlap.

    Args:
        s: The input string.

    Returns:
        The maximum number of non-overlapping substrings with distinct starts.

    Examples:
        >>> solve("abacaba")
        3
        >>> solve("aaaaa")
        1
        >>> solve("abcde")
        5
    """
    if not s:
        return 0

    n = len(s)
    # To maximize the count of substrings with distinct starting characters,
    # we want to find the smallest possible substrings for each character.
    # However, the problem is equivalent to finding how many unique characters
    # can serve as the start of a substring in a non-overlapping way.
    
    # In the simplest interpretation of "Maximum Substrings with Distinct Start":
    # We want to pick a set of indices {i_1, i_2, ... i_k} such that 
    # s[i_j] are all distinct and the substrings [i_j, end_j] do not overlap.
    # The smallest possible substring for any index i is just the character s[i] itself.
    # If we take substrings of length 1, we just need to count how many 
    # unique characters exist in the string.
    
    # Wait, if the substrings must be non-overlapping and each must start with 
    # a unique character, and we can choose the length of the substring, 
    # the best strategy is to pick substrings of length 1.
    # If we pick s[i] as a substring of length 1, it doesn't overlap with 
    # any other s[j] where i != j.
    
    # Therefore, the maximum number of such substrings is simply the number 
    # of unique characters present in the string.
    
    unique_chars = set()
    for char in s:
        unique_chars.add(char)
        
    return len(unique_chars)
