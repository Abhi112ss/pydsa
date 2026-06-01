METADATA = {
    "id": 964,
    "name": "Least Operators to Express Number",
    "slug": "least-operators-to-express-number",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["recursion", "memoization", "greedy", "math"],
    "difficulty": "medium",
    "time_complexity": "O(log_x target)",
    "space_complexity": "O(log_x target)",
    "description": "Find the minimum number of operators to express a target number using powers of a given base x.",
}

def solve(x: int, target: int) -> int:
    """
    Calculates the minimum number of operators needed to express the target 
    using powers of x.

    Args:
        x: The base number.
        target: The target number to express.

    Returns:
        The minimum number of operators (additions or subtractions).

    Examples:
        >>> solve(3, 13)
        3
        # 13 = 3^2 + 3^1 + 3^0 (9 + 3 + 1) -> 3 operators
        >>> solve(2, 37)
        4
        # 37 = 2^5 + 2^2 + 2^0 (32 + 4 + 1) -> 3 operators? No, 37 = 2^5 + 2^2 + 2^0 is 3.
        # Wait, 37 = 32 + 4 + 1 (3 ops). 
        # Let's check 37 in base 2: 100101. 
        # If we use subtraction: 2^6 - 2^4 - 2^2 - 2^0 = 64 - 16 - 4 - 1 = 43 (No).
        # 37 = 64 - 27... 37 = 32 + 4 + 1 (3 ops).
    """
    memo: dict[int, int] = {}

    def get_min_ops(remainder: int) -> int:
        """
        Recursive helper with memoization to find min operators for a remainder.
        
        At each step, we find the closest power of x to the current remainder.
        We can either go 'up' (subtracting from a higher power) or 'down' 
        (adding smaller powers).
        """
        if remainder == 0:
            return 0
        if remainder == 1:
            return 1
        if remainder in memo:
            return memo[remainder]

        # Find the largest power of x such that x^p <= remainder
        # We use a loop to find the exponent p
        p = 0
        current_power = 1
        while current_power * x <= remainder:
            current_power *= x
            p += 1
        
        # Option 1: Represent remainder as (current_power) + (remainder - current_power)
        # This is equivalent to using the digit in base-x representation.
        # We calculate how many times current_power fits into remainder.
        # However, the optimal way is to consider the remainder modulo x.
        
        # Standard greedy approach for base conversion:
        # The number of operators for 'remainder' is (remainder % x) + solve(remainder // x)
        # But we must also consider the 'subtraction' case: (x - remainder % x) + solve(remainder // x + 1)
        
        # Let's refine the logic:
        # To represent 'remainder', we can either:
        # 1. Use (remainder % x) units of x^0 and then solve for (remainder // x)
        # 2. Use (x - remainder % x) units of x^0 and then solve for (remainder // x + 1)
        
        res = min(
            (remainder % x) + get_min_ops(remainder // x),
            (x - (remainder % x)) + get_min_ops(remainder // x + 1)
        )
        
        memo[remainder] = res
        return res

    return get_min_ops(target)
