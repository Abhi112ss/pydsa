METADATA = {
    "id": 3477,
    "name": "Fruits Into Baskets II",
    "slug": "fruits-into-baskets-ii",
    "category": "Array",
    "aliases": [],
    "tags": ["greedy", "arrays"],
    "difficulty": "medium",
    "time_complexity": "O(n^2)",
    "space_complexity": "O(1)",
    "description": "Find the minimum number of fruits that cannot be placed into the first available basket that can accommodate them.",
}

def solve(fruits: list[int], baskets: list[int]) -> int:
    """
    Calculates the number of fruits that cannot be placed into any basket.
    
    Each fruit is processed in order. For each fruit, we look for the first 
    available basket (from left to right) that has a capacity greater than 
    or equal to the fruit's size. Once a basket is used, it cannot be reused.

    Args:
        fruits: A list of integers representing the sizes of the fruits.
        baskets: A list of integers representing the capacities of the baskets.

    Returns:
        The count of fruits that could not be placed in any basket.

    Examples:
        >>> solve([4, 2, 5], [3, 5, 4])
        1
        >>> solve([1, 2, 3], [1, 1, 1])
        2
    """
    n = len(fruits)
    # Track which baskets have already been occupied
    basket_used = [False] * n
    placed_count = 0

    for fruit_size in fruits:
        # Search for the first available basket that fits the current fruit
        for i in range(n):
            if not basket_used[i] and baskets[i] >= fruit_size:
                # Mark basket as used and increment successful placements
                basket_used[i] = True
                placed_count += 1
                break
    
    # The result is the total fruits minus those successfully placed
    return n - placed_count
