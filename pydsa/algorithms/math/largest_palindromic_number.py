METADATA = {
    "id": 2384,
    "name": "Largest Palindromic Number",
    "slug": "largest_palindromic_number",
    "category": "Greedy",
    "aliases": [],
    "tags": ["greedy", "math", "string"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Construct the largest possible palindromic number from a given string of digits.",
}

def solve(digits: str) -> str:
    """
    Constructs the largest possible palindromic number from the given digits.

    Args:
        digits: A string containing only numeric digits.

    Returns:
        A string representing the largest palindromic number. 
        Returns "0" if no valid palindrome (other than single digits) can be formed, 
        or if the result would be leading zeros.

    Examples:
        >>> solve("44556")
        '54645'
        >>> solve("001")
        '1'
        >>> solve("000")
        '0'
    """
    # Count the frequency of each digit (0-9)
    counts = [0] * 10
    for char in digits:
        counts[int(char)] += 1

    left_half = []
    middle_digit = ""
    
    # Build the left half of the palindrome greedily from largest to smallest digit
    for digit in range(9, -1, -1):
        # We take pairs of the same digit to place on both sides
        pairs = counts[digit] // 2
        if pairs > 0:
            left_half.append(str(digit) * pairs)
            counts[digit] %= 2  # Remaining digit (0 or 1) can be a middle element

    # Join the left half to form the prefix
    prefix = "".join(left_half)

    # Handle leading zeros: if the largest digit in the prefix is '0', 
    # the only valid palindrome is "0" (if we have any zeros)
    if prefix.startswith("0"):
        return "0"

    # Find the largest remaining single digit to place in the middle
    for digit in range(9, -1, -1):
        if counts[digit] > 0:
            middle_digit = str(digit)
            break

    # Construct the full palindrome: prefix + middle + reversed prefix
    # If prefix is empty and middle is empty, we check if we had any digits at all
    if not prefix and not middle_digit:
        # This case handles if the input was something like "000" 
        # but the logic above might result in empty strings.
        # However, based on problem constraints, we return "0" if only zeros exist.
        return "0"

    # If prefix is empty, the result is just the middle digit (e.g., "5")
    # If prefix exists, result is prefix + middle + prefix[::-1]
    result = prefix + middle_digit + prefix[::-1]
    
    # Final check for the "0" case (e.g., input "00")
    if not result:
        return "0"
        
    return result
