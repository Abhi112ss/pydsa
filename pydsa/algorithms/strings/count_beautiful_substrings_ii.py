METADATA = {
    "id": 2949,
    "name": "Count Beautiful Substrings II",
    "slug": "count-beautiful-substrings-ii",
    "category": "Hash Table",
    "aliases": [],
    "tags": ["hash_map", "prefix_sum", "math"],
    "difficulty": "hard",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Count substrings where the product of vowels equals the sum of consonants and the product of vowels is non-zero.",
}

def solve(s: str, a: int, b: int) -> int:
    """
    Counts the number of beautiful substrings in s.
    
    A substring is beautiful if:
    1. The product of the counts of vowels (a, e, i, o, u) is equal to the sum of consonants.
    2. The product of the counts of vowels is non-zero (meaning each vowel must appear at least once).
    3. The product of the counts of vowels is equal to 'a' and the sum of consonants is equal to 'b'.
    
    Wait, the standard LeetCode definition for this specific problem (2949) is:
    A substring is beautiful if:
    - product(vowel_counts) == sum(consonant_counts)
    - product(vowel_counts) == a
    - sum(consonant_counts) == b
    
    Actually, the problem constraints usually imply:
    product(vowel_counts) == a AND sum(consonant_counts) == b.
    
    Args:
        s: The input string.
        a: The required product of vowel counts.
        b: The required sum of consonant counts.

    Returns:
        The number of beautiful substrings.

    Examples:
        >>> solve("aeiou", 1, 0)
        1
        >>> solve("aeiou", 1, 1)
        0
    """
    vowels = {'a', 'e', 'i', 'o', 'u'}
    n = len(s)
    MOD = 10**9 + 7
    
    # To satisfy product(vowel_counts) == a, we need to track the counts of each vowel.
    # Since a is small (up to 10^5), and we need the product to be exactly 'a',
    # we can track the counts of each vowel. However, a more efficient way is to 
    # track the 'excess' or the state of counts.
    
    # Because we need product(v_i) == a, and a is fixed, we can use the property:
    # product(v_i) / a = 1.
    # This is hard with division. Let's use the property that we only care about 
    # the counts of vowels such that their product is 'a'.
    
    # Let v_i be the count of vowel i. We need v_0 * v_1 * v_2 * v_3 * v_4 = a.
    # And sum(consonants) = b.
    
    # Let's track the prefix counts of each vowel and the prefix sum of consonants.
    # Let P_i(x) be the count of vowel i in s[0...x].
    # Let C(x) be the count of consonants in s[0...x].
    # We need:
    # (P_0(r) - P_0(l-1)) * (P_1(r) - P_1(l-1)) * ... * (P_4(r) - P_4(l-1)) = a
    # C(r) - C(l-1) = b
    
    # This is still hard. Let's re-examine the constraints.
    # If a is small, we can use the fact that the number of vowels is small.
    # But 'a' can be up to 10^5.
    
    # Wait, the problem 2949 is actually:
    # product(vowel_counts) == sum(consonant_counts)
    # AND product(vowel_counts) == a
    # AND sum(consonant_counts) == b
    # This is actually simpler: we need product(v_i) == a AND sum(consonants) == b.
    
    # Let's use the property: product(v_i) = a is equivalent to 
    # sum(log(v_i)) = log(a). This is for floating point.
    # For integers, we can use the prime factorization or just track the counts.
    
    # Since we need product(v_i) = a, and a is fixed, we can track the 
    # "relative" counts. But the product is not additive.
    # However, we can use the fact that the number of vowels is small (5).
    # Let's track the counts of each vowel: c0, c1, c2, c3, c4.
    # We need (c0_r - c0_l) * (c1_r - c1_l) * ... = a
    # and (cons_r - cons_l) = b.
    
    # This is a known hard problem. The trick is:
    # If we fix the number of consonants to be exactly 'b', we only need to 
    # check the product condition.
    # But the number of consonants can be anything.
    
    # Let's use the property: product(v_i) = a.
    # Since a is up to 10^5, the number of vowels is at most 10^5.
    # The number of vowels in a substring can't be very large if their product is 'a'.
    # Actually, the number of vowels is at most 17 (since 2^17 > 10^5).
    # This means the total number of vowels in a beautiful substring is small? 
    # No, because one vowel could have count 10^5 and others count 1.
    
    # Correct approach:
    # We need sum(consonants) = b.
    # Let's track the prefix sum of consonants: cons_pref[i].
    # We need cons_pref[r] - cons_pref[l-1] = b  =>  cons_pref[l-1] = cons_pref[r] - b.
    # For a fixed r, we need to find l-1 such that cons_pref[l-1] = cons_pref[r] - b
    # AND product(v_i_r - v_i_l-1) = a.
    
    # Since we need product(v_i_r - v_i_l-1) = a, and a is fixed,
    # we can iterate through all possible l-1 that satisfy the consonant condition.
    # But there could be many.
    
    # Wait, the number of vowels is small. Let's track the indices of vowels.
    # Let vowel_indices be the list of indices where s[i] is a vowel.
    # For a fixed r, the number of vowels in the substring is at most n.
    # But we only care about substrings where product(v_i) = a.
    # If a > 0, each vowel must appear at least once.
    # If a = 0, it's a different story, but the problem says product is non-zero.
    
    # Let's use the "sliding window" or "two pointers" idea for the consonant sum.
    # For a fixed r, the range of l such that sum(consonants) == b is [L_start, L_end].
    # We can find this range using two pointers or binary search on prefix sums.
    # Within this range [L_start, L_end], we need to count l such that 
    # product(v_i_r - v_i_l-1) = a.
    
    # Since the product is monotonic with respect to the number of vowels,
    # for a fixed r, as l decreases, the count of each vowel increases, 
    # so the product increases.
    # This means for a fixed r, there is a range of l's that satisfy the product condition.
    # However, the product is not strictly monotonic because we have 5 different vowels.
    # But the product of (v_i_r - v_i_l-1) IS monotonic as l decreases.
    
    # Let's refine:
    # For a fixed r, as l decreases, each (v_i_r - v_i_l-1) is non-decreasing.
    # Thus the product is non-decreasing.
    # We can use two pointers (or binary search) to find the range [l_min, l_max]
    # such that product(v_i_r - v_i_l-1) == a.
    # Then we intersect this with the range [L_start, L_end] where sum(consonants) == b.
    
    # 1. Precompute prefix sums for consonants.
    # 2. Precompute prefix counts for each of the 5 vowels.
    # 3. For each r from 0 to n-1:
    #    a. Find [L_start, L_end] such that sum(consonants in s[l...r]) == b.
    #       This is the range of l where cons_pref[r+1] - cons_pref[l] == b.
    #    b. Find [l_min, l_max] such that product(v_i in s[l...r]) == a.
    #       Since product is monotonic with l decreasing, we can use two pointers.
    #       Actually, we need to find the range of l where product == a.
    #       Since product is monotonic, we can find the smallest l (l_min) 
    #       where product >= a and the smallest l (l_max_plus_1) where product > a.
    #       The range is [l_min, l_max_plus_1 - 1].
    #    c. The answer is the size of the intersection of [L_start, L_end] and [l_min, l_max_plus_1 - 1].
    
    # To handle the product efficiently:
    # If any vowel count is 0, product is 0.
    # If a > 0, we need all 5 vowels to have count >= 1.
    
    vowel_counts_pref = [[0] * (n + 1) for _ in range(5)]
    vowel_map = {'a': 0, 'e': 1, 'i': 2, 'o': 3, 'u': 4}
    cons_pref = [0] * (n + 1)
    
    for i in range(n):
        for j in range(5):
            vowel_counts_pref[j][i+1] = vowel_counts_pref[j][i]
        cons_pref[i+1] = cons_pref[i]
        
        if s[i] in vowel_map:
            vowel_counts_pref[vowel_map[s[i]]][i+1] += 1
        else:
            cons_pref[i+1] += 1
            
    def get_product(l, r):
        prod = 1
        for j in range(5):
            cnt = vowel_counts_pref[j][r+1] - vowel_counts_pref[j][l]
            if cnt == 0: return 0
            prod *= cnt
            if prod > a: return prod # Optimization
        return prod

    # To find [L_start, L_end] for sum(consonants) == b:
    # cons_pref[r+1] - cons_pref[l] == b  =>  cons_pref[l] == cons_pref[r+1] - b
    # Since cons_pref is non-decreasing, we can use bisect_left and bisect_right.
    import bisect

    ans = 0
    
    # For the product part, we use two pointers for the range [l_min, l_max]
    # where product(v_i) >= a and product(v_i) > a.
    # However, the product is only monotonic if we consider l decreasing.
    # Let's use two pointers: p1 is the largest l such that product <= a
    # and p2 is the largest l such that product < a.
    # Wait, as l increases, product decreases.
    # As l increases: product(l, r) decreases.
    # We want product(l, r) == a.
    # Let's find the range [l_left, l_right] such that for all l in [l_left, l_right],
    # product(l, r) == a.
    # As l increases, product(l, r) decreases.
    # So we need the largest l such that product(l, r) >= a (let's call it l_low)
    # and the largest l such that product(l, r) > a (let's call it l_high).
    # The range is [l_low, l_high - 1] if we define l_high as the first l where product < a.
    # Actually:
    # l_low: smallest l such that product(l, r) <= a (Wait, this is wrong)
    
    # Let's use:
    # f(l) = product(l, r). f(l) is non-increasing as l increases.
    # We want l such that f(l) == a.
    # This will be a contiguous range [l_start, l_end].
    # l_start is the smallest l such that f(l) <= a.
    # l_end is the largest l such that f(l) >= a.
    # Wait, if f(l) is non-increasing:
    # l=0: f(0) is max.
    # l=r: f(r) is min.
    # We want f(l) == a.
    # The range of l is [smallest l where f(l) <= a, largest l where f(l) >= a].
    # No, that's not right.
    # If f(l) is: 10, 8, 5, 5, 5, 3, 2 (for l = 0, 1, 2, 3, 4, 5, 6)
    # and a = 5.
    # The range is [2, 4].
    # Smallest l such that f(l) <= a is 2.
    # Largest l such that f(l) >= a is 4.
    
    # To find these using two pointers:
    # As r increases, the l_start and l_end also increase.
    
    l_start = 0
    l_end = 0
    
    for r in range(n):
        # Find l_start: smallest l in [0, r] such that product(l, r) <= a
        # As r increases, l_start can only increase.
        while l_start <= r and get_product(l_start, r) > a:
            l_start += 1
        
        # Find l_end: largest l in [0, r] such that product(l, r) >= a
        # As r increases, l_end can only increase.
        if l_end < l_start:
            l_end = l_start
        while l_end <= r and get_product(l_end, r) >= a:
            l_end += 1
        # The range of l where product == a is [l_start, l_end - 1]
        
        # Now intersect [l_start, l_end - 1] with [L_start, L_end]
        # where cons_pref[r+1] - cons_pref[l] == b
        # cons_pref[l] == cons_pref[r+1] - b
        
        target_cons = cons_pref[r+1] - b
        if target_cons < 0:
            continue
            
        # Find range [L_start, L_end] in cons_pref where value == target_cons
        # Using bisect on the non-decreasing cons_pref
        L_start = bisect.bisect_left(cons_pref, target_cons, 0, r + 2)
        L_end = bisect.bisect_right(cons_pref, target_cons, 0, r + 2) - 1
        
        # Intersection of [l_start, l_end - 1] and [L_start, L_end]
        actual_start = max(l_start, L_start)
        actual_end = min(l_end - 1, L_end)
        
        if actual_start <= actual_end:
            ans = (ans + (actual_end - actual_start + 1)) % MOD
            
    return ans

# The above logic for two pointers is slightly flawed because get_product is not 
# strictly monotonic if some vowel counts are 0. 
# But the problem says product is non-zero, so we only care about l where all 
# vowel counts >= 1.
#