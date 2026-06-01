METADATA = {
    "id": 2064,
    "name": "Minimized Maximum of Products Distributed to Any Store",
    "slug": "minimized-maximum-of-products-distributed-to-any-store",
    "category": "Binary Search",
    "aliases": [],
    "tags": ["binary_search", "greedy"],
    "difficulty": "medium",
    "time_complexity": "O(n log(max_product))",
    "space_complexity": "O(1)",
    "description": "Find the minimum possible value of the maximum number of products distributed to any store using binary search on the answer.",
}

def solve(items: list[int], stores: int) -> int:
    """
    Finds the minimum possible maximum number of products distributed to any store.

    Args:
        items: A list of integers representing the number of products in each package.
        stores: An integer representing the number of available stores.

    Returns:
        The minimized maximum number of products distributed to any store.

    Examples:
        >>> solve([4, 2, 5, 9], 3)
        5
        >>> solve([1, 1, 1], 1)
        3
        >>> solve([10, 10, 10], 10)
        3
    """
    
    def can_distribute(max_per_store: int) -> bool:
        """
        Checks if it is possible to distribute all items such that no store 
        receives more than `max_per_store` products.
        """
        if max_per_store == 0:
            return False
            
        total_stores_needed = 0
        for item_count in items:
            # Calculate how many stores are needed for the current package.
            # Using (item_count + max_per_store - 1) // max_per_store is a 
            # standard way to perform ceiling division.
            stores_for_this_package = (item_count + max_per_store - 1) // max_per_store
            total_stores_needed += stores_for_this_package
            
            # Early exit if we exceed the available stores
            if total_stores_needed > stores:
                return False
        return True

    # The lower bound is 1 (since items are positive and we must distribute them).
    # The upper bound is the sum of all items (all items in one store).
    low = 1
    high = sum(items)
    result = high

    # Binary search for the smallest valid 'max_per_store'
    while low <= high:
        mid = (low + high) // 2
        if can_distribute(mid):
            # If mid is feasible, try to find a smaller maximum
            result = mid
            high = mid - 1
        else:
            # If mid is not feasible, we must increase the allowed maximum
            low = mid + 1

    return result
