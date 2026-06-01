METADATA = {
    "id": 402,
    "name": "Remove K Digits",
    "slug": "remove-k-digits",
    "category": "Greedy",
    "aliases": [],
    "tags": ["greedy", "monotonic_stack", "string", "stack"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Given a non-negative integer represented as a string, remove k digits from the integer so that the new integer is the smallest possible.",
}

def solve(num: str, k: int) -> str:
    """
    Removes k digits from the string representation of a number to make the 
    resulting number the smallest possible.

    Args:
        num: A string representing a non-negative integer.
        k: The number of digits to remove.

    Returns:
        A string representing the smallest possible integer after removing k digits.

    Examples:
        >>> solve("1432219", 3)
        '1219'
        >>> solve("10200", 1)
        '200'
        >>> solve("10", 2)
        '0'
    """
    # If we need to remove all digits, the result is always "0"
    if k >= len(num):
        return "0"

    stack = []
    
    # Use a monotonic increasing stack to ensure digits are in non-decreasing order.
    # If the current digit is smaller than the top of the stack, removing the 
    # top digit will result in a smaller number.
    for digit in num:
        while k > 0 and stack and stack[-1] > digit:
            stack.pop()
            k -= 1
        stack.append(digit)

    # If k is still greater than 0, remove digits from the end (the largest ones)
    if k > 0:
        stack = stack[:-k]

    # Join the stack and strip leading zeros
    result = "".join(stack).lstrip("0")

    # If the result is empty (e.g., all zeros were stripped), return "0"
    return result if result else "0"
