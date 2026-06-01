METADATA = {
    "id": 1561,
    "name": "Maximum Number of Coins You Can Get",
    "slug": "maximum-number-of-coins-you-can-get",
    "category": "Greedy",
    "aliases": [],
    "tags": ["greedy", "sorting"],
    "difficulty": "medium",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(1)",
    "description": "Maximize the sum of coins collected by picking the second largest element from every triplet of piles.",
}

def solve(coins: list[int]) -> int:
    """
    Calculates the maximum number of coins you can get by picking the second 
    largest element from every triplet of piles.

    The strategy is to sort the piles and then pick the second largest element 
    from the largest available pairs, effectively leaving the smallest elements 
    to be the 'third' element in each triplet.

    Args:
        coins: A list of integers representing the number of coins in each pile.

    Returns:
        The maximum sum of coins that can be collected.

    Examples:
        >>> solve([2, 4, 1, 2, 7, 8])
        13
        >>> solve([9, 1, 9, 1, 9])
        18
    """
    # Sort the coins in ascending order to easily pick largest and smallest
    coins.sort()
    
    total_coins = 0
    n = len(coins)
    
    # We pick triplets. In each triplet, we want the second largest.
    # To maximize this, we pick the two largest available and the one smallest available.
    # The 'second largest' will be the one at index (n - 2), then (n - 4), etc.
    # We stop when we have picked n // 3 triplets.
    
    # Number of triplets we can form
    num_triplets = n // 3
    
    # Start from the second to last element and jump backwards by 2
    # This effectively skips the largest element (the one we 'give' to Alice)
    # and picks the second largest (the one we 'keep').
    current_index = n - 2
    for _ in range(num_triplets):
        total_coins += coins[current_index]
        current_index -= 2
        
    return total_coins
