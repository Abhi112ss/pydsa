METADATA = {
    "id": 3032,
    "name": "Count Numbers With Unique Digits II",
    "slug": "count-numbers-with-unique-digits-ii",
    "category": "Math",
    "aliases": [],
    "tags": ["math", "combinatorics", "digit_dp"],
    "difficulty": "medium",
    "time_complexity": "O(log10(n))",
    "space_complexity": "O(1)",
    "description": "Count how many integers in the range [low, high] have all unique digits.",
}

def solve(low: int, high: int) -> int:
    """
    Counts the number of integers in the range [low, high] where all digits are unique.

    Args:
        low (int): The lower bound of the range (inclusive).
        high (int): The upper bound of the range (inclusive).

    Returns:
        int: The count of numbers with unique digits in the given range.

    Examples:
        >>> solve(1, 10)
        10
        >>> solve(10, 20)
        9
    """

    def count_unique_up_to(n: int) -> int:
        """
        Helper function to count unique-digit numbers in the range [0, n]
        using a digit-based combinatorial approach.
        """
        if n < 0:
            return 0
        if n == 0:
            return 1

        s_n = str(n)
        length = len(s_n)
        count = 0

        # 1. Count all numbers with fewer digits than n
        # For a k-digit number, the first digit has 9 choices (1-9),
        # and subsequent digits have (9, 8, 7...) choices.
        # We also add 1 for the number '0' at the very end.
        for i in range(1, length):
            choices = 9
            for j in range(i - 1):
                choices *= (9 - j)
            count += choices

        # 2. Count numbers with exactly 'length' digits that are less than n
        used_digits = [False] * 10
        for i in range(length):
            digit = int(s_n[i])
            
            # Try placing a digit smaller than the current digit in s_n[i]
            # For the first position, we start from 1. For others, from 0.
            start_digit = 1 if i == 0 else 0
            for d in range(start_digit, digit):
                if not used_digits[d]:
                    # Calculate permutations for the remaining (length - 1 - i) positions
                    remaining_positions = length - 1 - i
                    choices = 1
                    available_digits = 10 - (i + 1)
                    for _ in range(remaining_positions):
                        choices *= available_digits
                        available_digits -= 1
                    count += choices
            
            # If the current digit is already used, we cannot form any more 
            # numbers with this prefix that are <= n.
            if used_digits[digit]:
                break
            used_digits[digit] = True
            
            # If we reached the last digit and it's unique, count the number n itself
            if i == length - 1:
                count += 1
        
        # Add 1 to account for the number 0
        return count + 1

    # The result for [low, high] is count(high) - count(low - 1)
    # Note: count_unique_up_to includes 0, so the subtraction works correctly.
    return count_unique_up_to(high) - count_unique_up_to(low - 1)
