METADATA = {
    "id": 2533,
    "name": "Number of Good Binary Strings",
    "slug": "number-of-good-binary-strings",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dp", "math"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Calculate the number of binary strings of length n where every contiguous block of 0s or 1s has a length of 2 or 3, modulo 10^9 + 7.",
}

def solve(n: int) -> int:
    """
    Calculates the number of good binary strings of length n.
    
    A string is good if every contiguous block of 0s or 1s has a length of 
    exactly 2 or 3.

    Args:
        n: The length of the binary string.

    Returns:
        The number of good binary strings of length n modulo 10^9 + 7.

    Examples:
        >>> solve(2)
        2
        >>> solve(3)
        2
        >>> solve(4)
        4
        >>> solve(5)
        6
    """
    MOD = 1_000_000_007

    if n < 2:
        return 0
    
    # dp[i] stores the number of good binary strings of length i.
    # A good string of length i can be formed by:
    # 1. Taking a good string of length (i-2) and appending '00' or '11'
    # 2. Taking a good string of length (i-3) and appending '000' or '111'
    # However, we must ensure we don't double count or violate the block rule.
    # Actually, the rule is simpler: a good string ends in either a block of 2 or 3.
    # Let dp[i] be the number of good strings of length i.
    # To avoid the complexity of tracking the last character, we observe that 
    # if we append a block of 2 (00 or 11), the previous block must have been 
    # the opposite character to ensure the block length doesn't exceed 3.
    # But the problem states "every contiguous block... has length 2 or 3".
    # This is equivalent to saying we can build the string using blocks of 2 or 3.
    # Let f(i) be the number of ways to partition i into parts of size 2 and 3.
    # Since each part can be either all 0s or all 1s, and the color must change 
    # between parts to maintain the block definition, we have 2 choices for the 
    # first block, and 1 choice for every subsequent block.
    # Wait, if we use blocks of 2 and 3, the color MUST change to keep the 
    # block size exactly 2 or 3. If we didn't change color, a block of 2 
    # followed by a block of 2 would become a block of 4.
    
    # Let dp[i] be the number of good strings of length i.
    # dp[i] = dp[i-2] + dp[i-3] is the number of ways to tile length i with 
    # tiles of size 2 and 3. 
    # For each tiling, there are exactly 2 ways to assign 0s and 1s 
    # (the first block can be 00 or 11, then all others are forced).
    # However, the standard DP for this is:
    # dp[i] = dp[i-2] + dp[i-3] where dp[i] is the number of ways to form 
    # a sequence of blocks.
    
    # Let's redefine: dp[i] is the number of good strings of length i.
    # To form a string of length i, the last block is either length 2 or 3.
    # If the last block is length 2 (e.g., ...00), the block before it 
    # must have ended with 1s.
    # Let dp[i] be the number of good strings of length i.
    # dp[i] = dp[i-2] + dp[i-3] is actually the number of ways to partition 
    # i into 2s and 3s. 
    # Let's use the property: dp[i] = dp[i-2] + dp[i-3].
    # Base cases:
    # dp[0] = 1 (empty string, base for recurrence)
    # dp[1] = 0
    # dp[2] = 1 (00 or 11 -> but we need to account for the 2 choices)
    
    # Correct approach:
    # Let dp[i] be the number of ways to form a valid sequence of blocks 
    # summing to i.
    # dp[i] = dp[i-2] + dp[i-3]
    # The total number of good strings is 2 * dp[i] because the first block 
    # can be 0s or 1s, and all subsequent blocks are determined by the 
    # requirement that they must be the opposite color.
    
    dp = [0] * (n + 1)
    dp[0] = 1 # Base case for the recurrence
    
    for i in range(2, n + 1):
        # If we add a block of 2
        if i >= 2:
            dp[i] = (dp[i] + dp[i-2]) % MOD
        # If we add a block of 3
        if i >= 3:
            dp[i] = (dp[i] + dp[i-3]) % MOD
            
    # Multiply by 2 because the first block can be either 0s or 1s.
    # All subsequent blocks must alternate colors.
    return (dp[n] * 2) % MOD
