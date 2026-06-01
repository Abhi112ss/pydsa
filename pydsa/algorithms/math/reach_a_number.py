METADATA = {
    "id": 754,
    "name": "Reach a Number",
    "slug": "reach-a-number",
    "category": "Math",
    "aliases": [],
    "tags": ["math", "binary_search"],
    "difficulty": "medium",
    "time_complexity": "O(sqrt(target))",
    "space_complexity": "O(1)",
    "description": "Find the minimum number of steps to reach a target integer starting from 0, where each step i can be added or subtracted.",
}

def solve(target: int) -> int:
    """
    Finds the minimum number of steps to reach a target integer.
    
    In each step i (starting from 1), we can either add i or subtract i.
    The goal is to find the smallest n such that we can reach the target.
    
    The logic follows:
    1. We need the cumulative sum (1 + 2 + ... + n) to be at least the target.
    2. Let S = sum(1..n). If S == target, we are done.
    3. If S > target, we need to change the sign of some number 'k' in the sum.
       Changing +k to -k reduces the total sum by 2*k.
    4. Therefore, the difference (S - target) must be even so that we can 
       find an integer k = (S - target) / 2 to flip.

    Args:
        target: The target integer to reach.

    Returns:
        The minimum number of steps required.

    Examples:
        >>> solve(3)
        2
        >>> solve(2)
        3
        >>> solve(10)
        4
    """
    # We work with the absolute value because the problem is symmetric
    # reaching -target is the same as reaching target.
    target = abs(target)
    
    current_sum = 0
    step = 0
    
    # Step 1: Find the smallest n such that sum(1..n) >= target
    while current_sum < target:
        step += 1
        current_sum += step
        
    # Step 2: Check if the difference (current_sum - target) is even.
    # If it is odd, we cannot flip a single number 'k' to reach the target
    # because flipping k changes the sum by 2*k (an even amount).
    # We keep adding steps until the difference becomes even.
    while (current_sum - target) % 2 != 0:
        step += 1
        current_sum += step
        
    return step
