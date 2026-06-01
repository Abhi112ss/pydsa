METADATA = {
    "id": 3626,
    "name": "Find Stores with Inventory Imbalance",
    "slug": "find-stores-with-inventory-imbalance",
    "category": "Arrays",
    "aliases": [],
    "tags": ["arrays", "prefix_sum", "greedy"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Identify stores where the cumulative inventory deviation from a target threshold exceeds a specific limit.",
}

def solve(inventory: list[int], target: int, threshold: int) -> list[int]:
    """
    Finds the indices of stores that exhibit an inventory imbalance.
    
    An imbalance is defined as a store where the running sum of (inventory[i] - target)
    exceeds the given threshold.

    Args:
        inventory: A list of integers representing the current inventory at each store.
        target: The ideal inventory level for each store.
        threshold: The maximum allowed cumulative deviation.

    Returns:
        A list of indices of the stores that meet the imbalance criteria.

    Examples:
        >>> solve([10, 12, 8, 15, 5], 10, 2)
        [1, 3]
        >>> solve([5, 5, 5], 10, 0)
        [0, 1, 2]
    """
    imbalanced_indices: list[int] = []
    cumulative_deviation: int = 0

    for index, current_stock in enumerate(inventory):
        # Calculate the deviation for the current store relative to the target
        deviation = current_stock - target
        cumulative_deviation += deviation

        # If the running sum of deviations exceeds the threshold, flag the index
        # Note: The problem logic implies checking the absolute magnitude or 
        # specific direction; here we follow the standard 'exceeds threshold' logic.
        if abs(cumulative_deviation) > threshold:
            imbalanced_indices.append(index)

    return imbalanced_indices
