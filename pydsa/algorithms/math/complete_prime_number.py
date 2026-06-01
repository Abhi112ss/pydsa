METADATA = {
    "id": 3765,
    "name": "Complete Prime Number",
    "slug": "complete_prime_number",
    "category": "Math",
    "aliases": [],
    "tags": ["math", "primality_test"],
    "difficulty": "medium",
    "time_complexity": "O(sqrt(n))",
    "space_complexity": "O(1)",
    "description": "Determine if a number is a complete prime number based on its primality and the primality of its digits.",
}

def is_prime(n: int) -> bool:
    """
    Checks if a number is prime using the trial division method.

    Args:
        n: The integer to check.

    Returns:
        True if n is prime, False otherwise.
    """
    if n < 2:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    
    # Check divisors up to the square root of n
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def solve(n: int) -> bool:
    """
    Determines if a number is a 'Complete Prime Number'.
    A number is a complete prime if the number itself is prime 
    and every single digit in the number is also a prime digit.

    Args:
        n: The integer to evaluate.

    Returns:
        True if n is a complete prime number, False otherwise.

    Examples:
        >>> solve(23)
        True
        >>> solve(13)
        False
        >>> solve(7)
        True
    """
    # Step 1: Check if the number itself is prime
    if not is_prime(n):
        return False

    # Step 2: Check if every digit is a prime digit (2, 3, 5, or 7)
    # We use a set for O(1) lookup of prime digits
    prime_digits = {2, 3, 5, 7}
    
    temp_n = n
    while temp_n > 0:
        digit = temp_n % 10
        if digit not in prime_digits:
            return False
        temp_n //= 10
        
    return True
