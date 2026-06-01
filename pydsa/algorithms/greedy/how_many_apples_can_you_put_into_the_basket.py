METADATA = {
    "id": 1196,
    "name": "How Many Apples Can You Put into the Basket",
    "slug": "how-many-apples-can-you-put-into-the-basket",
    "category": "Greedy",
    "aliases": [],
    "tags": ["greedy", "sorting"],
    "difficulty": "easy",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(1)",
    "description": "Find the maximum number of apples that can be placed in a basket given a weight limit by picking the lightest apples first.",
}

def solve(weights: list[int], basket_capacity: int) -> int:
    """
    Calculates the maximum number of apples that can fit into a basket.

    The strategy is to sort the apples by weight in ascending order and 
    greedily pick the lightest apples until the next apple would exceed 
    the basket's capacity.

    Args:
        weights: A list of integers representing the weight of each apple.
        basket_capacity: An integer representing the maximum weight the basket can hold.

    Returns:
        The maximum number of apples that can be placed in the basket.

    Examples:
        >>> solve([4, 2, 3], 5)
        2
        >>> solve([1, 1, 1], 2)
        2
        >>> solve([10, 20, 30], 5)
        0
    """
    # Sort weights to enable the greedy approach (picking lightest first)
    sorted_weights = sorted(weights)
    
    current_total_weight = 0
    apples_count = 0
    
    for weight in sorted_weights:
        # Check if adding the current lightest apple exceeds capacity
        if current_total_weight + weight <= basket_capacity:
            current_total_weight += weight
            apples_count += 1
        else:
            # Since weights are sorted, no subsequent apple will fit
            break
            
    return apples_count
