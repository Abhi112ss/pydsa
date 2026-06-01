METADATA = {
    "id": 2288,
    "name": "Apply Discount to Prices",
    "slug": "apply-discount-to-prices",
    "category": "Array",
    "aliases": [],
    "tags": ["monotonic_queue", "sliding_window"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Apply a discount to each price based on the next two consecutive prices that are less than or equal to it.",
}

from collections import deque

def solve(prices: list[int]) -> list[int]:
    """
    Applies a discount to each price in the list. 
    A price gets a discount equal to the value of the first price found 
    within the next two indices that is less than or equal to the current price.

    Args:
        prices: A list of integers representing the prices.

    Returns:
        A list of integers representing the prices after applying discounts.

    Examples:
        >>> solve([8, 4, 6, 2, 3])
        [4, 2, 0, 2, 3]
        >>> solve([1, 2, 3, 4, 5])
        [1, 2, 3, 4, 5]
    """
    n = len(prices)
    result = [0] * n
    # monotonic_queue stores indices of prices that could potentially be 
    # the discount for future elements.
    monotonic_queue = deque()

    # We iterate backwards to easily find the "next" valid discount for each index.
    for i in range(n - 1, -1, -1):
        # Remove indices from the queue that are outside the window of 2 elements.
        # The discount must be within the next two indices (i+1, i+2).
        while monotonic_queue and monotonic_queue[0] > i + 2:
            monotonic_queue.popleft()

        # Find the first element in the queue that is <= current price.
        # Since we are iterating backwards and want the *first* occurrence 
        # in the original array, we need to check the queue.
        # However, a standard monotonic queue for "next smaller" usually 
        # stores elements in increasing order.
        
        # Let's refine the logic: To find the first element in [i+1, i+2] 
        # that is <= prices[i], we can simply check the elements 
        # currently in our window.
        
        discount = 0
        # Check the elements in the queue. Since the window size is at most 2,
        # a simple scan of the queue is O(1) amortized.
        for index in monotonic_queue:
            if prices[index] <= prices[i]:
                discount = prices[index]
                break
        
        result[i] = prices[i] - discount

        # Maintain the monotonic property: remove elements from the back 
        # that are greater than the current price, as the current price 
        # is a "better" (closer and potentially smaller) candidate for 
        # future elements.
        while monotonic_queue and prices[monotonic_queue[-1]] > prices[i]:
            monotonic_queue.pop()
            
        monotonic_queue.append(i)

    # The logic above is slightly flawed for the "first" requirement if we 
    # use a standard monotonic queue. Let's use a simpler approach:
    # For each i, the discount is either prices[i+1] (if <= prices[i])
    # or prices[i+2] (if <= prices[i]).
    
    # Re-implementing with the correct O(n) logic:
    final_result = [0] * n
    for i in range(n):
        discount = 0
        if i + 1 < n and prices[i + 1] <= prices[i]:
            discount = prices[i + 1]
        elif i + 2 < n and prices[i + 2] <= prices[i]:
            discount = prices[i + 2]
        final_result[i] = prices[i] - discount
        
    return final_result

def solve_optimized(prices: list[int]) -> list[int]:
    """
    Optimized implementation using the observation that the discount 
    can only be at index i+1 or i+2.
    
    Args:
        prices: A list of integers representing the prices.

    Returns:
        A list of integers representing the prices after applying discounts.
    """
    n = len(prices)
    result = [0] * n
    
    for i in range(n):
        # Check the immediate next element
        if i + 1 < n and prices[i + 1] <= prices[i]:
            result[i] = prices[i] - prices[i + 1]
        # If not, check the element after that
        elif i + 2 < n and prices[i + 2] <= prices[i]:
            result[i] = prices[i] - prices[i + 2]
        # Otherwise, no discount is applied
        else:
            result[i] = prices[i]
            
    return result

# The problem asks for the first element within the next two indices.
# This is exactly what the O(n) loop above does.
solve = solve_optimized
