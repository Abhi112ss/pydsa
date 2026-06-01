METADATA = {
    "id": 3215,
    "name": "Count Triplets with Even XOR Set Bits II",
    "slug": "count_triplets_with_even_xor_set_bits_ii",
    "category": "Bit Manipulation",
    "aliases": [],
    "tags": ["bit_manipulation", "math", "combinatorics"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Count the number of triplets (i, j, k) such that the number of set bits in (nums[i] ^ nums[j] ^ nums[k]) is even.",
}

def solve(nums: list[int]) -> int:
    """
    Calculates the number of triplets (i, j, k) with 0 <= i < j < k < n such that 
    the number of set bits in (nums[i] ^ nums[j] ^ nums[k]) is even.

    The parity of the number of set bits in (a ^ b ^ c) is equal to 
    (parity(a) + parity(b) + parity(c)) % 2.
    For the XOR sum to have an even number of set bits, the sum of the parities 
    of the individual numbers must be even. This happens if:
    1. All three numbers have even parity.
    2. Exactly one number has even parity and two have odd parity.

    Args:
        nums: A list of integers.

    Returns:
        The total count of triplets satisfying the condition.

    Examples:
        >>> solve([1, 2, 3])
        1
        # 1 (01), 2 (10), 3 (11). Parities: 1, 1, 0.
        # 1^2^3 = 0 (00). Set bits: 0 (even). Triplet (0,1,2) works.
    """
    even_parity_count = 0
    odd_parity_count = 0

    for num in nums:
        # bin(num).count('1') % 2 gives the parity of set bits
        # Using bit_count() for Python 3.10+ efficiency
        if bin(num).count('1') % 2 == 0:
            even_parity_count += 1
        else:
            odd_parity_count += 1

    total_triplets = 0

    # Case 1: All three numbers have even parity.
    # Combination: C(even_parity_count, 3)
    if even_parity_count >= 3:
        total_triplets += (even_parity_count * (even_parity_count - 1) * (even_parity_count - 2)) // 6

    # Case 2: One number has even parity and two numbers have odd parity.
    # Combination: C(even_parity_count, 1) * C(odd_parity_count, 2)
    if even_parity_count >= 1 and odd_parity_count >= 2:
        total_triplets += even_parity_count * (odd_parity_count * (odd_parity_count - 1) // 2)

    return total_triplets
