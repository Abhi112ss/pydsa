METADATA = {
    "id": 2827,
    "name": "Number of Beautiful Integers in the Range",
    "slug": "number-of-beautiful-integers-in-the-range",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["digit-dp", "math"],
    "difficulty": "hard",
    "time_complexity": "O(log10(n))",
    "space_complexity": "O(log10(n))",
    "description": "Count integers in range [num1, num2] that have an even number of digits and the sum of digits is divisible by k.",
}

def solve(num1: int, num2: int, k: int) -> int:
    """
    Args:
        num1: The lower bound of the range.
        num2: The upper bound of the range.
        k: The divisor for the sum of digits.

    Returns:
        The count of beautiful integers in the range [num1, num2].
    """
    def count_beautiful(n: int, k: int) -> int:
        s = str(n)
        length = len(s)
        memo = {}

        def dp(index: int, current_sum: int, current_len: int, is_less: bool, is_started: bool) -> int:
            state = (index, current_sum, current_len, is_less, is_started)
            if state in memo:
                return memo[state]

            if index == length:
                if is_started and current_len % 2 == 0 and current_sum % k == 0:
                    return 1
                return 0

            res = 0
            limit = int(s[index]) if not is_less else 9

            for digit in range(limit + 1):
                new_is_less = is_less or (digit < limit)
                new_is_started = is_started or (digit > 0)
                
                if not new_is_started:
                    res += dp(index + 1, 0, 0, new_is_less, False)
                else:
                    new_len = current_len + 1 if not (not is_started and digit == 0) else 1
                    if not is_started and digit > 0:
                        new_len = 1
                    else:
                        new_len = current_len + 1
                    
                    res += dp(index + 1, (current_sum + digit) % k, new_len, new_is_less, True)

            memo[state] = res
            return res

        def dp_optimized(idx: int, rem: int, length_parity: int, is_less: bool, is_started: bool) -> int:
            state = (idx, rem, length_parity, is_less, is_started)
            if state in memo:
                return memo[state]
            
            if idx == length:
                return 1 if (is_started and length_parity == 0 and rem == 0) else 0
            
            res = 0
            upper = int(s[idx]) if not is_less else 9
            
            for d in range(upper + 1):
                next_is_less = is_less or (d < upper)
                if not is_started and d == 0:
                    res += dp_optimized(idx + 1, 0, 0, next_is_less, False)
                else:
                    res += dp_optimized(idx + 1, (rem + d) % k, (length_parity + 1) % 2, next_is_less, True)
            
            memo[state] = res
            return res

        return dp_optimized(0, 0, 0, False, False)

    return count_beautiful(num2, k) - count_beautiful(num1 - 1, k)