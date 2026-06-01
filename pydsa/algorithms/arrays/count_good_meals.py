METADATA = {
    "id": 1711,
    "name": "Count Good Meals",
    "slug": "count-good-meals",
    "category": "Math",
    "aliases": [],
    "tags": ["hash_map", "math", "two_pointer"],
    "difficulty": "medium",
    "time_complexity": "O(n + m log log m)",
    "space_complexity": "O(m)",
    "description": "Count pairs of ingredients whose sum is a prime number.",
}

def solve(nums: list[int]) -> int:
    """
    Counts the number of pairs (i, j) such that nums[i] + nums[j] is a prime number.

    Args:
        nums: A list of integers representing ingredient values.

    Returns:
        The total count of pairs whose sum is prime.

    Examples:
        >>> solve([2, 3, 5, 7])
        4
        >>> solve([1, 1, 1])
        3
    """
    if not nums:
        return 0

    # The maximum possible sum is twice the maximum value in nums
    max_val = max(nums)
    max_sum = 2 * max_val
    
    # Step 1: Sieve of Eratosthenes to precompute primes up to max_sum
    is_prime = [True] * (max_sum + 1)
    is_prime[0] = is_prime[1] = False
    for p in range(2, int(max_sum**0.5) + 1):
        if is_prime[p]:
            for i in range(p * p, max_sum + 1, p):
                is_prime[i] = False
    
    # Pre-extract list of primes to iterate over them instead of all numbers
    primes = [p for p, prime in enumerate(is_prime) if prime]

    # Step 2: Count frequencies of each number in nums
    counts = {}
    for num in nums:
        counts[num] = counts.get(num, 0) + 1
    
    # Get unique numbers to avoid redundant calculations
    unique_nums = list(counts.keys())
    total_good_meals = 0

    # Step 3: Iterate through unique numbers and check prime sums
    for i in range(len(unique_nums)):
        num_a = unique_nums[i]
        count_a = counts[num_a]
        
        for p in primes:
            num_b = p - num_a
            
            # Case 1: num_a + num_b = p where num_a == num_b
            # We only process this when num_a == num_b to avoid double counting
            if num_b == num_a:
                if num_b in counts:
                    # Combination formula nC2: n * (n - 1) // 2
                    total_good_meals += (count_a * (count_a - 1)) // 2
            
            # Case 2: num_a + num_b = p where num_a < num_b
            # We use num_a < num_b to ensure each pair is counted exactly once
            elif num_b > num_a and num_b in counts:
                total_good_meals += count_a * counts[num_b]
                
    return total_good_meals
