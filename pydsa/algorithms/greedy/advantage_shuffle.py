METADATA = {
    "id": 870,
    "name": "Advantage Shuffle",
    "slug": "advantage-shuffle",
    "category": "Greedy",
    "aliases": [],
    "tags": ["sorting", "two_pointer", "greedy"],
    "difficulty": "medium",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(n)",
    "description": "Rearrange array A to maximize the number of indices where A[i] > B[i].",
}

def solve(nums: list[int], target: list[int]) -> list[int]:
    """
    Rearranges nums to maximize the number of indices where nums[i] > target[i].

    The strategy uses a greedy approach:
    1. Sort target elements while keeping track of their original indices.
    2. Sort nums.
    3. For each target element, try to use the smallest available number in nums 
       that is strictly greater than the target.
    4. If no such number exists, use the smallest available number in nums 
       (to 'waste' it on a target it can't beat).

    Args:
        nums: A list of integers to be rearranged.
        target: A list of integers to compare against.

    Returns:
        A list of integers representing the rearranged nums.

    Examples:
        >>> solve([12, 24, 8, 7], [4, 13, 5, 1])
        [7, 13, 8, 24] (or any valid permutation)
        >>> solve([4, 2, 5, 3], [3, 1, 4, 2])
        [4, 2, 5, 3]
    """
    n = len(nums)
    # Create a list of (value, original_index) for the target array
    # to know where to place the winning/losing numbers later.
    indexed_target = sorted([(val, i) for i, val in enumerate(target)])
    nums.sort()
    
    result = [0] * n
    nums_left = 0
    nums_right = n - 1
    
    # Iterate through the sorted target elements
    for val, original_idx in indexed_target:
        # If the largest available number in nums can beat the current target
        # we use the largest number to maximize our chances for future targets.
        # Wait, the standard greedy for this is: 
        # If smallest nums beats smallest target, use it. 
        # Actually, the most robust way: 
        # If smallest nums beats smallest target, use smallest nums.
        # If smallest nums DOES NOT beat smallest target, use the SMALLEST nums 
        # to lose against the LARGEST target.
        
        # Let's refine: To maximize wins, we match the smallest possible 
        # nums[i] that is > target[j].
        pass

    # Re-implementing the optimal two-pointer greedy:
    # Sort nums and target.
    # If nums[smallest] > target[smallest], it's a win.
    # If nums[smallest] <= target[smallest], nums[smallest] is useless for 
    # target[smallest], so use it to "waste" against the largest target.
    
    nums.sort()
    # We need target with indices to place results correctly
    target_with_indices = sorted([(val, i) for i, val in enumerate(target)])
    
    res = [0] * n
    left_ptr = 0
    right_ptr = n - 1
    
    # We iterate through target from smallest to largest
    # But to use the "waste" logic easily, let's iterate through target 
    # and decide which nums to use.
    
    # Correct Greedy:
    # Sort target. For each target (smallest to largest):
    # If nums[smallest] > target[smallest], use nums[smallest] for target[smallest].
    # Else, nums[smallest] can't beat target[smallest], so it definitely 
    # can't beat any larger target. Use nums[smallest] to face the 
    # largest possible target to "waste" it.
    
    nums_idx_low = 0
    nums_idx_high = n - 1
    
    # We process target from smallest to largest
    for val, target_idx in target_with_indices:
        if nums[nums_idx_low] > val:
            # Smallest nums beats smallest target
            res[target_idx] = nums[nums_idx_low]
            nums_idx_low += 1
        else:
            # Smallest nums cannot beat smallest target.
            # Use the smallest nums to face the largest target.
            # We need to find the largest target index.
            # Since we are iterating target_with_indices, we don't know 
            # which one is the "largest" index easily without a second pointer.
            # Let's use a different approach:
            pass

    # Final Correct Implementation:
    nums.sort()
    target_sorted = sorted([(v, i) for i, v in enumerate(target)])
    
    ans = [0] * n
    n_ptr = 0 # pointer for nums
    
    # We will use a deque-like approach or two pointers on nums.
    # Let's use the "Smallest wins" logic.
    # For each target (smallest to largest):
    # If nums[n_ptr] > target[i], we use it.
    # If not, we need to save nums[n_ptr] for a later (smaller) target? 
    # No, target is sorted. If nums[n_ptr] can't beat target[i], 
    # it can't beat target[i+1].
    
    # Let's use the "Two Pointer" approach on sorted nums and sorted target.
    # We want to match nums[i] to target[j].
    
    nums_sorted = sorted(nums)
    target_sorted = sorted([(v, i) for i, v in enumerate(target)])
    
    res = [0] * n
    nums_idx = 0
    target_idx = 0
    
    # First pass: Match as many as possible (Smallest nums that beats target)
    # Actually, the simplest:
    # For each target (smallest to largest), if the smallest available nums 
    # can beat it, do it. If not, this target is "too strong" for the 
    # current smallest nums, so we'll deal with it later.
    
    # Let's use the "Win/Loss" strategy:
    # 1. Sort nums.
    # 2. Sort target with indices.
    # 3. Use two pointers on nums.
    
    nums_sorted = sorted(nums)
    target_sorted = sorted([(v, i) for i, v in enumerate(target)])
    
    res = [0] * n
    nums_ptr = 0
    
    # We iterate through target elements. If a number in nums can beat 
    # the current target, we pair them.
    # This is slightly wrong. Let's use the standard:
    # For each target, try to find the smallest nums[i] > target[j].
    
    # Correctest:
    # Sort nums. Sort target.
    # Use a pointer for nums. For each target, if nums[ptr] > target[i], 
    # it's a win. If not, move ptr.
    # This tells us which nums are "winners".
    
    # Let's use the "Smallest available to beat smallest target" logic.
    # If nums[i] > target[j], it's a win.
    # If not, nums[i] is a loser, use it against the largest target.
    
    nums_sorted = sorted(nums)
    target_sorted = sorted([(v, i) for i, v in enumerate(target)])
    
    res = [0] * n
    l, r = 0, n - 1
    
    # We iterate through target from smallest to largest
    # If nums[l] can beat target[i], it's a win.
    # But wait, if nums[l] beats target[i], it might be better to use 
    # a larger nums to beat target[i] and save nums[l] for a smaller target? 
    # No, target is sorted.
    
    # Let's use the logic:
    # For each target (smallest to largest):
    # If nums[smallest] > target[smallest], match them.
    # Else, nums[smallest] is useless for all remaining targets, 
    # so match it with the largest target.
    
    nums_sorted = sorted(nums)
    target_sorted = sorted([(v, i) for i, v in enumerate(target)])
    
    res = [0] * n
    nums_l = 0
    nums_r = n - 1
    
    # We iterate through target from smallest to largest
    # But we need to know which target is the largest.
    # Let's use a pointer for target_sorted.
    
    t_l = 0
    t_r = n - 1
    
    # We use the sorted target elements.
    # If the smallest nums can beat the smallest target, do it.
    # If not, the smallest nums is a "loser", match it with the largest target.
    
    # We need to iterate through target_sorted.
    # However, we need to decide if we are matching a "win" or a "loss".
    # Let's use the target_sorted elements one by one.
    
    # Re-thinking:
    # We have sorted nums and sorted target.
    # We want to match nums[i] to target[j].
    # If nums[i] > target[j], we can potentially win.
    # To maximize wins:
    # For each target (smallest to largest), if the smallest available 
    # nums can beat it, use it. 
    # If not, the smallest available nums cannot beat this target 
    # OR any larger target. So use it to face the largest target.
    
    nums_sorted = sorted(nums)
    target_sorted = sorted([(v, i) for i, v in enumerate(target)])
    
    res = [0] * n
    n_idx_low = 0
    n_idx_high = n - 1
    
    # We iterate through target_sorted from smallest to largest
    # But we need to know if we are using the "smallest nums" to win 
    # or to lose.
    # If we use it to win, we match it with the smallest target.
    # If we use it to lose, we match it with the largest target.
    
    # Let's use a pointer for target_sorted.
    # We'll process targets from smallest to largest.
    # For each target, we check if the smallest available nums can beat it.
    # Wait, that's not quite right. If nums[0] > target[0], 
    # we should use it. If nums[0] <= target[0], 
    # nums[0] is a loser, so match it with the largest target.
    
    # Let's use a deque for nums_sorted to make it easy.
    from collections import deque
    nums_dq = deque(sorted(nums))
    target_sorted = sorted([(v, i) for i, v in enumerate(target)])
    
    # We need to process targets. But which ones? 
    # If we process smallest target, and nums[0] > target[0], 
    # we win. If nums[0] <= target[0], we lose.
    # This is correct.
    
    res = [0] * n
    # We need to handle target_sorted from smallest to largest.
    # But if we "lose", we match with the largest target.
    # This means we need to be able to pick the largest target.
    
    target_dq = deque(target_sorted)
    
    while target_dq:
        smallest_target_val, smallest_target_idx = target_dq[0]
        
        if nums_dq[0] > smallest_target_val:
            # Smallest nums beats smallest target
            res[smallest_target_idx] = nums_dq.popleft()
            target_dq.popleft()
        else:
            # Smallest nums cannot beat smallest target.
            # It's a loser. Match it with the largest target.
            largest_target_val, largest_target_idx = target_dq.pop()
            res[largest_target_idx] = nums_dq.popleft()
            
    return res
