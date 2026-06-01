METADATA = {
    "id": 2048,
    "name": "Next Greater Numerically Balanced Number",
    "slug": "next-greater-numerically-balanced-number",
    "category": "Math",
    "aliases": [],
    "tags": ["math", "backtracking", "greedy"],
    "difficulty": "hard",
    "time_complexity": "O(log10(n))",
    "space_complexity": "O(log10(n))",
    "description": "Find the smallest numerically balanced number strictly greater than n.",
}

def solve(n: int) -> int:
    """
    Finds the smallest numerically balanced number strictly greater than n.
    A number is numerically balanced if it contains at most 3 occurrences of any digit.

    Args:
        n: The input integer.

    Returns:
        The smallest numerically balanced number greater than n.

    Examples:
        >>> solve(10)
        11
        >>> solve(123)
        124
        >>> solve(1000)
        1001
    """
    # Convert number to a list of digits for easier manipulation
    digits = [int(d) for d in str(n)]
    length = len(digits)

    def is_balanced(digit_counts: list[int]) -> bool:
        return all(count <= 3 for count in digit_counts)

    def find_next(index: int, current_counts: list[int], is_greater: bool) -> list[int] | None:
        """
        Backtracking function to construct the next valid number.
        
        Args:
            index: Current digit position being filled.
            current_counts: Frequency of each digit 0-9 used so far.
            is_greater: Boolean indicating if the number being built is already > n.
            
        Returns:
            A list of digits representing the valid number, or None if impossible.
        """
        if index == length:
            return []

        # Determine the starting digit for this position
        # If we are already greater than n, we can start from 0.
        # Otherwise, we must start from the digit at the current position in n.
        start_digit = 0 if is_greater else digits[index]

        for digit in range(start_digit, 10):
            # Check if adding this digit violates the 'at most 3' rule
            if current_counts[digit] < 3:
                new_is_greater = is_greater or (digit > digits[index])
                
                # Optimization: If we are not yet greater and we pick the same digit,
                # we must continue checking. If we pick a larger digit, we are now 'greater'.
                current_counts[digit] += 1
                result = find_next(index + 1, current_counts, new_is_greater)
                
                if result is not None:
                    return [digit] + result
                
                # Backtrack
                current_counts[digit] -= 1
        
        return None

    # 1. Try to find a balanced number with the same number of digits
    # We need to find a number STRICTLY greater than n.
    # To handle the "strictly greater" constraint in the backtracking, 
    # we can iterate through the digits and try to increment at the first possible position.
    
    # However, a simpler way to ensure "strictly greater" is to try to find 
    # the smallest balanced number >= n + 1.
    target_n = n + 1
    digits = [int(d) for d in str(target_n)]
    length = len(digits)

    # We use a slightly modified backtracking to find the smallest balanced number >= target_n
    def find_smallest_ge(index: int, current_counts: list[int], is_greater: bool) -> list[int] | None:
        if index == length:
            return []

        start_digit = 0 if is_greater else digits[index]

        for digit in range(start_digit, 10):
            if current_counts[digit] < 3:
                new_is_greater = is_greater or (digit > digits[index])
                current_counts[digit] += 1
                res = find_smallest_ge(index + 1, current_counts, new_is_greater)
                if res is not None:
                    return [digit] + res
                current_counts[digit] -= 1
        return None

    # Attempt to find a number with the same number of digits
    counts = [0] * 10
    result_digits = find_smallest_ge(0, counts, False)

    if result_digits:
        return int("".join(map(str, result_digits)))

    # 2. If no number with the same length is found, the next balanced number 
    # will be the smallest balanced number with length + 1 digits.
    # The smallest number with length + 1 digits is 1 followed by 0s.
    # e.g., for length 3, next is 1000.
    new_length = length + 1
    new_digits = [1] + [0] * (new_length - 1)
    
    # Since 100...0 is always balanced (at most 3 of any digit for reasonable lengths),
    # we just need to check if it's valid. For very large numbers, we'd need to 
    # construct it carefully, but for LeetCode constraints, 100...0 is fine.
    # A number like 1111... would fail, but 1000... is always valid.
    return int("".join(map(str, new_digits)))
