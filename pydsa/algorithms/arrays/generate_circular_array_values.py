METADATA = {
    "id": 2757,
    "name": "Generate Circular Array Values",
    "slug": "generate-circular-array-values",
    "category": "Simulation",
    "aliases": [],
    "tags": ["arrays", "simulation"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Generate an array of length n starting from nums[0], following a circular pattern of incrementing and decrementing indices.",
}

def solve(nums: list[int], n: int) -> list[int]:
    """
    Generates a circular array of length n based on the rules:
    1. Start with nums[0].
    2. The next index is (current_index + 1) % len(nums).
    3. The following index is (current_index - 1) % len(nums).
    4. Repeat the pattern of +1, -1, +1, -1...

    Args:
        nums: The source array of integers.
        n: The desired length of the resulting array.

    Returns:
        A list of n integers generated following the circular pattern.

    Examples:
        >>> solve([1, 2, 3], 5)
        [1, 2, 1, 2, 1]
        >>> solve([1, 2, 3, 4, 5, 6], 4)
        [1, 2, 1, 2]
    """
    result: list[int] = []
    num_len = len(nums)
    current_index = 0
    
    # direction: 1 for incrementing, -1 for decrementing
    direction = 1
    
    for _ in range(n):
        # Append the value at the current circular index
        result.append(nums[current_index])
        
        # Calculate the next index using modulo to ensure circularity
        # We add num_len before modulo to handle negative results from -1
        current_index = (current_index + direction) % num_len
        
        # Flip the direction for the next step
        direction *= -1
        
    return result
