METADATA = {
    "id": 556,
    "name": "Next Greater Element III",
    "slug": "next-greater-element-iii",
    "category": "Math",
    "aliases": [],
    "tags": ["two_pointer", "string_manipulation", "math"],
    "difficulty": "medium",
    "time_complexity": "O(log n)",
    "space_complexity": "O(log n)",
    "description": "Find the smallest integer with the same digits that is greater than the given integer.",
}

def solve(n: int) -> int:
    """
    Finds the smallest integer greater than n that has the same digits.
    This is equivalent to finding the next lexicographical permutation of the digits.

    Args:
        n: The input integer.

    Returns:
        The next greater integer with the same digits, or -1 if no such integer exists.

    Examples:
        >>> solve(12)
        >>> solve(21)
        -1
        >>> solve(1999)
        -1
        >>> solve(12345)
        12435
    """
    # Convert number to a list of digits for easy manipulation
    digits = list(str(n))
    length = len(digits)

    # Step 1: Find the first digit from the right that is smaller than the digit to its right
    # This is the 'pivot' point where the ascending order (from right) is broken.
    pivot_index = -1
    for i in range(length - 2, -1, -1):
        if digits[i] < digits[i + 1]:
            pivot_index = i
            break

    # If no such index is found, the digits are in descending order (largest possible permutation)
    if pivot_index == -1:
        return -1

    # Step 2: Find the smallest digit to the right of the pivot that is greater than the pivot
    # Since the suffix is in descending order, the first digit we find from the right
    # that is > digits[pivot_index] is the smallest one greater than the pivot.
    successor_index = -1
    for i in range(length - 1, pivot_index, -1):
        if digits[i] > digits[pivot_index]:
            successor_index = i
            break

    # Step 3: Swap the pivot with the successor
    digits[pivot_index], digits[successor_index] = digits[successor_index], digits[pivot_index]

    # Step 4: Reverse the suffix (everything to the right of the pivot)
    # The suffix was in descending order; reversing it makes it ascending (smallest possible)
    left, right = pivot_index + 1, length - 1
    while left < right:
        digits[left], digits[right] = digits[right], digits[left]
        left += 1
        right -= 1

    # Convert the list of digits back to an integer
    result_str = "".join(digits)
    result_int = int(result_str)

    # The problem specifies the result must fit in a 32-bit signed integer
    # 2^31 - 1 = 2147483647
    if result_int > 2147483647:
        return -1

    return result_int
