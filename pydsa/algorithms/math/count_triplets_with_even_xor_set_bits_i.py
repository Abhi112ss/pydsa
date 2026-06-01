METADATA = {
    "id": 3199,
    "name": "Count Triplets with Even XOR Set Bits I",
    "slug": "count-triplets-with-even-xor-set-bits-i",
    "category": "Bit Manipulation",
    "aliases": [],
    "tags": ["bit_manipulation", "math"],
    "difficulty": "medium",
    "time_complexity": "O(n^3)",
    "space_complexity": "O(1)",
    "description": "Count the number of triplets (i, j, k) such that the number of set bits in (nums[i] ^ nums[j] ^ nums[k]) is even.",
}

def solve(nums: list[int]) -> int:
    """
    Counts the number of triplets (i, j, k) where 0 <= i < j < k < n 
    such that the bitwise XOR of nums[i], nums[j], and nums[k] has an even 
    number of set bits (1s).

    Args:
        nums: A list of integers.

    Returns:
        The total count of triplets satisfying the condition.

    Examples:
        >>> solve([3, 1, 2])
        1
        >>> solve([1, 2, 3, 4, 5])
        4
    """
    n = len(nums)
    triplet_count = 0

    # Iterate through all unique combinations of triplets (i, j, k)
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                # Calculate the XOR sum of the triplet
                xor_sum = nums[i] ^ nums[j] ^ nums[k]
                
                # Check if the number of set bits (1s) in the XOR sum is even.
                # bit_count() is available in Python 3.10+
                if bin(xor_sum).count('1') % 2 == 0:
                    triplet_count += 1
                    
    return triplet_count
