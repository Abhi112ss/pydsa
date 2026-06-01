METADATA = {
    "id": 3513,
    "name": "Number of Unique XOR Triplets I",
    "slug": "number_of_unique_xor_triplets_i",
    "category": "Hash Table",
    "aliases": [],
    "tags": ["bit_manipulation", "hash_map"],
    "difficulty": "medium",
    "time_complexity": "O(n^2)",
    "space_complexity": "O(n)",
    "description": "Count the number of unique triplets in an array whose XOR sum is zero.",
}

def solve(nums: list[int]) -> int:
    """
    Counts the number of unique triplets (i, j, k) such that nums[i] ^ nums[j] ^ nums[k] == 0.
    
    The problem asks for unique triplets. Since the XOR operation is commutative 
    and associative, if a ^ b ^ c = 0, then c = a ^ b. We can iterate through 
    all pairs (i, j) and check if the required value (nums[i] ^ nums[j]) 
    exists in the array at an index k > j.

    Args:
        nums: A list of integers.

    Returns:
        The total count of unique triplets whose XOR sum is zero.

    Examples:
        >>> solve([1, 2, 3, 4, 5])
        1  # (1^2^3 = 0)
        >>> solve([0, 0, 0])
        1  # (0^0^0 = 0)
        >>> solve([1, 1, 1])
        0
    """
    n = len(nums)
    if n < 3:
        return 0

    # To handle duplicate values in nums and ensure we count unique index triplets,
    # we use a frequency map of the values.
    # However, the standard interpretation of "unique triplets" in LeetCode 
    # usually refers to unique sets of indices (i < j < k).
    
    # Pre-calculate frequencies to allow O(1) lookup of the third element.
    # We use a dictionary to store the count of each number.
    counts = {}
    for x in nums:
        counts[x] = counts.get(x, 0) + 1

    total_triplets = 0

    # To avoid overcounting and ensure i < j < k, we iterate through pairs
    # and use the frequency map carefully.
    # However, a more robust way to handle the "unique index triplets" requirement
    # while maintaining O(n^2) is to iterate through all pairs (i, j) where i < j
    # and check how many k > j satisfy nums[k] == (nums[i] ^ nums[j]).
    
    # To do this efficiently in O(n^2), we can use a suffix frequency map.
    # suffix_counts[j] will store the frequency of elements from index j to n-1.
    suffix_counts = [{} for _ in range(n + 1)]
    for i in range(n - 1, -1, -1):
        suffix_counts[i] = suffix_counts[i + 1].copy()
        suffix_counts[i][nums[i]] = suffix_counts[i].get(nums[i], 0) + 1

    for i in range(n):
        for j in range(i + 1, n - 1):
            # The required third value to make XOR sum zero
            target = nums[i] ^ nums[j]
            
            # We need to find how many k exist such that k > j and nums[k] == target
            # We use the precomputed suffix counts for index j + 1
            if target in suffix_counts[j + 1]:
                total_triplets += suffix_counts[j + 1][target]

    return total_triplets
