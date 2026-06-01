METADATA = {
    "id": 1067,
    "name": "Digit Count in Range",
    "slug": "digit-count-in-range",
    "category": "Math",
    "aliases": [],
    "tags": ["math", "dynamic_programming", "digit_dp"],
    "difficulty": "hard",
    "time_complexity": "O(log10(n))",
    "space_complexity": "O(1)",
    "description": "Count the occurrences of a specific digit in all integers within a given range [low, high].",
}

def solve(low: int, high: int, digit: int) -> int:
    """
    Calculates the total occurrences of a specific digit in the range [low, high].

    Args:
        low (int): The lower bound of the range (inclusive).
        high (int): The upper bound of the range (inclusive).
        digit (int): The digit to count (0-9).

    Returns:
        int: The total count of the specified digit in the range.

    Examples:
        >>> solve(1, 10, 1)
        2
        >>> solve(1, 100, 1)
        21
    """

    def count_digit_up_to(n: int, target_digit: int) -> int:
        """
        Helper function to count occurrences of target_digit in range [1, n].
        Uses a digit-by-digit combinatorial approach.
        """
        if n <= 0:
            return 0
        
        count = 0
        factor = 1  # Represents the current place value (1, 10, 100, ...)
        
        while factor <= n:
            # Split the number into three parts based on the current place value:
            # higher_digits: digits to the left of the current position
            # current_digit: the digit at the current position
            # lower_digits: digits to the right of the current position
            higher_digits = n // (factor * 10)
            current_digit = (n // factor) % 10
            lower_digits = n % factor
            
            # Case 1: The digit at the current position is greater than target_digit
            # The target digit appears (higher_digits + 1) * factor times
            if current_digit > target_digit:
                count += (higher_digits + 1) * factor
            
            # Case 2: The digit at the current position is exactly target_digit
            # The target digit appears (higher_digits * factor) + (lower_digits + 1) times
            elif current_digit == target_digit:
                count += (higher_digits * factor) + (lower_digits + 1)
            
            # Case 3: The digit at the current position is less than target_digit
            # The target digit appears (higher_digits * factor) times
            else:
                count += higher_digits * factor
            
            # Special handling for digit 0: 
            # We must subtract the cases where the leading digit is 0 (invalid numbers)
            if target_digit == 0:
                count -= factor
                
            factor *= 10
            
        return count

    # The count in [low, high] is count(high) - count(low - 1)
    # Note: The logic for digit 0 in count_digit_up_to handles the 'no leading zeros' 
    # constraint by subtracting the factor at each step.
    return count_digit_up_to(high, digit) - count_digit_up_to(low - 1, digit)
