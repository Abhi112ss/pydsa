METADATA = {
    "id": 238,
    "name": "Product of Array Except Self",
    "slug": "product_of_array_except_self",
    "category": "Arrays",
    "aliases": [],
    "tags": ["arrays", "prefix_sum"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Return an array such that each element at index i is the product of all elements in the original array except the one at index i, without using division.",
}

def solve(nums: list[int]) -> list[int]:
    """
    Computes the product of all elements in the array except the element at the current index.

    The algorithm uses a two-pass approach:
    1. First pass: Calculate the prefix product for each index and store it in the result array.
    2. Second pass: Calculate the suffix product on the fly and multiply it with the existing prefix product.

    Args:
        nums: A list of integers.

    Returns:
        A list of integers where each element is the product of all other elements.

    Examples:
        >>> solve([1, 2, 3, 4])
        [24, 12, 8, 6]
        >>> solve([-1, 1, 0, -3, 3])
        [0, 0, 9, 0, 0]
    """
    n = len(nums)
    # Initialize the result array with 1s
    result = [1] * n

    # First pass: Calculate prefix products.
    # result[i] will contain the product of all elements to the left of index i.
    prefix_product = 1
    for i in range(n):
        result[i] = prefix_product
        prefix_product *= nums[i]

    # Second pass: Calculate suffix products and multiply with prefix products.
    # suffix_product will track the product of all elements to the right of index i.
    suffix_product = 1
    for i in range(n - 1, -1, -1):
        # Multiply the existing prefix product (stored in result[i]) by the suffix product
        result[i] *= suffix_product
        # Update the suffix product for the next element to the left
        suffix_product *= nums[i]

    return result
