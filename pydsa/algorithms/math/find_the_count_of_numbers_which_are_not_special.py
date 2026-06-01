METADATA = {
    "id": 3233,
    "name": "Find the Count of Numbers Which Are Not Special",
    "slug": "find-the-count-of-numbers-which-are-not-special",
    "category": "Math",
    "aliases": [],
    "tags": ["math", "digit_dp", "combinatorics"],
    "difficulty": "hard",
    "time_complexity": "O(log10(n))",
    "space_complexity": "O(log10(n))",
    "description": "Count numbers up to n that cannot be represented as a sum of distinct powers of 4.",
}

def solve(n: int) -> int:
    """
    Calculates the count of numbers from 1 to n that are NOT 'special'.
    A number is special if it can be represented as a sum of distinct powers of 4.
    This is equivalent to saying the number's representation in base 4 
    contains only digits 0 and 1.

    Args:
        n: The upper bound integer.

    Returns:
        The count of non-special numbers in the range [1, n].

    Examples:
        >>> solve(10)
        7
        # Special numbers <= 10: 1 (4^0), 4 (4^1), 5 (4^1 + 4^0)
        # Non-special: 2, 3, 6, 7, 8, 9, 10 (Total 7)
    """
    
    def count_special_up_to(limit: int) -> int:
        """
        Counts how many numbers from 0 to limit are 'special'.
        A number is special if its base-4 digits are only 0 or 1.
        This is equivalent to treating the base-4 digits as binary digits.
        """
        if limit < 0:
            return 0
        
        # Convert limit to base 4 digits
        digits = []
        temp = limit
        while temp > 0:
            digits.append(temp % 4)
            temp //= 4
        digits.reverse()
        
        count = 0
        n_digits = len(digits)
        
        for i in range(n_digits):
            digit = digits[i]
            
            if digit > 1:
                # If we encounter a digit > 1 (i.e., 2 or 3), 
                # all subsequent positions can be either 0 or 1.
                # This is equivalent to filling the remaining (n_digits - 1 - i) 
                # positions with any combination of {0, 1}.
                # We add 2^(remaining_positions) and stop because we've 
                # covered all possible special numbers smaller than the prefix.
                count += (1 << (n_digits - 1 - i))
                return count
            
            # If digit is 0 or 1, we continue to the next digit to maintain 
            # the prefix constraint.
            if digit == 1:
                # If the current digit is 1, we can also consider the case 
                # where this position was 0. If it were 0, all remaining 
                # positions could be 0 or 1.
                count += (1 << (n_digits - 1 - i))
                
        # If we finish the loop, the number itself is special (all digits were 0 or 1)
        return count + 1

    # The problem asks for numbers in [1, n].
    # Total numbers in [1, n] is n.
    # Special numbers in [1, n] = count_special_up_to(n) - 1 (subtracting the number 0).
    # Non-special = n - (count_special_up_to(n) - 1)
    
    special_count_including_zero = count_special_up_to(n)
    special_count_excluding_zero = special_count_including_zero - 1
    
    return n - special_count_excluding_zero
