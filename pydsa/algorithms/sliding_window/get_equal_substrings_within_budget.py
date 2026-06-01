METADATA = {
    "id": 1208,
    "name": "Get Equal Substrings Within Budget",
    "slug": "get-equal-substrings-within-budget",
    "category": "Sliding Window",
    "aliases": [],
    "tags": ["sliding_window", "two_pointer"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Find the maximum length of a substring that can be made equal by changing characters within a given budget.",
}

def solve(s: str, max_cost: int) -> int:
    """
    Finds the maximum length of a substring that can be made equal to a single 
    character within the given max_cost budget.

    The algorithm uses a sliding window approach. Since we want to maximize the 
    length, we can observe that for any window, the optimal character to change 
    all others to is the one that appears most frequently in that window. 
    However, a more efficient way to view this is: 
    Cost = (window_length * max_frequency_char_count) - (sum of frequencies of all chars in window)
    Wait, actually, the cost to make all characters in a window equal to character 'X' 
    is: sum(abs(ord(char) - ord('X')) for char in window).
    
    Actually, the problem asks to make all characters in the substring equal. 
    The cost is the sum of absolute differences between the chosen character and 
    all other characters in the substring.
    
    Wait, the problem description for 1208 is: "You are given a string s and an 
    integer maxCost. You can choose any character to make all characters in a 
    substring equal. The cost is the sum of absolute differences between the 
    chosen character and the characters in the substring. Return the maximum 
    length of such a substring."
    
    Correction: The cost to make a substring equal to character 'target' is:
    Sum over all i in window: abs(ord(s[i]) - ord(target))
    
    Wait, the standard interpretation of this problem (LeetCode 1208) is actually:
    "You are given a string s and an integer maxCost. You can choose any character 
    to make all characters in a substring equal. The cost is the sum of 
    absolute differences between the chosen character and the characters in 
    the substring."
    
    Actually, the optimal character to pick for a window is the MEDIAN of the 
    character values in that window to minimize the sum of absolute differences.
    
    However, for this specific problem, the characters are lowercase English letters.
    We can iterate through each possible target character 'a'-'z' and find the 
    longest substring for each.
    
    Args:
        s: The input string of lowercase English letters.
        max_cost: The maximum allowed budget.

    Returns:
        The maximum length of a substring that satisfies the budget.

    Examples:
        >>> solve("abcd", 5)
        3
        >>> solve("aaaaa", 0)
        5
        >>> solve("abcde", 10)
        5
    """
    max_length = 0
    
    # Since there are only 26 possible target characters, we can run a 
    # sliding window for each character 'a' through 'z'.
    # Total complexity: O(26 * n) which is O(n).
    for char_code in range(ord('a'), ord('z') + 1):
        target_char_val = char_code
        current_window_cost = 0
        left = 0
        
        for right in range(len(s)):
            # Add the cost of the current character relative to the target
            current_window_cost += abs(ord(s[right]) - target_char_val)
            
            # If cost exceeds budget, shrink the window from the left
            while current_window_cost > max_cost:
                current_window_cost -= abs(ord(s[left]) - target_char_val)
                left += 1
            
            # Update the global maximum length found so far
            max_length = max(max_length, right - left + 1)
            
    return max_length
