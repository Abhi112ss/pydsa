METADATA = {
    "id": 2708,
    "name": "Maximum Strength of a Group",
    "slug": "maximum-strength-of-a-group",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dp", "math", "greedy"],
    "difficulty": "medium",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(n)",
    "description": "Find the maximum product of a non-empty subset of an array.",
}

def solve(nums: list[int]) -> int:
    """
    Calculates the maximum strength of a group by finding the maximum product 
    of a non-empty subset of the given integers.

    The strategy involves:
    1. Separating numbers into positive, negative, and zero.
    2. Using all positive numbers.
    3. Pairing negative numbers to ensure their product is positive.
    4. Handling edge cases where no positive product can be formed.

    Args:
        nums: A list of integers.

    Returns:
        The maximum product possible from a non-empty subset.

    Examples:
        >>> solve([3, 4, 5, -2, -3, -2])
        120
        >>> solve([-1, -2, -3, -4])
        24
        >>> solve([0, -1])
        0
        >>> solve([-1])
        -1
    """
    if len(nums) == 1:
        return nums[0]

    positives = []
    negatives = []
    has_zero = False

    for num in nums:
        if num > 0:
            positives.append(num)
        elif num < 0:
            negatives.append(num)
        else:
            has_zero = True

    # Sort negatives to pair the largest absolute values first
    negatives.sort()

    product = 1
    used_elements = 0

    # Multiply all positive numbers
    for val in positives:
        product *= val
        used_elements += 1

    # Pair negative numbers: two negatives make a positive
    # We iterate in steps of 2 to take pairs
    for i in range(0, len(negatives) // 2 * 2, 2):
        pair_product = negatives[i] * negatives[i + 1]
        product *= pair_product
        used_elements += 2

    # Edge Case Handling:
    # If no elements were used to form a positive product (e.g., only one negative and zeros,
    # or only zeros), we must decide between 0 and the largest single negative.
    if used_elements == 0:
        if has_zero:
            return 0
        # If no zero and no positives, and we couldn't pair negatives, 
        # the max is the largest negative (closest to 0).
        return max(negatives)

    return product
