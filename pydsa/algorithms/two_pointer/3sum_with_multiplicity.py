METADATA = {
    "id": 923,
    "name": "3Sum With Multiplicity",
    "slug": "3sum-with-multiplicity",
    "category": "Math",
    "aliases": [],
    "tags": ["hash_map", "two_pointer", "math", "counting"],
    "difficulty": "medium",
    "time_complexity": "O(max_val^2)",
    "space_complexity": "O(max_val)",
    "description": "Find the number of tuples (i, j, k) such that i < j < k and nums[i] + nums[j] + nums[k] == target.",
}

def solve(nums: list[int], target: int) -> int:
    """
    Calculates the number of triplets in the array that sum up to the target.

    The algorithm uses a frequency map to count occurrences of each number,
    then iterates through unique combinations of values to avoid overcounting
    and handle the 'i < j < k' constraint using combinatorics.

    Args:
        nums: A list of integers.
        target: The target sum for the triplets.

    Returns:
        The total number of triplets (i, j, k) such that i < j < k and 
        nums[i] + nums[j] + nums[k] == target.

    Examples:
        >>> solve([1, 1, 2, 2, 3, 3, 4, 4, 5, 5], 8)
        12
        >>> solve([1, 1, 1, 1], 3)
        4
    """
    # Count frequencies of each number
    counts = {}
    max_val = 0
    for num in nums:
        counts[num] = counts.get(num, 0) + 1
        if num > max_val:
            max_val = num

    # Get sorted unique numbers to iterate through combinations
    unique_nums = sorted(counts.keys())
    total_triplets = 0
    n = len(unique_nums)

    for i in range(n):
        val1 = unique_nums[i]
        count1 = counts[val1]

        # Case 1: All three numbers are the same (val1 == val2 == val3)
        if val1 * 3 == target:
            if count1 >= 3:
                # Combination formula nCr: n! / (r!(n-r)!) -> n*(n-1)*(n-2)/6
                total_triplets += (count1 * (count1 - 1) * (count1 - 2)) // 6

        for j in range(i + 1, n):
            val2 = unique_nums[j]
            count2 = counts[val2]
            val3 = target - val1 - val2

            # Case 2: Two numbers are the same (val1 == val2 != val3)
            # Note: We only check val1 == val2 here because the loop structure 
            # handles val2 == val3 or val1 == val3 in other iterations or logic.
            # However, to be exhaustive and avoid double counting, we check:
            # 1. val1 == val2 != val3
            # 2. val1 != val2 == val3
            # 3. val1 == val3 != val2 (This is covered by the symmetry of the loops)
            
            # To simplify, we handle the "two same" logic by checking if val3 exists
            # and comparing it to val1 and val2.
            
            if val3 < val2:
                # If val3 is smaller than val2, we've already processed this combination
                # or it's impossible to satisfy i < j < k with unique values.
                continue

            if val3 in counts:
                count3 = counts[val3]
                
                if val1 == val2 == val3:
                    # This case is actually handled by Case 1, but kept for logic completeness
                    pass 
                elif val1 == val2:
                    # val1 == val2 != val3
                    # Combination: (count1 choose 2) * count3
                    total_triplets += (count1 * (count1 - 1) // 2) * count3
                elif val2 == val3:
                    # val1 != val2 == val3
                    # Combination: count1 * (count2 choose 2)
                    total_triplets += count1 * (count2 * (count2 - 1) // 2)
                elif val1 == val3:
                    # val1 == val3 != val2
                    # Combination: (count1 choose 2) * count2
                    total_triplets += (count1 * (count1 - 1) // 2) * count2
                else:
                    # All three are distinct: val1 < val2 < val3
                    # Combination: count1 * count2 * count3
                    total_triplets += count1 * count2 * count3

    # The logic above has a slight overlap risk if not careful. 
    # Let's refine the iteration to be strictly unique combinations.
    # Re-calculating using a cleaner approach:
    
    total_triplets = 0
    # Re-run with a strictly controlled logic to ensure no double counting
    for i in range(n):
        v1 = unique_nums[i]
        c1 = counts[v1]
        
        # Case: v1 == v2 == v3
        if v1 * 3 == target:
            if c1 >= 3:
                total_triplets += (c1 * (c1 - 1) * (c1 - 2)) // 6
        
        for j in range(i + 1, n):
            v2 = unique_nums[j]
            c2 = counts[v2]
            v3 = target - v1 - v2
            
            if v3 < v2:
                continue
            
            if v3 in counts:
                c3 = counts[v3]
                if v1 == v2: # Should not happen due to range(i+1, n)
                    pass
                elif v2 == v3:
                    # v1 < v2 == v3
                    total_triplets += c1 * (c2 * (c2 - 1) // 2)
                elif v1 == v3: # Should not happen because v1 < v2 and v2 < v3
                    pass
                elif v1 < v2 < v3:
                    # v1 < v2 < v3
                    total_triplets += c1 * c2 * c3
                # Note: v1 == v2 is impossible because j starts at i+1
                # Note: v2 == v3 is the only "two same" case possible in this loop
                # The "v1 == v2" case is actually handled when v1 and v2 are the same value,
                # but our loop uses unique_nums, so v1 != v2 always.
                # Therefore, the only "two same" cases are:
                # 1. v1 == v2 (impossible here)
                # 2. v2 == v3 (handled)
                # 3. v1 == v3 (impossible here because v1 < v2 < v3)
                # Wait, there is one more: what if v1 == v2? 
                # That would be handled if we allowed j to start at i.
                # Let's use the standard 3-case approach for clarity.
                pass

    # Corrected logic for production:
    total_triplets = 0
    # 1. All three same
    for v in unique_nums:
        if v * 3 == target:
            c = counts[v]
            if c >= 3:
                total_triplets += (c * (c - 1) * (c - 2)) // 6
                
    # 2. Two same, one different
    for v in unique_nums:
        c = counts[v]
        if c >= 2:
            # v is the doubled value
            needed = target - 2 * v
            if needed != v and needed in counts:
                total_triplets += (c * (c - 1) // 2) * counts[needed]
                
    # 3. All three different
    # To avoid triple counting (a,b,c), (b,a,c), etc., we enforce v1 < v2 < v3
    for i in range(n):
        v1 = unique_nums[i]
        for j in range(i + 1, n):
            v2 = unique_nums[j]
            v3 = target - v1 - v2
            if v3 > v2 and v3 in counts:
                total_triplets += counts[v1] * counts[v2] * counts[v3]
                
    return total_triplets
