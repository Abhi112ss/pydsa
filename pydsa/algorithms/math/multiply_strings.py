METADATA = {
    "id": 43,
    "name": "Multiply Strings",
    "slug": "multiply-strings",
    "category": "Math",
    "aliases": [],
    "tags": ["string", "math", "simulation"],
    "difficulty": "medium",
    "time_complexity": "O(m*n)",
    "space_complexity": "O(m+n)",
    "description": "Given two non-negative integers represented as strings, return the product of them as a string.",
}

def solve(num1: str, num2: str) -> str:
    """
    Multiplies two non-negative integers represented as strings using manual multiplication simulation.

    Args:
        num1: The first non-negative integer as a string.
        num2: The second non-negative integer as a string.

    Returns:
        The product of num1 and num2 as a string.

    Examples:
        >>> solve("123", "456")
        '56088'
        >>> solve("2", "3")
        '6'
        >>> solve("0", "0")
        '0'
    """
    # Handle the edge case where one of the numbers is zero
    if num1 == "0" or num2 == "0":
        return "0"

    len1, len2 = len(num1), len(num2)
    # The maximum possible length of the product is len1 + len2
    result = [0] * (len1 + len2)

    # Iterate through both strings from right to left (least significant digit)
    for i in range(len1 - 1, -1, -1):
        digit1 = ord(num1[i]) - ord('0')
        for j in range(len2 - 1, -1, -1):
            digit2 = ord(num2[j]) - ord('0')
            
            # Calculate product of current digits and the position in the result array
            product = digit1 * digit2
            # The product of num1[i] and num2[j] contributes to indices i+j and i+j+1
            p1, p2 = i + j, i + j + 1
            
            # Add product to the current value at the target position
            total_sum = product + result[p2]
            
            # Update the positions: p2 gets the unit digit, p1 gets the carry
            result[p2] = total_sum % 10
            result[p1] += total_sum // 10

    # Convert the integer list back to a string, skipping leading zeros
    start_index = 0
    while start_index < len(result) and result[start_index] == 0:
        start_index += 1

    return "".join(map(str, result[start_index:]))
