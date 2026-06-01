METADATA = {
    "id": 319,
    "name": "Bulb Switcher",
    "slug": "bulb-switcher",
    "category": "Math",
    "aliases": [],
    "tags": ["math", "brainteaser"],
    "difficulty": "easy",
    "time_complexity": "O(1)",
    "space_complexity": "O(1)",
    "description": "Determine how many bulbs remain on after n rounds of toggling.",
}

def solve(n: int) -> int:
    """
    Calculates the number of bulbs that remain on after n rounds of toggling.

    A bulb at position i is toggled in every round that is a divisor of i.
    A bulb remains ON if it is toggled an odd number of times.
    A number has an odd number of divisors if and only if it is a perfect square.
    Therefore, the number of bulbs remaining ON is the count of perfect squares 
    less than or equal to n.

    Args:
        n (int): The total number of bulbs.

    Returns:
        int: The number of bulbs that remain ON.

    Examples:
        >>> solve(3)
        1
        >>> solve(8)
        2
    """
    # A bulb stays on if it is toggled an odd number of times.
    # Only perfect squares have an odd number of divisors.
    # The number of perfect squares up to n is the integer part of sqrt(n).
    
    if n < 0:
        return 0
        
    # Using integer square root to find the count of perfect squares <= n
    # Example: n=8, sqrt(8) is ~2.82, floor is 2 (squares are 1, 4)
    return int(n**0.5)
