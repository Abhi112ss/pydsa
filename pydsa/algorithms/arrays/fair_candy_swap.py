METADATA = {
    "id": 888,
    "name": "Fair Candy Swap",
    "slug": "fair-candy-swap",
    "category": "Math",
    "aliases": [],
    "tags": ["hash_set", "math"],
    "difficulty": "easy",
    "time_complexity": "O(n + m)",
    "space_complexity": "O(m)",
    "description": "Find two candy bars, one from each person, such that after swapping them, both people have the same total amount of candy.",
}

def solve(alice_candies: list[int], bob_candies: list[int]) -> int:
    """
    Args:
        alice_candies: A list of integers representing the candy amounts Alice has.
        bob_candies: A list of integers representing the candy amounts Bob has.

    Returns:
        The integer value of the candy Alice should swap with Bob.
    """
    sum_alice = sum(alice_candies)
    sum_bob = sum(bob_candies)
    set_bob = set(bob_candies)
    
    target_diff = (sum_alice - sum_bob) // 2
    
    for candy_alice in alice_candies:
        target_bob = candy_alice - target_diff
        if target_bob in set_bob:
            return candy_alice - target_diff
            
    return 0