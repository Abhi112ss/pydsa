METADATA = {
    "id": 3852,
    "name": "Smallest Pair With Different Frequencies",
    "slug": "smallest_pair_with_different_frequencies",
    "category": "Array",
    "aliases": [],
    "tags": ["hash_map", "sorting"],
    "difficulty": "medium",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(n)",
    "description": "Find the smallest pair of elements in an array such that their frequencies in the array are different.",
}

def solve(nums: list[int]) -> list[int]:
    """
    Finds the smallest pair (a, b) such that frequency(a) != frequency(b).
    The pair is considered smaller if a is smaller, or if a == b and b is smaller.
    Since the problem asks for a pair of elements from the array, and we need 
    the smallest pair, we sort the unique elements and check adjacent ones.

    Args:
        nums: A list of integers.

    Returns:
        A list of two integers [a, b] representing the smallest pair with 
        different frequencies. If no such pair exists, returns an empty list.

    Examples:
        >>> solve([1, 1, 2, 2, 3])
        [1, 3]
        >>> solve([1, 1, 2, 2])
        []
    """
    if not nums:
        return []

    # Step 1: Count frequencies of each number
    frequency_map: dict[int, int] = {}
    for num in nums:
        frequency_map[num] = frequency_map.get(num, 0) + 1

    # Step 2: Get unique elements and sort them to ensure we find the smallest pair
    unique_elements: list[int] = sorted(frequency_map.keys())
    n_unique = len(unique_elements)

    # If there's only one unique element, no pair with different frequencies can exist
    if n_unique < 2:
        return []

    # Step 3: Find the smallest pair (a, b) where freq(a) != freq(b)
    # We iterate through sorted unique elements. The smallest pair will involve
    # the smallest possible 'a' and the smallest possible 'b' that satisfies the condition.
    
    # We need to find the smallest pair (a, b) such that a < b and freq(a) != freq(b).
    # Because the elements are sorted, we can check every element against 
    # the smallest possible candidates.
    
    best_pair: list[int] | None = None

    for i in range(n_unique):
        val_i = unique_elements[i]
        freq_i = frequency_map[val_i]
        
        for j in range(i + 1, n_unique):
            val_j = unique_elements[j]
            freq_j = frequency_map[val_j]
            
            if freq_i != freq_j:
                # Since unique_elements is sorted, the first pair (i, j) we find
                # where freq_i != freq_j is a candidate for the smallest pair.
                # However, we must be careful: the smallest pair is defined by 
                # the values themselves. 
                # Because we iterate i from 0 upwards and j from i+1 upwards,
                # the first valid (i, j) we encounter is the lexicographically smallest.
                return [val_i, val_j]

    return []
