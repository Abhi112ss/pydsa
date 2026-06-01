METADATA = {
    "id": 2584,
    "name": "Split the Array to Make Coprime Products",
    "slug": "split-the-array-to-make-coprime-products",
    "category": "Math",
    "aliases": [],
    "tags": ["prime_factorization", "prefix_suffix", "math", "array"],
    "difficulty": "hard",
    "time_complexity": "O(n log(max_val))",
    "space_complexity": "O(n)",
    "description": "Find the index to split an array such that the product of the prefix and the product of the suffix are coprime.",
}

def solve(nums: list[int]) -> int:
    """
    Finds an index i such that the product of nums[0...i] and nums[i+1...n-1] are coprime.
    
    Two numbers are coprime if they share no common prime factors. This is equivalent 
    to saying that no prime factor of any number in the prefix appears in any 
    number in the suffix.

    Args:
        nums: A list of integers where each element is >= 2.

    Returns:
        The smallest index i such that the split is valid. Returns -1 if no such index exists.

    Examples:
        >>> solve([2, 3, 5, 7])
        0
        >>> solve([2, 2, 2])
        -1
        >>> solve([6, 10, 15])
        -1
    """
    n = len(nums)
    if n < 2:
        return -1

    # To ensure prefix and suffix products are coprime, we track the 
    # set of prime factors present in the prefix and the suffix.
    
    # Step 1: Identify all prime factors present in the entire array
    # and track their occurrences to determine if a prime is "exclusive" to a side.
    # However, a more efficient way is to track the first and last occurrence 
    # of every prime factor.
    
    prime_to_first_index = {}
    prime_to_last_index = {}

    def get_prime_factors(num: int) -> set[int]:
        factors = set()
        d = 2
        temp = num
        while d * d <= temp:
            if temp % d == 0:
                factors.add(d)
                while temp % d == 0:
                    temp //= d
            d += 1
        if temp > 1:
            factors.add(temp)
        return factors

    # Step 2: Map each prime factor to its first and last appearance in the array.
    # If a prime factor's last appearance is at index 'last' and its first is at 'first',
    # then any split index 'i' must satisfy either i < first (prime is in suffix)
    # or i >= last (prime is in prefix). 
    # Wait, the condition is: for a split at index i, the prefix is [0...i] and suffix is [i+1...n-1].
    # A prime factor is "shared" if it appears in both.
    # To NOT be shared, for every prime factor p, all its occurrences must be 
    # entirely within the prefix OR entirely within the suffix.
    
    # Let's track the range [min_idx, max_idx] for every prime factor.
    # For a split at index i, the prefix is [0, i] and suffix is [i+1, n-1].
    # A split is valid if for every prime factor p, max_idx[p] <= i OR min_idx[p] > i.
    
    prime_ranges = {} # prime -> [min_idx, max_idx]

    for idx, val in enumerate(nums):
        factors = get_prime_factors(val)
        for p in factors:
            if p not in prime_ranges:
                prime_ranges[p] = [idx, idx]
            else:
                prime_ranges[p][0] = min(prime_ranges[p][0], idx)
                prime_ranges[p][1] = max(prime_ranges[p][1], idx)

    # Step 3: Use a difference array or a sweep-line approach to find valid split points.
    # A split at index i is INVALID if there exists a prime p such that 
    # min_idx[p] <= i < max_idx[p].
    # This is because if min_idx <= i and max_idx > i, the prime p exists in 
    # both the prefix [0...i] and the suffix [i+1...n-1].
    
    # We want to find an i in [0, n-2] that is not covered by any [min_idx, max_idx - 1].
    bad_intervals = []
    for p in prime_ranges:
        start, end = prime_ranges[p]
        if start < end:
            # This prime spans across potential split points.
            # Any split index i where start <= i < end is invalid.
            bad_intervals.append((start, end - 1))

    if not bad_intervals:
        return 0

    # Step 4: Merge intervals to find gaps.
    bad_intervals.sort()
    
    # We check split indices i from 0 to n-2.
    # We use a sweep-line/merge approach to find the first i not in any bad_interval.
    
    # Instead of full merge, let's track the furthest 'bad' index reached.
    max_bad_reach = -1
    
    # Sort intervals by start time
    bad_intervals.sort()
    
    # We need to find the smallest i in [0, n-2] such that i is not in any [start, end].
    # We can use a prefix sum array (difference array) to mark bad indices.
    diff = [0] * (n + 1)
    for start, end in bad_intervals:
        diff[start] += 1
        diff[end + 1] -= 1
    
    current_coverage = 0
    for i in range(n - 1):
        current_coverage += diff[i]
        if current_coverage == 0:
            return i

    return -1
