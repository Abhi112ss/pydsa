METADATA = {
    "id": 3050,
    "name": "Pizza Toppings Cost Analysis",
    "slug": "pizza-toppings-cost-analysis",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dp", "bitmask", "greedy"],
    "difficulty": "medium",
    "time_complexity": "O(n * 2^k)",
    "space_complexity": "O(2^k)",
    "description": "Find the minimum cost to cover all required toppings using a subset of available topping combinations.",
}

def solve(toppings_required: list[int], topping_combinations: list[list[int]], combination_costs: list[int]) -> int:
    """
    Calculates the minimum cost to cover all required toppings using bitmask DP.

    Args:
        toppings_required: A list of integers representing the IDs of required toppings.
        topping_combinations: A list of lists, where each sub-list contains topping IDs 
            included in a specific combination.
        combination_costs: A list of costs corresponding to each combination in 
            topping_combinations.

    Returns:
        The minimum cost to cover all required toppings, or -1 if it is impossible.

    Examples:
        >>> solve([0, 1], [[0], [1], [0, 1]], [10, 10, 15])
        15
        >>> solve([0, 1, 2], [[0, 1], [1, 2]], [10, 10])
        20
        >>> solve([0, 1], [[0], [0]], [5, 10])
        5
    """
    num_required = len(toppings_required)
    if num_required == 0:
        return 0

    # Map the actual topping ID to a bit index (0 to num_required - 1)
    # This allows us to use a bitmask of size 2^num_required
    id_to_bit = {topping_id: i for i, topping_id in enumerate(toppings_required)}
    
    # Pre-calculate the bitmask for each combination
    # Only include toppings that are actually in the 'toppings_required' list
    combination_masks = []
    for combo in topping_combinations:
        mask = 0
        for topping in combo:
            if topping in id_to_bit:
                mask |= (1 << id_to_bit[topping])
        combination_masks.append(mask)

    # DP table: dp[mask] is the minimum cost to achieve the set of toppings represented by mask
    # Initialize with infinity
    inf = float('inf')
    num_states = 1 << num_required
    dp = [inf] * num_states
    dp[0] = 0

    # Iterate through each combination and update the DP table
    for i in range(len(combination_masks)):
        combo_mask = combination_masks[i]
        cost = combination_costs[i]
        
        # If the combination provides no required toppings, skip it
        if combo_mask == 0:
            continue
            
        # Update the DP table. We iterate through all existing reachable states.
        # To avoid using the same combination multiple times for the same state 
        # (if the problem implies combinations are single-use), we'd iterate backwards.
        # However, usually in these problems, you can pick combinations multiple times 
        # or they are distinct items. Given the structure, we treat them as distinct items.
        for current_mask in range(num_states - 1, -1, -1):
            if dp[current_mask] == inf:
                continue
            
            new_mask = current_mask | combo_mask
            if dp[new_mask] > dp[current_mask] + cost:
                dp[new_mask] = dp[current_mask] + cost

    result = dp[num_states - 1]
    return int(result) if result != inf else -1
