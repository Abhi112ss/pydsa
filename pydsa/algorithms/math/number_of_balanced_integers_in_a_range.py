METADATA = {
    "id": 3791,
    "name": "Number of Balanced Integers in a Range",
    "slug": "number_of_balanced_integers_in_a_range",
    "category": "Math",
    "aliases": [],
    "tags": ["digit_dp", "math"],
    "difficulty": "hard",
    "time_complexity": "O(log10(n))",
    "space_complexity": "O(log10(n))",
    "description": "Count integers in a given range [low, high] where the frequency of each digit is equal.",
}

def solve(low: int, high: int) -> int:
    """
    Args:
        low (int): The lower bound of the range.
        high (int): The upper bound of the range.

    Returns:
        int: The count of balanced integers in the range [low, high].
    """
    def count_balanced_up_to(n: int) -> int:
        if n < 0:
            return 0
        s = str(n)
        length = len(s)
        memo = {}

        def dp(index: int, is_less: bool, is_started: bool, counts: tuple[int, ...]) -> int:
            state = (index, is_less, is_started, counts)
            if state in memo:
                return memo[state]

            if index == length:
                if not is_started:
                    return 0
                first_count = -1
                for count in counts:
                    if count > 0:
                        if first_count == -1:
                            first_count = count
                        elif first_count != count:
                            return 0
                return 1 if first_count != -1 else 0

            res = 0
            limit = int(s[index]) if not is_less else 9

            for digit in range(limit + 1):
                new_is_less = is_less or (digit < limit)
                new_is_started = is_started or (digit > 0)

                if not new_is_started:
                    res += dp(index + 1, new_is_less, False, counts)
                else:
                    new_counts = list(counts)
                    new_counts[digit] += 1
                    
                    valid = True
                    current_max = 0
                    current_min = float('inf')
                    active_digits = 0
                    
                    for c in new_counts:
                        if c > 0:
                            active_digits += 1
                            if c > current_max:
                                current_max = c
                            if c < current_min:
                                current_min = c
                    
                    if active_digits > 0 and current_max > length:
                        valid = False
                    
                    if valid:
                        res += dp(index + 1, new_is_less, True, tuple(new_counts))

            memo[state] = res
            return res

        # The digit DP above is slightly inefficient due to the tuple state.
        # Let's use a more optimized approach for the specific "balanced" constraint.
        # A number is balanced if all present digits appear K times.
        # Total digits used = K * (number of distinct digits).
        # Since max digits is ~19 (for 64-bit int), K * distinct_digits <= 19.
        
        memo_optimized = {}

        def dp_optimized(idx: int, is_less: bool, is_started: bool, counts: tuple[int, ...]) -> int:
            state = (idx, is_less, is_started, counts)
            if state in memo_optimized:
                return memo_optimized[state]
            
            if idx == length:
                if not is_started:
                    return 0
                distinct_counts = set()
                for c in counts:
                    if c > 0:
                        distinct_counts.add(c)
                return 1 if len(distinct_counts) == 1 else 0

            res = 0
            upper = int(s[idx]) if not is_less else 9
            for d in range(upper + 1):
                next_is_less = is_less or (d < upper)
                if not is_started and d == 0:
                    res += dp_optimized(idx + 1, next_is_less, False, counts)
                else:
                    next_counts = list(counts)
                    next_counts[d] += 1
                    # Pruning: if any digit count exceeds the possible K, we could prune, 
                    # but K is not fixed. However, we know K * distinct_digits <= length.
                    # A simpler pruning: if any count > length, it's impossible.
                    if next_counts[d] <= length:
                        res += dp_optimized(idx + 1, next_is_less, True, tuple(next_counts))
            
            memo_optimized[state] = res
            return res

        # The state space for counts is too large for standard DP.
        # Let's use the property: K * number_of_digits = total_digits_in_number.
        # We can iterate over all possible total lengths (1 to length) 
        # and all possible K (1 to length) and all possible number of distinct digits.
        
        def count_with_fixed_k(target_len: int, k: int) -> int:
            # Count numbers of exactly target_len where each digit used appears exactly k times.
            # This is a combinatorial problem or a smaller DP.
            # But we need to respect the 'n' boundary.
            
            memo_comb = {}

            def solve_comb(idx: int, is_less: bool, is_started: bool, counts: tuple[int, ...]) -> int:
                state = (idx, is_less, is_started, counts)
                if state in memo_comb:
                    return memo_comb[state]
                
                if idx == length:
                    if not is_started: return 0
                    # Check if all non-zero counts are exactly k
                    for c in counts:
                        if c > 0 and c != k:
                            return 0
                    return 1

                res = 0
                upper = int(s[idx]) if not is_less else 9
                for d in range(upper + 1):
                    next_is_less = is_less or (d < upper)
                    if not is_started and d == 0:
                        res += solve_comb(idx + 1, next_is_less, False, counts)
                    else:
                        if counts[d] < k:
                            next_counts = list(counts)
                            next_counts[d] += 1
                            res += solve_comb(idx + 1, next_is_less, True, tuple(next_counts))
                
                memo_comb[state] = res
                return res

            # This is still essentially the same. Let's refine the approach.
            return 0

        # Correct approach: Digit DP where we track counts of all 10 digits.
        # To make it feasible, we only care about the counts.
        # Since we need to check if all non-zero counts are equal, 
        # we can pass the current counts in the DP.
        
        memo_final = {}

        def dp_final(idx: int, is_less: bool, is_started: bool, counts: tuple[int, ...]) -> int:
            state = (idx, is_less, is_started, counts)
            if state in memo_final:
                return memo_final[state]
            
            if idx == length:
                if not is_started:
                    return 0
                active_counts = [c for c in counts if c > 0]
                if not active_counts:
                    return 0
                return 1 if all(c == active_counts[0] for c in active_counts) else 0

            res = 0
            limit = int(s[idx]) if not is_less else 9
            for d in range(limit + 1):
                new_is_less = is_less or (d < limit)
                if not is_started and d == 0:
                    res += dp_final(idx + 1, new_is_less, False, counts)
                else:
                    new_counts = list(counts)
                    new_counts[d] += 1
                    # Pruning: if any count > length, it's impossible.
                    # Also, if we are at the end, we check the condition.
                    # To optimize, we can check if it's even possible to satisfy the condition.
                    # But for log10(n) <= 19, the state space is manageable if we use a tuple.
                    if new_counts[d] <= length:
                        res += dp_final(idx + 1, new_is_less, True, tuple(new_counts))
            
            memo_final[state] = res
            return res

        # The state space (idx, is_less, is_started, counts) is still potentially large.
        # However, the sum of counts is exactly 'idx' (if is_started).
        # The number of partitions of 'idx' into 10 parts is small.
        return dp_final(0, False, False, (0,) * 10)

    # The DP above is still a bit slow for a single call. 
    # Let's use a more direct combinatorial approach for numbers with length < len(str(high)).
    
    def count_exact_length(L: int, n_str: str, is_bounded: bool) -> int:
        # Count numbers of length L. 
        # If is_bounded is True, the number must be <= n_str.
        # If is_bounded is False, it can be any number of length L.
        
        # A number of length L is balanced if there exists K such that 
        # K * (number of distinct digits) = L.
        # Possible values for K: divisors of L.
        # Possible values for D (distinct digits): L / K.
        
        total_balanced = 0
        
        # Precompute factorials for combinations
        fact = [1] * 21
        for i in range(2, 21):
            fact[i] = fact[i-1] * i

        def nCr(n, r):
            if r < 0 or r > n: return 0
            return fact[n] // (fact[r] * fact[n-r])

        # For a fixed L, K, and D = L/K:
        # We need to choose D digits from {0..9} and arrange them such that each appears K times.
        # If the number must be <= n_str, we use digit DP.
        
        memo = {}

        def dp(idx: int, is_less: bool, is_started: bool, counts: tuple[int, ...], target_k: int) -> int:
            state = (idx, is_less, is_started, counts)
            if state in memo: return memo[state]
            
            if idx == L:
                if not is_started: return 0
                active = [c for c in counts if c > 0]
                return 1 if active and all(c == target_k for c in active) else 0
            
            res = 0
            limit = int(n_str[idx]) if (is_bounded and not is_less) else 9
            for d in range(limit + 1):
                new_is_less = is_less or (d < limit)
                if not is_started and d == 0:
                    # This case is actually handled by the fact that we are looking for 
                    # numbers of EXACT length L. So the first digit cannot be 0.
                    continue 
                else:
                    if counts[d] < target_k:
                        new_counts = list(counts)
                        new_counts[d] += 1
                        res += dp(idx + 1, new_is_less, True, tuple(new_counts), target_k)
            
            memo[state] = res
            return res

        # Actually, the simplest way is to iterate through all possible K.
        # For a fixed K, a number is balanced if all its non-zero digit counts are K.
        # The total number of digits used is K * D, where D is the number of distinct digits.
        # So K * D must equal the length of the number.
        
        # Let's use a single DP that counts all balanced numbers up to N.
        # A number is balanced if all its non-zero digit counts are equal.
        
        memo_all = {}
        s_n = str(n)
        len_n = len(s_n)

        def dp_all(idx: int, is_less: bool, is_started: bool, counts: tuple[int, ...]) -> int:
            state = (idx, is_less, is_started, counts)
            if state in memo_all: return memo_all[state]
            
            if idx == len_n:
                if not is_started: return 0
                active = [c for c in counts if c > 0]
                return 1 if active and all(c == active[0] for c in active) else 0
            
            res = 0
            limit = int(s_n[idx]) if not is_less else 9
            for d in range(limit + 1):
                new_is_less = is_less or (d < limit)
                if not is_started and d == 0:
                    res += dp_all(idx + 1, new_is_less, False, counts)
                else:
                    new_counts = list(counts)
                    new_counts[d] += 1
                    if new_counts[d] <= len_n:
                        res += dp_all(idx + 1, new_is_less, True, tuple(new_counts))
            
            memo_all[state] = res
            return res

        return dp_all(0, False, False, (0,) * 10)

    return count_balanced_up_to(high) - count_balanced_up_to(low - 1)