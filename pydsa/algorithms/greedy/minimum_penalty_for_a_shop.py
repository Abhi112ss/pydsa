METADATA = {
    "id": 2483,
    "name": "Minimum Penalty for a Shop",
    "slug": "minimum-penalty-for-a-shop",
    "category": "Array",
    "aliases": [],
    "tags": ["greedy", "array", "prefix-sum"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Find the minimum penalty for splitting items between two customers such that the difference between the sums of their items is minimized.",
}

def solve(items: list[int], split: int) -> int:
    """
    Calculates the minimum penalty for splitting items between two customers.

    The penalty is defined as the absolute difference between the sum of items
    assigned to the first customer (items[0...split-1]) and the second 
    customer (items[split...n-1]).

    Args:
        items: A list of integers representing the value of each item.
        split: An integer representing the index where the split occurs.

    Returns:
        The absolute difference between the sums of the two partitions.

    Examples:
        >>> solve([4, 2, 5, 3], 2)
        2
        >>> solve([1, 2, 3, 4, 5], 3)
        3
    """
    total_sum = sum(items)
    
    # We track the running sum of the first customer's items.
    # The second customer's sum will always be (total_sum - current_sum).
    first_customer_sum = 0
    
    # Iterate up to the split index to calculate the sum of the first partition.
    for i in range(split):
        first_customer_sum += items[i]
        
    second_customer_sum = total_sum - first_customer_sum
    
    # The penalty is the absolute difference between the two sums.
    return abs(first_customer_sum - second_customer_sum)
