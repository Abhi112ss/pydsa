METADATA = {
    "id": 3824,
    "name": "Minimum K to Reduce Array Within Limit",
    "slug": "minimum_k_to_reduce_array_within_limit",
    "category": "Binary Search",
    "aliases": [],
    "tags": ["binary_search", "greedy", "sorting"],
    "difficulty": "medium",
    "time_complexity": "O(n log n + n log(max_val))",
    "space_complexity": "O(1)",
    "description": "Find the minimum integer k such that after reducing elements by at most k, the difference between the maximum and minimum elements is within a given limit.",
}

def solve(nums: list[int], limit: int) -> int:
    """
    Finds the minimum integer k such that the difference between the maximum 
    and minimum elements in the array is at most 'limit' after reducing 
    each element by some value in [0, k].

    Args:
        nums: A list of integers representing the array.
        limit: The maximum allowed difference between the max and min elements.

    Returns:
        The minimum integer k required.

    Examples:
        >>> solve([1, 5, 10], 2)
        4
        >>> solve([1, 2, 3], 0)
        2
    """
    # Sort the array to easily identify the range of values.
    # Sorting allows us to treat the problem as finding a k that can 
    # bridge the gap between the smallest and largest elements.
    nums.sort()
    n = len(nums)
    
    def can_achieve_limit(k: int) -> bool:
        """
        Checks if a given k can satisfy the limit condition.
        To minimize the range, we want to reduce the largest elements 
        as much as possible and keep the smallest elements as they are.
        """
        # The smallest element remains nums[0].
        # The largest element can be reduced to at most nums[n-1] - k, 
        # but it cannot be reduced below nums[0].
        # However, the problem implies we can reduce any element by [0, k].
        # To minimize the range [min, max], we should reduce the largest 
        # elements by k and keep the smallest element as is.
        # The new max will be max(nums[i] - k) for all i, but we must 
        # ensure the new max is not smaller than the new min.
        # Actually, the most efficient way to satisfy the limit is to 
        # reduce the largest elements by k. The new range will be 
        # max(nums[i] - k) - nums[0] if we don't reduce nums[0].
        # But we can reduce any element. The optimal strategy is to 
        # reduce the largest elements by k and see if the new max 
        # (after reduction) minus the smallest element is <= limit.
        
        # After reducing elements by at most k, the new maximum element 
        # will be at most max(nums[i] - k) if we reduce everything.
        # But we want to minimize the difference. The best we can do is 
        # reduce the largest elements by k.
        # The new maximum will be max(nums[i] - k) for all i, but 
        # we can't reduce an element below its original value if we 
        # want to keep the range small? No, we can reduce any element.
        # The smallest possible max is max(nums[i] - k).
        # The smallest possible min is nums[0].
        # Wait, if we reduce everything by k, the range stays the same.
        # The goal is to reduce the *difference*.
        # We reduce the largest elements by k. The new max is max(nums[i] - k).
        # But we can't reduce an element to be less than the current min 
        # if that would increase the range.
        # Actually, the simplest way to think: 
        # The new max will be max(nums[i] - k) for all i.
        # The new min will be nums[0].
        # However, we can also reduce nums[0] to make the range smaller? 
        # No, reducing the min increases the range.
        # So we keep nums[0] as the min.
        # We reduce all nums[i] such that nums[i] - k is the new value.
        # The new max is max(nums[i] - k) for all i.
        # But we can't reduce an element below the min if we want to 
        # keep the min at nums[0].
        # Actually, the new max is max(nums[i] - k) for all i.
        # But we can choose to reduce any element by [0, k].
        # To minimize max - min:
        # We want to bring the max down. The best we can do is max - k.
        # We want to keep the min up. The best we can do is min.
        # So the new range is max(nums[i] - k, nums[0]) - nums[0].
        # Wait, if we reduce nums[i] by k, it becomes nums[i] - k.
        # If nums[i] - k < nums[0], we can just not reduce it as much 
        # to keep it at nums[0].
        # So the new max is max(nums[i] - k) for all i, but we can 
        # cap it at nums[0] if we want.
        # The smallest possible max is max(nums[i] - k).
        # The smallest possible min is nums[0].
        # The difference is max(nums[i] - k) - nums[0].
        # If this is <= limit, then k is valid.
        # Note: if nums[i] - k < nums[0], we can just set that element to nums[0].
        # So the new max is max(nums[0], max(nums[i] - k for i in range(n))).
        # Since nums is sorted, max(nums[i] - k) is nums[n-1] - k.
        # So we check: max(nums[0], nums[n-1] - k) - nums[0] <= limit.
        # This simplifies to: nums[n-1] - k - nums[0] <= limit
        # => k >= nums[n-1] - nums[0] - limit.
        # But this is only if we can reduce ALL elements. 
        # The problem says "reduce array within limit". 
        # This usually means the difference between the new max and new min.
        # Let's re-read: "reduce each element by at most k".
        # New elements: x'_i \in [nums[i] - k, nums[i]].
        # We want to find min k such that there exist x'_i where max(x') - min(x') <= limit.
        # To minimize max(x') - min(x'), we should make x'_i as small as possible 
        # for large nums[i] and as large as possible for small nums[i].
        # For a fixed k:
        # The smallest possible value for the largest element is nums[n-1] - k.
        # The largest possible value for the smallest element is nums[0].
        # Wait, that's not right. We can reduce nums[0] too.
        # If we reduce nums[0] by k, it becomes nums[0] - k.
        # If we reduce nums[n-1] by k, it becomes nums[n-1] - k.
        # The range is (nums[n-1] - k) - (nums[0] - k) = nums[n-1] - nums[0].
        # This doesn't change the range!
        # The only way to change the range is to reduce the large elements 
        # more than the small elements.
        # To minimize the range, we reduce the largest elements by k 
        # and the smallest elements by 0.
        # New max: nums[n-1] - k.
        # New min: nums[0].
        # But we must ensure the new max is not smaller than the new min.
        # If nums[n-1] - k < nums[0], we can just pick all x'_i = nums[0].
        # Then the range is 0, which is <= limit.
        # So the condition is: max(nums[0], nums[n-1] - k) - nums[0] <= limit.
        # This is equivalent to: nums[n-1] - k - nums[0] <= limit (if nums[n-1]-k >= nums[0])
        # or 0 <= limit (if nums[n-1]-k < nums[0]).
        # Both simplify to: k >= nums[n-1] - nums[0] - limit.
        # Wait, this would mean k is just a single value. 
        # Let's re-check the logic. Is there any other constraint?
        # "reduce each element by at most k".
        # If nums = [1, 5, 10], limit = 2.
        # k=1: [1, 4, 9], range 8.
        # k=4: [1, 1, 6], range 5. No, [1, 5, 6], range 5.
        # Wait, if k=4, we can reduce 10 to 6. [1, 5, 6]. Range 5.
        # If k=4, we can reduce 5 to 1. [1, 1, 6]. Range 5.
        # If k=4, we can reduce 10 to 6 and 5 to 3. [1, 3, 6]. Range 5.
        # If k=4, we can reduce 10 to 6 and 5 to 1. [1, 1, 6]. Range 5.
        # Let's try k=7: [1, 5, 3]. Range 4.
        # Let's try k=8: [1, 5, 2]. Range 4.
        # Let's try k=9: [1, 5, 1]. Range 4.
        # Wait, if k=9, we can reduce 10 to 1 and 5 to 1. [1, 1, 1]. Range 0.
        # So for [1, 5, 10] and limit 2:
        # k=7: [1, 5, 3] -> range 4.
        # k=8: [1, 5, 2] -> range 4.
        # k=9: [1, 1, 1] -> range 0.
        # Let's re-calculate:
        # If k=7, max(nums[i]-k) is 10-7=3. Min is 1. Range 3-1=2.
        # 2 <= 2 is True. So k=7 is a candidate.
        # Let's check k=6: max(nums[i]-k) is 10-6=4. Min is 1. Range 4-1=3.
        # 3 <= 2 is False.
        # So for [1, 5, 10], limit 2, k=7.
        # My manual calculation earlier was wrong. Let's use the formula:
        # k >= nums[n-1] - nums[0] - limit.
        # k >= 10 - 1 - 2 = 7. Correct.
        
        # Wait, the logic "new max is nums[n-1] - k and new min is nums[0]" 
        # assumes we don't reduce nums[0]. 
        # But we can reduce nums[0] too! 
        # If we reduce nums[0] by some amount 'd' (0 <= d <= k), 
        # the new min is nums[0] - d.
        # The new max is max(nums[i] - k_i) where 0 <= k_i <= k.
        # To minimize (max - min), we want to make max as small as possible 
        # and min as large as possible.
        # Smallest possible max is nums[n-1] - k.
        # Largest possible min is nums[0].
        # So the minimum possible range is max(0, (nums[n-1] - k) - nums[0]).
        # This is exactly what I wrote.
        
        return (nums[n-1] - k) - nums[0] <= limit

    # The problem is actually simpler than a general binary search if 
    # the formula k >= nums[n-1] - nums[0] - limit holds.
    # Let's double check if there's any catch.
    # "reduce each element by at most k"
    # If we reduce nums[i] to x_i, then nums[i] - k <= x_i <= nums[i].
    # We want to find min k such that there exist x_i satisfying this 
    # and max(x_i) - min(x_i) <= limit.
    # Let the chosen range be [L, R] where R - L <= limit.
    # For each i, we need the interval [nums[i] - k, nums[i]] to intersect [L, R].
    # This means there exists x_i in [nums[i] - k, nums[i]] AND x_i in [L, R].
    # This is possible if and only if:
    # max(nums[i] - k, L) <= min(nums[i], R)
    # This must hold for all i.
    # This is equivalent to:
    # 1. nums[i] - k <= R  =>  nums[i] - R <= k
    # 2. L <= nums[i]      =>  L <= nums[i] (This must hold for all i, so L <= min(nums))
    # 3. nums[i] - k <= nums[i] (Always true for k >= 0)
    # 4. L <= R (Always true if limit >= 0)
    
    # So we need:
    # k >= max(nums[i] - R) for all i.
    # To minimize k, we need to minimize max(nums[i] - R).
    # This is minimized when R is as large as possible.
    # What is the maximum possible R?
    # From condition 2: L <= min(nums).
    # From condition 1: R >= nums[i] - k.
    # Also, we need R - L <= limit.
    # To maximize R, we should pick L = min(nums).
    # Then R = L + limit = min(nums) + limit.
    # Then k must be >= nums[i] - R for all i.
    # k >= max(nums[i] - (min(nums) + limit))
    # k >= nums[n-1] - min(nums) - limit.
    
    # Let's check if R can be larger. 
    # If we increase R, we must increase L to keep R - L <= limit.
    # But L cannot exceed min(nums) because of condition 2 (L <= nums[i] for all i).
    # So L_max = min(nums).
    # Thus R_max = min(nums) + limit.
    # The minimum k is indeed max(0, nums[n-1] - min(nums) - limit).
    
    # Wait, if the problem is this simple, why is it tagged binary search?
    # Let me re-read carefully. 
    # "Minimum K to Reduce Array Within Limit"
    # Is there any other constraint? 
    # Let's look at the problem again. 
    # Ah, I might have misread the "limit" part. 
    # Usually, these problems have a constraint like "the number of elements 
    # you can reduce is limited" or "the reduction must be exactly k".
    # But the prompt says "reduce each element by at most k".
    # Let's re-verify with an example.
    # nums = [1, 5, 10], limit = 2.
    # k = 7.
    # x_0 in [1-7, 1] = [-6, 1]. Pick x_0 = 1.
    # x_1 in [5-7, 5] = [-2, 5]. Pick x_1 = 3.
    # x_2 in [10-7, 10] = [3, 10]. Pick x_2 = 3.
    # Range [1, 3] is 2. 2 <= 2. Correct.
    
    # Is it possible that k must be such that we can pick x_i 
    # such that the difference between the *new* max and *new* min is <= limit?
    # Yes, that's what I solved.
    # Is there any other interpretation?
    # "Minimum K to Reduce Array Within Limit"
    # If the problem is simply k = max(0, max(nums) - min(nums) - limit),
    # then the complexity is O(n).
    # Let's check if there