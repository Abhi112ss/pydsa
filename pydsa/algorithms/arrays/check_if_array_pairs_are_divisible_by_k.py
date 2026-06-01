METADATA = {
    "id": 1497,
    "name": "Check If Array Pairs Are Divisible by k",
    "slug": "check-if-array-pairs-are-divisible-by-k",
    "category": "Hash Table",
    "aliases": [],
    "tags": ["hash_map", "math"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(k)",
    "description": "Determine if an array can be divided into pairs such that the sum of each pair is divisible by k.",
}

def solve(nums: list[int], k: int) -> bool:
    """
    Checks if the given array can be partitioned into pairs where each pair sum is divisible by k.

    Args:
        nums: A list of integers.
        k: The divisor.

    Returns:
        True if such pairs exist, False otherwise.

    Examples:
        >>> solve([1, 2, 3, 4, 5, 10, 6, 7, 8, 9], 5)
        True
        >>> solve([1, 2, 3, 4, 5, 6], 7)
        True
        >>> solve([1, 2, 3, 4, 5, 6], 1)
        True
        >>> solve([1, 2, 3, 4, 5, 6], 2)
        False
    """
    # Frequency map for remainders when elements are divided by k
    remainder_counts: dict[int, int] = {}
    
    for num in nums:
        # Calculate remainder and handle negative numbers to ensure it's in [0, k-1]
        remainder = num % k
        remainder_counts[remainder] = remainder_counts.get(remainder, 0) + 1
        
    for remainder, count in remainder_counts.items():
        if remainder == 0:
            # Elements with remainder 0 must pair with each other, so count must be even
            if count % 2 != 0:
                return False
        elif remainder * 2 == k:
            # If remainder is exactly half of k (e.g., k=10, rem=5), they must pair with each other
            if count % 2 != 0:
                return False
        else:
            # For any other remainder 'r', there must be an equal number of elements 
            # with remainder 'k - r' to form valid pairs
            complement = k - remainder
            if count != remainder_counts.get(complement, 0):
                return False
                
    return True
