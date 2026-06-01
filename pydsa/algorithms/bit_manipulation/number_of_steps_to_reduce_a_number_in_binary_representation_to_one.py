METADATA = {
    "id": 1404,
    "name": "Number of Steps to Reduce a Number in Binary Representation to One",
    "slug": "number-of-steps-to-reduce-a-number-in-binary-representation-to-one",
    "category": "Bit Manipulation",
    "aliases": [],
    "tags": ["bit manipulation", "math"],
    "difficulty": "medium",
    "time_complexity": "O(log n)",
    "space_complexity": "O(1)",
    "description": "Calculate the number of steps to reduce a number to one by dividing by two if even or subtracting one if odd.",
}

def solve(num: int) -> int:
    """
    Calculates the number of steps to reduce a number to one.
    
    The rules are:
    - If the current number is even, divide it by two.
    - If the current number is odd, subtract one from it.

    Args:
        num: The integer to reduce.

    Returns:
        The total number of steps taken to reach one.

    Examples:
        >>> solve(14)
        6
        >>> solve(8)
        3
    """
    if num <= 1:
        return 0

    # The problem can be viewed bitwise:
    # 1. Dividing an even number by 2 is a right shift (removes a trailing 0).
    # 2. Subtracting 1 from an odd number turns a 1 into a 0.
    # Total steps = (number of bits to shift) + (number of 1s to flip to 0).
    # We stop when we reach 1, so we don't count the final '1' bit.
    
    steps = 0
    while num > 1:
        if num % 2 == 0:
            # Even: divide by 2 (right shift)
            num //= 2
        else:
            # Odd: subtract 1
            num -= 1
        steps += 1
        
    return steps
