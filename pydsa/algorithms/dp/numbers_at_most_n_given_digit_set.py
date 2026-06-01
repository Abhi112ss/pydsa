METADATA = {
    "id": 902,
    "name": "Numbers At Most N Given Digit Set",
    "slug": "numbers-at-most-n-given-digit-set",
    "category": "Math",
    "aliases": [],
    "tags": ["digit_dp", "math", "dynamic_programming"],
    "difficulty": "hard",
    "time_complexity": "O(log10(n) * len(digits))",
    "space_complexity": "O(log10(n))",
    "description": "Count how many positive integers less than or equal to n can be formed using only digits from a given set.",
}

def solve(digits: list[int], n: int) -> int:
    """
    Counts how many positive integers less than or equal to n can be formed 
    using only the digits provided in the digits list.

    Args:
        digits: A list of available single-digit integers.
        n: The upper bound integer.

    Returns:
        The total count of valid integers.

    Examples:
        >>> solve([1, 3, 5], 654)
        27
        >>> solve([9], 1)
        1
    """
    if not digits:
        return 0

    # Sort digits to handle them in increasing order for easier logic
    digits.sort()
    num_str = str(n)
    num_len = len(num_str)
    num_digits = len(digits)
    total_count = 0

    # Step 1: Count all valid numbers with fewer digits than n.
    # For a length 'i', there are (num_digits ^ i) possible combinations.
    for length in range(1, num_len):
        total_count += num_digits ** length

    # Step 2: Count valid numbers with exactly the same number of digits as n.
    # We iterate through the digits of n from left to right.
    for i in range(num_len):
        current_digit = int(num_str[i])
        
        # Count how many available digits are strictly less than the current digit of n.
        # If we pick a smaller digit at this position, all subsequent positions 
        # can be any of the available digits.
        smaller_digits_count = 0
        for d in digits:
            if d < current_digit:
                smaller_digits_count += 1
            else:
                break
        
        # Add combinations: (count of smaller digits) * (available digits ^ remaining positions)
        total_count += smaller_digits_count * (num_digits ** (num_len - 1 - i))

        # If the current digit of n is not in our allowed set, we cannot form 
        # any more numbers that match the prefix of n.
        if current_digit not in digits:
            break
        
        # If we have reached the last digit and it is in the set, 
        # it means the number 'n' itself is valid.
        if i == num_len - 1:
            total_count += 1

    return total_count
