METADATA = {
    "id": 599,
    "name": "Minimum Index Sum of Two Lists",
    "slug": "minimum_index_sum_of_two_lists",
    "category": "Hash Table",
    "aliases": [],
    "tags": ["hash_map"],
    "difficulty": "easy",
    "time_complexity": "O(n + m)",
    "space_complexity": "O(n)",
    "description": "Find all common strings between two lists that have the minimum index sum.",
}

def solve(list1: list[str], list2: list[str]) -> list[str]:
    """
    Find all common strings between two lists that have the minimum index sum.

    Args:
        list1: First list of strings.
        list2: Second list of strings.

    Returns:
        A list of common strings with the minimum index sum.

    Examples:
        >>> solve(["Shogun", "Tapioca Express", "Burger King", "KFC"], ["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"])
        ['Shogun']
        >>> solve(["Shogun", "Tapioca Express", "Burger King", "KFC"], ["KFC", "Shogun", "Burger King"])
        ['Shogun']
    """
    # Build a hash map from string to its index in list1 for O(1) lookups
    index_map = {string: idx for idx, string in enumerate(list1)}

    min_sum = float('inf')
    result = []

    # Iterate through list2, checking for common strings and tracking minimum index sum
    for idx2, string in enumerate(list2):
        if string in index_map:
            current_sum = index_map[string] + idx2
            if current_sum < min_sum:
                min_sum = current_sum
                result = [string]
            elif current_sum == min_sum:
                result.append(string)

    return result