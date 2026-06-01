METADATA = {
    "id": 3618,
    "name": "Split Array by Prime Indices",
    "slug": "split_array_by_prime_indices",
    "category": "Array",
    "aliases": [],
    "tags": ["sieve", "array", "greedy"],
    "difficulty": "medium",
    "time_complexity": "O(n log log n)",
    "space_complexity": "O(n)",
    "description": "Partition an array into subarrays such that each subarray starts at a prime index.",
}

def solve(nums: list[int]) -> list[list[int]]:
    """
    Splits the input array into subarrays where each subarray starts at a prime index.
    
    The partitioning logic follows a greedy approach: a new subarray is started 
    whenever the current index is a prime number. Note that index 0 and 1 
    are not prime.

    Args:
        nums: A list of integers to be partitioned.

    Returns:
        A list of lists, where each inner list is a subarray starting at a prime index.
        If the array starts with non-prime indices (0, 1), they are included in 
        the first subarray.

    Examples:
        >>> solve([10, 20, 30, 40, 50, 60])
        [[10, 20, 30], [40, 50], [60]]
        # Indices: 0, 1, 2 (prime), 3 (prime), 4, 5 (prime)
        # Subarrays: [idx 0-2], [idx 3-4], [idx 5]
    """
    n = len(nums)
    if n == 0:
        return []

    # Step 1: Sieve of Eratosthenes to find all primes up to n-1
    is_prime = [True] * n
    if n > 0:
        is_prime[0] = False
    if n > 1:
        is_prime[1] = False
    
    for p in range(2, int(n**0.5) + 1):
        if is_prime[p]:
            for i in range(p * p, n, p):
                is_prime[i] = False

    result: list[list[int]] = []
    current_subarray: list[int] = []

    # Step 2: Iterate through the array and partition based on prime indices
    for index in range(n):
        # If the current index is prime and we already have elements in the current subarray,
        # it means the current index marks the start of a NEW subarray.
        # Exception: The very first subarray (index 0, 1, etc.) is handled by checking 
        # if current_subarray is not empty.
        if is_prime[index] and current_subarray:
            result.append(current_subarray)
            current_subarray = []
        
        current_subarray.append(nums[index])

    # Append the final remaining subarray
    if current_subarray:
        result.append(current_subarray)

    return result
