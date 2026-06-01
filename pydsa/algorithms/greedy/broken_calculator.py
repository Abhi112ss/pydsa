METADATA = {
    "id": 991,
    "name": "Broken Calculator",
    "slug": "broken-calculator",
    "category": "Math",
    "aliases": [],
    "tags": ["greedy", "math"],
    "difficulty": "medium",
    "time_complexity": "O(log target)",
    "space_complexity": "O(1)",
    "description": "Find the minimum number of operations to reach a target value using only multiplication by 2 and subtraction of 1.",
}

def solve(multiplier: int, target: int) -> int:
    """
    Calculates the minimum number of operations to reach the target value.
    
    The strategy is to work backwards from the target to the multiplier.
    If the target is divisible by the multiplier, we divide it (which is the 
    inverse of multiplication). If it is not, we add 1 (the inverse of subtraction).
    This greedy approach is optimal because dividing reduces the number much 
    faster than subtracting.

    Args:
        multiplier (int): The factor used for multiplication operations.
        target (int): The target value to reach.

    Returns:
        int: The minimum number of operations required.

    Examples:
        >>> solve(2, 5)
        3
        # 5 -> 4 -> 2 -> 1 (3 steps)
        >>> solve(3, 10)
        3
        # 10 -> 9 -> 3 -> 1 (3 steps)
    """
    operations_count = 0
    
    # Work backwards from target to multiplier
    while target > multiplier:
        operations_count += 1
        if target % multiplier == 0:
            # If divisible, perform the inverse of multiplication
            target //= multiplier
        else:
            # If not divisible, perform the inverse of subtraction
            target += 1
            
    # After the loop, target is <= multiplier.
    # The only way to reach the target from the multiplier is through subtraction.
    # The number of subtractions needed is (multiplier - target).
    # However, since we are working backwards, we are actually adding 1s 
    # to reach the multiplier from the target.
    return operations_count + (multiplier - target)
