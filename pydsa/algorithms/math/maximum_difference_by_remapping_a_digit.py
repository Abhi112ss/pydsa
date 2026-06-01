METADATA = {
    "id": 2566,
    "name": "Maximum Difference by Remapping a Digit",
    "slug": "maximum-difference-by-remapping-a-digit",
    "category": "Math",
    "aliases": [],
    "tags": ["greedy", "math"],
    "difficulty": "medium",
    "time_complexity": "O(log(max(num1, num2)))",
    "space_complexity": "O(1)",
    "description": "Maximize the difference between two numbers by remapping exactly one digit in each number.",
}

def solve(num1: int, num2: int) -> int:
    """
    Calculates the maximum possible difference between two numbers by remapping 
    exactly one digit in each number.

    To maximize (A - B), we want to make A as large as possible and B as small as possible.
    - For the larger number, we find the first digit (from left to right) that is not '9' 
      and change it to '9'.
    - For the smaller number, we find the first digit (from left to right) that is not '0' 
      and change it to '0'.

    Args:
        num1: The first integer.
        num2: The second integer.

    Returns:
        The maximum possible difference between the two numbers.

    Examples:
        >>> solve(123, 456)
        873
        # num1 becomes 923, num2 becomes 056 (or 456 -> 056 is not allowed, 
        # but the logic is to change the first non-zero digit to 0)
        # Actually, the rule is: change one digit in num1 and one in num2.
        # To maximize num1 - num2:
        # If num1 > num2: num1 -> change first non-9 to 9, num2 -> change first non-0 to 0.
        # If num2 > num1: num2 -> change first non-9 to 9, num1 -> change first non-0 to 0.
    """
    
    def remap_to_maximize(n: int) -> int:
        """Changes the first digit that is not 9 to 9."""
        s = list(str(n))
        for i in range(len(s)):
            if s[i] != '9':
                s[i] = '9'
                break
        return int("".join(s))

    def remap_to_minimize(n: int) -> int:
        """Changes the first digit that is not 0 to 0."""
        s = list(str(n))
        for i in range(len(s)):
            if s[i] != '0':
                s[i] = '0'
                break
        return int("".join(s))

    # Determine which number should be the 'large' one and which the 'small' one
    # to maximize the absolute difference.
    if num1 > num2:
        # Maximize num1, minimize num2
        new_num1 = remap_to_maximize(num1)
        new_num2 = remap_to_minimize(num2)
        return new_num1 - new_num2
    else:
        # Maximize num2, minimize num1
        new_num2 = remap_to_maximize(num2)
        new_num1 = remap_to_minimize(num1)
        return new_num2 - new_num1
