METADATA = {
    "id": 805,
    "name": "Split Array With Same Average",
    "slug": "split-array-with-same-average",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dynamic_programming", "math", "bitmask", "subset_sum"],
    "difficulty": "hard",
    "time_complexity": "O(n * sum)",
    "space_complexity": "O(sum)",
    "description": "Determine if an array can be split into two non-empty subsets such that both subsets have the same average.",
}

def solve(nums: list[int]) -> bool:
    """
    Determines if the array can be split into two non-empty subsets with the same average.

    The condition for two subsets A and B to have the same average is:
    sum(A) / len(A) == sum(B) / len(B)
    Since sum(A) + sum(B) = total_sum and len(A) + len(B) = n,
    this simplifies to: sum(A) / k = total_sum / n
    => sum(A) = (total_sum * k) / n
    where k is the size of subset A (1 <= k < n).

    Args:
        nums: A list of integers.

    Returns:
        True if such a split exists, False otherwise.

    Examples:
        >>> solve([1, 2, 3, 4, 5, 6, 7, 8])
        True
        >>> solve([3, 3, 4])
        False
    """
    n = len(nums)
    total_sum = sum(nums)

    # If we can't find a k such that (total_sum * k) % n == 0, 
    # then no integer sum(A) can satisfy the condition.
    # We only need to check k from 1 to n // 2 because of symmetry.
    possible_k = []
    for k in range(1, n // 2 + 1):
        if (total_sum * k) % n == 0:
            possible_k.append(k)

    if not possible_k:
        return False

    # dp[i] will be a bitmask where the j-th bit is set if 
    # a sum of 'i' can be achieved using exactly 'j' elements.
    # dp[s] = bitmask of counts
    # Using a list of integers (bitmasks) to represent possible counts for each sum.
    # Max sum is n * 10000, but we only care about sums up to total_sum // 2.
    # However, to optimize, we use the property that we only need to check 
    # specific target sums for specific k values.
    
    # To keep space complexity manageable and avoid O(n * sum) if sum is huge,
    # we use the bitmask approach: dp[s] is a bitmask where bit 'k' is 1 
    # if sum 's' can be formed by 'k' elements.
    dp = [0] * (total_sum + 1)
    dp[0] = 1  # Sum 0 is possible with 0 elements (bit 0 set)

    for num in nums:
        # Iterate backwards to ensure each number is used at most once (0/1 Knapsack)
        for s in range(total_sum, num - 1, -1):
            # If sum (s - num) was possible with 'count' elements,
            # then sum 's' is possible with 'count + 1' elements.
            # We shift the bitmask of (s - num) left by 1.
            dp[s] |= (dp[s - num] << 1)

    # Check if any of our valid k values have their corresponding target sum bit set
    for k in possible_k:
        target_sum = (total_sum * k) // n
        # Check if the k-th bit is set in the bitmask for target_sum
        if (dp[target_sum] >> k) & 1:
            return True

    return False
