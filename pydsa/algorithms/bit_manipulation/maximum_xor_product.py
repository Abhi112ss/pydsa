METADATA = {
    "id": 2939,
    "name": "Maximum Xor Product",
    "slug": "maximum_xor_product",
    "category": "Bit Manipulation",
    "aliases": [],
    "tags": ["bit_manipulation", "greedy", "sorting"],
    "difficulty": "hard",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(n)",
    "description": "Partition an array into two non-empty subsets to maximize the product of their XOR sums.",
}

def solve(nums: list[int]) -> int:
    """
    Finds the maximum product of the XOR sums of two non-empty subsets.

    The problem asks to partition the array into two subsets A and B such that 
    (XOR_sum(A) * XOR_sum(B)) is maximized. 
    Let S be the XOR sum of all elements in the array. 
    If XOR_sum(A) = x, then XOR_sum(B) = S ^ x.
    We want to maximize x * (S ^ x).

    Args:
        nums: A list of integers.

    Returns:
        The maximum product of the XOR sums of the two subsets.

    Examples:
        >>> solve([1, 2, 3])
        0
        >>> solve([8, 1, 2, 12, 15])
        121
    """
    total_xor_sum = 0
    for num in nums:
        total_xor_sum ^= num

    # We want to find a value 'x' (representing XOR sum of subset A)
    # such that x * (total_xor_sum ^ x) is maximized.
    # To maximize the product, we want both x and (total_xor_sum ^ x) 
    # to be as large as possible, specifically focusing on bits 
    # that are NOT in total_xor_sum.
    
    # Step 1: Identify bits that are 0 in total_xor_sum.
    # These bits can be 'distributed' to either x or (total_xor_sum ^ x).
    # To maximize the product, we want to make x as large as possible 
    # using these bits.
    
    # Step 2: Use Gaussian elimination (Linear Basis) to find the 
    # maximum possible value for bits that are 0 in total_xor_sum.
    basis = []
    for num in nums:
        # We only care about bits that are 0 in total_xor_sum
        # because bits that are 1 in total_xor_sum will always 
        # result in one subset having 1 and the other having 0 at that position.
        # However, the standard approach is to build a basis for all bits
        # and then greedily construct x.
        for b in basis:
            num = min(num, num ^ b)
        if num > 0:
            basis.append(num)
            basis.sort(reverse=True)

    # We want to maximize x * (total_xor_sum ^ x).
    # Let's define x as the XOR sum of a subset.
    # We want to pick bits for x such that we maximize the product.
    # A key observation: bits that are 1 in total_xor_sum will always 
    # contribute to exactly one of the two terms.
    # Bits that are 0 in total_xor_sum can be contributed to both terms 
    # (if we can make them 1 in x, they become 1 in (total_xor_sum ^ x) too).
    
    # Let's refine x to prioritize bits that are 0 in total_xor_sum.
    # First, find the maximum possible value for bits that are 0 in total_xor_sum.
    target_x = 0
    
    # We want to maximize the bits that are 0 in total_xor_sum.
    # Let's extract the part of the basis that can influence bits where total_xor_sum is 0.
    # Actually, a simpler greedy approach:
    # 1. Start with x = 0.
    # 2. For bits from most significant to least significant:
    #    If bit i is 0 in total_xor_sum:
    #       Try to make bit i in x equal to 1.
    #    If bit i is 1 in total_xor_sum:
    #       We can't make both x and (total_xor_sum ^ x) have bit i.
    #       One will have it, one won't. This doesn't change the product's 
    #       magnitude as much as the 0-bits do.
    
    # Correct Greedy Strategy:
    # We want to maximize x where x is the XOR sum of some subset.
    # We want to maximize the bits that are 0 in total_xor_sum.
    # Let's build a basis specifically for the "0-bits".
    
    # Let's find the maximum possible value of x considering only bits 
    # where total_xor_sum has a 0.
    x_for_zero_bits = 0
    # We use the basis to maximize x_for_zero_bits, but we only care 
    # about bits where total_xor_sum is 0.
    # Actually, we can just use the basis to maximize x, but 
    # prioritize bits that are 0 in total_xor_sum.
    
    # Let's re-evaluate:
    # We want to maximize x * (total_xor_sum ^ x).
    # Let x_bits_0 be the bits of x where total_xor_sum is 0.
    # Let x_bits_1 be the bits of x where total_xor_sum is 1.
    # x = x_bits_0 | x_bits_1
    # total_xor_sum ^ x = x_bits_0 | (~x_bits_1)
    # To maximize the product, we want x_bits_0 to be as large as possible.
    
    # Step 1: Maximize bits that are 0 in total_xor_sum.
    # We can use the basis to find the maximum value of (x & ~total_xor_sum).
    max_zero_bits_val = 0
    for b in basis:
        # If XORing with b increases the value of the bits that are 0 in total_xor_sum
        if (max_zero_bits_val ^ b) & ~total_xor_sum > max_zero_bits_val & ~total_xor_sum:
            max_zero_bits_val ^= b
        # Or if it's equal, we might want to check if it helps bits that are 1 in total_xor_sum
        # but the priority is the 0-bits.
        elif (max_zero_bits_val ^ b) & ~total_xor_sum == max_zero_bits_val & ~total_xor_sum:
            if (max_zero_bits_val ^ b) > max_zero_bits_val:
                max_zero_bits_val ^= b

    # Now we have the best possible value for the bits that are 0 in total_xor_sum.
    # We still need to decide the bits that are 1 in total_xor_sum.
    # For a bit i where total_xor_sum is 1, one of (x) or (total_xor_sum ^ x) 
    # will have bit i, and the other won't.
    # To maximize the product (A * B), where A + B is constant (roughly), 
    # we want A and B to be as close as possible.
    # However, the bits where total_xor_sum is 1 are fixed in their sum.
    # Let's use the basis to find the best x.
    
    # Let's use a more robust approach:
    # We want to maximize x * (total_xor_sum ^ x).
    # Let's find the maximum possible value of x using the basis, 
    # but with a custom comparison.
    # We want to maximize the "0-bits" first, then balance the "1-bits".
    
    current_x = 0
    # We want to maximize (current_x & ~total_xor_sum)
    # Then, among those, we want to make current_x and (total_xor_sum ^ current_x) 
    # as close as possible? No, that's for sum. For product, we want them close.
    # Actually, for bits where total_xor_sum is 1, one is 1 and one is 0.
    # This doesn't change the product's "scale" as much as the 0-bits.
    
    # Let's refine:
    # 1. Maximize bits that are 0 in total_xor_sum.
    # 2. For bits that are 1 in total_xor_sum, we want to distribute them 
    #    to make x and (total_xor_sum ^ x) close.
    
    # Let's build the basis.
    # Then, find the maximum possible value of (x & ~total_xor_sum).
    # Let this be 'best_zero_bits'.
    # Then, we want to find the best 'x_bits_1' such that 
    # (best_zero_bits | x_bits_1) * (best_zero_bits | (total_xor_sum ^ x_bits_1)) is max.
    
    # Actually, the simplest way to maximize x * (S ^ x) is:
    # 1. Maximize the bits that are 0 in S.
    # 2. For bits that are 1 in S, we want to make the two numbers as close as possible.
    
    # Let's find the maximum possible value of (x & ~total_xor_sum) using the basis.
    # We can transform the basis to only represent bits that are 0 in total_xor_sum.
    
    # Let's use the basis to find the maximum possible value of x, 
    # where the priority of bits is:
    # Priority 1: Bits that are 0 in total_xor_sum (from MSB to LSB).
    # Priority 2: Bits that are 1 in total_xor_sum (to make x and S^x close).
    
    # To make x and S^x close, we want to pick bits such that x is 
    # roughly half of the total sum? No, that's not right.
    # If bit i is 1 in S, then in the product, one term gets 2^i and the other gets 0.
    # This is fixed. The only way to change the product is via the 0-bits.
    # If bit i is 0 in S, then both terms can get 2^i.
    
    # Wait, if bit i is 0 in S, then either both get 2^i or both get 0.
    # If bit i is 1 in S, then one gets 2^i and the other gets 0.
    
    # Let's re-calculate:
    # Let x = (x_0) | (x_1) where x_0 are bits where S is 0, and x_1 are bits where S is 1.
    # S ^ x = (x_0) | (S_1 ^ x_1) where S_1 are bits where S is 1.
    # Product = [x_0 + x_1] * [x_0 + (S_1 ^ x_1)]
    # Since x_0 and x_1 are bitwise disjoint, this is:
    # Product = [x_0 + x_1] * [x_0 + (S_1 - x_1)]  <-- because S_1 ^ x_1 is just S_1 - x_1 
    # if x_1 is a subset of S_1.
    # Product = x_0^2 + x_0(S_1 - x_1) + x_1*x_0 + x_1(S_1 - x_1)
    # Product = x_0^2 + x_0*S_1 + x_1*S_1 - x_1^2
    # To maximize this, we need to maximize x_0 and then maximize (x_1 * S_1 - x_1^2).
    # The term (x_1 * S_1 - x_1^2) is a downward parabola with respect to x_1.
    # It is maximized when x_1 is as close to S_1 / 2 as possible.
    
    # So the strategy is:
    # 1. Maximize x_0 (the bits where S is 0).
    # 2. Then, among all ways to get that max x_0, pick x_1 to be as close to S_1 / 2 as possible.
    
    # Let's simplify:
    # The bits where S is 0 are the most important. Let's call the set of these bits 'ZeroBits'.
    # We want to maximize (x & ZeroBits).
    # Let's find the basis for the elements, but we'll use a custom comparison 
    # to prioritize ZeroBits.
    
    # Actually, we can just use the basis to find the maximum possible value of 
    # (x & ~total_xor_sum). Let this be 'max_x0'.
    # Then we want to find the best x_1.
    
    # Let's use the basis to find all possible x.
    # But we only need to find the best x.
    # Let's use the basis to maximize (x & ~total_xor_sum).
    # Let's call this value 'best_x0'.
    # Now, we want to find the best 'x1' such that x = best_x0 | x1.
    # We can use the basis to find all possible values of x, 
    # but we only care about the bits where S is 1.
    
    # Let's refine the basis:
    # For each element in nums, we can represent it as (val_0, val_1) 
    # where val_0 = num & ~total_xor_sum and val_1 = num & total_xor_sum.
    # We want to maximize (x_0, x_1) where x_0 is maximized, 
    # and then x_1 is as close to S_1 / 2 as possible.
    
    # This is equivalent to:
    # 1. Build a basis for the pairs (val_0, val_1).
    # 2. Use the basis to maximize val_0.
    # 3. Then use the remaining basis elements to get val_1 as close to S_1 / 2 as possible.
    
    # Let's implement this.
    
    # Step 1: Build basis for (val_0, val_1)
    # We can treat (val_0, val_1) as a single large integer: (val_0 << 64) | val_1
    # This way, maximizing the large integer automatically maximizes val_0 first.
    
    combined_basis = []
    for num in nums:
        val_0 = num & ~total_xor_sum
        val_1 = num & total_xor_sum
        combined_val = (val_0 << 64) | val_1
        
        for b in combined_basis:
            combined_val = min(combined_val, combined_val ^ b)
        if combined_val > 0:
            combined_basis.append(combined_val)
            combined_basis.sort(reverse=True)
            
    # Step 2: Maximize the combined value to get the best x_0.
    # However, we don't want to just maximize the combined value, 
    # because maximizing the combined value might make x_1 very large or very small, 
    # and we want x_1 to be close to S_1 / 2.
    
    # Wait, the "maximize combined value" will maximize x_0, 
    # but it will also maximize x_1 (because x_1 is in the lower bits).
    # We want to maximize x_0, and THEN find x_1 that is close to S_1 / 2.
    
    # Let's find the maximum possible x_0 first.
    max_x0 = 0
    for b in combined_basis:
        b_0 = b >> 64
        if (max_x0 ^ b_0) > max_x0: # This is not quite right for bitwise
            pass 
            
    # Let's use a more standard approach for the basis.
    # We want to maximize x_0. Let's find the basis for x_0.
    # But we need to keep track of the x_1 that comes with it.
    
    # Let's use a basis of (val_0, val_1) where we prioritize val_0.
    # To maximize x_0, we use the basis.
    # To then adjust x_1, we use the basis elements that have val_0 == 0.
    
    # 1. Build basis for (val_0, val_1)
    # 2. Find max_x0 using the basis.
    # 3. The basis elements that have val_0 == 0 can be used to adjust