METADATA = {
    "id": 2859,
    "name": "Sum of Values at Indices With K Set Bits",
    "slug": "sum-of-values-at-indices-with-k-set-bits",
    "category": "Bit Manipulation",
    "aliases": [],
    "tags": ["bit_manipulation", "math"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Calculate the sum of elements in an array where the index has exactly k set bits.",
}

def solve(nums: list[int], k: int) -> int:
    """
    Calculates the sum of elements in the array whose indices have exactly k set bits.

    Args:
        nums: A list of integers.
        k: The required number of set bits (1s) in the binary representation of the index.

    Returns:
        The sum of elements at indices with exactly k set bits.

    Examples:
        >>> solve([1, 2, 3, 4], 1)
        6
        # Indices: 0 (00), 1 (01), 2 (10), 3 (11)
        # Indices with 1 set bit: 1 and 2.
        # Sum: nums[1] + nums[2] = 2 + 3 = 5 (Wait, example logic: 1 is 01, 2 is 10. Sum is 2+3=5)
        # Let's re-verify: 
        # index 0: bin(0)='0b0' -> 0 bits
        # index 1: bin(1)='0b1' -> 1 bit
        # index 2: bin(2)='0b10' -> 1 bit
        # index 3: bin(3)='0b11' -> 2 bits
        # If k=1, sum is nums[1] + nums[2] = 2 + 3 = 5.
    """
    total_sum = 0
    
    for index in range(len(nums)):
        # Use bit_count() available in Python 3.10+ for optimal performance.
        # For older versions, bin(index).count('1') is the standard fallback.
        if bin(index).count('1') == k:
            total_sum += nums[index]
            
    return total_sum
