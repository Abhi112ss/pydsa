METADATA = {
    "id": 2376,
    "name": "Count Special Integers",
    "slug": "count-special-integers",
    "category": "Math",
    "aliases": [],
    "tags": ["digit_dp", "math", "combinatorics"],
    "difficulty": "hard",
    "time_complexity": "O(log(n))",
    "space_complexity": "O(log(n))",
    "description": "Count integers in the range [1, n] that have all unique digits.",
}

def solve(n: int) -> int:
    """
    Counts the number of special integers in the range [1, n].
    A special integer is an integer where all its digits are unique.

    Args:
        n: The upper bound integer.

    Returns:
        The count of special integers between 1 and n inclusive.

    Examples:
        >>> solve(20)
        19
        >>> solve(100)
        90
    """
    s_n = str(n)
    length = len(s_n)

    def count_permutations(n_digits: int, k_choices: int) -> int:
        """Calculates P(n_digits, k_choices) = n! / (n - k)!"""
        res = 1
        for i in range(k_choices):
            res *= (n_digits - i)
        return res

    total_count = 0

    # 1. Count all special integers with fewer digits than n
    # For a number with 'i' digits, the first digit has 9 choices (1-9),
    # and the remaining 'i-1' digits have P(9, i-1) choices.
    for i in range(1, length):
        total_count += 9 * count_permutations(9, i - 1)

    # 2. Count special integers with exactly 'length' digits using Digit DP logic
    used_digits = set()
    for i in range(length):
        digit = int(s_n[i])
        
        # Try placing a digit smaller than the current digit in s_n[i]
        # For the first position, we start from 1. For others, we start from 0.
        start_digit = 1 if i == 0 else 0
        for d in range(start_digit, digit):
            if d not in used_digits:
                # If we place 'd', we have (length - 1 - i) positions left to fill
                # and (10 - (i + 1)) available digits left to choose from.
                remaining_positions = length - 1 - i
                available_digits = 10 - (i + 1)
                total_count += count_permutations(available_digits, remaining_positions)
        
        # If the current digit is already used, we cannot form any more 
        # numbers that match the prefix of n, so we break.
        if digit in used_digits:
            break
        used_digits.add(digit)
        
        # If we reached the last digit and it's unique, n itself is a special integer
        if i == length - 1:
            total_count += 1

    return total_count
