METADATA = {
    "id": 1999,
    "name": "Smallest Greater Multiple Made of Two Digits",
    "slug": "smallest-greater-multiple-made-of-two-digits",
    "category": "Math",
    "aliases": [],
    "tags": ["math", "greedy"],
    "difficulty": "medium",
    "time_complexity": "O(1)",
    "space_complexity": "O(1)",
    "description": "Find the smallest multiple of a given number that consists only of two specific digits.",
}

def solve(num: int, digit1: int, digit2: int) -> int:
    """
    Args:
        num: The divisor.
        digit1: The first allowed digit.
        digit2: The second allowed digit.

    Returns:
        The smallest multiple of num consisting only of digit1 and digit2.
    """
    digits = sorted([digit1, digit2])
    queue = []
    
    if digits[0] > 0:
        queue.append(digits[0])
    queue.append(digits[1])
    
    index = 0
    while index < len(queue):
        current_val = queue[index]
        index += 1
        
        if current_val % num == 0:
            return current_val
        
        next_val_1 = current_val * 10 + digits[0]
        next_val_2 = current_val * 10 + digits[1]
        
        queue.append(next_val_1)
        queue.append(next_val_2)
        
    return -1