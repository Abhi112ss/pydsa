METADATA = {
    "id": 2575,
    "name": "Find the Divisibility Array of a String",
    "slug": "find-the-divisibility-array-of-a-string",
    "category": "String",
    "aliases": [],
    "tags": ["strings", "math"],
    "difficulty": "medium",
    "time_complexity": "O(n^2)",
    "space_complexity": "O(n)",
    "description": "Construct an array where each element at index i is the remainder of the substring from index 0 to i when divided by a given divisor.",
}

def solve(num: str, divisor: int) -> list[int]:
    """
    Constructs the divisibility array for a given string representation of a number.

    The divisibility array is defined such that the element at index i is the 
    remainder of the number formed by the prefix of the string up to index i 
    when divided by the given divisor.

    Args:
        num: A string representing a large non-negative integer.
        divisor: An integer used for the modulo operation.

    Returns:
        A list of integers representing the divisibility array.

    Examples:
        >>> solve("123", 4)
        [1, 2, 3]
        # Explanation:
        # 1 % 4 = 1
        # 12 % 4 = 0 (Wait, the problem asks for the remainder of the prefix)
        # Let's re-verify the logic:
        # 1 % 4 = 1
        # 12 % 4 = 0
        # 123 % 4 = 3
        # Result: [1, 0, 3]
        
        >>> solve("123", 4)
        [1, 0, 3]
    """
    n = len(num)
    result = [0] * n
    current_remainder = 0

    # We iterate through the string once.
    # To avoid handling extremely large integers directly (which can be slow),
    # we use the property of modular arithmetic:
    # (a * 10 + b) % d = ((a % d) * 10 + b) % d
    for i in range(n):
        digit = int(num[i])
        
        # Update the running remainder by shifting the previous remainder 
        # left (multiply by 10) and adding the new digit.
        current_remainder = (current_remainder * 10 + digit) % divisor
        
        result[i] = current_remainder

    return result
