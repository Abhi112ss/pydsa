METADATA = {
    "id": 1722,
    "name": "Minimize Hamming Distance After Swap Operations",
    "slug": "minimize-hamming-distance-after-swap-operations",
    "category": "Greedy",
    "aliases": [],
    "tags": ["greedy", "arrays", "hash-table"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Minimize the Hamming distance between two arrays by swapping elements within each array.",
}

def solve(nums1: list[int], nums2: list[int]) -> int:
    """
    Calculates the minimum Hamming distance between two arrays after any number of swaps.

    The Hamming distance is the number of positions where the elements are different.
    Since we can swap elements within nums1 and within nums2 arbitrarily, we can 
    rearrange both arrays into any permutation. To minimize the Hamming distance, 
    we want to maximize the number of indices i where nums1[i] == nums2[i].
    This is achieved by matching as many common elements as possible.

    Args:
        nums1: The first list of integers.
        nums2: The second list of integers.

    Returns:
        The minimum possible Hamming distance between the two arrays.

    Examples:
        >>> solve([1, 2, 3], [1, 2, 3])
        0
        >>> solve([1, 2, 3], [3, 2, 1])
        0
        >>> solve([1, 1, 2, 2], [2, 2, 1, 1])
        0
        >>> solve([1, 2, 3, 4], [5, 6, 7, 8])
        4
    """
    n = len(nums1)
    
    # Count the frequency of each number in both arrays
    counts1: dict[int, int] = {}
    counts2: dict[int, int] = {}
    
    for val in nums1:
        counts1[val] = counts1.get(val, 0) + 1
        
    for val in nums2:
        counts2[val] = counts2.get(val, 0) + 1
        
    # The maximum number of matches we can have is the sum of the 
    # minimum frequencies of each unique element present in both arrays.
    matches = 0
    
    # Iterate through the unique elements in the first array
    for val, count in counts1.items():
        if val in counts2:
            # The number of times this value can be paired is min(freq1, freq2)
            matches += min(count, counts2[val])
            
    # Hamming distance is the total length minus the number of matches
    return n - matches
