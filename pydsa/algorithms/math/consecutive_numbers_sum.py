METADATA = {
    "id": 829,
    "name": "Consecutive Numbers Sum",
    "slug": "consecutive-numbers-sum",
    "category": "Math",
    "aliases": [],
    "tags": ["math", "number_theory"],
    "difficulty": "medium",
    "time_complexity": "O(sqrt(n))",
    "space_complexity": "O(1)",
    "description": "Find the number of ways to represent a positive integer n as a sum of consecutive positive integers.",
}

def solve(n: int) -> int:
    """
    Calculates the number of ways to represent n as a sum of consecutive positive integers.

    The problem can be modeled using the arithmetic progression formula:
    n = a + (a + 1) + (a + 2) + ... + (a + k - 1)
    where 'a' is the starting integer and 'k' is the number of terms.
    
    n = k * a + (k * (k - 1)) / 2
    k * a = n - (k * (k - 1)) / 2
    
    For a valid 'a' to exist:
    1. (n - (k * (k - 1)) / 2) must be greater than 0 (since a >= 1).
    2. (n - (k * (k - 1)) / 2) must be divisible by k.

    Args:
        n: The target positive integer.

    Returns:
        The count of ways to represent n as a sum of consecutive positive integers.

    Examples:
        >>> solve(5)
        2
        # 5 = 5 (k=1)
        # 5 = 2 + 3 (k=2)
        >>> solve(9)
        3
        # 9 = 9 (k=1)
        # 9 = 4 + 5 (k=2)
        # 9 = 2 + 3 + 4 (k=3)
    """
    count = 0
    # k represents the number of terms in the consecutive sequence.
    # The smallest sum of k terms is k*(k+1)/2 (when a=1).
    # Therefore, k*(k-1)/2 must be less than n.
    # This implies k^2 is roughly 2n, so k goes up to sqrt(2n).
    k = 1
    while True:
        # Calculate the sum of the offsets: 0 + 1 + 2 + ... + (k-1)
        # This is the 'arithmetic' part of the progression formula.
        offset_sum = (k * (k - 1)) // 2
        
        # If the offset sum alone exceeds or equals n, no positive 'a' can exist.
        if offset_sum >= n:
            break
            
        # Check if (n - offset_sum) is divisible by k.
        # If it is, then a = (n - offset_sum) / k is a valid positive integer.
        if (n - offset_sum) % k == 0:
            count += 1
            
        k += 1
        
    return count
