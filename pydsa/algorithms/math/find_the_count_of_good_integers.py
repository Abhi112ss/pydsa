METADATA = {
    "id": 3272,
    "name": "Find the Count of Good Integers",
    "slug": "find-the-count-of-good-integers",
    "category": "Math",
    "aliases": [],
    "tags": ["math", "digit_dp", "combinatorics"],
    "difficulty": "medium",
    "time_complexity": "O(log(n))",
    "space_complexity": "O(1)",
    "description": "Count integers in a range [low, high] where all digits are unique.",
}

def solve(low: int, high: int) -> int:
    """
    Counts the number of 'good' integers in the range [low, high].
    A good integer is defined as an integer where all its digits are unique.

    Args:
        low (int): The lower bound of the range (inclusive).
        high (int): The upper bound of the range (inclusive).

    Returns:
        int: The count of integers in [low, high] with unique digits.

    Examples:
        >>> solve(1, 10)
        10
        >>> solve(10, 20)
        9
    """

    def count_unique_digits_up_to(n: int) -> int:
        """
        Helper function using Digit DP logic to count unique-digit numbers 
        from 0 to n.
        """
        if n < 0:
            return 0
        if n == 0:
            return 1

        s = str(n)
        length = len(s)
        count = 0

        # 1. Count numbers with fewer digits than n (e.g., if n=100, count 1-9 and 10-99)
        # These are always less than n and don't have leading zero constraints.
        for i in range(1, length):
            # First digit can be 1-9 (9 choices)
            # Subsequent (i-1) digits can be any of the remaining (9, 8, 7...)
            current_perm = 9
            for j in range(i - 1):
                current_perm *= (9 - j)
            count += current_perm

        # 2. Count numbers with the same number of digits as n
        used_digits = set()
        for i in range(length):
            digit = int(s[i])
            
            # Try placing a digit smaller than the current digit in s[i]
            # For the first position, we start from 1 to avoid leading zeros
            # For subsequent positions, we start from 0
            start_digit = 1 if i == 0 else 0
            for d in range(start_digit, digit):
                if d not in used_digits:
                    # Calculate permutations for the remaining (length - 1 - i) positions
                    # We have (10 - (i + 1)) digits left to choose from
                    remaining_slots = length - 1 - i
                    available_digits = 10 - (i + 1)
                    
                    perms = 1
                    for k in range(remaining_slots):
                        perms *= (available_digits - k)
                    count += perms

            # If the current digit is already used, we cannot form any more 
            # numbers with this prefix that are <= n
            if digit in used_digits:
                break
            used_digits.add(digit)
            
            # If we reached the last digit and it's unique, count the number n itself
            if i == length - 1:
                count += 1
        
        # Add 1 to account for the number 0
        return count + 1

    # The result for [low, high] is count(high) - count(low - 1)
    return count_unique_digits_up_to(high) - count_unique_digits_up_to(low - 1)
