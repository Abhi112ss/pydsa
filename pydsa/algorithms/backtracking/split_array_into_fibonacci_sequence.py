METADATA = {
    "id": 842,
    "name": "Split Array into Fibonacci Sequence",
    "slug": "split-array-into-fibonacci-sequence",
    "category": "Backtracking",
    "aliases": [],
    "tags": ["recursion", "string_manipulation", "backtracking"],
    "difficulty": "medium",
    "time_complexity": "O(2^n)",
    "space_complexity": "O(n)",
    "description": "Determine if a string can be split into a Fibonacci-like sequence of integers.",
}

def solve(digits: str) -> list[int]:
    """
    Splits a string of digits into a Fibonacci-like sequence.

    A Fibonacci-like sequence is a sequence where each number (starting from the 
    third) is the sum of the previous two. All numbers must be non-negative 
    and cannot have leading zeros unless the number is exactly '0'.

    Args:
        digits: A string containing only digits.

    Returns:
        A list of integers representing the Fibonacci sequence if one exists, 
        otherwise an empty list.

    Examples:
        >>> solve("112358")
        [1, 1, 2, 3, 5, 8]
        >>> solve("123258")
        []
    """
    n = len(digits)
    result: list[int] = []

    def is_valid_number(s: str) -> bool:
        """Checks if a string is a valid non-negative integer without leading zeros."""
        if not s:
            return False
        # Leading zero check: if length > 1 and starts with '0', it's invalid
        if len(s) > 1 and s[0] == '0':
            return False
        # Check for integer overflow (though Python handles large ints, 
        # the problem constraints usually imply 32-bit signed integer limits)
        try:
            val = int(s)
            return val <= 2**31 - 1
        except ValueError:
            return False

    def backtrack(index: int) -> bool:
        """
        Recursive backtracking function to find the sequence.

        Args:
            index: The current starting position in the digits string.

        Returns:
            True if a valid sequence is found from this index, False otherwise.
        """
        # Base case: if we reached the end of the string and have at least 3 numbers
        if index == n:
            return len(result) >= 3

        # Try all possible lengths for the next number in the sequence
        for end in range(index + 1, n + 1):
            current_str = digits[index:end]
            
            # Check for leading zeros or integer overflow
            if not is_valid_number(current_str):
                # If we encounter a leading zero (e.g., "05"), 
                # we cannot extend this specific number further.
                break
            
            current_val = int(current_str)
            
            # Fibonacci constraint check
            if len(result) >= 2:
                expected_sum = result[-1] + result[-2]
                if current_val < expected_sum:
                    # Current number is too small, try a longer string
                    continue
                if current_val > expected_sum:
                    # Current number is already too large, no point in extending
                    break
            
            # If valid, add to sequence and recurse
            result.append(current_val)
            if backtrack(end):
                return True
            
            # Backtrack: remove the last added number
            result.pop()
            
        return False

    # Start the backtracking process from index 0
    if backtrack(0):
        return result
    return []
