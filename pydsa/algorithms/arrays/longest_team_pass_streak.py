METADATA = {
    "id": 3390,
    "name": "Longest Team Pass Streak",
    "slug": "longest_team_pass_streak",
    "category": "Array",
    "aliases": [],
    "tags": ["sliding_window", "arrays"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Find the length of the longest contiguous subarray where all elements satisfy a specific condition.",
}

def solve(passes: list[int], threshold: int) -> int:
    """
    Calculates the longest streak of consecutive passes that meet or exceed a threshold.

    Args:
        passes: A list of integers representing the scores of consecutive passes.
        threshold: The minimum score required for a pass to be considered successful.

    Returns:
        The length of the longest contiguous sequence of successful passes.

    Examples:
        >>> solve([1, 2, 3, 4, 5], 3)
        3
        >>> solve([1, 5, 1, 5, 5, 1], 4)
        2
        >>> solve([1, 1, 1], 2)
        0
    """
    max_streak = 0
    current_streak = 0

    for score in passes:
        # Check if the current pass meets the required threshold
        if score >= threshold:
            current_streak += 1
            # Update the global maximum if the current streak is longer
            if current_streak > max_streak:
                max_streak = current_streak
        else:
            # Reset the streak counter if a pass fails the threshold
            current_streak = 0

    return max_streak
