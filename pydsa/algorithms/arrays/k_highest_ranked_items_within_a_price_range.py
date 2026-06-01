METADATA = {
    "id": 2146,
    "name": "K Highest Ranked Items Within a Price Range",
    "slug": "k-highest-ranked-items-within-a-price-range",
    "category": "Sorting",
    "aliases": [],
    "tags": ["sorting", "greedy"],
    "difficulty": "medium",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(n)",
    "description": "Find the top k items within a specific price range based on score (descending) and name (ascending).",
}

def solve(items: list[list[str]], k: int, price_low: int, price_high: int) -> list[str]:
    """
    Finds the k highest ranked items within a given price range.
    
    Ranking criteria:
    1. Higher score comes first.
    2. If scores are equal, the item with the lexicographically smaller name comes first.

    Args:
        items: A list of items where each item is [name, score, price].
        k: The number of items to return.
        price_low: The minimum inclusive price.
        price_high: The maximum inclusive price.

    Returns:
        A list of the top k item names.

    Examples:
        >>> solve([["item1", "10", "5"], ["item2", "10", "10"], ["item3", "15", "7"]], 2, 5, 10)
        ['item3', 'item1']
    """
    filtered_items = []

    for name, score_str, price_str in items:
        score = int(score_str)
        price = int(price_str)
        
        # Filter items based on the price range constraint
        if price_low <= price <= price_high:
            filtered_items.append((score, name))

    # Sort the filtered items.
    # To handle descending score and ascending name in one pass:
    # We use -score for the first element of the tuple to sort descending,
    # and the name as the second element to sort ascending.
    filtered_items.sort(key=lambda x: (-x[0], x[1]))

    # Extract the names of the top k items
    result = []
    for i in range(min(k, len(filtered_items))):
        result.append(filtered_items[i][1])

    return result
