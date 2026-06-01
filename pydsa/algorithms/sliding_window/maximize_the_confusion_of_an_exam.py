METADATA = {
    "id": 2024,
    "name": "Maximize the Confusion of an Exam",
    "slug": "maximize-the-confusion-of-an-exam",
    "category": "Sliding Window",
    "aliases": [],
    "tags": ["sliding_window", "two_pointer"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Find the maximum number of consecutive true or false answers possible by changing at most k answers.",
}

def solve(answer_key: str, k: int) -> int:
    """
    Calculates the maximum number of consecutive 'T' or 'F' answers possible 
    by changing at most k answers.

    Args:
        answer_key: A string consisting of 'T' and 'F'.
        k: The maximum number of changes allowed.

    Returns:
        The maximum length of a contiguous subarray of identical characters.

    Examples:
        >>> solve("TFFT", 1)
        3
        >>> solve("TTFTTFTT", 1)
        5
    """

    def get_max_consecutive(target_char: str) -> int:
        """
        Uses a sliding window to find the longest subarray containing 
        the target_char and at most k non-target characters.
        """
        max_len = 0
        left = 0
        changes_used = 0
        
        for right in range(len(answer_key)):
            # If the current character is not our target, it counts as a change
            if answer_key[right] != target_char:
                changes_used += 1
            
            # If we exceeded k changes, shrink the window from the left
            while changes_used > k:
                if answer_key[left] != target_char:
                    changes_used -= 1
                left += 1
            
            # Update the maximum window size found so far
            max_len = max(max_len, right - left + 1)
            
        return max_len

    # The answer is the maximum of trying to maximize 'T's or maximizing 'F's
    return max(get_max_consecutive("T"), get_max_consecutive("F"))
