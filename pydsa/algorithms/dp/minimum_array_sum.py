METADATA = {
    "id": 3366,
    "name": "Minimum Array Sum",
    "slug": "minimum-array-sum",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dynamic_programming", "greedy"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Find the minimum possible sum of an array after applying two types of operations a limited number of times.",
}

def solve(nums: list[int], op1: int, op2: int) -> int:
    """
    Calculates the minimum sum of the array after applying at most op1 operations 
    of type 1 (nums[i] = ceil(nums[i] / 2)) and at most op2 operations 
    of type 2 (if nums[i] >= 3, nums[i] = floor(nums[i] / 3)).

    Args:
        nums: A list of integers representing the initial array.
        op1: Maximum number of type 1 operations allowed.
        op2: Maximum number of type 2 operations allowed.

    Returns:
        The minimum possible sum of the array.

    Examples:
        >>> solve([4, 5, 2], 1, 1)
        6
        >>> solve([2, 3, 5], 1, 1)
        4
    """
    n = len(nums)
    
    # dp[i][j][k] represents the minimum sum for the suffix starting at index i,
    # with j operations of type 1 remaining and k operations of type 2 remaining.
    # Since we only need the results from the next index (i+1), we can optimize 
    # space, but for clarity and given constraints, a 3D table or memoization is used.
    # Given n is up to 100, op1/op2 up to 100, O(n * op1 * op2) is ~10^6, which is fine.
    
    memo: dict[tuple[int, int, int], int] = {}

    def get_min_sum(index: int, rem_op1: int, rem_op2: int) -> int:
        if index == n:
            return 0
        
        state = (index, rem_op1, rem_op2)
        if state in memo:
            return memo[state]

        val = nums[index]
        
        # Option 0: No operations on this element
        res = val + get_min_sum(index + 1, rem_op1, rem_op2)

        # Option 1: Apply only Type 1 operation (ceil(x/2))
        if rem_op1 > 0:
            # ceil(val / 2) is equivalent to (val + 1) // 2
            val_op1 = (val + 1) // 2
            res = min(res, val_op1 + get_min_sum(index + 1, rem_op1 - 1, rem_op2))

        # Option 2: Apply only Type 2 operation (floor(x/3))
        if rem_op2 > 0 and val >= 3:
            val_op2 = val // 3
            res = min(res, val_op2 + get_min_sum(index + 1, rem_op1, rem_op2 - 1))

        # Option 3: Apply Type 1 then Type 2
        # Note: The problem implies we can apply both to the same element.
        # We must check both orders: (val -> op1 -> op2) and (val -> op2 -> op1)
        if rem_op1 > 0 and rem_op2 > 0:
            # Order: Type 1 then Type 2
            v1 = (val + 1) // 2
            v12 = v1 // 3
            res = min(res, v12 + get_min_sum(index + 1, rem_op1 - 1, rem_op2 - 1))

            # Order: Type 2 then Type 1
            if val >= 3:
                v2 = val // 3
                v21 = (v2 + 1) // 2
                res = min(res, v21 + get_min_sum(index + 1, rem_op1 - 1, rem_op2 - 1))

        memo[state] = res
        return res

    # Using iterative DP to avoid recursion depth issues in some environments,
    # though for n=100, recursion with memoization is safe.
    # Let's implement the iterative version for production-grade robustness.
    
    # dp[i][j][k] where i is index, j is op1, k is op2
    # We iterate backwards from n to 0
    dp = [[[0] * (op2 + 1) for _ in range(op1 + 1)] for _ in range(n + 1)]

    for i in range(n - 1, -1, -1):
        val = nums[i]
        for j in range(op1 + 1):
            for k in range(op2 + 1):
                # Case 1: Do nothing
                best = val + dp[i + 1][j][k]

                # Case 2: Type 1 only
                if j > 0:
                    best = min(best, ((val + 1) // 2) + dp[i + 1][j - 1][k])

                # Case 3: Type 2 only
                if k > 0 and val >= 3:
                    best = min(best, (val // 3) + dp[i + 1][j][k - 1])

                # Case 4: Both operations
                if j > 0 and k > 0:
                    # Type 1 then Type 2
                    v12 = ((val + 1) // 2) // 3
                    best = min(best, v12 + dp[i + 1][j - 1][k - 1])
                    
                    # Type 2 then Type 1
                    if val >= 3:
                        v21 = (val // 3 + 1) // 2
                        best = min(best, v21 + dp[i + 1][j - 1][k - 1])
                
                dp[i][j][k] = best

    return dp[0][op1][op2]
