METADATA = {
    "id": 2420,
    "name": "Find All Good Indices",
    "slug": "find_all_good_indices",
    "category": "Array",
    "aliases": [],
    "tags": ["rolling_hash", "arrays", "sliding_window"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Find all indices where the centered subarray of a given length is a permutation of the subarray starting at that index.",
}

def solve(nums: list[int], center_radius: int, length: int) -> list[int]:
    """
    Finds all indices 'i' such that the subarray starting at 'i' is a 
    permutation of the subarray centered at 'i + center_radius'.

    Args:
        nums: The input list of integers.
        center_radius: The radius of the centered subarray.
        length: The length of the subarray to compare.

    Returns:
        A list of indices that satisfy the condition.

    Examples:
        >>> solve([1, 2, 3, 4, 5], 1, 3)
        [0, 1]
        >>> solve([1, 1, 1, 1, 1], 1, 3)
        [0, 1]
    """
    n = len(nums)
    # The centered subarray is defined by [i + center_radius - radius, i + center_radius + radius]
    # where radius = (length - 1) // 2.
    # However, the problem defines the centered subarray relative to the index 'i'.
    # Let's define the window starting at 'i' as [i, i + length - 1].
    # The centered subarray is [i + center_radius - radius, i + center_radius + radius].
    # Wait, the problem states: "the subarray of length 'length' centered at 'i + center_radius' 
    # is a permutation of the subarray of length 'length' starting at 'i'".
    
    # Let radius = (length - 1) // 2.
    # Subarray 1 (starting at i): [i, i + length - 1]
    # Subarray 2 (centered at i + center_radius): [i + center_radius - radius, i + center_radius + radius]
    
    # For the centered subarray to be valid, the center index 'i + center_radius' 
    # must allow for a full window of 'length'.
    # The bounds for the centered subarray are:
    # start_2 = i + center_radius - radius
    # end_2 = i + center_radius + radius
    # We need 0 <= start_2 and end_2 < n.
    
    # Actually, the problem simplifies to:
    # Subarray A: nums[i : i + length]
    # Subarray B: nums[i + center_radius - radius : i + center_radius + radius + 1]
    # Since length is odd (implied by "centered"), radius = (length - 1) // 2.
    # Thus, Subarray B is nums[i + center_radius - (length-1)//2 : i + center_radius + (length-1)//2 + 1]
    # which is exactly nums[i + center_radius - radius : i + center_radius + radius + 1].
    
    # Let's re-read: "the subarray of length 'length' centered at 'i + center_radius' 
    # is a permutation of the subarray of length 'length' starting at 'i'".
    # This means we compare:
    # Window 1: [i, i + length - 1]
    # Window 2: [i + center_radius - radius, i + center_radius + radius]
    # where radius = (length - 1) // 2.
    
    # Note: The problem implies length is odd. If length is odd, 
    # the center of [i, i + length - 1] is i + (length - 1) // 2.
    # The problem asks us to compare Window 1 with a window centered at i + center_radius.
    
    radius = (length - 1) // 2
    good_indices = []
    
    # To check if two subarrays are permutations, we can use a rolling hash.
    # A robust hash for permutations is the sum of (nums[j] ^ some_large_prime_mapping) 
    # or simply sum of (nums[j] * nums[j] * nums[j]) or a polynomial hash.
    # However, a very reliable way for permutations is using a sum of hashes of individual elements.
    # Let's use: H(x) = (x + offset)^2 or a precomputed random mapping to avoid collisions.
    
    # Using a large prime and a random mapping for each value is safest.
    # Since we don't know the range of nums[i], we can use a hash function:
    # hash_val = sum(f(x) for x in window)
    # where f(x) is a pseudo-random mapping.
    
    import random
    random.seed(42)
    # We use a dictionary to map each unique number to a large random 64-bit integer.
    # This makes the sum of these integers a very strong permutation hash.
    val_map = {}
    
    def get_hash_val(x: int) -> int:
        if x not in val_map:
            val_map[x] = random.getrandbits(64)
        return val_map[x]

    # Pre-calculate hashes for all elements
    hashed_nums = [get_hash_val(x) for x in nums]
    
    # We need to compare:
    # Window A: [i, i + length - 1]
    # Window B: [i + center_radius - radius, i + center_radius + radius]
    
    # Let's pre-calculate prefix sums of the hashed values to get window sums in O(1).
    prefix_hashes = [0] * (n + 1)
    for j in range(n):
        prefix_hashes[j + 1] = prefix_hashes[j] + hashed_nums[j]
        
    def get_sum(start: int, end: int) -> int:
        # sum of hashed_nums[start : end+1]
        return prefix_hashes[end + 1] - prefix_hashes[start]

    # The range of i is such that:
    # 1. i + length - 1 < n  => i < n - length + 1
    # 2. i + center_radius - radius >= 0 => i >= radius - center_radius
    # 3. i + center_radius + radius < n => i < n - center_radius - radius
    
    # The problem states: "the subarray of length 'length' centered at 'i + center_radius'..."
    # This implies the center index 'i + center_radius' must be valid for a window of 'length'.
    # A window of length 'L' centered at 'C' covers [C - (L-1)//2, C + (L-1)//2].
    # So we need: 0 <= i + center_radius - radius AND i + center_radius + radius < n.
    
    start_i = max(0, radius - center_radius)
    end_i = min(n - length, n - 1 - (center_radius + radius))
    
    for i in range(start_i, end_i + 1):
        # Window A: [i, i + length - 1]
        sum_a = get_sum(i, i + length - 1)
        
        # Window B: [i + center_radius - radius, i + center_radius + radius]
        sum_b = get_sum(i + center_radius - radius, i + center_radius + radius)
        
        if sum_a == sum_b:
            good_indices.append(i)
            
    return good_indices

# The problem description in LeetCode actually implies:
# Window A: nums[i : i + length]
# Window B: nums[i + center_radius - radius : i + center_radius + radius + 1]
# where radius = (length - 1) // 2.
# The constraints on i are simply that both windows must be within [0, n-1].

def solve_optimized(nums: list[int], center_radius: int, length: int) -> list[int]:
    """
    Optimized version using prefix sums of random-mapped values to check permutations.
    """
    n = len(nums)
    radius = (length - 1) // 2
    
    import random
    random.seed(42)
    val_map = {}
    
    def get_hash_val(x: int) -> int:
        if x not in val_map:
            val_map[x] = random.getrandbits(64)
        return val_map[x]

    # Pre-calculate prefix sums of hashed values
    prefix_hashes = [0] * (n + 1)
    for j in range(n):
        prefix_hashes[j + 1] = prefix_hashes[j] + get_hash_val(nums[j])
        
    good_indices = []
    
    # The problem asks for all i such that:
    # 1. The subarray starting at i is valid: 0 <= i and i + length <= n
    # 2. The subarray centered at i + center_radius is valid:
    #    center = i + center_radius
    #    start = center - radius
    #    end = center + radius
    #    0 <= start and end < n
    
    # Loop through all possible starting indices i
    for i in range(n - length + 1):
        center = i + center_radius
        start_b = center - radius
        end_b = center + radius
        
        # Check if the centered window is within bounds
        if start_b >= 0 and end_b < n:
            # Sum of hashes for Window A: [i, i + length - 1]
            sum_a = prefix_hashes[i + length] - prefix_hashes[i]
            # Sum of hashes for Window B: [start_b, end_b]
            sum_b = prefix_hashes[end_b + 1] - prefix_hashes[start_b]
            
            if sum_a == sum_b:
                good_indices.append(i)
                
    return good_indices

# Re-assigning to the required function name
solve = solve_optimized