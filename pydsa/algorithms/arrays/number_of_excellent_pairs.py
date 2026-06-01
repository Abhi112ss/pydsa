METADATA = {
    "id": 2354,
    "name": "Number of Excellent Pairs",
    "slug": "number-of-excellent-pairs",
    "category": "Bit Manipulation",
    "aliases": [],
    "tags": ["hash_map", "bit_manipulation", "counting"],
    "difficulty": "medium",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(n)",
    "description": "Count pairs (a, b) such that the number of set bits in (a AND b) plus the number of set bits in (a OR b) is maximized.",
}

def solve(nums: list[int]) -> int:
    """
    Calculates the number of excellent pairs (a, b) that maximize bit_count(a & b) + bit_count(a | b).

    The key insight is the bitwise identity: bit_count(a & b) + bit_count(a | b) = bit_count(a) + bit_count(b).
    Therefore, we need to find pairs (a, b) such that bit_count(a) + bit_count(b) is maximized.

    Args:
        nums: A list of integers.

    Returns:
        The number of excellent pairs modulo 10^9 + 7.

    Examples:
        >>> solve([1, 2, 3, 4])
        4
        >>> solve([8, 1, 2, 3, 4, 5, 6, 7])
        12
    """
    MOD = 10**9 + 7
    
    # Count the frequency of each bit count present in the input array.
    # Since nums[i] <= 10^9, the maximum number of set bits is 30.
    bit_counts = [0] * 31
    for num in nums:
        # bin(num).count('1') is efficient in Python for counting set bits.
        count = bin(num).count('1')
        bit_counts[count] += 1
        
    max_sum = 0
    # Find the maximum possible sum of bit counts from any two elements.
    # We iterate through all possible bit count combinations.
    for i in range(31):
        if bit_counts[i] == 0:
            continue
        for j in range(31):
            if bit_counts[j] == 0:
                continue
            if i + j > max_sum:
                max_sum = i + j
                
    # Count how many pairs (a, b) result in the max_sum.
    # A pair is formed by picking one element with bit_count i and one with bit_count j.
    total_excellent_pairs = 0
    for i in range(31):
        if bit_counts[i] == 0:
            continue
        # We need j such that i + j == max_sum
        j = max_sum - i
        if 0 <= j <= 30:
            # The number of ways to pick one from group i and one from group j.
            total_excellent_pairs += bit_counts[i] * bit_counts[j]
            
    return total_excellent_pairs % MOD
