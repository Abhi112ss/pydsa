METADATA = {
    "id": 3646,
    "name": "Next Special Palindrome Number",
    "slug": "next_special_palindrome_number",
    "category": "Math",
    "aliases": [],
    "tags": ["math", "string_manipulation"],
    "difficulty": "medium",
    "time_complexity": "O(log n)",
    "space_complexity": "O(log n)",
    "description": "Find the smallest palindrome strictly greater than the given integer n.",
}

def solve(n: int) -> int:
    """
    Finds the smallest palindrome strictly greater than the given integer n.

    Args:
        n: The input integer.

    Returns:
        The smallest palindrome integer that is strictly greater than n.

    Examples:
        >>> solve(123)
        131
        >>> solve(9)
        11
        >>> solve(1221)
        1331
    """
    s = str(n)
    length = len(s)
    
    # Helper to create a palindrome from a left half
    def create_palindrome(left_half: str, is_odd: bool) -> int:
        if is_odd:
            # If length is odd, the last char of left_half is the middle element
            return int(left_half + left_half[:-1][::-1])
        else:
            # If length is even, mirror the whole left_half
            return int(left_half + left_half[::-1])

    # Step 1: Try to create a palindrome by mirroring the current prefix
    mid = (length + 1) // 2
    prefix = s[:mid]
    candidate = create_palindrome(prefix, length % 2 != 0)

    # If the mirrored candidate is already greater than n, it's our answer
    if candidate > n:
        return candidate

    # Step 2: If not, we must increment the prefix to find the next palindrome
    # This handles cases like 123 -> 131 or 1221 -> 1331
    new_prefix_val = int(prefix) + 1
    new_prefix_str = str(new_prefix_val)

    # Case: Incrementing the prefix increases the number of digits (e.g., 99 -> 100)
    # This happens if the prefix was all 9s (e.g., n=99, prefix=9, new_prefix=10)
    if len(new_prefix_str) > len(prefix):
        # The smallest palindrome with length + 1 digits is always 10...01
        # e.g., 99 -> 101, 999 -> 1001
        return 10**length + 1

    # Otherwise, construct the palindrome using the incremented prefix
    return create_palindrome(new_prefix_str, length % 2 != 0)
