METADATA = {
    "id": 3895,
    "name": "Count Digit Appearances",
    "slug": "count_digit_appearances",
    "category": "Math",
    "aliases": [],
    "tags": ["math", "strings", "counting"],
    "difficulty": "easy",
    "time_complexity": "O(n * log10(n))",
    "space_complexity": "O(1)",
    "description": "Count the total number of times a specific digit appears in all integers from 0 to n.",
}

def solve(n: int, digit: int) -> int:
    """
    Counts the total occurrences of a specific digit in all integers from 0 to n.

    Args:
        n: The upper bound of the range (inclusive).
        digit: The single-digit integer to count.

    Returns:
        The total count of the specified digit appearing in the range [0, n].

    Examples:
        >>> solve(12, 1)
        5  # 1, 10, 11 (two 1s), 12
        >>> solve(20, 2)
        2  # 2, 20
    """
    if digit < 0 or digit > 9:
        return 0

    count = 0
    
    # Special case for digit 0: 0 is included in the range [0, n]
    if digit == 0:
        count += 1

    # We use a digit-by-digit counting approach (digit DP logic simplified)
    # to achieve O(log10(n)) complexity per digit position.
    # However, for a standard 'easy' implementation, iterating through the range
    # is O(n log n). Given the prompt's expected complexity, we implement 
    # the efficient mathematical approach.
    
    factor = 1
    while factor <= n:
        lower_numbers = n % factor
        current_digit = (n // factor) % 10
        higher_numbers = n // (factor * 10)

        # Count occurrences based on the current digit position (units, tens, etc.)
        if current_digit > digit:
            count += (higher_numbers + 1) * factor
        elif current_digit == digit:
            count += higher_numbers * factor + (lower_numbers + 1)
        else:
            count += higher_numbers * factor

        # Adjustment for digit 0 to avoid counting leading zeros
        if digit == 0:
            count -= factor

        factor *= 10

    # The mathematical approach above counts occurrences in [1, n].
    # If digit is 0, we already handled the '0' in the range [0, n] at the start.
    # But the math logic for digit 0 is tricky with leading zeros.
    # Let's use a more robust digit-by-digit counting for all digits.
    
    return _count_digit_occurrences_robust(n, digit)

def _count_digit_occurrences_robust(n: int, digit: int) -> int:
    """
    A robust mathematical implementation to count digit occurrences in O(log n).
    """
    count = 0
    # If digit is 0, we must account for the number 0 itself
    if digit == 0:
        count += 1
        
    factor = 1
    while factor <= n:
        # Split n into: higher | current | lower
        # Example: n=1234, factor=100 -> higher=12, current=3, lower=4
        higher = n // (factor * 10)
        current = (n // factor) % 10
        lower = n % factor
        
        if digit > 0:
            if current < digit:
                count += higher * factor
            elif current == digit:
                count += higher * factor + (lower + 1)
            else:
                count += (higher + 1) * factor
        else:
            # Special logic for digit 0 to prevent counting leading zeros
            if current == 0:
                count += (higher - 1) * factor + (lower + 1)
            else:
                count += higher * factor
                
        factor *= 10
        
    return count

# Note: The prompt asks for O(n log n) expected time, which implies 
# a simple iteration. Below is the iterative version as requested by 
# the "Expected time" hint in the prompt.

def solve_iterative(n: int, digit: int) -> int:
    """
    Counts the total occurrences of a specific digit in all integers from 0 to n
    using the iterative approach suggested by the prompt.

    Args:
        n: The upper bound of the range (inclusive).
        digit: The single-digit integer to count.

    Returns:
        The total count of the specified digit appearing in the range [0, n].
    """
    target_digit_str = str(digit)
    total_count = 0
    
    # Iterate through every number in the range [0, n]
    for i in range(n + 1):
        # Convert number to string and count occurrences of the target digit
        total_count += str(i).count(target_digit_str)
        
    return total_count

# Re-assigning solve to the iterative version to match the prompt's complexity hint
solve = solve_iterative