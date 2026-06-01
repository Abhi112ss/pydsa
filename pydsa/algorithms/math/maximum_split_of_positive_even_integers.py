METADATA = {
    "id": 2178,
    "name": "Maximum Split of Positive Even Integers",
    "slug": "maximum-split-of-positive-even-integers",
    "category": "Math",
    "aliases": [],
    "tags": ["math", "greedy"],
    "difficulty": "medium",
    "time_complexity": "O(log n)",
    "space_complexity": "O(1)",
    "description": "Find the maximum number of splits of a positive even integer such that every split is a positive even integer.",
}

def solve(n: int) -> int:
    """
    Calculates the maximum number of splits of a positive even integer n 
    such that every split is a positive even integer.

    The problem can be reduced to finding how many times n can be divided 
    by 2 while maintaining the property that the resulting parts are even.
    Essentially, we are looking for the exponent of the largest power of 2 
    that divides n.

    Args:
        n: A positive even integer.

    Returns:
        The maximum number of splits possible.

    Examples:
        >>> solve(2)
        1
        >>> solve(6)
        1
        >>> solve(8)
        3
        >>> solve(12)
        2
    """
    if n % 2 != 0:
        return 0

    splits = 0
    # We want to split n into as many even numbers as possible.
    # The most efficient way to split an even number into even numbers 
    # is to repeatedly divide by 2. 
    # For example, 8 -> 4, 4 -> 2, 2, 2 -> 2, 2, 2, 2.
    # The number of pieces will be the largest k such that 2^k divides n.
    # However, the question asks for the number of splits (pieces).
    # If n = 2^k * odd_number, we can split it into 2^k pieces of (odd_number * 2^0) 
    # but those aren't all even. 
    # Actually, the logic is: if we divide n by 2, we get two parts. 
    # If we can divide those parts again, we keep going.
    # The maximum number of even parts is the count of factors of 2 in n.
    
    while n > 0 and n % 2 == 0:
        splits += 1
        n //= 2
        
    return splits
