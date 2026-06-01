METADATA = {
    "id": 3234,
    "name": "Count the Number of Substrings With Dominant Ones",
    "slug": "count-the-number-of-substrings-with-dominant-ones",
    "category": "Array",
    "aliases": [],
    "tags": ["sliding_window", "two_pointer", "prefix_sum"],
    "difficulty": "hard",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Count the number of substrings where the number of ones is at least twice the number of zeros.",
}

def solve(nums: list[int]) -> int:
    """
    Counts the number of substrings where the count of ones is at least 
    twice the count of zeros.

    Args:
        nums: A list of integers containing only 0s and 1s.

    Returns:
        The total count of substrings satisfying the condition.

    Examples:
        >>> solve([1, 0, 1, 1, 0])
        7
        >>> solve([0, 0, 0])
        0
    """
    n = len(nums)
    # We want: count(1) >= 2 * count(0)
    # Let count(1) = P[i] - P[j] (where P is prefix sum of 1s)
    # Let count(0) = (i - j) - (P[i] - P[j])
    # Condition: (P[i] - P[j]) >= 2 * ((i - j) - (P[i] - P[j]))
    # (P[i] - P[j]) >= 2*(i - j) - 2*(P[i] - P[j])
    # 3 * (P[i] - P[j]) >= 2 * (i - j)
    # 3*P[i] - 3*P[j] >= 2*i - 2*j
    # 3*P[i] - 2*i >= 3*P[j] - 2*j
    
    # Let val[i] = 3 * prefix_sum[i] - 2 * i
    # We need to find pairs (j, i) such that j < i and val[i] >= val[j]
    # However, the condition is for substrings [j, i-1].
    # Let's redefine:
    # Let S[i] be the prefix sum of (3 * nums[k] - 2) for k in 0...i-1
    # We want sum_{k=j}^{i-1} (3 * nums[k] - 2) >= 0
    # Let P[i] = sum_{k=0}^{i-1} (3 * nums[k] - 2), with P[0] = 0
    # Condition: P[i] - P[j] >= 0  => P[i] >= P[j] for j < i
    
    # Wait, the problem is actually simpler if we track the positions of zeros.
    # For a fixed end index 'i', we want to find how many start indices 'j' 
    # satisfy count(1) >= 2 * count(0).
    
    zero_indices = [-1]  # To handle boundaries easily
    for idx, val in enumerate(nums):
        if val == 0:
            zero_indices.append(idx)
    zero_indices.append(n)
    
    total_count = 0
    num_zeros = len(zero_indices) - 2
    
    # Precompute prefix sums of ones to get count of ones in O(1)
    prefix_ones = [0] * (n + 1)
    for i in range(n):
        prefix_ones[i + 1] = prefix_ones[i] + nums[i]
        
    # Iterate through every possible end position 'r'
    for r in range(n):
        # We look at substrings ending at 'r'.
        # Instead of iterating all 'l', we iterate through blocks of zeros.
        # Let's find the index of the last zero seen before or at 'r'.
        # But it's more efficient to iterate through the zero_indices list.
        pass

    # Re-evaluating: The condition is count(1) >= 2 * count(0).
    # Let's use the zero_indices approach.
    # For a fixed 'r', as 'l' decreases, count(0) increases in steps.
    # Between two consecutive zeros, count(0) is constant.
    
    # Let's find the index of the last zero seen so far.
    last_zero_idx_in_list = 0 # index in zero_indices
    
    # We'll use a more direct approach:
    # For each r, we iterate through the zeros that appear before or at r.
    # Let the zeros be at indices z_1, z_2, ..., z_k <= r.
    # For a fixed number of zeros 'z_count', the possible 'l' values 
    # fall in a range [z_{k-z_count-1}+1, z_{k-z_count}].
    
    # Let's find all zero positions
    zeros = [i for i, x in enumerate(nums) if x == 0]
    
    ans = 0
    for r in range(n):
        # Find how many zeros are <= r. 
        # We can maintain this with a pointer.
        pass

    # Correct O(n) approach:
    # For each r, we want to count l <= r such that:
    # (ones in [l, r]) >= 2 * (zeros in [l, r])
    # Let f(i) = 3 * nums[i] - 2. We want sum_{k=l}^r f(k) >= 0.
    # This is equivalent to P[r+1] - P[l] >= 0 where P is prefix sum of f(i).
    # P[r+1] >= P[l].
    # This is a classic problem: count pairs (l, r+1) with l < r+1 and P[l] <= P[r+1].
    # This can be solved with a Fenwick tree or Segment tree in O(n log n).
    # But the problem asks for O(n). Let's check if the constraints allow O(n log n).
    # Actually, the "dominant ones" problem usually implies a sliding window 
    # or a specific property.
    
    # Let's use the property that for a fixed r, as l decreases, 
    # the condition count(1) >= 2*count(0) becomes harder to satisfy.
    # However, the number of zeros is the limiting factor.
    
    # Let's use the zero_indices approach properly.
    # For each r, we iterate backwards through the zeros.
    # Let zeros be at indices z_m, z_{m-1}, ..., z_1 where z_m <= r.
    # For a fixed number of zeros 'k', the range of 'l' is (z_{m-k}, z_{m-k+1}].
    # In this range, count(0) is exactly 'k'.
    # We need count(1) >= 2k.
    # count(1) = (r - l + 1) - k.
    # (r - l + 1) - k >= 2k  => r - l + 1 >= 3k => l <= r - 3k + 1.
    
    # Optimization: The number of zeros is at most n. 
    # But we only care about k such that 3k <= r + 1.
    
    zeros = [i for i, x in enumerate(nums) if x == 0]
    zero_ptr = 0
    ans = 0
    
    for r in range(n):
        # Update zero_ptr to point to the first zero index > r
        while zero_ptr < len(zeros) and zeros[zero_ptr] <= r:
            zero_ptr += 1
        
        # The zeros at or before r are zeros[0...zero_ptr-1]
        # Let's iterate through the number of zeros 'k' we want to include.
        # k = 0, 1, 2, ... up to zero_ptr
        # If k = 0: l is in (zeros[zero_ptr-1] if zero_ptr > 0 else -1, r]
        #    Condition: count(1) >= 0 (always true for k=0)
        #    Wait, if k=0, count(0)=0, so count(1) >= 0 is always true.
        #    The range of l for k=0 is (zeros[zero_ptr-1] if zero_ptr > 0 else -1, r]
        #    But we must ensure count(0) is actually 0.
        #    So l must be > the last zero index.
        
        # Case k = 0:
        last_z = zeros[zero_ptr-1] if zero_ptr > 0 else -1
        # l can be any value in (last_z, r].
        # Number of such l: r - last_z
        ans += (r - last_z)
        
        # Case k > 0:
        # We pick k zeros. The zeros are zeros[zero_ptr-k ... zero_ptr-1].
        # The smallest index l can be is zeros[zero_ptr-k-1] + 1 (or 0).
        # The largest index l can be is zeros[zero_ptr-k].
        # For a fixed k, count(0) = k.
        # We need count(1) >= 2k.
        # Total elements in [l, r] is (r - l + 1).
        # (r - l + 1) - k >= 2k  => l <= r - 3k + 1.
        # So l must be in [max(0, zeros[zero_ptr-k-1]+1), min(r - 3k + 1, zeros[zero_ptr-k] - 1 if k < zero_ptr else r)].
        # Wait, the range of l that gives exactly k zeros is:
        # l \in (zeros[zero_ptr-k-1] if zero_ptr-k-1 >= 0 else -1, zeros[zero_ptr-k]]
        # Actually, if we want exactly k zeros, l must be > the (k+1)-th zero from the right.
        # Let's use the indices of zeros: z_{p}, z_{p-1}, ..., z_{p-k+1} are the k zeros.
        # The l must be in (z_{p-k}, z_{p-k+1}]? No.
        # Let's say the zeros are at indices: idx[0], idx[1], ..., idx[m-1] where idx[m-1] <= r.
        # If we want exactly k zeros, the zeros are idx[m-k], ..., idx[m-1].
        # The l must be in (idx[m-k-1] if m-k-1 >= 0 else -1, idx[m-k]].
        # Wait, if l is in (idx[m-k-1], idx[m-k]], then the zeros in [l, r] are idx[m-k], ..., idx[m-1].
        # That is exactly k zeros.
        # Condition: count(1) >= 2k  =>  (r - l + 1) - k >= 2k  =>  l <= r - 3k + 1.
        # So for a fixed k > 0, we need to count l such that:
        # 1. idx[m-k-1] < l <= idx[m-k]  (to have exactly k zeros)
        # 2. l <= r - 3k + 1
        # This is equivalent to: l \in (idx[m-k-1], min(idx[m-k], r - 3k + 1)]
        # The number of such l is max(0, min(idx[m-k], r - 3k + 1) - idx[m-k-1])
        
        # Let's re-verify with k=1:
        # l \in (idx[m-2], min(idx[m-1], r - 3 + 1)]
        # If r=4, nums=[1,0,1,1,0], zeros=[1, 4], m=2.
        # r=4, zero_ptr=2, m=2.
        # k=0: last_z = 4. ans += (4-4) = 0. Wait, k=0 should be l in (1, 4].
        # Let's fix the k=0 logic.
        
        # Corrected logic:
        # For a fixed r, let the zeros at or before r be at indices z_0, z_1, ..., z_{m-1}.
        # For k = 0: l \in (z_{m-1}, r]. Count = r - z_{m-1}.
        # For k > 0: l \in (z_{m-k-1} if m-k-1 >= 0 else -1, z_{m-k}].
        #    Condition: l <= r - 3k + 1.
        #    Count = max(0, min(z_{m-k}, r - 3k + 1) - (z_{m-k-1} if m-k-1 >= 0 else -1))
        # Wait, if k=m, the range is ( -1, z_0 ].
        # Let's trace r=4, nums=[1,0,1,1,0], zeros=[1, 4], m=2.
        # r=0: m=0. k=0: l in (-1, 0]. ans += 1. (Sub: [1])
        # r=1: m=1. k=0: l in (1, 1]. ans += 0. k=1: l in (-1, 1]. l <= 1-3+1= -1. ans += 0.
        # r=2: m=1. k=0: l in (1, 2]. ans += 1. (Sub: [1])
        # r=3: m=1. k=0: l in (1, 3]. ans += 2. (Sub: [1,1], [1,1,1]... no, [1,1], [0,1,1])
        # Wait, if r=3, zeros=[1], m=1. k=0: l in (1, 3]. ans += 2. (Sub: [1], [1,1])
        # r=4: m=2. k=0: l in (4, 4]. ans += 0. k=1: l in (1, 4]. l <= 4-3+1=2. l in (1, 2]. ans += 1. (Sub: [1,1,0])
        # k=2: l in (-1, 1]. l <= 4-6+1= -1. ans += 0.
        
        # Let's re-trace r=4, nums=[1,0,1,1,0] manually:
        # Substrings: [1], [1], [1,1], [1,1,1], [1,0,1,1], [0,1,1], [1,1,0]... this is confusing.
        # Let's use the condition: count(1) >= 2 * count(0).
        # [1]: 1>=0 (Y)
        # [1,0]: 1>=2 (N)
        # [1,0,1]: 2>=2 (Y)
        # [1,0,1,1]: 3>=2 (Y)
        # [1,0,1,1,0]: 3>=4 (N)
        # [0]: 0>=2 (N)
        # [0,1]: 1>=2 (N)
        # [0,1,1]: 2>=2 (Y)
        # [0,1,1,0]: 2>=4 (N)
        # [1]: 1>=0 (Y)
        # [1,1]: 2>=0 (Y)
        # [1,1,0]: 2>=2 (Y)
        # [1]: 1>=0 (Y)
        # [1,0]: 1>=2 (N)
        # [0]: 0>=2 (N)
        # Total: 1+1+1+1+1+1+1 = 7. Correct.
        
    # Let's refine the loop.
    return _optimized_solve(nums)

def _optimized_solve(nums: list[int]) -> int:
    n = len(nums)
    zeros = [i for i, x in enumerate(nums) if x == 0]
    m = len(zeros)
    
    ans = 0
    zero_ptr = 0 # index in 'zeros'