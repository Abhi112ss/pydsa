METADATA = {
    "id": 1435,
    "name": "Create a Session Bar Chart",
    "slug": "create-a-session-bar-chart",
    "category": "Hash Table",
    "aliases": [],
    "tags": ["hash_map", "arrays", "counting"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(k)",
    "description": "Count the frequency of session types and return them in a specific bar chart format.",
}

def solve(sessions: list[str], categories: list[str]) -> list[dict[str, int]]:
    """
    Counts the frequency of each session type and returns a list of dictionaries
    representing a bar chart for the specified categories.

    Args:
        sessions: A list of strings representing the types of sessions recorded.
        categories: A list of strings representing the categories to be included in the chart.

    Returns:
        A list of dictionaries where each dictionary contains a category name 
        and its corresponding count.

    Examples:
        >>> solve(["A", "B", "A", "C", "B", "A"], ["A", "B", "C"])
        [{'A': 3}, {'B': 2}, {'C': 1}]
        >>> solve(["X", "Y"], ["A", "B"])
        [{'A': 0}, {'B': 0}]
    """
    # Initialize a frequency map to store counts of each session type
    frequency_map: dict[str, int] = {}
    for session in sessions:
        frequency_map[session] = frequency_map.get(session, 0) + 1

    # Construct the result list based on the order of provided categories
    # We ensure that even if a category has 0 sessions, it is included in the chart
    result: list[dict[str, int]] = []
    for category in categories:
        count = frequency_map.get(category, 0)
        result.append({category: count})

    return result
