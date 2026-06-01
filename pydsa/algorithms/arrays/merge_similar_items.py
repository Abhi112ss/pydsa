METADATA = {
    "id": 2363,
    "name": "Merge Similar Items",
    "slug": "merge_similar_items",
    "category": "array",
    "aliases": [],
    "tags": ["hash_map", "sorting", "array"],
    "difficulty": "easy",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(n)",
    "description": "Merge items with the same value by summing their weights and return them sorted by value.",
}


def solve(items1: list[list[int]], items2: list[list[int]]) -> list[list[int]]:
    """Merge similar items from two lists.

    Args:
        items1: A list of [value, weight] pairs.
        items2: Another list of [value, weight] pairs.

    Returns:
        A list of [value, total_weight] pairs sorted by value in ascending order.

    Examples:
        >>> solve([[1, 1], [4, 5], [3, 8]], [[3, 1], [1, 5]])
        [[1, 6], [3, 9], [4, 5]]
        >>> solve([], [[2, 3], [2, 4]])
        [[2, 7]]
    """
    weight_by_value: dict[int, int] = {}

    # Aggregate weights from the first list
    for value, weight in items1:
        weight_by_value[value] = weight_by_value.get(value, 0) + weight

    # Aggregate weights from the second list
    for value, weight in items2:
        weight_by_value[value] = weight_by_value.get(value, 0) + weight

    # Sort the keys to produce the final ordered list
    merged_items: list[list[int]] = []
    for value in sorted(weight_by_value):
        merged_items.append([value, weight_by_value[value]])

    return merged_items