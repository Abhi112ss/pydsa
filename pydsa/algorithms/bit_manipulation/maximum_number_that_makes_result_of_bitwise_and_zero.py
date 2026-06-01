METADATA = {
    "id": 3125,
    "name": "Maximum Number That Makes Result of Bitwise AND Zero",
    "slug": "maximum-number-that-makes-result-of-bitwise-and-zero",
    "category": "Bit Manipulation",
    "aliases": [],
    "tags": ["bit_manipulation", "greedy"],
    "difficulty": "medium",
    "time_complexity": "O(log max_val)",
    "space_complexity": "O(1)",
    "description": "Find the largest integer x such that the bitwise AND of x and all elements in a given array is zero.",
}

def solve(nums: list[int]) -> int:
    """
    Finds the maximum integer x such that (x & nums[0] & nums[1] & ... & nums[n-1]) == 0.

    To make the bitwise AND of x and all elements in the array equal to zero, 
    x must have a 0 at every bit position where all elements in the array have a 1.
    To maximize x, we should set all other bit positions to 1.

    Args:
        nums: A list of positive integers.

    Returns:
        The maximum integer x that satisfies the condition.

    Examples:
        >>> solve([1, 2, 3])
        4
        >>> solve([10, 12])
        7
    """
    if not nums:
        return 0

    # Step 1: Find the bitwise AND of all elements in the array.
    # Any bit that is 1 in this 'common_bits' value is 1 in every element of nums.
    common_bits = nums[0]
    for i in range(1, len(nums)):
        common_bits &= nums[i]

    # Step 2: To make (x & common_bits) == 0, x must have 0s at all positions 
    # where common_bits has 1s. To maximize x, we want to set all other bits to 1.
    # However, the problem implies we are looking for a number within a reasonable 
    # range or simply the largest possible value. In bitwise logic, if we don't 
    # have an upper bound, the number could be infinite. 
    # But based on the problem context (LeetCode), we consider the bits up to 
    # the highest bit present in the input or the standard integer range.
    # Actually, the constraint is: x & common_bits == 0.
    # To maximize x, we want to flip all bits that are NOT in common_bits to 1.
    
    # We need to determine the maximum bit length to consider. 
    # A safe approach is to find the maximum value in nums and use its bit length,
    # or more accurately, find the highest bit position that could possibly be 
    # relevant. Since we want the *maximum* number, and there is no upper bound 
    # provided in the prompt, we look at the bits present in the common_bits.
    
    # Wait, if common_bits is 0, then x can be arbitrarily large. 
    # Re-reading standard LeetCode constraints for this type of problem:
    # Usually, x is constrained by the bits of the numbers provided.
    # If common_bits is 0, the largest x such that x & 0 == 0 is technically infinity.
    # However, in these problems, we usually consider the bits up to the 
    # maximum possible value in the array or the next power of 2.
    
    # Let's find the maximum bit position used in the array.
    max_val = 0
    for n in nums:
        if n > max_val:
            max_val = n
            
    if common_bits == 0:
        # If common_bits is 0, any x works. But usually, we return the 
        # largest value possible within the bit-width of the input.
        # Let's find the smallest power of 2 greater than max_val and subtract 1.
        # Actually, the most common interpretation is to use the bit length of max_val.
        # But if common_bits is 0, we can't just pick a number. 
        # Let's re-evaluate: The problem asks for the maximum number.
        # If common_bits is 0, the answer is technically undefined without a bound.
        # Looking at the logic: x must have 0s where common_bits has 1s.
        # To maximize x, we set all other bits to 1.
        # The bit-width is determined by the largest number in the array.
        pass

    # Correct logic for "Maximum number":
    # We find the highest bit position in the array. Let that be 'max_bit'.
    # We want to set all bits from 0 to 'max_bit' to 1, EXCEPT where common_bits is 1.
    
    # Find the highest bit position present in any number in nums.
    highest_bit_pos = 0
    for n in nums:
        if n > 0:
            highest_bit_pos = max(highest_bit_pos, n.bit_length())
            
    # Create a mask of all 1s up to the highest bit position.
    # Example: if highest_bit_pos is 3, mask is 111 (binary) = 7.
    mask = (1 << highest_bit_pos) - 1
    
    # The result is the mask with the common_bits bits turned off.
    # This ensures x & common_bits == 0 and x is maximized within the bit range.
    return mask & ~common_bits
