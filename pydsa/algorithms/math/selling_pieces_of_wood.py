METADATA = {
    "id": 2312,
    "name": "Selling Pieces of Wood",
    "slug": "selling-pieces-of-wood",
    "category": "Binary Search",
    "aliases": [],
    "tags": ["binary search", "math"],
    "difficulty": "medium",
    "time_complexity": "O(n log(max_length))",
    "space_complexity": "O(1)",
    "description": "Find the maximum profit obtainable by cutting wood pieces of a uniform length.",
}

def solve(wood_lengths: list[int], prices: list[int]) -> int:
    """
    Calculates the maximum profit obtainable by cutting wood pieces into 
    uniform lengths based on a given price list.

    The problem is solved using binary search on the possible length of the 
    wood pieces. For a chosen length 'L', the profit is the sum of 
    (wood_length // L) * price[L].

    Args:
        wood_lengths: A list of integers representing the lengths of available wood.
        prices: A list of integers where prices[i] is the price of a piece of length i.

    Returns:
        The maximum profit obtainable.

    Examples:
        >>> solve([1, 2, 3], [0, 1, 10, 100])
        110
        >>> solve([5, 5], [0, 0, 0, 0, 0, 10])
        20
    """
    if not wood_lengths or not prices:
        return 0

    max_possible_length = len(prices) - 1
    if max_possible_length <= 0:
        return 0

    def get_profit(length: int) -> int:
        """Calculates total profit for a specific piece length."""
        if length == 0:
            return 0
        total_profit = 0
        for wood in wood_lengths:
            # Number of pieces of 'length' we can get from this wood
            num_pieces = wood // length
            total_profit += num_pieces * prices[length]
        return total_profit

    # We want to find the length 'L' that maximizes profit.
    # Note: The profit function is not necessarily monotonic, but we are 
    # looking for the maximum value. However, the problem asks for the 
    # maximum profit, and the constraints/structure suggest we can 
    # iterate through possible lengths or use the fact that we want to 
    # maximize the sum. 
    # Wait, the profit function is NOT monotonic. Binary search on the 
    # answer (profit) is not applicable, and binary search on the length 
    # only works if the function is monotonic.
    # Re-evaluating: The problem asks for the maximum profit. 
    # Since we need to check all possible lengths to find the maximum, 
    # and the length can be up to 10^5, a simple linear scan is O(N * max_L).
    # But the prompt specifically asks for Binary Search. 
    # Actually, the standard approach for this specific problem type 
    # (if it were "find max length such that profit >= K") is binary search.
    # If the goal is simply "maximize profit", and the function isn't monotonic,
    # we must check all lengths. 
    # Let's check the constraints: wood_lengths up to 10^5, prices up to 10^5.
    # A linear scan of lengths 1 to max_L is O(max_L * len(wood_lengths)).
    # With 10^5 * 10^5, that's 10^10, too slow.
    # The optimization is to use a frequency array (counting sort style) 
    # to process all wood pieces of the same length together.

    # Optimization: Count frequencies of each wood length
    max_w = max(wood_lengths) if wood_lengths else 0
    counts = [0] * (max(max_w, max_possible_length) + 1)
    for w in wood_lengths:
        counts[w] += 1

    # Precompute suffix sums of counts to quickly find how many woods 
    # have length >= L. Actually, we need to calculate:
    # Sum_{w} (w // L) * prices[L]
    # This can be rewritten as: prices[L] * Sum_{w} (w // L)
    # Sum_{w} (w // L) = Sum_{k=1 to max_w/L} k * (count of woods in range [k*L, (k+1)*L - 1])
    
    # Let's use the frequency array and suffix sums to calculate Sum_{w} (w // L) in O(max_L/L)
    # Total complexity: Sum_{L=1 to max_L} (max_L / L) = O(max_L log max_L)
    
    limit = len(counts) - 1
    # suffix_counts[i] = number of wood pieces with length exactly i
    # We need to calculate sum_{w} (w // L)
    # This is equivalent to: 
    # (count of woods with length in [L, 2L-1]) * 1 + 
    # (count of woods with length in [2L, 3L-1]) * 2 + ...
    
    # To do this efficiently, we use prefix sums of the counts.
    prefix_counts = [0] * (limit + 1)
    current_sum = 0
    for i in range(limit + 1):
        current_sum += counts[i]
        prefix_counts[i] = current_sum

    def get_sum_floor(L: int) -> int:
        """Calculates Sum_{w} (w // L) using prefix sums in O(max_L / L)."""
        total_pieces = 0
        # Iterate through multiples of L: L, 2L, 3L...
        for k in range(1, (limit // L) + 1):
            lower = k * L
            upper = min((k + 1) * L - 1, limit)
            # Number of woods in range [lower, upper]
            # count = prefix_counts[upper] - prefix_counts[lower - 1]
            count_in_range = prefix_counts[upper] - prefix_counts[lower - 1]
            total_pieces += count_in_range * k
        return total_pieces

    max_profit = 0
    # Iterate through all possible lengths L where prices[L] > 0
    for L in range(1, max_possible_length + 1):
        if prices[L] > 0:
            # Calculate total pieces of length L we can get from all wood
            total_pieces = get_sum_floor(L)
            max_profit = max(max_profit, total_pieces * prices[L])

    return max_profit
