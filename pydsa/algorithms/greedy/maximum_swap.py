METADATA = {
    "id": 670,
    "name": "Maximum Swap",
    "slug": "maximum-swap",
    "category": "Greedy",
    "aliases": [],
    "tags": ["math", "greedy"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Find the maximum value obtained by performing at most one swap of two digits in a given integer.",
}

def solve(num: int) -> int:
    """
    Finds the maximum value possible by performing at most one swap of two digits.

    The algorithm uses a greedy approach: it identifies the last occurrence of 
    each digit (0-9) and attempts to swap the leftmost digit that can be 
    replaced by a larger digit appearing later in the number.

    Args:
        num: The input integer.

    Returns:
        The maximum integer possible after at most one swap.

    Examples:
        >>> solve(2736)
        7236
        >>> solve(9973)
        9973
        >>> solve(1993)
        9913
    """
    # Convert number to a list of digits for easy swapping
    digits = list(str(num))
    n = len(digits)
    
    # Store the last seen index of each digit 0-9
    # Space complexity is O(1) because the size is fixed at 10
    last_occurrence = [-1] * 10
    for index, digit_char in enumerate(digits):
        last_occurrence[int(digit_char)] = index

    # Iterate through the digits from left to right
    for i in range(n):
        current_digit = int(digits[i])
        
        # Check if there is a larger digit (9 down to current_digit + 1)
        # that appears later in the number
        for target_digit in range(9, current_digit, -1):
            target_index = last_occurrence[target_digit]
            
            # If a larger digit exists at a position after the current index, swap and return
            if target_index > i:
                digits[i], digits[target_index] = digits[target_index], digits[i]
                return int("".join(digits))

    # If no beneficial swap is found, return the original number
    return num
