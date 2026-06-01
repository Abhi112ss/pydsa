METADATA = {
    "id": 3896,
    "name": "Minimum Operations to Transform Array into Alternating Prime",
    "slug": "minimum-operations-to-transform-array-into-alternating-prime",
    "category": "Greedy",
    "aliases": [],
    "tags": ["greedy", "math", "sieve"],
    "difficulty": "medium",
    "time_complexity": "O(N * max_val)",
    "space_complexity": "O(max_val)",
    "description": "Find the minimum operations to make an array alternate between two prime numbers.",
}

def solve(nums: list[int]) -> int:
    """
    Calculates the minimum number of operations to transform an array into an 
    alternating sequence of two prime numbers.

    An alternating sequence is defined as [p1, p2, p1, p2, ...].
    An operation consists of changing an element to any prime number.

    Args:
        nums: A list of integers.

    Returns:
        The minimum number of operations required.

    Examples:
        >>> solve([1, 2, 1, 2])
        2
        >>> solve([3, 5, 7, 11])
        2
    """
    if not nums:
        return 0

    max_val = max(nums)
    # We need to consider primes up to max_val, but since we can change 
    # elements to ANY prime, we should consider the smallest primes 
    # if the array is large. However, the problem implies we transform 
    # existing values or pick new ones. To minimize operations, we 
    # want to keep as many existing elements as possible that are already prime.
    
    # Step 1: Sieve of Eratosthenes to find all primes up to max_val
    is_prime = [True] * (max_val + 1)
    is_prime[0] = is_prime[1] = False
    for p in range(2, int(max_val**0.5) + 1):
        if is_prime[p]:
            for i in range(p * p, max_val + 1, p):
                is_prime[i] = False
    
    primes = [p for p, prime in enumerate(is_prime) if prime]
    
    # If no primes exist in the range, we must change all elements to 
    # the smallest prime (2). But since we can pick ANY prime, 
    # we just need to find the best two primes.
    
    # To minimize operations, we maximize the number of elements we KEEP.
    # An element at index i can be kept if:
    # 1. nums[i] is prime.
    # 2. If i is even, nums[i] == p1.
    # 3. If i is odd, nums[i] == p2.
    
    # Count occurrences of primes at even and odd indices
    even_index_primes = {}
    odd_index_primes = {}
    
    for i, val in enumerate(nums):
        if is_prime[val]:
            if i % 2 == 0:
                even_index_primes[val] = even_index_primes.get(val, 0) + 1
            else:
                odd_index_primes[val] = odd_index_primes.get(val, 0) + 1
                
    # Case 1: p1 and p2 are different
    # We want to maximize even_index_primes[p1] + odd_index_primes[p2]
    # where p1 != p2.
    
    # Get top two primes for even indices and top two for odd indices
    # to handle the p1 != p2 constraint.
    def get_top_two(d: dict[int, int]) -> list[tuple[int, int]]:
        # Returns list of (prime, count) sorted by count descending
        return sorted(d.items(), key=lambda x: x[1], reverse=True)[:2]

    top_even = get_top_two(even_index_primes)
    top_odd = get_top_two(odd_index_primes)
    
    max_kept = 0
    
    # Try combinations of top primes
    # If we pick p1 from top_even and p2 from top_odd
    if not top_even and not top_odd:
        # No primes in array at all, must change all
        max_kept = 0
    elif not top_even:
        # Only odd indices have primes
        # We can pick p1 as any prime (0 kept) and p2 as top_odd[0]
        max_kept = top_odd[0][1]
    elif not top_odd:
        # Only even indices have primes
        max_kept = top_even[0][1]
    else:
        # Both have primes, check if they are the same
        for p_even, count_even in top_even:
            for p_odd, count_odd in top_odd:
                if p_even != p_odd:
                    max_kept = max(max_kept, count_even + count_odd)
                else:
                    # If they are the same, we can't use both as p1 and p2 
                    # for an alternating sequence unless we pick a different 
                    # prime for one of them.
                    # Option A: Use p_even as p1, and the next best p_odd as p2
                    # Option B: Use p_odd as p2, and the next best p_even as p1
                    # These are covered by the loop if we had more than 1 in top_even/odd
                    pass
        
        # If the best p_even and p_odd are the same, we must consider 
        # the possibility that the best strategy is to pick a prime 
        # that isn't in the top list (count 0) or the second best.
        # The logic above handles p_even != p_odd. 
        # If all primes in even are the same as all primes in odd:
        # We either take (top_even[0] + second_best_odd) or (second_best_even + top_odd[0])
        
        # Check if we can pick p1 = p_even and p2 = some other prime
        # or p2 = p_odd and p1 = some other prime.
        # This is actually covered if we consider the case where one count is 0.
        # Let's refine:
        
        # Try all combinations of top 2 from each
        # Also consider the case where we pick a prime that exists in one but not the other
        # or a prime that exists in neither (count 0).
        
        # To be safe, if top_even[0][0] == top_odd[0][0], 
        # max_kept is max(top_even[0][1] + (top_odd[1][1] if len(top_odd)>1 else 0),
        #                top_odd[0][1] + (top_even[1][1] if len(top_even)>1 else 0))
        
        # The nested loop above handles this if we ensure we check 
        # the case where we pick a prime with 0 count.
        # Let's add a dummy prime with 0 count to the lists.
        
        # Re-calculating max_kept more robustly:
        max_kept = 0
        # Candidates for p1: top_even primes + one prime not in top_even
        # Candidates for p2: top_odd primes + one prime not in top_odd
        
        # Actually, the only way to get a high max_kept is to use existing primes.
        # If p1 == p2, we can't use them. We must pick p1 != p2.
        # The best p1, p2 will either be:
        # 1. p1 in top_even, p2 in top_odd (where p1 != p2)
        # 2. p1 in top_even, p2 is some other prime (count 0)
        # 3. p2 in top_odd, p1 is some other prime (count 0)
        
        # Case 1:
        for p_e, c_e in top_even:
            for p_o, c_o in top_odd:
                if p_e != p_o:
                    max_kept = max(max_kept, c_e + c_o)
        
        # Case 2 & 3:
        if top_even:
            max_kept = max(max_kept, top_even[0][1])
        if top_odd:
            max_kept = max(max_kept, top_odd[0][1])

    # Total operations = total elements - max elements we can keep
    return len(nums) - max_kept
