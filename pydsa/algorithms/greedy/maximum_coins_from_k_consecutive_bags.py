METADATA = {
    "id": 3413,
    "name": "Maximum Coins From K Consecutive Bags",
    "slug": "maximum-coins-from-k-consecutive-bags",
    "category": "Greedy",
    "aliases": [],
    "tags": ["greedy", "sorting"],
    "difficulty": "medium",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(1)",
    "description": "Maximize the total coins collected by picking k consecutive bags using a greedy approach with sorted values.",
}

def solve(bags: list[int], k: int) -> int:
    """
    Args:
        bags: A list of integers representing the number of coins in each bag.
        k: The number of consecutive bags to pick.

    Returns:
        The maximum number of coins that can be collected.
    """
    bags.sort()
    n = len(bags)
    max_coins = 0
    
    left_pointer = 0
    right_pointer = n - 1
    
    for i in range(k):
        if i % 2 == 0:
            max_coins += bags[right_pointer] - bags[left_pointer]
            right_pointer -= 1
        else:
            max_coins += bags[right_pointer] - bags[left_pointer]
            left_pointer += 1
            
    return max_coins

def solve_optimal(bags: list[int], k: int) -> int:
    """
    Args:
        bags: A list of integers representing the number of coins in each bag.
        k: The number of consecutive bags to pick.

    Returns:
        The maximum number of coins that can be collected.
    """
    bags.sort()
    n = len(bags)
    max_coins = 0
    
    left = 0
    right = n - 1
    
    for i in range(k):
        if i % 2 == 0:
            max_coins += bags[right] - bags[left]
            right -= 1
        else:
            max_coins += bags[right] - bags[left]
            left += 1
            
    return max_coins

def solve(bags: list[int], k: int) -> int:
    """
    Args:
        bags: A list of integers representing the number of coins in each bag.
        k: The number of consecutive bags to pick.

    Returns:
        The maximum number of coins that can be collected.
    """
    bags.sort()
    n = len(bags)
    total_coins = 0
    
    left_index = 0
    right_index = n - 1
    
    for i in range(k):
        if i % 2 == 0:
            total_coins += bags[right_index] - bags[left_index]
            right_index -= 1
        else:
            total_coins += bags[right_index] - bags[left_index]
            left_index += 1
            
    return total_coins