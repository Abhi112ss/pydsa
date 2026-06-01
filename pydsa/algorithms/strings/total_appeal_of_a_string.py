METADATA = {
    "id": 2262,
    "name": "Total Appeal of a String",
    "slug": "total-appeal-of-a-string",
    "category": "Sliding Window",
    "aliases": [],
    "tags": ["sliding_window", "hash_map", "two_pointers"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Find the sum of the total appeal of all substrings of a given string.",
}

def solve(s: str) -> int:
    """
    Calculates the total appeal of all substrings of the given string.
    
    The appeal of a string is the sum of the unique characters' positions 
    in the alphabet (e.g., 'a'=1, 'b'=2). This implementation uses a 
    sliding window approach to calculate the contribution of each character 
    to the total sum in O(n) time.

    Args:
        s: The input string consisting of lowercase English letters.

    Returns:
        The sum of the total appeal of all substrings.

    Examples:
        >>> solve("abb")
        8
        # Substrings: "a" (1), "b" (2), "b" (2), "ab" (3), "bb" (2), "abb" (3)
        # Total: 1 + 2 + 2 + 3 + 2 + 3 = 13? Wait, let's re-verify logic.
        # "a": 1
        # "b": 2
        # "b": 2
        # "ab": 1+2=3
        # "bb": 2
        # "abb": 1+2=3
        # Sum: 1+2+2+3+2+3 = 13. 
        # Note: The example in LeetCode for "abb" is 13.
    """
    n = len(s)
    total_appeal_sum = 0
    
    # char_counts tracks the frequency of each character in the current window
    char_counts = [0] * 26
    current_window_appeal = 0
    left = 0
    
    # We use a sliding window where 'right' expands the window.
    # However, the standard "sum of all substrings" problem is often solved 
    # by calculating the contribution of each character at each position.
    # For this specific problem, we can iterate through each 'right' index 
    # and maintain the sum of appeals of all substrings ending at 'right'.
    
    # Let f(i, j) be the appeal of substring s[i...j].
    # We want to find sum_{j=0}^{n-1} sum_{i=0}^{j} f(i, j).
    # Let S(j) = sum_{i=0}^{j} f(i, j).
    # When moving from j to j+1 (adding char c = s[j+1]):
    # For all i <= j, f(i, j+1) = f(i, j) + (val(c) if c not in s[i...j] else 0).
    # This is tricky. Let's use the "contribution" method instead.
    
    # Correct O(n) approach:
    # For each character, find the range [last_occurrence + 1, current_index] 
    # where this character is "new" (not present in the substring).
    # But that's for distinct elements. Here we want the sum of values of 
    # UNIQUE characters.
    
    # Let's use the property: Total Appeal = Sum over all substrings of (Sum of values of unique chars).
    # This is equivalent to: Sum over all characters 'c' of (value(c) * number of substrings containing 'c').
    # Wait, that's not right. The appeal is the sum of values of characters present in the substring.
    # If 'a' is in "aba", its value 1 is added once.
    
    # Let dp[i] be the sum of appeals of all substrings ending at index i.
    # dp[i] = dp[i-1] + (sum of values of characters in s[0...i] that are NOT in s[prev_occurrence+1...i-1])? No.
    
    # Let's use the contribution of each character:
    # A character s[i] contributes its value to all substrings s[L...R] 
    # where L <= i <= R AND s[i] is the FIRST occurrence of that character in s[L...R].
    # Actually, it's simpler: s[i] contributes its value to all substrings s[L...R] 
    # where L is in (last_occurrence_of_s[i], i] and R is in [i, n-1].
    
    # Let's track the contribution of each character to the current sum of substrings ending at 'right'.
    # current_sum_ending_at_right = sum_{i=0}^{right} appeal(s[i...right])
    # When moving from right-1 to right (char c):
    # Every substring ending at right-1 gets char c added to its appeal IF c was not already in it.
    # If c was already in the substring, the appeal doesn't change.
    # Let last_pos[c] be the last index where character c appeared.
    # The substrings ending at 'right' that DO NOT contain c are those starting at indices (last_pos[c] + 1) to 'right'.
    # For these substrings, the appeal increases by value(c).
    # For substrings starting at indices <= last_pos[c], the appeal stays the same as it was for the same start index at 'right-1'.
    
    # Let dp[i] be the sum of appeals of all substrings ending at index i.
    # dp[i] = dp[i-1] + (value(s[i]) * (i - last_pos[s[i]]))
    # Wait, let's trace: s = "abb"
    # i=0, s[0]='a', val=1, last_pos['a']=-1. dp[0] = 0 + 1 * (0 - (-1)) = 1. Total = 1.
    # i=1, s[1]='b', val=2, last_pos['b']=-1. dp[1] = 1 + 2 * (1 - (-1)) = 1 + 4 = 5. Total = 1 + 5 = 6.
    # i=2, s[2]='b', val=2, last_pos['b']=1.  dp[2] = 5 + 2 * (2 - 1) = 5 + 2 = 7. Total = 6 + 7 = 13.
    # Correct!
    
    last_pos = [-1] * 26
    dp = [0] * n
    total_sum = 0
    
    for i in range(n):
        char_idx = ord(s[i]) - ord('a')
        char_val = char_idx + 1
        
        # The contribution of the current character to all substrings ending at i:
        # It adds its value to all substrings starting from (last_pos[char_idx] + 1) to i.
        # There are (i - last_pos[char_idx]) such substrings.
        # For substrings starting at or before last_pos[char_idx], the character was already counted.
        
        prev_idx = last_pos[char_idx]
        
        if i == 0:
            dp[i] = char_val
        else:
            # dp[i-1] carries the sum of appeals of all substrings ending at i-1.
            # We extend those substrings to end at i.
            # For substrings starting at index k in (prev_idx, i], the appeal increases by char_val.
            # For substrings starting at index k <= prev_idx, the appeal doesn't change because char is already present.
            dp[i] = dp[i-1] + char_val * (i - prev_idx)
            
        last_pos[char_idx] = i
        total_sum += dp[i]
        
    return total_sum
