METADATA = {
    "id": 3566,
    "name": "Partition Array into Two Equal Product Subsets",
    "slug": "partition-array-into-two-equal-product-subsets",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dp", "math", "subset sum"],
    "difficulty": "medium",
    "time_complexity": "O(n * target_product)",
    "space_complexity": "O(target_product)",
    "description": "Determine if an array can be partitioned into two subsets such that the product of elements in each subset is equal.",
}

import math

def solve(nums: list[int]) -> bool:
    """
    Determines if the given array can be partitioned into two subsets with equal products.

    The problem is equivalent to finding if a subset exists whose product is 
    exactly the square root of the total product of the array. To avoid 
    integer overflow and handle large products, we use the property that 
    if the total product is P, we need a subset with product sqrt(P).

    Args:
        nums: A list of positive integers.

    Returns:
        True if such a partition exists, False otherwise.

    Examples:
        >>> solve([2, 2, 4, 4])
        True
        >>> solve([1, 2, 3, 6])
        True
        >>> solve([2, 3, 4])
        False
    """
    if not nums:
        return True

    total_product = 1
    for num in nums:
        total_product *= num

    # If the total product is not a perfect square, we cannot partition it into two equal products
    root = math.isqrt(total_product)
    if root * root != total_product:
        return False

    target = root

    # We use a DP approach similar to the Subset Sum problem.
    # dp[i] will be True if a product of 'i' can be formed using a subset of nums.
    # Since we are dealing with products, we use a set or a boolean array up to 'target'.
    # Given the constraints and the nature of products, a set is often more efficient 
    # if the target is large but the number of reachable products is sparse.
    
    # However, to strictly follow the O(n * target) requirement:
    dp = [False] * (target + 1)
    dp[1] = True  # Base case: product of 1 is always possible with an empty subset

    for num in nums:
        # Iterate backwards to ensure each element is used at most once (0/1 Knapsack style)
        # We only care about products that are divisors of the target.
        for current_product in range(target, num - 1, -1):
            # If (current_product / num) was a reachable product, then current_product is reachable
            if current_product % num == 0:
                prev_product = current_product // num
                if dp[prev_product]:
                    dp[current_product] = True
                    
        # Optimization: if we already found the target, we can exit early
        if dp[target]:
            return True

    return dp[target]
