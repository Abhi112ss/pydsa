METADATA = {
    "id": 638,
    "name": "Shopping Offers",
    "slug": "shopping-offers",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dynamic_programming", "backtracking", "memoization"],
    "difficulty": "medium",
    "time_complexity": "O(special_offers ^ needs_sum)",
    "space_complexity": "O(needs_sum)",
    "description": "Find the minimum cost to satisfy customer needs using a combination of special offers and individual item prices.",
}

def solve(price: list[int], special: list[list[int]], needs: list[int]) -> int:
    """
    Calculates the minimum cost to satisfy the customer's needs.

    Args:
        price: A list of integers where price[i] is the price of the i-th item.
        special: A list of lists where special[i] is a special offer. 
                 special[i][0] is the cost, and special[i][1:] are the quantities.
        needs: A list of integers representing the required quantity of each item.

    Returns:
        The minimum cost to satisfy the needs.

    Examples:
        >>> solve([2, 5], [[6, 2, 2], [3, 0, 2]], [3, 2])
        9
        >>> solve([5, 2], [[10, 2, 2], [12, 3, 0, 1]], [3, 2])
        12
    """
    memo: dict[tuple[int, ...], int] = {}

    def get_min_cost(current_needs: tuple[int, ...]) -> int:
        # If we have already computed the cost for this specific need state, return it
        if current_needs in memo:
            return memo[current_needs]

        # Base case: Calculate cost using only individual item prices
        # This serves as the upper bound for our recursion
        min_total_cost = sum(
            current_needs[i] * price[i] for i in range(len(price))
        )

        # Try applying each special offer
        for offer in special:
            offer_cost = offer[0]
            offer_items = offer[1:]
            
            # Check if the offer is valid (we cannot exceed the current needs)
            can_use_offer = True
            new_needs_list = list(current_needs)
            for i in range(len(current_needs)):
                if offer_items[i] > current_needs[i]:
                    can_use_offer = False
                    break
                new_needs_list[i] -= offer_items[i]
            
            # If valid, recurse with the updated needs
            if can_use_offer:
                min_total_cost = min(
                    min_total_cost, 
                    offer_cost + get_min_cost(tuple(new_needs_list))
                )

        memo[current_needs] = min_total_cost
        return min_total_cost

    # Convert list to tuple to make it hashable for the memoization dictionary
    return get_min_cost(tuple(needs))
