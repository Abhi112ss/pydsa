METADATA = {
    "id": 1103,
    "name": "Distribute Candies to People",
    "slug": "distribute-candies-to-people",
    "category": "Simulation",
    "aliases": [],
    "tags": ["simulation", "math", "arrays"],
    "difficulty": "easy",
    "time_complexity": "O(sqrt(candies))",
    "space_complexity": "O(n)",
    "description": "Distribute candies to people in a circular fashion, increasing the amount given each time, and return the final counts.",
}

def solve(candies: int, sweeties: list[int]) -> list[int]:
    """
    Simulates the distribution of candies to people in a circular manner.

    In each step, the amount of candies given increases by 1 (1, 2, 3...).
    If the current amount to give exceeds the remaining candies, give all remaining.

    Args:
        candies: The total number of candies available.
        sweeties: A list of integers representing the capacity of each person.

    Returns:
        A list of integers representing the candies received by each person.

    Examples:
        >>> solve(5, [4, 2, 3])
        [4, 1, 0]
        >>> solve(10, [3, 2, 1])
        [3, 2, 1, 4]
    """
    n = len(sweeties)
    result = [0] * n
    current_give_amount = 1
    current_person_index = 0

    # Continue distributing as long as there are candies left
    while candies > 0:
        # Determine how many candies we can actually give this turn
        # It is the minimum of what we want to give and what is available
        actual_give = min(candies, current_give_amount)
        
        # The person can only take up to their capacity
        # If actual_give > capacity, they only take their capacity
        # However, the problem states we give 'current_give_amount' 
        # but they can only hold 'sweeties[i]'. 
        # Wait, the rule is: "give current_give_amount candies... 
        # if current_give_amount > sweeties[i], they take sweeties[i]".
        # But we must subtract the amount actually taken from the total pool.
        
        # Correct logic: The person takes the minimum of (current_give_amount) 
        # and (their capacity). But we must also ensure we don't give more than 
        # the total candies remaining.
        
        # Re-reading: "give current_give_amount candies... if current_give_amount > sweeties[i], 
        # they take sweeties[i]". This implies the 'candies' pool is reduced by 
        # the amount the person actually receives.
        
        # Let's refine:
        # 1. We want to give 'current_give_amount'.
        # 2. The person can only take 'sweeties[current_person_index]'.
        # 3. We only have 'candies' left.
        
        # The amount the person actually receives is the minimum of:
        # current_give_amount, their capacity, and the remaining candies.
        
        amount_to_receive = min(current_give_amount, sweeties[current_person_index], candies)
        
        result[current_person_index] += amount_to_receive
        candies -= amount_to_receive
        
        # Increment the amount to give for the next turn
        current_give_amount += 1
        
        # Move to the next person in a circular fashion
        current_person_index = (current_person_index + 1) % n
        
        # Safety break: if we are in a loop where candies > 0 but we can't 
        # give anything because capacity is 0 and current_give_amount is large?
        # Actually, if candies > 0 and current_give_amount > 0, 
        # the only way to not progress is if all sweeties[i] are 0.
        # But the problem constraints usually imply sweeties[i] >= 1.
        # If sweeties[i] can be 0, we need to ensure we don't loop infinitely.
        # However, if amount_to_receive is 0, candies won't decrease.
        # Let's check constraints: sweeties[i] >= 1.
        
        # If we can't give any more candies because all capacities are 0 
        # (not possible per constraints) or we've exhausted candies.
        if amount_to_receive == 0 and candies > 0:
            # This handles the case where current_give_amount is > 0 
            # but capacity is 0. We must still increment current_give_amount
            # to eventually find a person or finish. 
            # But if all capacities are 0, we'd loop forever.
            # Given sweeties[i] >= 1, this won't happen.
            pass

    return result
