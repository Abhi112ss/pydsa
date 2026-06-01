METADATA = {
    "id": 1849,
    "name": "Splitting a String Into Descending Consecutive Values",
    "slug": "splitting-a-string-into-descending-consecutive-values",
    "category": "Backtracking",
    "aliases": [],
    "tags": ["backtracking", "string_manipulation"],
    "difficulty": "medium",
    "time_complexity": "O(2^n)",
    "space_complexity": "O(n)",
    "description": "Determine if a string can be split into a sequence of descending consecutive integers.",
}

def solve(s: str) -> bool:
    """
    Args:
        s: The input string consisting of digits.

    Returns:
        True if the string can be split into descending consecutive values, False otherwise.
    """
    n = len(s)

    def backtrack(index: int, last_value: int) -> bool:
        if index == n:
            return True

        for end_index in range(index + 1, n + 1):
            substring = s[index:end_index]
            
            if len(substring) > 1 and substring[0] == '0':
                break
            
            current_value = int(substring)

            if last_value != -1 and current_value >= last_value:
                break

            if backtrack(end_index, current_value):
                return True

        return False

    return backtrack(0, -1)