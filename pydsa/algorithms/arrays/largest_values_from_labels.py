METADATA = {
    "id": 1090,
    "name": "Largest Values From Labels",
    "slug": "largest-values-from-labels",
    "category": "Greedy",
    "aliases": [],
    "tags": ["greedy", "sorting"],
    "difficulty": "medium",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(n)",
    "description": "Find the maximum possible sum of values from a subset of items such that no two items share a label that is less than a given limit.",
}

def solve(items: list[list[int]], allowed_labels: int) -> int:
    """
    Calculates the maximum sum of values from items such that each selected 
    item has a unique label, and all selected labels are >= allowed_labels.

    Args:
        items: A list of items where each item is [value, label].
        allowed_labels: The minimum threshold for a label to be considered.

    Returns:
        The maximum possible sum of values.

    Examples:
        >>> solve([[5, 10], [4, 9], [3, 10], [1, 2]], 5)
        9
        >>> solve([[10, 5], [10, 5], [10, 5]], 1)
        10
    """
    # Sort items by value in descending order to greedily pick the largest values first
    items.sort(key=lambda x: x[0], reverse=True)

    total_sum = 0
    used_labels = set()

    for value, label in items:
        # Check if the label meets the minimum threshold requirement
        if label >= allowed_labels:
            # If the label hasn't been used yet, include this item's value
            if label not in used_labels:
                total_sum += value
                used_labels.add(label)

    return total_sum
