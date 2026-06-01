METADATA = {
    "id": 1955,
    "name": "Count Number of Special Subsequences",
    "slug": "count-number-of-special-subsequences",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dp", "math", "subsequence"],
    "difficulty": "hard",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Count the number of subsequences that contain three non-empty parts consisting of 0s, 1s, and 2s in that order.",
}

def solve(nums: list[int]) -> int:
    """
    Counts the number of special subsequences in the given list.
    
    A special subsequence is a subsequence that consists of some number of 0s, 
    followed by some number of 1s, followed by some number of 2s.
    All three parts must be non-empty.

    Args:
        nums: A list of integers containing only 0, 1, and 2.

    Returns:
        The total count of special subsequences modulo 10^9 + 7.

    Examples:
        >>> solve([0, 1, 2, 2])
        3
        >>> solve([0, 0, 1, 1, 2, 2])
        27
    """
    MOD = 1_000_000_007

    # count0: number of subsequences consisting only of 0s
    # count1: number of subsequences consisting of 0s followed by 1s
    # count2: number of subsequences consisting of 0s, then 1s, then 2s
    count0 = 0
    count1 = 0
    count2 = 0

    for num in nums:
        if num == 0:
            # To form a new '0' subsequence:
            # 1. We can add this 0 to all existing '0' subsequences.
            # 2. We can start a new '0' subsequence with just this 0.
            # 3. We can skip this 0 (keep existing count0).
            # Formula: count0 = count0 (old) + count0 (old) + 1 (new)
            # Simplified: count0 = 2 * count0 + 1
            count0 = (2 * count0 + 1) % MOD
            
        elif num == 1:
            # To form a new '0...1' subsequence:
            # 1. Add this 1 to all existing '0...1' subsequences.
            # 2. Add this 1 to all existing '0' subsequences to create new '0...1's.
            # 3. Skip this 1.
            # Formula: count1 = count1 (old) + count1 (old) + count0 (old)
            # Simplified: count1 = 2 * count1 + count0
            count1 = (2 * count1 + count0) % MOD
            
        elif num == 2:
            # To form a new '0...1...2' subsequence:
            # 1. Add this 2 to all existing '0...1...2' subsequences.
            # 2. Add this 2 to all existing '0...1' subsequences to create new '0...1...2's.
            # 3. Skip this 2.
            # Formula: count2 = count2 (old) + count2 (old) + count1 (old)
            # Simplified: count2 = 2 * count2 + count1
            count2 = (2 * count2 + count1) % MOD

    return count2