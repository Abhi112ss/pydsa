METADATA = {
    "id": 1058,
    "name": "Minimize Rounding Error to Meet Target",
    "slug": "minimize-rounding-error-to-meet-target",
    "category": "Greedy",
    "aliases": [],
    "tags": ["greedy", "math", "sorting"],
    "difficulty": "medium",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(n)",
    "description": "Minimize the total rounding error when rounding elements to integers to reach a target sum.",
}

def solve(nums: list[float], target: int) -> int:
    """
    Minimizes the total rounding error to reach a target sum by rounding elements.

    The strategy is to first round all numbers down to their floor values. 
    Then, calculate the remaining difference needed to reach the target. 
    To minimize error, we greedily pick elements that have the largest 
    fractional parts to round up, as these elements contribute the least 
    additional error when moving from floor to ceiling.

    Args:
        nums: A list of floating point numbers.
        target: The target integer sum to reach.

    Returns:
        The minimum total absolute rounding error.

    Examples:
        >>> solve([1.2, 2.8, 3.5], 7)
        1.5
        >>> solve([1.1, 1.1, 1.1], 4)
        0.9
    """
    import math

    # Step 1: Calculate the floor of each number and the initial sum
    # Also track the fractional parts to decide which ones to round up
    floors = []
    fractional_parts = []
    current_sum = 0
    
    for num in nums:
        floor_val = math.floor(num)
        floors.append(floor_val)
        # The error added by rounding down is (num - floor_val)
        # The error added by rounding up is (ceil_val - num)
        # However, the problem asks for the sum of |rounded_val - original_val|
        # Let's track the fractional part to identify the "cheapest" elements to round up
        fractional_parts.append(num - floor_val)
        current_sum += floor_val

    # Step 2: Determine how many elements must be rounded up
    # Each element we round up increases the current_sum by exactly 1
    needed_ups = target - current_sum
    
    # If target is less than the sum of floors, it's impossible under standard 
    # rounding rules (though problem constraints usually imply target >= sum(floors))
    # If target > sum(ceilings), it's also impossible.
    # Based on problem logic, we assume target is reachable.
    
    # Step 3: Sort fractional parts in descending order.
    # Elements with large fractional parts are "closer" to their ceiling.
    # Rounding them up results in a smaller error contribution relative to the floor.
    # Actually, the error for floor is (num - floor).
    # The error for ceil is (ceil - num).
    # Total error = sum(abs(rounded[i] - nums[i]))
    
    # Let's refine the error calculation:
    # If we round DOWN: error = num - floor
    # If we round UP: error = ceil - num = (floor + 1) - num
    
    # We start by assuming everything is rounded DOWN.
    # Initial error = sum(num - floor)
    total_error = sum(fractional_parts)
    
    # If we change an element from floor to ceil:
    # New error = (old_error - (num - floor)) + (ceil - num)
    # New error = old_error - (num - floor) + (1 - (num - floor))
    # New error = old_error - 2 * (num - floor) + 1
    # Change in error = 1 - 2 * (num - floor)
    
    # To minimize total error, we want the most negative 'change in error'.
    # This happens when (num - floor) is as large as possible.
    
    # Sort fractional parts descending to pick the largest ones to round up
    fractional_parts.sort(reverse=True)
    
    # Step 4: Apply the 'needed_ups' to the elements with largest fractional parts
    for i in range(needed_ups):
        # Subtract the difference between rounding down and rounding up
        # Error change = (1 - frac) - frac = 1 - 2*frac
        total_error += (1 - 2 * fractional_parts[i])
        
    return round(total_error)
