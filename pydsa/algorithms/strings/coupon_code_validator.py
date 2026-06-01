METADATA = {
    "id": 3606,
    "name": "Coupon Code Validator",
    "slug": "coupon_code_validator",
    "category": "String",
    "aliases": [],
    "tags": ["string_manipulation", "regex"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Validate a coupon code based on specific character type and positional constraints.",
}

def solve(coupon_code: str) -> bool:
    """
    Validates a coupon code based on specific structural rules.
    
    Rules:
    1. Length must be exactly 10 characters.
    2. Must start with exactly 2 uppercase letters.
    3. Must contain exactly 3 digits.
    4. The remaining 5 characters must be lowercase letters.
    5. The digits must appear in strictly increasing order of their indices.
    6. The digits must be in non-decreasing numerical order.

    Args:
        coupon_code: The string representing the coupon code to validate.

    Returns:
        True if the coupon code is valid according to all rules, False otherwise.

    Examples:
        >>> solve("AB123abcde")
        True
        >>> solve("AB132abcde")
        False
        >>> solve("A123abcdef")
        False
    """
    # Rule 1: Length check
    if len(coupon_code) != 10:
        return False

    # Rule 2: First two characters must be uppercase letters
    if not (coupon_code[0].isupper() and coupon_code[1].isupper()):
        return False

    # Rule 3 & 4: Check character types for the rest of the string
    # We also need to track the positions and values of digits for Rule 5 & 6
    digit_indices = []
    digit_values = []
    
    # The first 2 are uppercase, so we check from index 2 to 9
    # However, the problem implies a specific structure: 2 Upper, 3 Digits, 5 Lower
    # Let's verify the exact composition:
    
    # Check if indices 0,1 are Upper (already done)
    # Check if indices 2-9 contain exactly 3 digits and 5 lowercase letters
    # and no other characters.
    
    remaining_chars = coupon_code[2:]
    digit_count = 0
    lower_count = 0
    
    for i, char in enumerate(remaining_chars):
        if char.isdigit():
            digit_count += 1
            # Store the actual index in the original string and the digit value
            digit_indices.append(i + 2)
            digit_values.append(int(char))
        elif char.islower():
            lower_count += 1
        else:
            # Any character that is not a digit or lowercase letter is invalid
            return False

    # Rule 3 & 4: Verify counts
    if digit_count != 3 or lower_count != 5:
        return False

    # Rule 5: Digits must be in strictly increasing order of their indices
    # (This is naturally true if we iterate through the string, but we verify logic)
    # Rule 6: Digits must be in non-decreasing numerical order
    for j in range(len(digit_values) - 1):
        if digit_values[j] > digit_values[j + 1]:
            return False

    return True
