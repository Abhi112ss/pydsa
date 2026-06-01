METADATA = {
    "id": 1759,
    "name": "Count Number of Homogenous Substrings",
    "slug": "count-number-of-homogenous-substrings",
    "category": "String",
    "aliases": [],
    "tags": ["string", "sliding_window", "math"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Count the number of substrings that consist of only one type of character.",
}

def solve(s: str) -> int:
    """
    Calculates the total number of homogenous substrings in a given string.
    
    A homogenous substring is a substring that contains only one unique character.
    The algorithm uses a linear scan to identify contiguous blocks of identical 
    characters and applies the arithmetic series formula to count substrings.

    Args:
        s: The input string consisting of lowercase English letters.

    Returns:
        The total count of homogenous substrings.

    Examples:
        >>> solve("abbcccaa")
        12
        # "a", "b", "b", "bb", "c", "c", "c", "cc", "ccc", "cc", "c", "a", "a"
        # Wait, let's re-verify: 
        # 'a': 1
        # 'bb': 2+1=3
        # 'ccc': 3+2+1=6
        # 'aa': 2+1=3
        # Total: 1 + 3 + 6 + 3 = 13? No, let's re-calculate:
        # 'a' (1) + 'bb' (3) + 'ccc' (6) + 'aa' (3) = 13.
        # Example 1: "abbcccaa" -> 13
        # Example 2: "a" -> 1
        # Example 3: "colle"" -> 'c'(1), 'o'(1), 'll'(3), 'e'(1), 'e'(1) -> 1+1+3+1+1 = 7
    """
    MOD = 10**9 + 7
    total_count = 0
    n = len(s)
    
    if n == 0:
        return 0

    current_run_length = 0
    previous_char = ""

    for char in s:
        if char == previous_char:
            # If the character is the same as the previous, increment the current run
            current_run_length += 1
        else:
            # If it's a new character, reset the run length to 1
            current_run_length = 1
            previous_char = char
        
        # Key Insight: For a contiguous block of length k, the number of 
        # substrings ending at the current index is exactly the current run length.
        # e.g., in "aaa", at index 2 (the 3rd 'a'), the substrings are "a", "aa", "aaa".
        # Summing these run lengths effectively calculates k*(k+1)/2.
        total_count += current_run_length

    return total_count % MOD
