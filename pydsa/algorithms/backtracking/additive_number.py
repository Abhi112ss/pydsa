METADATA = {
    "id": 306,
    "name": "Additive Number",
    "slug": "additive-number",
    "category": "String",
    "aliases": [],
    "tags": ["recursion", "string", "backtracking"],
    "difficulty": "hard",
    "time_complexity": "O(n^3)",
    "space_complexity": "O(n)",
    "description": "Determine if a string can be split into a sequence of numbers where each subsequent number is the sum of the previous two.",
}

def solve(num: str) -> bool:
    """
    Determines if the input string represents an additive number sequence.

    An additive number is a string that can be split into a sequence of 
    non-negative integers such that each subsequent number is the sum of 
    the previous two.

    Args:
        num: The input string to validate.

    Returns:
        True if the string is an additive number, False otherwise.

    Examples:
        >>> solve("112358")
        True
        >>> solve("199100199")
        True
        >>> solve("1023")
        False
    """
    n = len(num)
    if n < 3:
        return False

    def is_valid_number(s: str) -> bool:
        """Checks if a string is a valid non-negative integer without leading zeros."""
        if len(s) > 1 and s[0] == '0':
            return False
        return True

    def backtrack(idx: int, num1: int, num2: int) -> bool:
        """
        Recursively validates the rest of the string.

        Args:
            idx: The current index in the string we are checking from.
            num1: The first number of the current pair.
            num2: The second number of the current pair.

        Returns:
            True if the remaining string follows the additive rule.
        """
        if idx == n:
            # If we reached the end of the string, the sequence is valid
            return True

        target_sum = num1 + num2
        target_str = str(target_sum)
        
        # Check if the remaining string starts with the required sum
        if not num.startswith(target_str, idx):
            return False
        
        # Move forward: the new pair is (num2, target_sum)
        return backtrack(idx + len(target_str), num2, target_sum)

    # Iterate through all possible lengths for the first two numbers
    # i is the end index of the first number, j is the end index of the second number
    for i in range(1, n):
        for j in range(i + 1, n):
            s1 = num[:i]
            s2 = num[i:j]

            # Validate leading zeros for the first two numbers
            if not is_valid_number(s1) or not is_valid_number(s2):
                continue

            val1 = int(s1)
            val2 = int(s2)

            # Start the recursive validation from the end of the second number
            if backtrack(j, val1, val2):
                return True

    return False
