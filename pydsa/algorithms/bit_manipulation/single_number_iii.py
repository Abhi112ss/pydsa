METADATA = {
    "id": 260,
    "name": "Single Number III",
    "slug": "single-number-iii",
    "category": "Bit Manipulation",
    "aliases": [],
    "tags": ["xor", "bit_mask", "bit-manipulation"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Find the two elements in an array that appear only once while all other elements appear twice.",
}

def solve(nums: list[int]) -> list[int]:
    """
    Finds the two unique numbers in an array where every other number appears twice.

    Args:
        nums: A list of integers where every element appears twice except for two.

    Returns:
        A list containing the two unique integers.

    Examples:
        >>> solve([1, 2, 1, 3, 2, 5])
        [3, 5]
        >>> solve([0, 1, 0, 1, 1])
        [1, 1] # Note: Problem constraints usually imply distinct single numbers.
    """
    # Step 1: XOR all numbers. 
    # The result will be (x ^ y) where x and y are the two unique numbers.
    xor_sum = 0
    for num in nums:
        xor_sum ^= num

    # Step 2: Find a bit that is set in xor_sum.
    # This bit must be set in one of the unique numbers and not the other.
    # We use the lowbit trick: x & -x gives the rightmost set bit.
    lowbit = xor_sum & -xor_sum

    # Step 3: Partition the numbers into two groups based on the lowbit.
    # One group will contain x, the other will contain y.
    # All other numbers appearing twice will fall into the same group and cancel out.
    unique_one = 0
    unique_two = 0
    
    for num in nums:
        if num & lowbit:
            unique_one ^= num
        else:
            unique_two ^= num

    return [unique_one, unique_two]
