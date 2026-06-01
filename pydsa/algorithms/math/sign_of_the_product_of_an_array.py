METADATA = {
    "id": 1822,
    "name": "Sign of the Product of an Array",
    "slug": "sign-of-the-product-of-an-array",
    "category": "Math",
    "aliases": [],
    "tags": ["counting", "sign_check"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Determine the sign of the product of all elements in an array without calculating the actual product.",
}

def solve(nums: list[int]) -> int:
    """
    Determines the sign of the product of all integers in the given array.

    The sign is determined by the number of negative integers and the presence 
    of any zero. Calculating the actual product is avoided to prevent integer 
    overflow.

    Args:
        nums: A list of integers.

    Returns:
        1 if the product is positive, -1 if the product is negative, 
        and 0 if the product is zero.

    Examples:
        >>> solve([1, 2, 3])
        1
        >>> solve([-1, -2, -3])
        -1
        >>> solve([-1, 2, -3, 4])
        1
        >>> solve([1, 2, 0])
        0
    """
    negative_count = 0

    for number in nums:
        # If any element is zero, the entire product is zero
        if number == 0:
            return 0
        
        # Count how many negative numbers exist to determine the final sign
        if number < 0:
            negative_count += 1

    # If the count of negative numbers is even, the product is positive.
    # If the count is odd, the product is negative.
    return 1 if negative_count % 2 == 0 else -1
