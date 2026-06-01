METADATA = {
    "id": 2665,
    "name": "Counter II",
    "slug": "counter_ii",
    "category": "Math",
    "aliases": [],
    "tags": ["digit_dp", "math", "combinatorics"],
    "difficulty": "hard",
    "time_complexity": "O(log n)",
    "space_complexity": "O(log n)",
    "description": "Count how many integers in the range [1, n] have a specific digit at a specific position.",
}

def solve(n: int, position: int, digit: int) -> int:
    """
    Counts how many integers in the range [1, n] have the given digit at the 
    specified position (1-indexed from the right).

    Args:
        n: The upper bound of the range [1, n].
        position: The 1-indexed position from the right (e.g., 1 is units, 2 is tens).
        digit: The digit to look for at that position.

    Returns:
        The count of integers in [1, n] that have 'digit' at 'position'.

    Examples:
        >>> solve(25, 1, 5)
        2
        >>> solve(100, 2, 0)
        9
    """
    # The position is 1-indexed from the right.
    # We use power of 10 to isolate the digit at the target position.
    # Example: n=123, position=2 (tens), digit=2.
    # divisor = 10^(2-1) = 10.
    divisor = 10 ** (position - 1)
    
    # The cycle length is the number of integers it takes for the digit 
    # at 'position' to repeat its pattern.
    # For position 1 (units), cycle is 10 (0,1,2...9).
    # For position 2 (tens), cycle is 100 (00,01...99).
    cycle_length = divisor * 10
    
    # 1. Calculate how many full cycles of 'cycle_length' exist in [0, n].
    # We use n + 1 because we are counting from 0 to n.
    # However, the problem asks for [1, n]. Since the digit 0 at a position 
    # might be counted for the number 0, we handle the range carefully.
    # A simpler way: count occurrences in [0, n] and subtract if digit is 0 
    # and we counted the number 0.
    
    # Total full cycles
    full_cycles = (n + 1) // cycle_length
    
    # Each full cycle contains exactly 'divisor' occurrences of the target digit.
    count = full_cycles * divisor
    
    # 2. Handle the remaining part (the partial cycle).
    remainder = (n + 1) % cycle_length
    
    # The target digit starts appearing in the cycle at: digit * divisor
    # and ends at: (digit + 1) * divisor - 1
    start_of_digit_range = digit * divisor
    end_of_digit_range = (digit + 1) * divisor - 1
    
    # If the remainder falls within or after the digit's range in the cycle
    if remainder > start_of_digit_range:
        # The count is the number of elements in the intersection of 
        # [start_of_digit_range, end_of_digit_range] and [0, remainder - 1]
        count += min(remainder - 1, end_of_digit_range) - start_of_digit_range + 1

    # 3. Adjust for the range [1, n].
    # If the digit we are looking for is 0, the logic above counted the number 0.
    # Since the range is [1, n], we must subtract 1 if digit is 0.
    if digit == 0:
        count -= 1
        
    return count
