METADATA = {
    "id": 1012,
    "name": "Numbers With Repeated Digits",
    "slug": "numbers-with-repeated-digits",
    "category": "Math",
    "aliases": [],
    "tags": ["digit_dp", "combinatorics", "math"],
    "difficulty": "hard",
    "time_complexity": "O(log10(n))",
    "space_complexity": "O(log10(n))",
    "description": "Count the number of integers in the range [1, n] that have at least one repeated digit.",
}

def solve(n: int) -> int:
    """
    Calculates the count of numbers in the range [1, n] that have at least one repeated digit.
    
    The approach uses the principle of complement: 
    Total numbers in [1, n] minus numbers with all unique digits.

    Args:
        n: The upper bound of the range (inclusive).

    Returns:
        The count of numbers with repeated digits.

    Examples:
        >>> solve(20)
        1
        >>> solve(100)
        9
    """
    if n < 10:
        return 0

    s_n = str(n)
    length = len(s_n)

    def count_unique_digits(limit_str: str) -> int:
        """
        Counts how many numbers from 1 to limit_str have all unique digits.
        """
        count = 0
        
        # 1. Count numbers with fewer digits than the limit_str
        # Example: if n=100, count unique numbers with 1 digit and 2 digits.
        for i in range(1, len(limit_str)):
            # First digit can be 1-9 (9 choices)
            # Subsequent (i-1) digits can be any of the remaining (9, 8, 7...)
            current_count = 9
            choices = 9
            for _ in range(i - 1):
                current_count *= choices
                choices -= 1
            count += current_count

        # 2. Count numbers with the same number of digits as limit_str
        # We iterate through the digits of the limit_str to stay under the bound.
        used_digits = set()
        for i in range(len(limit_str)):
            digit = int(limit_str[i])
            
            # Try placing a digit smaller than the current digit in limit_str
            # For the first position, we can't use 0.
            start_digit = 1 if i == 0 else 0
            for d in range(start_digit, digit):
                if d not in used_digits:
                    # Calculate permutations for the remaining positions
                    # Remaining positions: len(limit_str) - 1 - i
                    # Available digits: 10 - (i + 1)
                    remaining_positions = len(limit_str) - 1 - i
                    available_digits = 10 - (i + 1)
                    
                    permutations = 1
                    for _ in range(remaining_positions):
                        permutations *= available_digits
                        available_digits -= 1
                    count += permutations
            
            # If the current digit is already used, we cannot form any more 
            # unique-digit numbers that match the prefix of limit_str.
            if digit in used_digits:
                break
            used_digits.add(digit)
            
            # If we reached the end of the string without breaking, 
            # it means the number n itself has unique digits.
            if i == len(limit_str) - 1:
                count += 1
                
        return count

    # Total numbers (n) - numbers with unique digits
    return n - count_unique_digits(s_n)
