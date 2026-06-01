METADATA = {
    "id": 2819,
    "name": "Minimum Relative Loss After Buying Chocolates",
    "slug": "minimum-relative-loss-after-buying-chocolates",
    "category": "Arrays",
    "aliases": [],
    "tags": ["arrays", "sorting"],
    "difficulty": "medium",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(1)",
    "description": "Find the minimum relative loss by selecting k chocolates such that the sum of their prices is maximized.",
}

def solve(prices: list[int], k: int) -> int:
    """
    Calculates the minimum relative loss after buying k chocolates.
    
    The relative loss is defined as the sum of (price_i - min_price_in_selection) 
    for all selected chocolates. To minimize this, we need to maximize the 
    prices of the selected chocolates while keeping the minimum price in the 
    selection as high as possible. However, the problem simplifies to:
    Loss = Sum(selected_prices) - k * min(selected_prices).
    
    To minimize this, we should pick the k largest prices. Let the sorted 
    prices be p_0, p_1, ..., p_{n-1}. If we pick the k largest, the 
    minimum price among them is p_{n-k}.
    
    Args:
        prices: A list of integers representing chocolate prices.
        k: The number of chocolates to buy.

    Returns:
        The minimum relative loss as an integer.

    Examples:
        >>> solve([1, 2, 3, 4, 5], 3)
        3
        # Selected: [3, 4, 5]. Min is 3. Loss: (3-3) + (4-3) + (5-3) = 3.
        >>> solve([10, 20, 30], 2)
        10
        # Selected: [20, 30]. Min is 20. Loss: (20-20) + (30-20) = 10.
    """
    # Sort prices in ascending order to easily access the largest elements
    prices.sort()
    
    n = len(prices)
    # The k largest elements start from index n - k
    start_index = n - k
    
    # The minimum price in our selection of the k largest elements
    min_price_in_selection = prices[start_index]
    
    total_loss = 0
    # Calculate the sum of (price - min_price) for the k largest elements
    for i in range(start_index, n):
        total_loss += (prices[i] - min_price_in_selection)
        
    return total_loss
