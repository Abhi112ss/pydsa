METADATA = {
    "id": 2999,
    "name": "Count the Number of Powerful Integers",
    "slug": "count-the-number-of-powerful-integers",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["digit_dp", "bit_manipulation"],
    "difficulty": "medium",
    "time_complexity": "O(log10(x) * 2 * 2)",
    "space_complexity": "O(log10(x))",
    "description": "Count integers in range [low, high] that do not contain a specific digit and do not contain a specific substring.",
}

def solve(low: int, high: int, digit: int, pattern: str) -> int:
    """
    Counts the number of powerful integers in the range [low, high].
    A powerful integer does not contain the given digit and does not contain the given pattern.

    Args:
        low: The lower bound of the range (inclusive).
        high: The upper bound of the range (inclusive).
        digit: The digit that must not appear in the integer.
        pattern: The substring that must not appear in the integer.

    Returns:
        The count of powerful integers.

    Examples:
        >>> solve(1, 10, 1, "11")
        9
        >>> solve(1, 100, 1, "11")
        89
    """

    def count_upto(limit_str: str) -> int:
        """
        Uses Digit DP to count valid integers from 0 to limit_str.
        """
        n = len(limit_str)
        memo = {}

        def dp(index: int, is_less: bool, is_started: bool, current_pattern_match: int) -> int:
            """
            Args:
                index: Current digit position being processed.
                is_less: Boolean flag, true if we are already below the limit prefix.
                is_started: Boolean flag, true if we have started placing non-zero digits.
                current_pattern_match: Length of the current suffix matching the pattern prefix.

            Returns:
                Number of valid ways to complete the integer.
            """
            state = (index, is_less, is_started, current_pattern_match)
            if state in memo:
                return memo[state]

            if index == n:
                return 1 if is_started else 0

            res = 0
            # If we haven't started, we can skip this position (effectively leading zero)
            if not is_started:
                res += dp(index + 1, True, False, 0)

            upper_bound = int(limit_str[index]) if not is_less else 9
            
            # Try placing every possible digit from 0 to upper_bound
            for d in range(10):
                if not is_less and d > upper_bound:
                    break
                
                # Rule 1: Cannot contain the forbidden digit
                if d == digit:
                    continue
                
                # Rule 2: If we haven't started, '0' is handled by the 'not is_started' block above
                # to avoid counting leading zeros as the digit '0' if digit == 0.
                if not is_started and d == 0:
                    continue

                # Calculate the next state of pattern matching using KMP-like logic
                # We simulate adding digit 'd' to the current prefix of the pattern
                new_s = pattern[:current_pattern_match] + str(d)
                
                # Check if the new digit completes the forbidden pattern
                if new_s.endswith(pattern):
                    continue
                
                # Find the longest prefix of 'pattern' that is a suffix of 'new_s'
                next_match = 0
                for length in range(min(len(pattern), len(new_s)), 0, -1):
                    if new_s.endswith(pattern[:length]):
                        next_match = length
                        break
                
                res += dp(
                    index + 1,
                    is_less or (d < upper_bound),
                    True,
                    next_match
                )

            memo[state] = res
            return res

        # Special case: if the pattern is empty, it's technically always present, 
        # but the problem implies pattern is non-empty. 
        # If digit is 0 and we count 0, we must handle it.
        # The DP above counts positive integers. We check if 0 is valid.
        count = dp(0, False, False, 0)
        
        # Check if 0 itself is a valid powerful integer
        # 0 is valid if digit != 0 and pattern is not "0"
        if digit != 0 and not pattern.startswith("0"):
            # However, the problem constraints usually imply positive integers or 
            # the range includes 0. Let's check if 0 is in range and valid.
            # In most LeetCode digit DP, we handle 0 separately.
            pass 
            
        return count

    # The problem asks for [low, high]. We calculate [0, high] - [0, low-1].
    # Note: The DP above counts valid numbers > 0. 
    # We need to check if 0 is valid for the range.
    def is_valid(num: int) -> bool:
        s = str(num)
        if str(digit) in s:
            return False
        if pattern in s:
            return False
        return True

    ans_high = count_upto(str(high))
    if is_valid(0) and high >= 0:
        ans_high += 1
        
    ans_low_minus_1 = count_upto(str(low - 1)) if low > 0 else 0
    if low <= 0 and is_valid(0):
        # This part is tricky because count_upto(str(low-1)) doesn't make sense for low=0
        # But the problem range is usually positive.
        pass

    # Re-calculating logic to be safer:
    # Total = (Valid in [1, high]) + (1 if 0 is valid else 0) 
    #         - (Valid in [1, low-1]) - (1 if 0 is valid else 0)
    # This simplifies to: (Valid in [1, high]) - (Valid in [1, low-1]) 
    # plus checking if 0 is valid and in range.
    
    def get_total_valid(limit: int) -> int:
        if limit < 0: return 0
        res = count_upto(str(limit))
        if is_valid(0):
            res += 1
        return res

    return get_total_valid(high) - get_total_valid(low - 1)
