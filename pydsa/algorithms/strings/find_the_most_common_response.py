METADATA = {
    "id": 3527,
    "name": "Find the Most Common Response",
    "slug": "find_the_most_common_response",
    "category": "Hash Table",
    "aliases": [],
    "tags": ["hash_map", "strings"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Find the string that appears most frequently in a given list of responses.",
}

def solve(responses: list[str]) -> str:
    """
    Finds the most common response in a list of strings.

    If there is a tie, the first response encountered that reaches the 
    maximum frequency is returned (standard behavior for single-pass max tracking).

    Args:
        responses: A list of strings representing user responses.

    Returns:
        The string that appears most frequently in the input list.

    Examples:
        >>> solve(["yes", "no", "yes", "maybe", "no", "yes"])
        'yes'
        >>> solve(["apple", "banana", "apple", "banana"])
        'apple'
    """
    if not responses:
        return ""

    frequency_map: dict[str, int] = {}
    max_frequency: int = 0
    most_common_response: str = ""

    for response in responses:
        # Update the count for the current response
        current_count = frequency_map.get(response, 0) + 1
        frequency_map[response] = current_count

        # If this response's frequency exceeds the current max, update trackers
        # Using '>' ensures we keep the first one encountered in case of ties
        if current_count > max_frequency:
            max_frequency = current_count
            most_common_response = response

    return most_common_response
