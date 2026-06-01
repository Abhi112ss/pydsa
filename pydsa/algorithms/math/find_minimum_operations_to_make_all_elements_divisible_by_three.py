METADATA = {
    "id": 3190,
    "name": "Find Minimum Operations to Make All Elements Divisible by Three",
    "slug": "find-minimum-operations-to-make-all-elements-divisible-by-three",
    "category": "Math",
    "aliases": [],
    "tags": ["math", "greedy"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Calculate the minimum number of operations to make every element in an array divisible by three by adding or subtracting one.",
}

def solve(nums: list[int]) -> int:
    """
    Calculates the minimum number of operations to make all elements in the list divisible by 3.
    
    An operation consists of adding or subtracting 1 from an element.
    An element is divisible by 3 if num % 3 == 0.
    If num % 3 == 1, we can subtract 1 (1 operation).
    If num % 3 == 2, we can add 1 (1 operation).

    Args:
        nums: A list of integers.

    Returns:
        The minimum number of operations required.

    Examples:
        >>> solve([1, 2, 3, 4])
        3
        >>> solve([3, 6, 9])
        0
        >>> solve([1, 1, 1])
        3
    """
    operations_count = 0
    
    for number in nums:
        # Check the remainder when divided by 3
        remainder = number % 3
        
        # If the remainder is not 0, it takes exactly 1 operation 
        # to make the number divisible by 3 (either +1 or -1).
        if remainder != 0:
            operations_count += 1
            
    return operations_count
