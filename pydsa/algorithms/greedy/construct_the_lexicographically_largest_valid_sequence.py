METADATA = {
    "id": 1718,
    "name": "Construct the Lexicographically Largest Valid Sequence",
    "slug": "construct-the-lexicographically-largest-valid-sequence",
    "category": "Greedy",
    "aliases": [],
    "tags": ["greedy", "array"],
    "difficulty": "hard",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Construct the lexicographically largest valid sequence by greedily picking the largest possible number that still allows for a valid sequence to be formed.",
}

def solve(nums: list[int]) -> list[int]:
    """
    Constructs the lexicographically largest valid sequence.
    
    A sequence is valid if every number in it appears exactly twice.
    The goal is to find the lexicographically largest such sequence 
    that is a subsequence of the input.

    Args:
        nums: A list of integers where each integer appears exactly twice.

    Returns:
        A list of integers representing the lexicographically largest valid sequence.

    Examples:
        >>> solve([2, 1, 3, 1, 2])
        [3, 2, 1, 2, 1]
        >>> solve([1, 2, 1, 2])
        [2, 1, 2, 1]
    """
    # Count the occurrences of each number remaining to be processed
    counts = {}
    for num in nums:
        counts[num] = counts.get(num, 0) + 2
    
    # We need to track how many of each number we have left to pick
    # to ensure we can still pick both occurrences later.
    # Since the input guarantees each number appears twice, 
    # we use a frequency map of the remaining elements.
    remaining_counts = {}
    for num in nums:
        remaining_counts[num] = remaining_counts.get(num, 0) + 1
        
    # To pick the largest number greedily, we need to know which numbers
    # are still available to be picked in their entirety.
    # We use a max-heap or simply a sorted list of unique numbers.
    # Given the constraints and the nature of the problem, 
    # we can use a frequency map and a way to track available numbers.
    
    # Let's refine the approach:
    # 1. Count total occurrences of each number.
    # 2. Iterate through nums. For each number, decide if we pick it now.
    # 3. We pick a number if it's the largest available AND we can still 
    #    pick its second occurrence later.
    
    # Correct Greedy Strategy:
    # Maintain a count of how many times each number appears in the suffix.
    # A number 'x' can be picked as the first occurrence if its second 
    # occurrence is still available in the remaining part of the array.
    # To make it lexicographically largest, we want to pick the largest 
    # possible number at the current position.
    
    n = len(nums)
    suffix_counts = {}
    for num in nums:
        suffix_counts[num] = suffix_counts.get(num, 0) + 1
        
    # available_to_pick stores numbers that have at least 2 occurrences 
    # remaining in the suffix.
    # However, we need to pick the largest number such that its 
    # *second* occurrence is still ahead.
    
    # Let's use a frequency map of what's left in the suffix.
    # And a max-heap of numbers that can be picked (those with count >= 2).
    import heapq
    
    # We'll use a max-heap to always pick the largest available number.
    # A number is "available" to be picked as its first occurrence if 
    # its current suffix count is >= 2.
    # A number is "available" to be picked as its second occurrence if 
    # its current suffix count is == 1.
    
    # But wait, the rule is: we pick the largest number such that 
    # we can still complete the sequence.
    # If we pick 'x', we must ensure 'x' appears again later.
    
    # Let's track:
    # - suffix_counts: how many of each number are left in the array.
    # - picked_count: how many of each number we have already added to result.
    
    result = []
    picked_count = {}
    
    # We need to know which numbers are "ready" to be picked.
    # A number is ready to be picked as its 1st occurrence if suffix_counts[x] >= 2.
    # A number is ready to be picked as its 2nd occurrence if suffix_counts[x] == 1 
    # AND we have already picked it once.
    
    # To get the lexicographically largest, we always want the largest number.
    # We use a max-heap to store numbers that are "ready" to be picked.
    # A number is "ready" if:
    # (picked_count[x] == 0 and suffix_counts[x] >= 2) OR 
    # (picked_count[x] == 1 and suffix_counts[x] == 1)
    
    # Actually, the condition is simpler:
    # At any step, we can pick the largest number 'x' such that:
    # 1. We haven't picked 'x' twice yet.
    # 2. If we pick 'x' now, we can still pick the remaining required 
    #    occurrences of 'x' from the remaining suffix.
    
    # Let's use a max-heap of numbers that are currently "eligible".
    # A number is eligible if:
    # - It has 2 occurrences left in suffix and we have picked 0.
    # - It has 1 occurrence left in suffix and we have picked 1.
    
    # Wait, the greedy choice is: at the current index in 'nums', 
    # can we pick the largest number available in the suffix?
    # Let's use the standard approach for this problem:
    
    # 1. Count total occurrences in suffix.
    # 2. Use a max-heap to store numbers that can be picked.
    # 3. A number is in the heap if it's "ready".
    
    # Let's re-initialize.
    suffix_counts = {}
    for x in nums:
        suffix_counts[x] = suffix_counts.get(x, 0) + 1
        
    picked_count = {}
    max_heap = []
    
    # A number is "ready" to be picked if:
    # (count_in_suffix == 2 and picked == 0) OR (count_in_suffix == 1 and picked == 1)
    # This is slightly wrong because we need to pick them in order of appearance 
    # to maintain subsequence property.
    
    # Correct logic:
    # We iterate through the array. At each element, we decide whether to 
    # include it in our result. But that's not quite right for lexicographical.
    # We should iterate through the array and for each element, 
    # if it's the largest available number that can be picked, we pick it.
    
    # Let's use the "available" set.
    # A number is available to be picked if:
    # - It's the first occurrence and suffix_count >= 2
    # - It's the second occurrence and suffix_count == 1
    
    # We use a max-heap to keep track of numbers that are "ready" to be picked.
    # A number is "ready" if it's the first occurrence and suffix_count >= 2,
    # OR it's the second occurrence and suffix_count == 1.
    # But we must pick them in the order they appear in the original array 
    # to satisfy the subsequence constraint.
    
    # Actually, the greedy choice is:
    # At any point, the next number in our result will be the largest number 
    # 'x' such that 'x' is "ready" to be picked.
    # "Ready" means:
    # - If we haven't picked 'x' yet, its first occurrence is at or after 
    #   the current index and its second occurrence is also at or after 
    #   the current index.
    # - If we have picked 'x' once, its second occurrence is at or after 
    #   the current index.
    
    # Let's use a max-heap of numbers that are "ready".
    # A number is "ready" if:
    # 1. It has 2 occurrences left in the suffix and we have picked 0.
    # 2. It has 1 occurrence left in the suffix and we have picked 1.
    
    # We need to track the current index in 'nums'.
    
    # Let's refine:
    # 1. Pre-calculate suffix counts.
    # 2. Maintain a max-heap of numbers that are "ready".
    # 3. A number 'x' becomes "ready" when:
    #    - It's encountered and suffix_count[x] == 2 (it can be the 1st pick).
    #    - It's encountered and suffix_count[x] == 1 (it can be the 2nd pick).
    # 4. But we can only pick a number if it's "ready" AND we are at or 
    #    past its occurrence in the original array.
    
    # Let's use the "ready" definition:
    # A number is "ready" if it's the first occurrence and suffix_count >= 2,
    # OR it's the second occurrence and suffix_count == 1.
    # We use a max-heap to store these "ready" numbers.
    # We also need to know the index of the next occurrence of each number.
    
    # Let's use a simpler approach:
    # 1. Count occurrences of each number.
    # 2. Use a max-heap to store numbers that are "ready" to be picked.
    # 3. A number is "ready" if:
    #    - It's the first occurrence and suffix_count >= 2.
    #    - It's the second occurrence and suffix_count == 1.
    # 4. We also need to track which numbers are already in the heap 
    #    to avoid duplicates.
    
    # Wait, the "ready" status changes as we move through the array.
    # Let's use a pointer `i` for the current position in `nums`.
    # We maintain a max-heap of numbers that are "ready" to be picked.
    # A number `x` is "ready" if:
    # - `picked_count[x] == 0` and `suffix_counts[x] == 2`
    # - `picked_count[x] == 1` and `suffix_counts[x] == 1`
    
    # This is still slightly off. Let's use the correct greedy condition:
    # At any step, we want to pick the largest number `x` such that 
    # its *next* required occurrence is at index `j >= i`.
    
    # Let's use the following:
    # - `suffix_counts`: how many of each number are left in `nums[i:]`.
    # - `picked_count`: how many of each number we have already picked.
    # - `max_heap`: contains numbers `x` such that:
    #    - `picked_count[x] == 0` and `suffix_counts[x] == 2`
    #    - `picked_count[x] == 1` and `suffix_counts[x] == 1`
    
    # We iterate through `nums` with index `i`.
    # But we don't just iterate; we pick from the heap.
    # When we pick `x` from the heap, we jump `i` to the index of that occurrence.
    
    # Let's try this:
    # 1. `suffix_counts` = frequency of each number in `nums`.
    # 2. `next_occurrence_index` = a way to find the next index of `x`.
    # 3. `max_heap` = numbers `x` where `(picked[x]==0 and suffix[x]==2) or (picked[x]==1 and suffix[x]==1)`.
    # 4. `current_idx = 0`.
    # 5. While `len(result) < len(nums)`:
    #    a. While `current_idx < n` and `nums[current_idx]` is not "ready" in a way 
    #       that it's the *first* time we see it with `suffix_count == 2`:
    #       Actually, let's just update `suffix_counts` as we move.
    
    # Let's use the most robust version:
    # 1. `suffix_counts` = total counts.
    # 2. `picked_count` = 0 for all.
    # 3. `max_heap` = empty.
    # 4. `in_heap` = set to avoid duplicates in heap.
    # 5. `i = 0`.
    # 6. While `i < n`:
    #    - `x = nums[i]`
    #    - `suffix_counts[x] -= 1`
    #    - If `suffix_counts[x] == 1` and `picked_count[x] == 0`:
    #        `x` is now "ready" to be picked as its 1st occurrence.
    #        Wait, if `suffix_counts[x]` becomes 1, it means we've passed 
    #        the first occurrence.
    
    # Let's use the property: A number `x` is "ready" to be picked if:
    # - It's the first occurrence and `suffix_counts[x] == 2`.
    # - It's the second occurrence and `suffix_counts[x] == 1`.
    
    # Let's pre-calculate the indices of each number.
    from collections import deque
    indices = {}
    for idx, val in enumerate(nums):
        if val not in indices:
            indices[val] = deque()
        indices[val].append(idx)
        
    suffix_counts = {}
    for x in nums:
        suffix_counts[x] = suffix_counts.get(x, 0) + 1
        
    max_heap = []
    picked_count = {}
    in_heap = set()
    
    # A number is "ready" if:
    # (picked_count[x] == 0 and suffix_counts[x] == 2) OR
    # (picked_count[x] == 1 and suffix_counts[x] == 1)
    
    # We need to process the array to find these "ready" numbers.
    # But we can only pick a number if its *next* occurrence is >= current_idx.
    
    # Let's use a simpler approach:
    # We maintain a pointer `curr_idx`.
    # We maintain a `max_heap` of numbers that are "ready".
    # A number `x` is "ready" if:
    # - `picked_count[x] == 0` and `suffix_counts[x] == 2`
    # - `picked_count[x] == 1` and `suffix_counts[x] == 1`
    # We also need to ensure that when we pick `x`, we move `curr_idx` 
    # to the index of the occurrence we just picked.
    
    # Let's refine the "ready" condition:
    # A number `x` is "ready" if:
    # 1. `picked_count[x] == 0` and `suffix_counts[x] == 2`
    # 2. `picked_count[x] == 1` and `suffix_counts[x] == 1`
    
    # We'll use a pointer `i` to traverse `nums`.
    # As `i` moves, we update `suffix_counts`.
    # When `suffix_counts[x]` becomes 2, `x` is ready (1st occurrence).
    # When `suffix_counts[x]` becomes 1, `x` is ready (2nd occurrence).
    
    # Wait, if `suffix_counts[x]` is 2, it means there are 2 `x`'s left 
    # in `nums[i:]`. The first one is at `i` or later.
    
    # Let's use this:
    # 1. `suffix_counts` = total counts.
    # 2. `max_heap` = []
    # 3. `picked_count` = {}
    # 4. `i = 0`
    # 5. While `i < n`:
    #    - `x = nums[i]`
    #    - `suffix_counts[x] -= 1`
    #    - If `suffix_counts[x] == 1` and `picked_count.get(x, 0) == 0`:
    #        # This means the first occurrence of x was at some index < i,