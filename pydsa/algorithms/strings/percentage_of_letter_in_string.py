METADATA = {
    "id": 2277,
    "name": "Percentage of Letter in String",
    "slug": "percentage-of-letter-in-string",
    "category": "String",
    "aliases": [],
    "tags": ["string", "hash-map", "math"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Calculate the percentage of a specific character in a given string, rounded to two decimal places.",
}

def solve(s: str, target: str) -> float:
    """
    Calculates the percentage of the target character in the string s.

    Args:
        s: The input string to analyze.
        target: The single character to count.

    Returns:
        The percentage of the target character in s, rounded to two decimal places.

    Examples:
        >>> solve("leetcode", "e")
        37.5
        >>> solve("leetcode", "l")
        12.5
        >>> solve("leetcode", "z")
        0.0
    """
    if not s:
        return 0.0

    # Count the occurrences of the target character
    # Since we only care about one character, we don't need a full hash map
    target_count = s.count(target)
    
    # Calculate the percentage
    # Formula: (count / total_length) * 100
    percentage = (target_count / len(s)) * 100
    
    # Round to two decimal places as required by the problem
    return round(percentage, 2)
