METADATA = {
    "id": 1726,
    "name": "Tuple with Same Product",
    "slug": "tuple-with-same-product",
    "category": "Hash Table",
    "aliases": [],
    "tags": ["hash_map", "arrays"],
    "difficulty": "medium",
    "time_complexity": "O(n^2)",
    "space_complexity": "O(n^2)",
    "description": "Count the number of pairs of tuples that have the same product of elements.",
}

def solve(nums: list[int]) -> int:
    """
    Counts the number of pairs of tuples that have the same product of elements.

    Args:
        nums: A list of integers where each integer represents a tuple's product.

    Returns:
        The total number of pairs of indices (i, j) such that i < j and 
        the product of elements in nums[i] equals the product of elements in nums[j].

    Examples:
        >>> solve([2, 2, 2])
        3
        >>> solve([1, 2, 2, 2])
        3
        >>> solve([3, 2, 5, 0, 0, 0, 1, 1])
        3
    """
    # Dictionary to store the frequency of each product encountered so far
    product_counts: dict[int, int] = {}
    total_pairs: int = 0

    for product in nums:
        # If the product has been seen before, every previous occurrence 
        # can form a valid pair with the current element.
        if product in product_counts:
            total_pairs += product_counts[product]
            product_counts[product] += 1
        else:
            product_counts[product] = 1

    return total_pairs
