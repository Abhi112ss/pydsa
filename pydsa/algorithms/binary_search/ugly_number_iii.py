METADATA = {
    "id": 1201,
    "name": "Ugly Number III",
    "slug": "ugly-number-iii",
    "category": "Math",
    "aliases": [],
    "tags": ["binary_search", "math", "inclusion_exclusion"],
    "difficulty": "hard",
    "time_complexity": "O(log(2e9))",
    "space_complexity": "O(1)",
    "description": "Find the n-th number that is divisible by a, b, or c using binary search and the inclusion-exclusion principle.",
}

def solve(a: int, b: int, c: int, n: int) -> int:
    """
    Finds the n-th number that is divisible by a, b, or c.

    Args:
        a: The first divisor.
        b: The second divisor.
        c: The third divisor.
        n: The target index (1-indexed).

    Returns:
        The n-th ugly number.

    Examples:
        >>> solve(2, 3, 5, 10)
        12
        >>> solve(2, 3, 5, 1)
        2
    """

    def gcd(x: int, y: int) -> int:
        """Compute the greatest common divisor of x and y."""
        while y:
            x, y = y, x % y
        return x

    def lcm(x: int, y: int) -> int:
        """Compute the least common multiple of x and y."""
        if x == 0 or y == 0:
            return 0
        return abs(x * y) // gcd(x, y)

    def count_multiples(target: int) -> int:
        """
        Counts how many numbers up to 'target' are divisible by a, b, or c
        using the Principle of Inclusion-Exclusion.
        """
        # Single counts
        count = (target // a) + (target // b) + (target // c)
        
        # Subtract double counts (multiples of LCM of pairs)
        lcm_ab = lcm(a, b)
        lcm_bc = lcm(b, c)
        lcm_ac = lcm(a, c)
        count -= (target // lcm_ab) + (target // lcm_bc) + (target // lcm_ac)
        
        # Add back triple counts (multiples of LCM of all three)
        lcm_abc = lcm(lcm_ab, c)
        count += (target // lcm_abc)
        
        return count

    # Binary search range: 1 to 2e9 (as per problem constraints)
    low = 1
    high = 2 * 10**9
    ans = high

    while low <= high:
        mid = (low + high) // 2
        # If the count of multiples up to mid is at least n, 
        # mid could be our answer, but we try to find a smaller one.
        if count_multiples(mid) >= n:
            ans = mid
            high = mid - 1
        else:
            low = mid + 1

    return ans
