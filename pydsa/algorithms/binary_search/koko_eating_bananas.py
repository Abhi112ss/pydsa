METADATA = {
    "id": 875,
    "name": "Koko Eating Bananas",
    "slug": "koko-eating-bananas",
    "category": "Binary Search",
    "aliases": [],
    "tags": ["binary_search", "greedy"],
    "difficulty": "medium",
    "time_complexity": "O(n log m)",
    "space_complexity": "O(1)",
    "description": "Find the minimum integer speed k such that Koko can eat all bananas within h hours.",
}

import math

def solve(piles: list[int], h: int) -> int:
    """
    Finds the minimum integer speed k such that Koko can eat all bananas within h hours.

    Args:
        piles: A list of integers where piles[i] is the number of bananas in the i-th pile.
        h: The maximum number of hours Koko has to eat all the bananas.

    Returns:
        The minimum integer speed k (bananas per hour).

    Examples:
        >>> solve([3, 6, 7, 11], 8)
        4
        >>> solve([30, 11, 23, 4, 20], 5)
        30
        >>> solve([30, 11, 23, 4, 20], 6)
        23
    """
    
    def can_finish(speed: int) -> bool:
        """Helper to check if a given speed allows Koko to finish within h hours."""
        total_hours_needed = 0
        for pile in piles:
            # math.ceil(pile / speed) calculates hours needed for one pile
            # Using integer arithmetic: (pile + speed - 1) // speed
            total_hours_needed += (pile + speed - 1) // speed
            if total_hours_needed > h:
                return False
        return total_hours_needed <= h

    # The minimum possible speed is 1 banana per hour.
    # The maximum necessary speed is the size of the largest pile.
    low = 1
    high = max(piles)
    result = high

    # Binary search over the range of possible speeds [1, max(piles)]
    while low <= high:
        mid_speed = (low + high) // 2
        
        if can_finish(mid_speed):
            # If Koko can finish at this speed, try a slower speed to find the minimum
            result = mid_speed
            high = mid_speed - 1
        else:
            # If Koko cannot finish, she must eat faster
            low = mid_speed + 1
            
    return result
