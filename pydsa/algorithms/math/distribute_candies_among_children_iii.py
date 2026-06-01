METADATA = {
    "id": 2927,
    "name": "Distribute Candies Among Children III",
    "slug": "distribute-candies-among-children-iii",
    "category": "Math",
    "aliases": [],
    "tags": ["combinatorics", "math"],
    "difficulty": "medium",
    "time_complexity": "O(1)",
    "space_complexity": "O(1)",
    "description": "Calculate the number of ways to distribute n candies among k children such that each child receives at least one candy, using stars and bars.",
}

def solve(n: int, k: int) -> int:
    """
    Calculates the number of ways to distribute n identical candies among k distinct children
    such that each child receives at least one candy.

    This is a classic combinatorial problem solvable using the 'Stars and Bars' theorem.
    To ensure each child gets at least one candy, we first give 1 candy to each of the k children.
    This leaves (n - k) candies to be distributed among k children with no further restrictions.
    The formula for distributing 'm' items into 'k' bins is C(m + k - 1, k - 1).
    Substituting m = n - k, we get C((n - k) + k - 1, k - 1) = C(n - 1, k - 1).

    Args:
        n: The total number of candies.
        k: The total number of children.

    Returns:
        The number of ways to distribute the candies.

    Examples:
        >>> solve(3, 2)
        2
        >>> solve(5, 3)
        6
    """
    # If there are fewer candies than children, it's impossible to give each child at least one.
    if n < k:
        return 0
    
    # The problem reduces to finding the number of ways to choose (k-1) positions 
    # out of (n-1) possible gaps between candies.
    # This is equivalent to the binomial coefficient C(n-1, k-1).
    
    # We calculate C(N, R) where N = n-1 and R = k-1.
    N = n - 1
    R = k - 1
    
    # Optimization: C(N, R) == C(N, N - R)
    if R > N // 2:
        R = N - R
        
    # Calculate the binomial coefficient iteratively to avoid large factorials
    # and maintain precision.
    numerator = 1
    denominator = 1
    for i in range(R):
        numerator = numerator * (N - i)
        denominator = denominator * (i + 1)
        
    return numerator // denominator
