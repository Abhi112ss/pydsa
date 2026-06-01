METADATA = {
    "id": 3621,
    "name": "Number of Integers With Popcount-Depth Equal to K I",
    "slug": "number-of-integers-with-popcount-depth-equal-to-k-i",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["digit_dp", "bit_manipulation", "math"],
    "difficulty": "hard",
    "time_complexity": "O(log10(n) * log(n))",
    "space_complexity": "O(log10(n))",
    "description": "Count integers up to n whose popcount-depth equals k using digit DP.",
}

def solve(n_str: str, k: int) -> int:
    """
    Counts the number of integers in the range [1, n] whose popcount-depth equals k.
    
    The popcount-depth is defined as the number of steps to reach 1 by repeatedly 
    applying the popcount function (number of set bits).
    
    Args:
        n_str: The upper bound n as a string.
        k: The target popcount-depth.

    Returns:
        The count of integers in [1, n] with popcount-depth equal to k.

    Examples:
        >>> solve("10", 1)
        4  # Popcounts: 1(1), 2(1), 3(2), 4(1), 5(2), 6(2), 7(3), 8(1), 9(2), 10(2)
           # Depth 1: 1, 2, 4, 8. Wait, depth is steps to reach 1.
           # Let f(x) = popcount(x). Depth(x) = 1 + Depth(f(x)) if x > 1, else 0.
           # If k=1: f(x)=1. x in {1, 2, 4, 8}.
    """
    MOD = 10**9 + 7
    
    # Precompute depth for small values (up to max possible popcount of n)
    # Max n is ~10^100, so max popcount is ~333 (for 10^100 < 2^333)
    # We'll use a safe upper bound for popcount.
    MAX_POPCOUNT = 1000 
    depth_map = [0] * (MAX_POPCOUNT + 1)
    
    def get_popcount(x: int) -> int:
        return bin(x).count('1')

    # depth_map[i] = steps to reach 1 starting from i
    # depth_map[1] = 0
    for i in range(2, MAX_POPCOUNT + 1):
        depth_map[i] = 1 + depth_map[get_popcount(i)]

    # We need to find x in [1, n] such that depth(x) == k
    # If k=0, only x=1 works.
    # If k > 0, depth(x) = 1 + depth(popcount(x)) = k => depth(popcount(x)) = k - 1
    
    if k == 0:
        return 1 if int(n_str) >= 1 else 0

    # Target popcounts: set of integers p such that depth_map[p] == k - 1
    target_popcounts = []
    for p in range(1, MAX_POPCOUNT + 1):
        if depth_map[p] == k - 1:
            target_popcounts.append(p)

    # Digit DP to count numbers <= n with a specific popcount
    # Since n is given as a string (base 10), but popcount is base 2, 
    # we convert n to binary to perform digit DP on bits.
    n_val = int(n_str)
    binary_n = bin(n_val)[2:]
    num_bits = len(binary_n)

    # memoization for digit DP: (index, current_popcount, is_less, is_started)
    memo = {}

    def count_with_popcount(idx: int, current_pop: int, is_less: bool, target_pop: int) -> int:
        state = (idx, current_pop, is_less)
        if state in memo:
            return memo[state]
        
        if current_pop > target_pop:
            return 0
        
        if idx == num_bits:
            return 1 if current_pop == target_pop else 0
        
        res = 0
        limit = int(binary_n[idx]) if not is_less else 1
        
        for digit in range(limit + 1):
            new_is_less = is_less or (digit < limit)
            new_pop = current_pop + (1 if digit == 1 else 0)
            res += count_with_popcount(idx + 1, new_pop, new_is_less, target_pop)
            
        memo[state] = res
        return res

    total_count = 0
    # We need to sum counts for all valid target popcounts
    # Note: x=0 is not in [1, n], but popcount(0)=0, and depth(0) is undefined.
    # The problem implies x >= 1.
    for p in target_popcounts:
        memo = {}
        # count_with_popcount counts numbers in [0, n] with popcount p
        # Since p >= 1, 0 is never counted.
        total_count = (total_count + count_with_popcount(0, 0, False, p)) % MOD

    # Special case: if k=1, depth(x)=1 means popcount(x)=1.
    # The loop above handles this: target_popcounts will contain p where depth_map[p]=0.
    # depth_map[1] is 0, so p=1 is in target_popcounts.
    
    return total_count
