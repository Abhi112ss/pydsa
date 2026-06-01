METADATA = {
    "id": 3583,
    "name": "Count Special Triplets",
    "slug": "count_special_triplets",
    "category": "Arrays",
    "aliases": [],
    "tags": ["arrays", "two_pointer"],
    "difficulty": "medium",
    "time_complexity": "O(n^2)",
    "space_complexity": "O(1)",
    "description": "Count the number of triplets (i, j, k) such that i < j < k and the elements satisfy specific arithmetic conditions.",
}

def solve(nums: list[int]) -> int:
    """
    Counts the number of special triplets (i, j, k) in the array.
    A triplet is special if i < j < k and nums[j] - nums[i] == nums[k] - nums[j].
    This is equivalent to finding arithmetic progressions of length 3.

    Args:
        nums: A list of integers.

    Returns:
        The total count of special triplets.

    Examples:
        >>> solve([1, 3, 5, 7, 9])
        4
        # Triplets: (1,3,5), (3,5,7), (5,7,9), (1,5,9)
        >>> solve([1, 2, 3, 4, 5])
        4
        >>> solve([1, 1, 1])
        1
    """
    n = len(nums)
    if n < 3:
        return 0

    count = 0
    
    # We iterate through each element as the potential middle element 'j' of the triplet.
    # For a fixed j, we need to find how many i < j and k > j satisfy:
    # nums[i] + nums[k] = 2 * nums[j]
    
    # To achieve O(n^2), we can use a frequency map for elements to the right of j.
    # However, since we need to maintain the i < j < k constraint, 
    # we can use a frequency map for elements to the right and update it as we move j.
    
    right_freq = {}
    for x in nums:
        right_freq[x] = right_freq.get(x, 0) + 1
        
    left_freq = {}
    
    for j in range(n):
        # Remove current element from right_freq because it is now the middle element 'j'
        right_freq[nums[j]] -= 1
        if right_freq[nums[j]] == 0:
            del right_freq[nums[j]]
            
        # For the current nums[j], check all possible nums[i] seen so far in left_freq
        # The required nums[k] must be: 2 * nums[j] - nums[i]
        for val_i, freq_i in left_freq.items():
            val_k = 2 * nums[j] - val_i
            if val_k in right_freq:
                count += freq_i * right_freq[val_k]
        
        # Add current element to left_freq for the next iteration
        left_freq[nums[j]] = left_freq.get(nums[j], 0) + 1
                
    return count
