METADATA = {
    "id": 948,
    "name": "Bag of Tokens",
    "slug": "bag-of-tokens",
    "category": "Greedy",
    "aliases": [],
    "tags": ["two_pointer", "greedy", "sorting"],
    "difficulty": "medium",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(1)",
    "description": "Maximize score by strategically exchanging power for score and vice versa using a two-pointer approach on sorted tokens.",
}

def solve(power: int, alist: list[int], score: int, target: int) -> int:
    """
    Calculates the maximum score achievable given a starting power and a list of tokens.

    Args:
        power: The initial amount of power available.
        alist: A list of integers representing the power required for each token.
        score: The initial score.
        target: The target score to reach.

    Returns:
        The maximum score achievable, capped at the target.

    Examples:
        >>> solve(100, [100, 200, 300], 0, 1)
        1
        >>> solve(100, [100, 200, 300], 0, 2)
        1
        >>> solve(100, [100, 200, 300], 0, 4)
        1
    """
    if target <= 0:
        return 0

    # Sort tokens to allow greedy selection: 
    # Smallest power for maximum score gain, largest power for minimum power loss.
    alist.sort()
    
    left_index = 0
    right_index = len(alist) - 1
    current_score = score
    current_power = power

    while left_index <= right_index:
        # Case 1: We have enough power to buy the cheapest token to increase score
        if current_power >= alist[left_index]:
            current_power -= alist[left_index]
            current_score += 1
            left_index += 1
            
            # Check if we reached the target immediately after gaining score
            if current_score >= target:
                return target
        
        # Case 2: We don't have enough power to buy, but we can sell the most expensive 
        # token to gain power, provided there's at least one more token to buy later.
        elif left_index < right_index and current_power + alist[right_index] >= 0:
            # Note: The problem implies we only sell if it helps us buy more tokens.
            # If left_index == right_index, selling won't help us buy anything else.
            current_power += alist[right_index]
            current_score -= 1
            right_index -= 1
        
        # Case 3: Cannot buy and cannot profitably sell to gain more score later
        else:
            break

    return min(current_score, target)
