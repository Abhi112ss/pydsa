METADATA = {
    "id": 1717,
    "name": "Maximum Score From Removing Substrings",
    "slug": "maximum-score-from-removing-substrings",
    "category": "Greedy",
    "aliases": [],
    "tags": ["stack", "greedy", "string"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Maximize the score by greedily removing substrings 'ab' and 'ba' based on their respective values.",
}

def solve(s: str, num_ab: int, num_ba: int) -> int:
    """
    Calculates the maximum score possible by removing substrings 'ab' and 'ba'.

    The strategy is to greedily remove the substring with the higher value first
    using a stack to ensure all possible occurrences are captured, then perform
    a second pass to remove the other substring from the remaining characters.

    Args:
        s: The input string.
        num_ab: The score gained by removing "ab".
        num_ba: The score gained by removing "ba".

    Returns:
        The maximum total score.

    Examples:
        >>> solve("aabbaa", 5, 4)
        10
        >>> solve("aabbaa", 4, 5)
        9
    """

    def remove_substring(text: str, target: str, score: int) -> tuple[str, int]:
        """
        Helper to remove a specific target substring using a stack.

        Args:
            text: The string to process.
            target: The substring to look for (e.g., "ab").
            score: The points awarded per removal.

        Returns:
            A tuple containing (the resulting string, total score gained).
        """
        stack: list[str] = []
        total_score = 0
        first_char = target[0]
        second_char = target[1]

        for char in text:
            # If current char completes the target with the top of the stack
            if stack and stack[-1] == first_char and char == second_char:
                stack.pop()
                total_score += score
            else:
                stack.append(char)
        
        return "".join(stack), total_score

    # Determine which substring to prioritize based on value
    if num_ab >= num_ba:
        # Pass 1: Remove 'ab'
        remaining_s, score1 = remove_substring(s, "ab", num_ab)
        # Pass 2: Remove 'ba' from what's left
        _, score2 = remove_substring(remaining_s, "ba", num_ba)
    else:
        # Pass 1: Remove 'ba'
        remaining_s, score1 = remove_substring(s, "ba", num_ba)
        # Pass 2: Remove 'ab' from what's left
        _, score2 = remove_substring(remaining_s, "ab", num_ab)

    return score1 + score2
