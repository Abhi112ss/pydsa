METADATA = {
    "id": 3329,
    "name": "Count Substrings With K-Frequency Characters II",
    "slug": "count-substrings-with-k-frequency-characters-ii",
    "category": "Sliding Window",
    "aliases": [],
    "tags": ["sliding_window", "two_pointer", "hash_table"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Count the number of substrings where every character that appears in the substring appears exactly k times.",
}

def solve(s: str, k: int) -> int:
    """
    Counts the number of substrings where every character present in the 
    substring appears exactly k times.

    Args:
        s: The input string consisting of lowercase English letters.
        k: The required frequency for each character present in the substring.

    Returns:
        The total count of valid substrings.

    Examples:
        >>> solve("abacaba", 1)
        7
        >>> solve("aaabbb", 3)
        2
    """
    n = len(s)
    total_count = 0

    # The number of unique characters in a valid substring can range from 1 to 26.
    # We iterate through each possible number of unique characters 'target_unique_count'.
    for target_unique_count in range(1, 27):
        # If the total characters required (target_unique_count * k) exceeds string length, break.
        if target_unique_count * k > n:
            break

        char_frequency = {}
        left = 0
        # count_at_k tracks how many characters currently have a frequency of exactly k.
        count_at_k = 0

        for right in range(n):
            char_right = s[right]
            char_frequency[char_right] = char_frequency.get(char_right, 0) + 1
            
            # If this character just reached frequency k, increment our tracker.
            if char_frequency[char_right] == k:
                count_at_k += 1
            # If it just exceeded k, it's no longer a valid candidate for this window.
            elif char_frequency[char_right] == k + 1:
                count_at_k -= 1

            # Shrink the window if the number of unique characters exceeds our target.
            while len(char_frequency) > target_unique_count:
                char_left = s[left]
                if char_frequency[char_left] == k:
                    count_at_k -= 1
                elif char_frequency[char_left] == k + 1:
                    count_at_k += 1
                
                char_frequency[char_left] -= 1
                if char_frequency[char_left] == 0:
                    del char_frequency[char_left]
                left += 1

            # A substring is valid if:
            # 1. The number of unique characters matches target_unique_count.
            # 2. Every character in the window appears exactly k times.
            # Since we know len(char_frequency) == target_unique_count, 
            # we only need to check if count_at_k == target_unique_count.
            if len(char_frequency) == target_unique_count and count_at_k == target_unique_count:
                total_count += 1

    return total_count
