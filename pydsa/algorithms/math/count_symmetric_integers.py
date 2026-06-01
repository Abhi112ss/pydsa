METADATA = {
    "id": 2843,
    "name": "Count Symmetric Integers",
    "slug": "count-symmetric-integers",
    "category": "Math",
    "aliases": [],
    "tags": ["math", "string_manipulation"],
    "difficulty": "easy",
    "time_complexity": "O(1)",
    "space_complexity": "O(1)",
    "description": "Count how many integers in a given range [low, high] have an even number of digits and the sum of their first half equals the sum of their second half.",
}

def solve(low: int, high: int) -> int:
    """
    Counts the number of symmetric integers in the range [low, high].
    
    A symmetric integer is defined as an integer with an even number of digits 
    where the sum of the first half of its digits equals the sum of the second half.

    Args:
        low (int): The lower bound of the range (inclusive).
        high (int): The upper bound of the range (inclusive).

    Returns:
        int: The count of symmetric integers in the range.

    Examples:
        >>> solve(1, 100)
        1
        >>> solve(10, 100)
        1
        >>> solve(1000, 10000)
        0
    """
    symmetric_count = 0

    for num in range(low, high + 1):
        digits_str = str(num)
        n = len(digits_str)

        # Symmetric integers must have an even number of digits
        if n % 2 == 0:
            midpoint = n // 2
            
            # Split the string into two halves
            first_half = digits_str[:midpoint]
            second_half = digits_str[midpoint:]
            
            # Calculate sums of digits for both halves
            # Using generator expressions for efficient summation
            sum_first = sum(int(digit) for digit in first_half)
            sum_second = sum(int(digit) for digit in second_half)
            
            if sum_first == sum_second:
                symmetric_count += 1
                
    return symmetric_count
