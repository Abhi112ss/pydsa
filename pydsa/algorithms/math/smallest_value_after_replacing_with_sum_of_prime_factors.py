METADATA = {
    "id": 2507,
    "name": "Smallest Value After Replacing With Sum of Prime Factors",
    "slug": "smallest-value-after-replacing-with-sum-of-prime-factors",
    "category": "Math",
    "aliases": [],
    "tags": ["math", "prime_factorization"],
    "difficulty": "medium",
    "time_complexity": "O(n * sqrt(max_val))",
    "space_complexity": "O(1)",
    "description": "Repeatedly replace a number with the sum of its prime factors until the value becomes 2.",
}

def solve(n: int) -> int:
    """
    Repeatedly replaces the number n with the sum of its prime factors 
    until the number reaches 2.

    Args:
        n: The starting integer.

    Returns:
        The smallest value reached after the replacement process.

    Examples:
        >>> solve(4)
        2
        >>> solve(15)
        2
        >>> solve(2)
        2
    """
    current_value = n

    while current_value > 2:
        current_value = _get_sum_of_prime_factors(current_value)
        
    return current_value

def _get_sum_of_prime_factors(num: int) -> int:
    """
    Calculates the sum of prime factors of a given number.
    If a prime factor appears multiple times, it is added multiple times.

    Args:
        num: The integer to factorize.

    Returns:
        The sum of the prime factors.
    """
    prime_sum = 0
    divisor = 2
    temp_num = num

    # Iterate through potential divisors starting from 2
    while divisor * divisor <= temp_num:
        while temp_num % divisor == 0:
            # If divisor divides temp_num, it is a prime factor
            prime_sum += divisor
            temp_num //= divisor
        divisor += 1
    
    # If temp_num > 1, the remaining temp_num is a prime factor
    if temp_num > 1:
        prime_sum += temp_num
        
    return prime_sum
