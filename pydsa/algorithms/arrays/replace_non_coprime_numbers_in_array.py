METADATA = {
    "id": 2197,
    "name": "Replace Non-Coprime Numbers in Array",
    "slug": "replace-non-coprime-numbers-in-array",
    "category": "Stack",
    "aliases": [],
    "tags": ["stack", "math", "greedy"],
    "difficulty": "hard",
    "time_complexity": "O(n * log(max_val))",
    "space_complexity": "O(n)",
    "description": "Replace adjacent non-coprime numbers in an array with their greatest common divisor until all adjacent elements are coprime.",
}

import math

def solve(nums: list[int]) -> list[int]:
    """
    Replaces adjacent non-coprime numbers in the array with their GCD.
    
    The algorithm uses a stack to maintain a sequence of numbers that are 
    pairwise coprime. When a new number is encountered, it is compared 
    with the top of the stack. If they are not coprime, they are replaced 
    by their GCD, and this process repeats with the new GCD and the 
    new top of the stack.

    Args:
        nums: A list of integers.

    Returns:
        A list of integers where all adjacent elements are coprime.

    Examples:
        >>> solve([2, 6, 3, 4])
        [1, 1, 4]
        >>> solve([10, 5, 2, 11])
        [5, 2, 11]
    """
    stack: list[int] = []

    for current_num in nums:
        # While the stack is not empty and the current number shares a 
        # common divisor > 1 with the top of the stack
        while stack and math.gcd(stack[-1], current_num) > 1:
            # Replace the current number with the GCD of itself and the stack top
            current_num = math.gcd(stack[-1], current_num)
            # Pop the stack top as it has been merged into the current_num
            stack.pop()
        
        # Push the resulting number (which is now coprime to the new stack top)
        stack.append(current_num)

    return stack
