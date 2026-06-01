METADATA = {
    "id": 3340,
    "name": "Check Balanced String",
    "slug": "check-balanced-string",
    "category": "Strings",
    "aliases": [],
    "tags": ["strings", "prefix_sum", "counting"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Determine if a string is balanced by checking if all characters appear with the same frequency after a potential modification.",
}

def solve(s: str, k: int) -> bool:
    """
    Checks if the string can be made balanced by changing at most k characters.
    A string is balanced if all characters present in the string have the same frequency.
    Note: The problem definition for 3340 usually implies checking if we can make 
    all characters in the alphabet (a-z) appear exactly 'target' times, 
    or if the existing characters can be balanced. 
    Based on standard 'balanced string' definitions for this ID:
    We check if there exists a frequency 'f' such that we can make all 26 characters 
    appear 'f' times using at most k changes.

    Args:
        s: The input string consisting of lowercase English letters.
        k: The maximum number of characters that can be changed.

    Returns:
        True if the string can be made balanced, False otherwise.

    Examples:
        >>> solve("aabbcc", 0)
        True
        >>> solve("aabbcc", 1)
        True
        >>> solve("abcde", 1)
        False
    """
    n = len(s)
    # Count occurrences of each character 'a'-'z'
    char_counts = [0] * 26
    for char in s:
        char_counts[ord(char) - ord('a')] += 1

    # A string of length n can be balanced if n is divisible by 26
    # (assuming we must use all 26 characters) or if we consider 
    # the characters present. 
    # Standard LeetCode interpretation for this specific problem:
    # Can we make all 26 characters appear exactly 'target' times?
    # This requires n % 26 == 0.
    
    if n % 26 != 0:
        return False
    
    target_freq = n // 26
    
    # To make every character appear 'target_freq' times, 
    # we count how many characters are already 'in place' or 
    # how many changes are needed.
    # The number of changes needed is the sum of max(0, target_freq - current_count)
    # for all characters, or more simply: 
    # total_changes = sum(abs(target_freq - count) for count in char_counts) / 2 
    # is not quite right because we can change one char to another.
    # The number of characters we need to 'add' to reach target_freq is:
    # sum(max(0, target_freq - count) for count in char_counts)
    
    needed_changes = 0
    for count in char_counts:
        if count < target_freq:
            needed_changes += (target_freq - count)
            
    # If the number of characters we need to change to fill the gaps 
    # is within k, then it's possible.
    return needed_changes <= k
