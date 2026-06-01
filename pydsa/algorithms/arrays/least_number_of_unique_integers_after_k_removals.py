METADATA = {
    "id": 1481,
    "name": "Least Number of Unique Integers after K Removals",
    "slug": "least-number-of-unique-integers-after-k-removals",
    "category": "Greedy",
    "aliases": [],
    "tags": ["greedy", "hash_map", "sorting"],
    "difficulty": "medium",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(n)",
    "description": "Find the minimum number of unique integers remaining after removing exactly k elements from an array.",
}

from collections import Counter

def solve(arr: list[int], k: int) -> int:
    """
    Calculates the minimum number of unique integers remaining after removing k elements.

    The strategy is to use a greedy approach: count the frequency of each integer,
    sort these frequencies in ascending order, and remove the integers with the
    smallest frequencies first to minimize the count of unique integers.

    Args:
        arr: A list of integers.
        k: The number of elements to remove.

    Returns:
        The minimum number of unique integers remaining in the array.

    Examples:
        >>> solve([4, 3, 1, 1, 3, 3, 2], 3)
        2
        >>> solve([5, 5, 5, 5], 1)
        1
        >>> solve([1, 2, 3], 3)
        0
    """
    # Step 1: Count the frequency of each integer
    counts = Counter(arr)
    
    # Step 2: Extract the frequencies and sort them ascendingly
    # We want to eliminate as many unique numbers as possible, 
    # so we target those with the smallest counts first.
    frequencies = sorted(counts.values())
    
    unique_count = len(frequencies)
    
    # Step 3: Iterate through sorted frequencies and subtract from k
    for freq in frequencies:
        if k >= freq:
            # We have enough removals left to completely eliminate this unique integer
            k -= freq
            unique_count -= 1
        else:
            # We cannot fully eliminate this integer or any subsequent ones
            break
            
    return unique_count
