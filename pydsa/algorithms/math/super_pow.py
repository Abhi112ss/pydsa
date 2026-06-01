METADATA = {
    "id": 372,
    "name": "Super Pow",
    "slug": "super-pow",
    "category": "Math",
    "aliases": [],
    "tags": ["math", "recursion", "modular_exponentiation"],
    "difficulty": "medium",
    "time_complexity": "O(log b)",
    "space_complexity": "O(log b)",
    "description": "Given two integers a and b, where b is an array representing a large integer, return (a^b) % 1337.",
}

def solve(a: int, b: list[int]) -> int:
    """
    Computes (a^b) % 1337 where b is a large integer represented as an array.

    Args:
        a: The base integer.
        b: A list of integers representing the digits of the exponent.

    Returns:
        The result of (a^b) % 1337.

    Examples:
        >>> solve(2, [1, 0])
        1024
        >>> solve(2, [1, 2])
        16
    """
    MOD = 1337

    def power(base: int, exp: int) -> int:
        """Computes (base^exp) % MOD using binary exponentiation."""
        res = 1
        base %= MOD
        while exp > 0:
            if exp % 2 == 1:
                res = (res * base) % MOD
            base = (base * base) % MOD
            exp //= 2
        return res

    def super_pow_recursive(digits: list[int]) -> int:
        """
        Uses the property: a^[1,2,3] = (a^[1,2])^10 * a^3 (mod 1337).
        """
        if not digits:
            return 1
        
        # Pop the last digit to reduce the problem size
        last_digit = digits.pop()
        
        # Part 1: (a ^ remaining_digits) ^ 10 % MOD
        # Part 2: a ^ last_digit % MOD
        # Combine using: (Part 1 * Part 2) % MOD
        part1 = power(super_pow_recursive(digits), 10)
        part2 = power(a, last_digit)
        
        return (part1 * part2) % MOD

    # We pass a copy of b to avoid mutating the original input list
    return super_pow_recursive(list(b))
