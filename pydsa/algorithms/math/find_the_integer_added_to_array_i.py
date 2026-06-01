METADATA = {
    "id": 3131,
    "name": "Find the Integer Added to Array I",
    "slug": "find-the-integer-added-to-array-i",
    "category": "Math",
    "aliases": [],
    "tags": ["math", "array", "arithmetic progression"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Find the missing integer in an arithmetic progression where each element increases by 1.",
}

def solve(nums: list[int]) -> int:
    """
    Finds the missing integer in an arithmetic progression where the common 
    difference is 1.

    The problem states that the array is an arithmetic progression with a 
    common difference of 1, but one integer has been removed.

    Args:
        nums: A list of integers representing the sequence with one missing element.

    Returns:
        The missing integer that completes the arithmetic progression.

    Examples:
        >>> solve([1, 2, 4, 5, 6])
        3
        >>> solve([10, 11, 12, 14])
        13
    """
    # The sequence is an arithmetic progression with difference 1.
    # The missing number can be found by calculating the difference between
    # the expected sum of the full range and the actual sum of the array.
    
    n = len(nums)
    actual_sum = sum(nums)
    
    # The full sequence should have (n + 1) elements.
    # The range starts at min(nums) and ends at max(nums).
    # Since the difference is 1, the sequence is simply [min, min+1, ..., max].
    start_val = nums[0]
    end_val = nums[-1]
    
    # The number of elements in the complete sequence is (end_val - start_val + 1).
    # However, we know exactly one element is missing, so the full sequence 
    # length must be n + 1.
    # The sum of an arithmetic progression is: (count * (first + last)) / 2
    count = n + 1
    expected_sum = (count * (start_val + end_val)) // 2
    
    # The difference between the expected sum and actual sum is the missing number.
    return expected_sum - actual_sum
