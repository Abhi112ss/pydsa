METADATA = {
    "id": 3348,
    "name": "Smallest Divisible Digit Product II",
    "slug": "smallest-divisible-digit-product-ii",
    "category": "Math",
    "aliases": [],
    "tags": ["math", "digit_dp", "greedy"],
    "difficulty": "hard",
    "time_complexity": "O(log n)",
    "space_complexity": "O(log n)",
    "description": "Find the smallest non-negative integer whose digits' product is divisible by a given number n.",
}

def solve(n: int) -> str:
    """
    Finds the smallest non-negative integer whose digits' product is divisible by n.
    
    The problem asks for the smallest number such that the product of its digits 
    is a multiple of n. Since we want the smallest number, we want the fewest 
    number of digits, and then the smallest lexicographical sequence.
    
    Args:
        n: The target divisor.

    Returns:
        A string representing the smallest non-negative integer.

    Examples:
        >>> solve(1)
        '0' (Wait, product of digits of 0 is 0, 0 % 1 == 0. Smallest non-negative is 0)
        Actually, for n=1, the smallest non-negative integer is 0.
        However, standard digit product problems usually imply positive integers 
        unless 0 is explicitly allowed. If n=1, 0 is the smallest.
        If n=10, digits must multiply to a multiple of 10 (e.g., 25 -> 10, 52 -> 10).
        Smallest is 25.
    """
    if n == 0:
        return "0"
    if n == 1:
        return "0"

    # Special case: if n is divisible by 0 (not possible) or if we can use '0'
    # The product of digits of '0' is 0. 0 % n is always 0 for n > 0.
    # However, in most competitive programming contexts for this specific problem,
    # '0' is considered to have a digit product of 0.
    # If the problem implies the number must be positive, we'd start from 1.
    # Given the "Smallest Divisible Digit Product" context, 0 is the smallest non-negative.
    # But if the product must be a multiple of n and n > 0, 0 works.
    # Let's assume the standard interpretation where we look for the smallest 
    # positive integer if n > 1, or handle the digit 0 carefully.
    # Actually, if we use the digit 0, the product is 0, which is divisible by any n.
    # The smallest non-negative integer with digit product 0 is 0.
    # If the problem constraints or test cases imply positive integers, 
    # we look for the smallest number whose digits are in [1-9] or contains 0.
    # But any number containing 0 has product 0. The smallest number containing 0 is 0.
    # If the problem implies the product must be a NON-ZERO multiple of n, 
    # then we cannot use the digit 0.
    
    # Re-evaluating: Usually, these problems imply the product of digits 
    # must be a multiple of n AND the product must be > 0 (to avoid the trivial 0).
    # If the product must be > 0, we can only use digits 1-9.
    # This means n must only have prime factors 2, 3, 5, and 7.
    
    temp_n = n
    for p in [2, 3, 5, 7]:
        while temp_n % p == 0:
            temp_n //= p
            
    if temp_n > 1:
        # If n has prime factors other than 2, 3, 5, 7, no product of digits 1-9 
        # can be a multiple of n. However, the digit 0 makes the product 0.
        # 0 is divisible by any n. The smallest non-negative integer is 0.
        # If the problem implies positive integers, and n has factors > 7, 
        # we must use the digit 0. The smallest positive integer with digit 0 is 10.
        # But 10's product is 0. 0 % n == 0.
        # Let's check if n=10. Smallest positive integer with product divisible by 10:
        # 25 (2*5=10). 10 (1*0=0, 0%10=0). 
        # If 0 is allowed as a digit, any number with a 0 works.
        # The smallest non-negative integer is 0.
        # If the problem implies the product must be a POSITIVE multiple of n:
        return "-1" # This would be the case if n has prime factors > 7.

    # If we need a positive product, we need to find the smallest number 
    # composed of digits 2-9 such that their product is a multiple of n.
    # We use a greedy approach: to minimize the number of digits, 
    # we should use the largest possible digits (like 9, 8, 7...) 
    # to satisfy the prime factor requirements.
    
    # Count required prime factors
    factors = {2: 0, 3: 0, 5: 0, 7: 0}
    for p in [2, 3, 5, 7]:
        while temp_n % p == 0:
            factors[p] += 1
            temp_n //= p
            
    # We want to satisfy these counts using digits 2-9.
    # To minimize the number of digits, we use digits that "consume" 
    # the most prime factors.
    # 9 consumes two 3s.
    # 8 consumes three 2s.
    # 7 consumes one 7.
    # 6 consumes one 2 and one 3.
    # 5 consumes one 5.
    # 4 consumes two 2s.
    # 3 consumes one 3.
    # 2 consumes one 2.
    
    # This is a variation of the change-making problem or knapsack, 
    # but since we want the smallest number, we want the fewest digits.
    # For a fixed number of digits, we want the smallest leading digits.
    
    # Let's use dynamic programming to find the minimum number of digits.
    # dp[c2][c3][c5][c7] = min digits needed
    # Given n can be up to 10^18, log2(n) is ~60.
    # Max counts: c2 ~ 60, c3 ~ 40, c5 ~ 26, c7 ~ 22.
    # This DP is too large.
    
    # Greedy approach for minimum digits:
    # 1. Use as many 9s as possible for 3s.
    # 2. Use as many 8s as possible for 2s.
    # 3. Use as many 7s as possible for 7s.
    # 4. Use as many 5s as possible for 5s.
    # 5. Handle remaining 2s and 3s using 6, 4, 3, 2.
    
    # Wait, the greedy choice for 2s and 3s is tricky because 6 uses both.
    # Let's refine:
    # To minimize digits, we prioritize:
    # 7s: count7 = factors[7]
    # 5s: count5 = factors[5]
    # 3s: We can use 9s (two 3s) or 3s (one 3).
    # 2s: We can use 8s (three 2s) or 4s (two 2s) or 2s (one 2).
    # 6s: Use 6s to combine a 2 and a 3 if it helps reduce total digit count.
    
    # Correct Greedy for minimum digits:
    # The number of digits is minimized by using the largest possible factors.
    # Total digits = count7 + count5 + (digits for 2s and 3s).
    # For 2s and 3s, we want to find digits from {2, 3, 4, 6, 8, 9} 
    # that satisfy the counts with minimum total digits.
    
    # Since the number of 2s and 3s is small, we can iterate on the number of 6s.
    # Let k be the number of 6s used.
    # Remaining 2s: factors[2] - k
    # Remaining 3s: factors[3] - k
    # We must have k <= min(factors[2], factors[3]).
    # For a fixed k:
    # digits_from_2s = ceil((factors[2] - k) / 3) if we use 8s
    # Actually, we can use 8s, 4s, 2s. To minimize digits, use 8s.
    # digits_from_3s = ceil((factors[3] - k) / 2) if we use 9s.
    
    # But we can also use 4s or 2s. 
    # Let's try all possible counts of 6s, 9s, 8s, 4s, 3s, 2s.
    # Actually, the number of digits is small. Let's use BFS to find the shortest path.
    # State: (c2, c3, c5, c7)
    # But we want the smallest number, so BFS finds the shortest length, 
    # then we can find the lexicographically smallest.
    
    import collections
    
    # target_factors = (f2, f3, f5, f7)
    target = (factors[2], factors[3], factors[5], factors[7])
    
    # queue stores (c2, c3, c5, c7)
    # dist stores min digits to reach this state
    # parent stores (prev_state, digit)
    queue = collections.deque([(0, 0, 0, 0)])
    visited = {(0, 0, 0, 0): (None, None)}
    
    # To handle the "at least" requirement, we cap the counts at target.
    # If we have more 2s than needed, it's fine.
    
    while queue:
        curr = queue.popleft()
        if curr == target:
            break
            
        c2, c3, c5, c7 = curr
        
        # Try digits 2-9
        for d in range(2, 10):
            # Calculate factors of d
            d2, d3, d5, d7 = 0, 0, 0, 0
            if d == 2: d2 = 1
            elif d == 3: d3 = 1
            elif d == 4: d2 = 2
            elif d == 5: d5 = 1
            elif d == 6: d2, d3 = 1, 1
            elif d == 7: d7 = 1
            elif d == 8: d2 = 3
            elif d == 9: d3 = 2
            
            next_state = (
                min(target[0], c2 + d2),
                min(target[1], c3 + d3),
                min(target[2], c5 + d5),
                min(target[3], c7 + d7)
            )
            
            if next_state not in visited:
                visited[next_state] = (curr, d)
                queue.append(next_state)
                
    # Reconstruct path
    res = []
    curr = target
    while curr != (0, 0, 0, 0):
        prev, digit = visited[curr]
        res.append(str(digit))
        curr = prev
        
    # The BFS finds the shortest length. To ensure lexicographical smallest,
    # we should iterate digits 2-9 in the BFS and the first time we hit a state, 
    # it's the shortest. But for the same length, we need the smallest number.
    # Standard BFS finds shortest path. To get lexicographical smallest among 
    # shortest paths, we should process digits in increasing order.
    # However, the reconstruction goes backwards. 
    # To get the smallest number, we need to ensure that for a fixed length, 
    # we pick the smallest digits at the beginning.
    # A better way: BFS finds the shortest length. Then use DP to find the 
    # smallest number of that length.
    
    # Let's refine the BFS:
    # To get the smallest number:
    # 1. BFS to find the minimum distance (number of digits) to reach target.
    # 2. Use the distance to perform a greedy construction from left to right.
    
    # Re-run BFS to get distances
    dist = {(0, 0, 0, 0): 0}
    queue = collections.deque([(0, 0, 0, 0)])
    while queue:
        curr = queue.popleft()
        c2, c3, c5, c7 = curr
        for d in range(2, 10):
            d2, d3, d5, d7 = 0, 0, 0, 0
            if d == 2: d2 = 1
            elif d == 3: d3 = 1
            elif d == 4: d2 = 2
            elif d == 5: d5 = 1
            elif d == 6: d2, d3 = 1, 1
            elif d == 7: d7 = 1
            elif d == 8: d2 = 3
            elif d == 9: d3 = 2
            
            nxt = (min(target[0], c2 + d2), min(target[1], c3 + d3), 
                   min(target[2], c5 + d5), min(target[3], c7 + d7))
            if nxt not in dist:
                dist[nxt] = dist[curr] + 1
                queue.append(nxt)
                
    # Now construct the number digit by digit
    # We want to pick the smallest digit d such that dist[target_after_d] = dist[current] - 1
    # Wait, the distance is from (0,0,0,0) to target.
    # We want to go from (0,0,0,0) to target in 'min_len' steps.
    # At each step, pick smallest d such that there exists a path from 
    # (new_state) to target with (min_len - current_len - 1) steps.
    
    # Let's use BFS from target backwards to find min distance to target.
    dist_to_target = {target: 0}
    queue = collections.deque([target])
    while queue:
        curr = queue.popleft()
        c2, c3, c5, c7 = curr
        # To go backwards, we need to know which digits could have led to 'curr'
        # This is hard because of the 'min(target, ...)' capping.
        # Let's use the 'dist' from (0,0,0,0) to target.
        # Let L = dist[target].
        # We want to find digits d1, d2, ... dL such that 
        # state0 -> state1 -> ... -> stateL = target
        # and d1 is minimal, then d2 is minimal, etc.
        # A digit d is valid at step i if dist[state_i] + dist_from_state_i_to_target == L.
        # But we don't have dist_from_state_i_to_target.
        
        # Let's use the BFS to find the shortest distance from (0,0,0,0) to all states.
        # Then, let f(state) be the minimum digits to reach 'target' from 'state'.
        # f(state) = 1 + min(f(next_state)) for d in 2..9.
        # This is just BFS from target backwards.
        # To handle the 'min' cap, we treat the state as (c2, c3, c5, c7) 
        # where c_i is the number of factors of prime p_i we HAVE.
        # The target is (target_c2, target_c3, target_c5, target_c7).
        # A transition is: next_c_i = min(target_c_i, curr_c_i + d_i).
        # This is exactly what we did.
        pass

    # Let's use the BFS result to reconstruct the smallest number.
    # The BFS finds the shortest path. To get the lexicographically smallest:
    # In the BFS, when we visit a state, we record the digit used.
    # To ensure lexicographical smallest, we must ensure that if two paths 
    # have the same length, we