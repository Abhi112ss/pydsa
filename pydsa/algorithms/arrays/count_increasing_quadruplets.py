METADATA = {
    "id": 2552,
    "name": "Count Increasing Quadruplets",
    "slug": "count-increasing-quadruplets",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dp", "arrays", "counting"],
    "difficulty": "hard",
    "time_complexity": "O(n^2)",
    "space_complexity": "O(n^2)",
    "description": "Count the number of indices (i, j, k, l) such that 0 <= i < j < k < l < n and nums[i] < nums[k] < nums[j] < nums[l].",
}

def solve(nums: list[int]) -> int:
    """
    Counts the number of quadruplets (i, j, k, l) such that i < j < k < l 
    and nums[i] < nums[k] < nums[j] < nums[l].

    The problem asks for a specific pattern: a 1-3-2-4 pattern in terms of values.
    We can optimize the O(n^4) brute force to O(n^2) by fixing the middle 
    elements (j, k) and precomputing how many valid 'i's and 'l's exist.

    Args:
        nums: A list of unique integers.

    Returns:
        The total count of valid quadruplets.

    Examples:
        >>> solve([1, 3, 2, 4])
        1
        >>> solve([1, 2, 3, 4])
        0
    """
    n = len(nums)
    # count_smaller_than[k][val] will store how many elements in nums[0...k-1] 
    # are smaller than 'val'.
    # However, to keep space O(n^2) and time O(n^2), we can use a 2D array 
    # to store the count of elements smaller than nums[j] to the left of k.
    
    # Let's use a more direct DP approach:
    # For a fixed j and k (where j < k and nums[k] < nums[j]), 
    # we need:
    # 1. Number of i < j such that nums[i] < nums[k]
    # 2. Number of l > k such that nums[l] > nums[j]
    
    # Precompute 'less_than[k][x]' which is the count of elements in nums[0...k-1] 
    # that are less than x.
    # Since values are 1 to n, we can use a 2D array.
    less_than = [[0] * (n + 1) for _ in range(n)]
    
    for k in range(1, n):
        # Copy previous counts
        for val in range(1, n + 1):
            less_than[k][val] = less_than[k-1][val]
        # Increment count for the element at k-1
        less_than[k][nums[k-1]] += 1

    # Precompute 'greater_than[j][x]' which is the count of elements in nums[j+1...n-1]
    # that are greater than x.
    greater_than = [[0] * (n + 1) for _ in range(n)]
    for j in range(n - 2, -1, -1):
        for val in range(1, n + 1):
            greater_than[j][val] = greater_than[j+1][val]
        # Increment count for the element at j+1
        greater_than[j][nums[j+1]] += 1
    
    # To handle "greater than x" efficiently, we can transform the greater_than 
    # logic or just use the property: count(greater than x) = total_elements_in_range - count(less than or equal to x)
    # But since we need specifically nums[l] > nums[j], we can precompute 
    # suffix counts of elements greater than a value.
    
    # Let's refine:
    # For fixed j, k:
    # count_i = number of i < j where nums[i] < nums[k]
    # count_l = number of l > k where nums[l] > nums[j]
    
    # We can compute count_i using the less_than table:
    # count_i = less_than[j][nums[k]] (this counts elements in nums[0...j-1] < nums[k])
    
    # We can compute count_l using a suffix sum approach:
    # Let suffix_greater[k][val] be count of l > k where nums[l] > val.
    suffix_greater = [[0] * (n + 1) for _ in range(n)]
    for k in range(n - 2, -1, -1):
        for val in range(1, n + 1):
            suffix_greater[k][val] = suffix_greater[k+1][val]
        # We want to count elements in nums[k+1...n-1] that are > val.
        # Instead of a full 2D array for suffix_greater, let's just use the 
        # fact that we only care about nums[j].
        
    # Re-calculating suffix_greater more efficiently:
    # suffix_greater[k][val] = count of l in [k+1, n-1] such that nums[l] > val
    for k in range(n - 1, -1, -1):
        # We'll fill this in a way that suffix_greater[k][v] is count of l > k with nums[l] > v
        # This is actually easier to compute as:
        # suffix_greater[k][v] = suffix_greater[k+1][v] + (1 if nums[k+1] > v else 0)
        # But we need to do this for all v.
        pass # Logic handled below

    # Let's restart the precomputation logic to be cleaner.
    # count_i[j][k] = count of i < j such that nums[i] < nums[k]
    # count_l[j][k] = count of l > k such that nums[l] > nums[j]
    
    # count_i[j][k] is simply the number of elements in nums[0...j-1] that are < nums[k]
    # We can use a 2D array where prefix_smaller[j][val] is count of nums[0...j-1] < val
    prefix_smaller = [[0] * (n + 1) for _ in range(n + 1)]
    for j in range(1, n + 1):
        for val in range(1, n + 1):
            prefix_smaller[j][val] = prefix_smaller[j-1][val]
        # Add the element nums[j-1]
        # We need to increment all prefix_smaller[j][v] where v > nums[j-1]
        # Wait, the definition is: prefix_smaller[j][v] = count of i < j such that nums[i] < v
        # So for a fixed j, we increment prefix_smaller[j][v] for all v > nums[j-1]
        # No, that's not right. Let's use:
        # prefix_smaller[j][v] = count of i in [0, j-1] such that nums[i] < v
    
    # Correct Precomputation:
    # prefix_smaller[j][v] : count of i < j such that nums[i] < v
    prefix_smaller = [[0] * (n + 1) for _ in range(n + 1)]
    for j in range(1, n + 1):
        for v in range(1, n + 1):
            prefix_smaller[j][v] = prefix_smaller[j-1][v]
        # After processing j-1, we add nums[j-1] to the counts
        # For all v > nums[j-1], prefix_smaller[j][v] increases by 1
        for v in range(nums[j-1] + 1, n + 1):
            prefix_smaller[j][v] += 1
            
    # suffix_greater[k][v] : count of l > k such that nums[l] > v
    suffix_greater = [[0] * (n + 1) for _ in range(n + 1)]
    for k in range(n - 1, -1, -1):
        for v in range(1, n + 1):
            suffix_greater[k][v] = suffix_greater[k+1][v]
        # After processing k+1, we add nums[k] to the counts
        # For all v < nums[k], suffix_greater[k][v] increases by 1
        # Wait, the index is l > k. So we use nums[k+1...n-1]
        # Let's use k as the index of the element we just "passed"
        # suffix_greater[k][v] will be count of l in [k+1, n-1] such that nums[l] > v
        # This is equivalent to suffix_greater[k+1][v] + (1 if nums[k+1] > v else 0)
        # But we are iterating k downwards.
        # When k = n-1, suffix_greater[n-1][v] = 0 (no l > n-1)
        # When k = n-2, suffix_greater[n-2][v] = (1 if nums[n-1] > v else 0)
        # When k = n-3, suffix_greater[n-3][v] = suffix_greater[n-2][v] + (1 if nums[n-2] > v else 0)
        # This is slightly confusing. Let's simplify.
        
    # Let's use a simpler approach for suffix_greater:
    # suffix_greater[k][v] = count of l in [k+1, n-1] such that nums[l] > v
    suffix_greater = [[0] * (n + 1) for _ in range(n + 1)]
    for k in range(n - 2, -1, -1):
        # suffix_greater[k] is based on suffix_greater[k+1] and nums[k+1]
        for v in range(1, n + 1):
            suffix_greater[k][v] = suffix_greater[k+1][v]
            if nums[k+1] > v:
                suffix_greater[k][v] += 1

    total_quadruplets = 0
    # Iterate over all possible j and k (the middle two elements)
    # Requirement: j < k and nums[k] < nums[j]
    for j in range(n):
        for k in range(j + 1, n):
            if nums[k] < nums[j]:
                # We need i < j such that nums[i] < nums[k]
                # This is prefix_smaller[j][nums[k]]
                count_i = prefix_smaller[j][nums[k]]
                
                # We need l > k such that nums[l] > nums[j]
                # This is suffix_greater[k][nums[j]]
                count_l = suffix_greater[k][nums[j]]
                
                total_quadruplets += count_i * count_l
                
    return total_quadruplets
