METADATA = {
    "id": 3670,
    "name": "Maximum Product of Two Integers With No Common Bits",
    "slug": "maximum_product_of_two_integers_with_no_common_bits",
    "category": "Bit Manipulation",
    "aliases": [],
    "tags": ["bit_manipulation", "arrays"],
    "difficulty": "medium",
    "time_complexity": "O(n^2)",
    "space_complexity": "O(1)",
    "description": "Find the maximum product of two integers in an array such that they share no common set bits.",
}

def solve(nums: list[int]) -> int:
    """
    Finds the maximum product of two integers in the list that have no common set bits.

    Two integers have no common bits if their bitwise AND result is zero.

    Args:
        nums: A list of integers.

    Returns:
        The maximum product of two integers from the list that share no common bits.
        Returns 0 if no such pair exists.

    Examples:
        >>> solve([1, 2, 4, 8])
        64
        >>> solve([3, 4, 5])
        20
        >>> solve([1, 1, 1])
        0
    """
    max_product = 0
    n = len(nums)

    # Iterate through all unique pairs in the array
    for i in range(n):
        for j in range(i + 1, n):
            # Check if the two numbers have no common set bits using bitwise AND
            if (nums[i] & nums[j]) == 0:
                # Calculate product and update the maximum found so far
                current_product = nums[i] * nums[j]
                if current_product > max_product:
                    max_product = current_product

    return max_product
