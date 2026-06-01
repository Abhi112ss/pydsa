METADATA = {
    "id": 477,
    "name": "Total Hamming Distance",
    "slug": "total-hamming-distance",
    "category": "Bit Manipulation",
    "aliases": [],
    "tags": ["bit_manipulation", "math"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Calculate the sum of Hamming distances between all pairs of integers in an array.",
}

def solve(nums: list[int]) -> int:
    """
    Calculates the total Hamming distance for all pairs in the given list.

    The Hamming distance between two integers is the number of positions at 
    which the corresponding bits are different. Instead of comparing all 
    pairs (O(n^2)), we count the number of 0s and 1s at each bit position.
    For a specific bit position, if there are 'k' ones and 'n-k' zeros, 
    there are exactly k * (n-k) pairs with different bits at that position.

    Args:
        nums: A list of integers.

    Returns:
        The total Hamming distance of all pairs in the list.

    Examples:
        >>> solve([4, 8, 2])
        2
        >>> solve([1, 1, 1])
        0
        >>> solve([0])
        0
    """
    total_distance = 0
    n = len(nums)
    
    # Integers in LeetCode problems are typically 32-bit signed/unsigned.
    # We iterate through each bit position from 0 to 30 (for positive integers).
    for bit_position in range(32):
        count_ones = 0
        mask = 1 << bit_position
        
        for num in nums:
            # Check if the bit at the current position is set
            if num & mask:
                count_ones += 1
        
        # The number of zeros at this bit position is (total elements - count of ones)
        count_zeros = n - count_ones
        
        # Each pair consisting of one '1' and one '0' contributes 1 to the total distance
        total_distance += count_ones * count_zeros
        
    return total_distance
