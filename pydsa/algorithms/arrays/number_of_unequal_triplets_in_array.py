METADATA = {
    "id": 2475,
    "name": "Number of Unequal Triplets in Array",
    "slug": "number-of-unequal-triplets-in-array",
    "category": "Math",
    "aliases": [],
    "tags": ["math", "hash_map", "counting"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Count the number of triplets (i, j, k) such that nums[i], nums[j], and nums[k] are all distinct.",
}

def solve(nums: list[int]) -> int:
    """
    Calculates the number of triplets (i, j, k) where nums[i], nums[j], and nums[k] 
    are all distinct.

    The approach uses the principle of inclusion-exclusion or complementary counting.
    Total triplets = n * (n - 1) * (n - 2) / 6 (if order doesn't matter) or 
    n * (n - 1) * (n - 2) (if order matters). 
    Since the problem asks for triplets (i, j, k) where i < j < k is not specified, 
    but usually in LeetCode "triplets" implies distinct indices, we look at 
    combinations. However, the problem asks for the number of triplets (i, j, k) 
    such that nums[i], nums[j], and nums[k] are distinct. 
    Standard interpretation for this specific problem: count sets of 3 indices 
    where the values are different.

    Args:
        nums: A list of integers.

    Returns:
        The total number of triplets with distinct values.

    Examples:
        >>> solve([1, 2, 3, 4])
        4
        >>> solve([1, 1, 2, 2])
        0
    """
    n = len(nums)
    if n < 3:
        return 0

    # Count frequencies of each number
    counts: dict[int, int] = {}
    for num in nums:
        counts[num] = counts.get(num, 0) + 1

    # Total ways to choose 3 indices out of n: nC3
    # nC3 = n * (n - 1) * (n - 2) // 6
    total_combinations = n * (n - 1) * (n - 2) // 6

    # We subtract cases where at least two numbers are the same.
    # Case 1: All three are the same (e.g., {1, 1, 1})
    # Case 2: Exactly two are the same (e.g., {1, 1, 2})
    
    # However, a more direct way to count distinct triplets is to use the 
    # counts of unique elements. If we have unique values v1, v2, v3... 
    # with counts c1, c2, c3...
    # The number of ways to pick one from v_i, one from v_j, and one from v_k 
    # is c_i * c_j * c_k.
    
    # To do this in O(n), we use the identity for sum of products of triples:
    # (sum c_i)^3 = sum(c_i^3) + 3 * sum(c_i^2 * (sum c_j - c_i)) + 6 * sum(c_i * c_j * c_k)
    # This is getting complicated. Let's use a simpler symmetric polynomial approach:
    # Let S1 = sum(c_i)
    # Let S2 = sum(c_i^2)
    # Let S3 = sum(c_i^3)
    # The sum of products of triples (c_i * c_j * c_k) for i < j < k is:
    # (S1^3 - 3*S1*S2 + 2*S3) / 6

    s1 = n
    s2 = 0
    s3 = 0
    
    for val in counts.values():
        s2 += val * val
        s3 += val * val * val
        
    # Using Newton's Sums for elementary symmetric polynomials:
    # e1 = s1
    # e2 = (s1^2 - s2) / 2
    # e3 = (s1^3 - 3*s1*s2 + 2*s3) / 6
    
    distinct_triplets = (s1**3 - 3 * s1 * s2 + 2 * s3) // 6
    
    return distinct_triplets
