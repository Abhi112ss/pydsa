METADATA = {
    "id": 1073,
    "name": "Adding Two Negabinary Numbers",
    "slug": "adding-two-negabinary-numbers",
    "category": "Math",
    "aliases": [],
    "tags": ["math", "arrays"],
    "difficulty": "medium",
    "time_complexity": "O(max(N, M))",
    "space_complexity": "O(max(N, M))",
    "description": "Add two negabinary numbers represented as lists of bits and return the result as a negabinary list.",
}

def solve(a: list[int], b: list[int]) -> list[int]:
    """
    Adds two negabinary numbers represented as lists of bits.

    In negabinary (base -2), the place values are powers of -2:
    ..., 16, -8, 4, -2, 1.
    When adding, if the sum at a position is not 0 or 1, we must adjust
    the carry. Specifically, if the sum is S, we want S = bit + (-2 * carry).
    This implies:
    - bit = S % 2 (but we need to handle the sign carefully)
    - carry = (S - bit) // -2

    Args:
        a: A list of integers representing the first negabinary number.
        b: A list of integers representing the second negabinary number.

    Returns:
        A list of integers representing the sum in negabinary.

    Examples:
        >>> solve([1, 1, 0], [1, 1, 0])
        [0, 1, 1]
        >>> solve([1], [1])
        [0, 1]
    """
    result = []
    i = len(a) - 1
    j = len(b) - 1
    carry = 0

    # Iterate through both lists from least significant bit to most significant
    while i >= 0 or j >= 0 or carry != 0:
        val_a = a[i] if i >= 0 else 0
        val_b = b[j] if j >= 0 else 0
        
        # Calculate the current sum including the carry from the previous position
        current_sum = val_a + val_b + carry
        
        # In base -2, we need the digit to be 0 or 1.
        # If current_sum is 2, digit is 0 and carry is -1 (since 2 = 0 + (-2 * -1))
        # If current_sum is -1, digit is 1 and carry is 1 (since -1 = 1 + (-2 * 1))
        # A general way to handle this:
        # digit = current_sum % 2 is not enough because % in Python handles negatives differently.
        # We use the property: digit = current_sum % 2, but we must ensure 
        # current_sum = digit + (-2 * next_carry)
        
        digit = current_sum % 2
        # If current_sum is odd, digit is 1. If even, digit is 0.
        # However, Python's % operator on negative numbers: -1 % 2 = 1.
        # Let's verify: if current_sum = -1, digit = 1. 
        # -1 = 1 + (-2 * carry) => -2 = -2 * carry => carry = 1.
        # If current_sum = 2, digit = 0.
        # 2 = 0 + (-2 * carry) => 2 = -2 * carry => carry = -1.
        
        # Correct logic for negabinary carry:
        # We want: current_sum = digit + (-2 * next_carry)
        # Therefore: next_carry = (current_sum - digit) // -2
        
        # To ensure digit is always 0 or 1:
        if digit < 0: # This case shouldn't happen with Python's % 2
            digit += 2
            
        # Re-calculating carry based on the chosen digit
        # This handles the sign flip inherent in base -2
        carry = (current_sum - digit) // -2
        
        result.append(digit)
        
        i -= 1
        j -= 1

    # The result is built from LSB to MSB, so reverse it
    return result[::-1]
