METADATA = {
    "id": 3821,
    "name": "Find Nth Smallest Integer With K One Bits",
    "slug": "find_nth_smallest_integer_with_k_one_bits",
    "category": "Math",
    "aliases": [],
    "tags": ["binary_search", "combinatorics", "digit_dp"],
    "difficulty": "medium",
    "time_complexity": "O(log^2(max_val))",
    "space_complexity": "O(1)",
    "description": "Find the n-th smallest integer that has exactly k set bits using binary search and combinatorics.",
}

def solve(n: int, k: int) -> int:
    """
    Finds the n-th smallest integer that has exactly k set bits.

    Args:
        n (int): The rank of the integer to find (1-indexed).
        k (int): The exact number of set bits (1s) required.

    Returns:
        int: The n-th smallest integer with exactly k set bits.

    Examples:
        >>> solve(1, 1)
        1
        >>> solve(3, 2)
        5
    """
    
    # Precompute combinations (Pascal's triangle) up to 64 bits
    # Since we are dealing with integers up to ~2^64, 64 is a safe upper bound.
    C = [[0] * 65 for _ in range(65)]
    for i in range(65):
        C[i][0] = 1
        for j in range(1, i + 1):
            C[i][j] = C[i - 1][j - 1] + C[i - 1][j]

    def count_with_k_bits(limit: int, target_k: int) -> int:
        """
        Counts how many integers in the range [0, limit] have exactly target_k bits set.
        Uses a digit-based combinatorial approach.
        """
        if target_k < 0:
            return 0
        
        count = 0
        current_k = target_k
        # Iterate through bits from most significant to least significant
        for i in range(63, -1, -1):
            if (limit >> i) & 1:
                # If the i-th bit is set, we can count all numbers where this bit is 0
                # and we choose current_k bits from the remaining i positions.
                count += C[i][current_k]
                current_k -= 1
                if current_k < 0:
                    break
        
        # Check if the limit itself has exactly target_k bits
        if current_k == 0:
            count += 1
            
        return count

    # Binary search for the smallest integer X such that count_with_k_bits(X, k) >= n
    # The range is from 0 to 2^64 - 1 (or a sufficiently large number)
    low = 0
    high = (1 << 64) - 1
    ans = high

    while low <= high:
        mid = (low + high) // 2
        # If the number of integers <= mid with k bits is at least n,
        # then mid could be our answer, but we look for a smaller one.
        if count_with_k_bits(mid, k) >= n:
            ans = mid
            high = mid - 1
        else:
            low = mid + 1

    return ans
