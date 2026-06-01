METADATA = {
    "id": 3255,
    "name": "Find the Power of K-Size Subarrays II",
    "slug": "find-the-power-of-k-size-subarrays-ii",
    "category": "Array",
    "aliases": [],
    "tags": ["sliding_window", "arrays", "math"],
    "difficulty": "hard",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Calculate the sum of powers of all k-sized subarrays where power is defined by the product of elements modulo k.",
}

def solve(nums: list[int], k: int) -> int:
    """
    Calculates the sum of the products of all k-sized subarrays modulo k.
    
    The power of a subarray is defined as (product of all elements in subarray) % k.
    The goal is to find the sum of these powers for all possible k-sized subarrays.
    
    Note: Since we need (product % k), and k can be large, we must handle 
    the sliding window carefully. However, the problem asks for the sum of 
    (product % k). A standard sliding window with division is tricky if 
    elements are not coprime to k. 
    
    Wait, the problem definition for "Power of K-Size Subarrays II" usually 
    implies a specific mathematical property or a constraint where we can 
    efficiently update the product. If k is prime, we use modular inverse. 
    If k is not prime, we track the count of prime factors of k present in the window.

    Args:
        nums: A list of integers.
        k: The size of the subarray and the modulus.

    Returns:
        The sum of the powers of all k-sized subarrays.

    Examples:
        >>> solve([1, 2, 3, 4], 2)
        # Subarrays of size 2: [1,2], [2,3], [3,4]
        # (1*2)%2 = 0; (2*3)%2 = 0; (3*4)%2 = 0. Sum = 0.
        0
    """
    n = len(nums)
    if k > n:
        return 0

    # To handle non-coprime elements with a sliding window, we track 
    # the prime factorization of k.
    # Let k = p1^a1 * p2^a2 * ...
    # For any product P, P % k can be calculated if we know:
    # 1. The product of all elements in the window that are NOT divisible by any pi.
    # 2. The total count of each prime factor pi in the window.
    
    # Step 1: Factorize k
    temp_k = k
    factors = {}
    d = 2
    while d * d <= temp_k:
        if temp_k % d == 0:
            count = 0
            while temp_k % d == 0:
                count += 1
                temp_k //= d
            factors[d] = count
        d += 1
    if temp_k > 1:
        factors[temp_k] = factors.get(temp_k, 0) + 1

    # Step 2: Prepare to track window state
    # current_prime_counts: maps prime factor -> count in current window
    # current_product_coprime: product of elements in window after removing all factors of k
    current_prime_counts = {p: 0 for p in factors}
    current_product_coprime = 1
    MOD = 10**9 + 7 # Standard large prime for sum if required, though problem asks for sum of (prod % k)

    def get_val_info(val: int):
        """Returns (product_without_k_factors, {prime_factor: count})"""
        p_prod = val
        p_counts = {}
        for p in factors:
            count = 0
            while p_prod > 0 and p_prod % p == 0:
                count += 1
                p_prod //= p
            if count > 0:
                p_counts[p] = count
        return p_prod % k, p_counts

    # Since we need (product % k), we can't just use modular inverse if gcd(val, k) > 1.
    # Instead, we maintain:
    # product = (product_of_coprime_parts) * (p1^c1 * p2^c2 * ...)
    # We calculate this modulo k.
    
    def calculate_current_mod_k() -> int:
        res = current_product_coprime
        for p, count in current_prime_counts.items():
            # We need to multiply res by p^count, but we must do it carefully
            # to avoid overflow before modulo, though Python handles large ints.
            # However, we only care about the result modulo k.
            # We use pow(p, count, k)
            res = (res * pow(p, count, k)) % k
        return res

    # Initial window
    for i in range(k):
        val = nums[i]
        p_prod, p_counts = get_val_info(val)
        current_product_coprime = (current_product_coprime * p_prod) % k
        for p, count in p_counts.items():
            current_prime_counts[p] += count

    total_sum = calculate_current_mod_k()

    # Sliding window
    for i in range(k, n):
        # Remove nums[i-k]
        old_val = nums[i-k]
        old_p_prod, old_p_counts = get_val_info(old_val)
        
        # Modular inverse for the coprime part
        # Since current_product_coprime is coprime to k, we can use pow(x, -1, k) 
        # if we use a modular inverse function or pow(x, phi(k)-1, k)
        # But wait, current_product_coprime is not necessarily coprime to k 
        # if we only removed factors of k. 
        # Actually, by definition of get_val_info, p_prod is coprime to k.
        # Therefore, we can use modular inverse.
        
        # To avoid needing Euler's Totient, we can use the property that 
        # current_product_coprime is always coprime to k.
        # We need to find x such that (x * old_p_prod) % k == current_product_coprime
        # We use the extended Euclidean algorithm for modular inverse.
        
        def extended_gcd(a: int, b: int):
            if a == 0: return b, 0, 1
            gcd, x1, y1 = extended_gcd(b % a, a)
            x = y1 - (b // a) * x1
            y = x1
            return gcd, x, y

        def mod_inverse(a: int, m: int):
            gcd, x, y = extended_gcd(a, m)
            if gcd != 1: return None
            return (x % m + m) % m

        inv = mod_inverse(old_p_prod, k)
        current_product_coprime = (current_product_coprime * inv) % k
        for p, count in old_p_counts.items():
            current_prime_counts[p] -= count

        # Add nums[i]
        new_val = nums[i]
        new_p_prod, new_p_counts = get_val_info(new_val)
        current_product_coprime = (current_product_coprime * new_p_prod) % k
        for p, count in new_p_counts.items():
            current_prime_counts[p] += count
            
        total_sum += calculate_current_mod_k()

    return total_sum

# Note: The problem description in the prompt is slightly ambiguous regarding 
# the sum's modulus. Usually, LeetCode problems ask for (sum % 10^9 + 7).
# However, the "Power" itself is defined as (product % k).
# I will implement the logic to return the sum of (product % k).
