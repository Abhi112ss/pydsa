METADATA = {
    "id": 2719,
    "name": "Count of Integers",
    "slug": "count_of_integers",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dp", "math", "digit-dp"],
    "difficulty": "hard",
    "time_complexity": "O(log(num) * max_sum)",
    "space_complexity": "O(log(num) * max_sum)",
    "description": "Count integers in range [low, high] such that the sum of their digits is within [min_sum, max_sum].",
}

def solve(low: int, high: int, min_sum: int, max_sum: int) -> int:
    """
    Counts the number of integers in the range [low, high] whose digit sum 
    is between min_sum and max_sum inclusive.

    Args:
        low: The lower bound of the range (inclusive).
        high: The upper bound of the range (inclusive).
        min_sum: The minimum allowed sum of digits.
        max_sum: The maximum allowed sum of digits.

    Returns:
        The count of integers satisfying the condition.

    Examples:
        >>> solve(1, 10, 1, 2)
        3
        >>> solve(10, 20, 2, 3)
        3
    """
    MOD = 10**9 + 7

    def count_with_digit_dp(n: int, target_min: int, target_max: int) -> int:
        """
        Standard Digit DP to count numbers from 0 to n with digit sum in [target_min, target_max].
        """
        s_n = str(n)
        length = len(s_n)
        # memo stores (index, current_sum, is_less, is_started)
        # index: current digit position being processed
        # current_sum: sum of digits placed so far
        # is_less: boolean, true if we are already smaller than the prefix of n
        # is_started: boolean, true if we have started placing non-zero digits
        memo = {}

        def dp(idx: int, current_sum: int, is_less: bool, is_started: bool) -> int:
            if current_sum > target_max:
                return 0
            if idx == length:
                return 1 if target_min <= current_sum <= target_max else 0
            
            state = (idx, current_sum, is_less, is_started)
            if state in memo:
                return memo[state]

            res = 0
            # Determine the upper limit for the current digit
            limit = int(s_n[idx]) if not is_less else 9

            for digit in range(limit + 1):
                new_is_less = is_less or (digit < limit)
                new_is_started = is_started or (digit > 0)
                
                # If we haven't started, the current digit doesn't contribute to sum
                # (though for digit sum, leading zeros are effectively 0 anyway)
                new_sum = current_sum + digit if new_is_started else 0
                
                res = (res + dp(idx + 1, new_sum, new_is_less, new_is_started)) % MOD

            memo[state] = res
            return res

        return dp(0, 0, False, False)

    # The result for [low, high] is count(high) - count(low - 1)
    # We use the digit DP to find counts up to high and up to low-1
    ans_high = count_with_digit_dp(high, min_sum, max_sum)
    ans_low = count_with_digit_dp(low - 1, min_sum, max_sum)

    return (ans_high - ans_low + MOD) % MOD
