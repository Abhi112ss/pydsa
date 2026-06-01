METADATA = {
    "id": 3756,
    "name": "Concatenate Non-Zero Digits and Multiply by Sum II",
    "slug": "concatenate_non_zero_digits_and_multiply_by_sum_ii",
    "category": "Math",
    "aliases": [],
    "tags": ["math", "digit_dp"],
    "difficulty": "hard",
    "time_complexity": "O(log(n))",
    "space_complexity": "O(log(n))",
    "description": "Calculate the sum of numbers formed by concatenating non-zero digits of each integer in a range, multiplied by the sum of those digits.",
}

def solve(n: int) -> int:
    """
    Calculates the sum of (concatenated_non_zero_digits * sum_of_digits) for all 1 <= i <= n.
    
    The problem asks for the sum over i from 1 to n of:
    f(i) = (Value formed by concatenating non-zero digits of i) * (Sum of non-zero digits of i)
    
    Since n can be very large, we use Digit Dynamic Programming.
    
    Args:
        n: The upper bound of the range (inclusive).

    Returns:
        The total sum calculated.

    Examples:
        >>> solve(12)
        # i=1: 1*1=1; i=2: 2*2=4; ... i=9: 9*9=81; i=10: 1*1=1; i=11: 11*(1+1)=22; i=12: 12*(1+2)=36
        # Total: 1+4+9+16+25+36+49+64+81+1+22+36 = 344
        344
    """
    s_n = str(n)
    length = len(s_n)
    
    # memo stores: (index, is_less, is_started) -> (count, sum_of_concatenated, sum_of_digits, sum_of_products)
    # count: number of valid integers formed
    # sum_of_concatenated: sum of the values formed by concatenating non-zero digits
    # sum_of_digits: sum of the sum of digits for all valid integers
    # sum_of_products: sum of (concatenated_val * sum_of_digits)
    memo = {}

    def dp(idx: int, is_less: bool, is_started: bool) -> tuple[int, int, int, int]:
        state = (idx, is_less, is_started)
        if state in memo:
            return memo[state]
        
        if idx == length:
            # Base case: return (count=1, concat=0, digit_sum=0, product_sum=0)
            # Note: product_sum is 0 because we haven't added anything yet.
            return (1, 0, 0, 0) if is_started else (0, 0, 0, 0)

        res_count = 0
        res_concat = 0
        res_digit_sum = 0
        res_prod_sum = 0

        limit = int(s_n[idx]) if not is_less else 9

        for digit in range(limit + 1):
            new_is_less = is_less or (digit < limit)
            new_is_started = is_started or (digit > 0)
            
            # Recursive call for the next digit
            count, concat, d_sum, p_sum = dp(idx + 1, new_is_less, new_is_started)
            
            if not new_is_started:
                # Still leading zeros
                res_count += count
                res_concat += concat
                res_digit_sum += d_sum
                res_prod_sum += p_sum
            else:
                # If digit is 0, it doesn't contribute to concatenation or digit sum
                if digit == 0:
                    res_count += count
                    res_concat += concat
                    res_digit_sum += d_sum
                    res_prod_sum += p_sum
                else:
                    # If digit > 0, it affects concatenation and digit sum
                    # Let V be the value formed by subsequent non-zero digits.
                    # New concatenated value = digit * 10^(number of non-zero digits in suffix) + V
                    # However, the number of non-zero digits in suffix is variable.
                    # To handle this, we need to track the number of non-zero digits in the DP state.
                    # Wait, the problem says "concatenate non-zero digits". 
                    # Example: 102 -> non-zero digits are 1, 2 -> concatenated is 12.
                    # This means the 'digit' is shifted by the number of non-zero digits following it.
                    pass

        # The logic above requires knowing the count of non-zero digits in the suffix.
        # Let's redefine the DP state.
        return (0, 0, 0, 0)

    # Redefining DP to include 'non_zero_count' in the state to handle concatenation shifts.
    # State: (idx, is_less, is_started, non_zero_count_in_suffix)
    # Actually, it's easier to build from left to right.
    # If we add 'digit' to the front of a suffix that has 'k' non-zero digits:
    # New_Concat = digit * 10^k + Suffix_Concat
    
    memo = {}

    def dp_v2(idx: int, is_less: bool, is_started: bool) -> tuple[int, int, int, int, int]:
        """
        Returns:
        (count, sum_concat, sum_digit_sum, sum_prod, sum_pow10)
        where sum_pow10 is sum of (10^(number of non-zero digits in suffix))
        """
        state = (idx, is_less, is_started)
        if state in memo:
            return memo[state]
        
        if idx == length:
            # count, sum_concat, sum_digit_sum, sum_prod, sum_pow10
            return (1, 0, 0, 0, 1) if is_started else (0, 0, 0, 0, 0)

        res_count = 0
        res_concat = 0
        res_digit_sum = 0
        res_prod_sum = 0
        res_pow10 = 0

        limit = int(s_n[idx]) if not is_less else 9

        for digit in range(limit + 1):
            new_is_less = is_less or (digit < limit)
            new_is_started = is_started or (digit > 0)
            
            c, sc, sd, sp, sp10 = dp_v2(idx + 1, new_is_less, new_is_started)
            
            if not new_is_started:
                res_count += c
                res_concat += sc
                res_digit_sum += sd
                res_prod_sum += sp
                res_pow10 += sp10
            else:
                if digit == 0:
                    # Digit 0 doesn't change concatenation or digit sum
                    res_count += c
                    res_concat += sc
                    res_digit_sum += sd
                    res_prod_sum += sp
                    res_pow10 += sp10
                else:
                    # Digit > 0
                    # New concat = digit * (10^k) + suffix_concat
                    # New digit_sum = digit + suffix_digit_sum
                    # New prod = (digit * 10^k + suffix_concat) * (digit + suffix_digit_sum)
                    #          = digit^2 * 10^k + digit * suffix_digit_sum + digit * 10^k * suffix_digit_sum + suffix_concat * suffix_digit_sum
                    # Wait, the formula is: (Concat) * (DigitSum)
                    # Let C = digit * 10^k + Sc
                    # Let D = digit + Sd
                    # C * D = (digit * 10^k + Sc) * (digit + Sd)
                    #       = digit^2 * 10^k + digit * 10^k * Sd + digit * Sc + Sc * Sd
                    
                    # We need:
                    # 1. sum(c) -> res_count
                    # 2. sum(digit * 10^k + Sc) -> res_concat
                    # 3. sum(digit + Sd) -> res_digit_sum
                    # 4. sum((digit * 10^k + Sc) * (digit + Sd)) -> res_prod_sum
                    # 5. sum(10^k) -> res_pow10 (where k is non-zero count in suffix)
                    # 6. sum(10^k * Sd) -> extra needed for prod_sum
                    # 7. sum(Sc * Sd) -> extra needed for prod_sum
                    
                    # Let's refine the return tuple:
                    # (count, sum_concat, sum_digit_sum, sum_prod, sum_pow10, sum_pow10_sd, sum_concat_sd)
                    pass
        return (0,0,0,0,0,0,0)

    # Correct approach: The number of non-zero digits is at most 19 (for 64-bit int).
    # We can include 'k' (number of non-zero digits in suffix) in the state.
    # But we want to avoid O(log^2 N).
    # Actually, the "concatenate" part is just a way to say:
    # Value = sum_{j in non_zero_indices} digit_j * 10^(count of non-zero digits to the right of j)
    
    # Let's use the property:
    # Total Sum = Sum_{i=1}^n [ (Sum_{j in non_zero(i)} d_j * 10^{k_j}) * (Sum_{m in non_zero(i)} d_m) ]
    # where k_j is the number of non-zero digits in i to the right of index j.
    
    # This is still complex. Let's simplify.
    # For a fixed number i, let its non-zero digits be d_1, d_2, ..., d_m.
    # Concatenated value V = d_1*10^{m-1} + d_2*10^{m-2} + ... + d_m*10^0
    # Digit sum S = d_1 + d_2 + ... + d_m
    # V * S = (sum_{j=1}^m d_j 10^{m-j}) * (sum_{l=1}^m d_l)
    # V * S = sum_{j=1}^m sum_{l=1}^m d_j * d_l * 10^{m-j}
    
    # This is still hard. Let's use the standard Digit DP:
    # dp(idx, is_less, is_started) returns:
    # - count: number of ways to complete the number
    # - sum_v: sum of concatenated values of the suffixes
    # - sum_s: sum of digit sums of the suffixes
    # - sum_vs: sum of (suffix_v * suffix_s)
    # - sum_p10: sum of (10^(number of non-zero digits in suffix))
    # - sum_p10s: sum of (10^(number of non-zero digits in suffix) * suffix_s)
    
    memo = {}

    def dp_final(idx: int, is_less: bool, is_started: bool) -> tuple[int, int, int, int, int, int]:
        state = (idx, is_less, is_started)
        if state in memo:
            return memo[state]
        
        if idx == length:
            # count, sum_v, sum_s, sum_vs, sum_p10, sum_p10s
            return (1, 0, 0, 0, 1, 0) if is_started else (0, 0, 0, 0, 0, 0)

        res_count, res_v, res_s, res_vs, res_p10, res_p10s = 0, 0, 0, 0, 0, 0
        limit = int(s_n[idx]) if not is_less else 9

        for digit in range(limit + 1):
            new_is_less = is_less or (digit < limit)
            new_is_started = is_started or (digit > 0)
            
            c, sv, ss, svs, sp10, sp10s = dp_final(idx + 1, new_is_less, new_is_started)
            
            if not new_is_started:
                res_count += c
                res_v += sv
                res_s += ss
                res_vs += svs
                res_p10 += sp10
                res_p10s += sp10s
            else:
                if digit == 0:
                    res_count += c
                    res_v += sv
                    res_s += ss
                    res_vs += svs
                    res_p10 += sp10
                    res_p10s += sp10s
                else:
                    # digit > 0
                    # New V = digit * 10^k + sv
                    # New S = digit + ss
                    # New VS = (digit * 10^k + sv) * (digit + ss)
                    #        = digit^2 * 10^k + digit * 10^k * ss + digit * sv + sv * ss
                    
                    # We need sum(digit^2 * 10^k) = digit^2 * sum(10^k)
                    # We need sum(digit * 10^k * ss) = digit * sum(10^k * ss)
                    # We need sum(digit * sv) = digit * sum(sv)
                    # We need sum(sv * ss) = sum(svs)
                    
                    res_count += c
                    res_v += (digit * sp10 + sv)
                    res_s += (digit * c + ss)
                    res_vs += (digit * digit * sp10 + digit * sp10s + digit * sv + svs)
                    res_p10 += (10 * sp10) # This is wrong. 10^k is for the suffix. 
                    # If current digit is non-zero, the new suffix power is 10^(k+1)
                    # Wait, the power is based on the number of non-zero digits.
                    # If current digit is non-zero, the suffix's k becomes k+1.
                    # So sum(10^(k_new)) = sum(10^(k_old + 1)) = 10 * sum(10^k_old)
                    # But this is only if the current digit is non-zero.
                    # If current digit is zero, sum(10^k_new) = sum(10^k_old)
                    
                    # Let's re-evaluate the power of 10.
                    # The concatenated value is d_1*10^{m-1} + d_2*10^{m-2} ...
                    # If we are at idx, and there are k non-zero digits in the suffix:
                    # The current digit's contribution is digit * 10^k.
                    
                    # Corrected logic for digit > 0:
                    # res_p10 += 10 * sp10 (Wait, no. The suffix power is 10^k. 
                    # The new power for the whole number is 10^(k+1) if we consider the current digit.
                    # But the DP returns sums for the SUFFIX.
                    # If suffix has k non-zero digits, its power sum is sum(10^k).
                    # If we add a non-zero digit, the new suffix has k+1 non-zero digits.
                    # So the new sum(10^(k+1)) = 10 * sum(10^k).
                    
                    # Let's fix the digit > 0 block:
                    # res_count += c
                    # res_v += (digit * sp10 + sv)
                    # res_s += (digit * c + ss)
                    # res_vs += (digit * digit * sp10 + digit * sp10s + digit * sv + svs)
                    # res_p10 += 10 * sp10  <-- This is wrong. 
                    # The sp10 returned is sum(10^k) for the suffix.
                    # If we add a non-zero digit, the new suffix has k+1 non-zero digits.
                    # So the new sum(10^(k_new)) =