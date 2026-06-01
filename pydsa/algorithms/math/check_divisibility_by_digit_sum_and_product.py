METADATA = {
    "id": 3622,
    "name": "Check Divisibility by Digit Sum and Product",
    "slug": "check_divisibility_by_digit_sum_and_product",
    "category": "Math",
    "aliases": [],
    "tags": ["math", "digit_manipulation"],
    "difficulty": "easy",
    "time_complexity": "O(log10(n))",
    "space_complexity": "O(1)",
    "description": "Check if a number is divisible by both the sum and the product of its digits.",
}

def solve(n: int) -> bool:
    """
    Determines if a given integer n is divisible by both the sum of its digits 
    and the product of its digits.

    Args:
        n: The integer to check.

    Returns:
        True if n is divisible by both the sum and product of its digits, 
        False otherwise. Note that if the product of digits is 0, 
        divisibility by product is considered False to avoid division by zero.

    Examples:
        >>> solve(12)
        True  # sum=3 (12%3==0), product=2 (12%2==0)
        >>> solve(13)
        False # sum=4 (13%4!=0)
        >>> solve(10)
        False # product=0 (cannot divide by zero)
    """
    if n < 0:
        n = abs(n)
        
    digit_sum = 0
    digit_product = 1
    temp_n = n

    # Iterate through each digit using modulo and integer division
    while temp_n > 0:
        digit = temp_n % 10
        digit_sum += digit
        digit_product *= digit
        temp_n //= 10

    # Handle the edge case where n is 0 (though problem constraints usually imply n > 0)
    if n == 0:
        return False

    # Check divisibility by sum (sum will always be > 0 for n > 0)
    if n % digit_sum != 0:
        return False

    # Check divisibility by product (must ensure product is not zero to avoid ZeroDivisionError)
    if digit_product == 0 or n % digit_product != 0:
        return False

    return True
