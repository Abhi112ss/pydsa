METADATA = {
    "id": 3397,
    "name": "Maximum Number of Distinct Elements After Operations",
    "slug": "maximum-number-of-distinct-elements-after-operations",
    "category": "Greedy",
    "aliases": [],
    "tags": ["greedy", "hash_map"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Find the maximum number of distinct elements possible by performing operations to change elements within a given range.",
}

def solve(nums: list[int], k: int) -> int:
    """
    Calculates the maximum number of distinct elements possible after at most k operations.
    An operation consists of changing an element to any other integer.

    Args:
        nums: A list of integers representing the initial elements.
        k: The maximum number of operations allowed.

    Returns:
        The maximum number of distinct elements possible.

    Examples:
        >>> solve([1, 2, 2, 2, 3], 2)
        5
        >>> solve([1, 1, 1], 1)
        2
    """
    # Count the frequency of each number present in the array
    counts = {}
    for num in nums:
        counts[num] = counts.get(num, 0) + 1

    distinct_count = len(counts)
    # Calculate how many 'extra' elements we have (duplicates)
    # These are the elements we can potentially change to new distinct values
    extra_elements = 0
    for val in counts.values():
        extra_elements += (val - 1)

    # We want to use our k operations to turn extra elements into new distinct values.
    # However, we are limited by two things:
    # 1. The number of operations we actually have (k).
    # 2. The number of extra elements available to be changed.
    
    # Each operation can turn one 'extra' element into a brand new distinct element.
    # If we have more k than extra elements, we can't create more distinct elements 
    # than the total size of the array (n).
    # If we have more extra elements than k, we can only create k new distinct elements.
    
    # The number of new distinct elements we can add is min(k, extra_elements)
    # But wait, the problem asks for the maximum number of distinct elements.
    # If we have k operations, we can use them to change duplicates into values 
    # that don't exist in the set yet.
    
    # Let's refine:
    # Total distinct elements = (Initial distinct elements) + (New elements created)
    # New elements created = min(k, extra_elements)
    
    # Note: If k > extra_elements, we have used all duplicates to make new distinct values.
    # Any remaining k would have to be used on already distinct elements, 
    # which doesn't increase the count of distinct elements.
    
    new_distinct_elements = min(k, extra_elements)
    
    return distinct_count + new_distinct_elements
