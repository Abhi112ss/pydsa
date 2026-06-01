METADATA = {
    "id": 3487,
    "name": "Maximum Unique Subarray Sum After Deletion",
    "slug": "maximum_unique_subarray_sum_after_deletion",
    "category": "Array",
    "aliases": [],
    "tags": ["sliding_window", "hash_map", "prefix_sum"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Find the maximum sum of a subarray containing only unique elements, allowing for the deletion of at most one element from the subarray.",
}

def solve(nums: list[int]) -> int:
    """
    Args:
        nums: A list of integers.

    Returns:
        The maximum sum of a subarray with unique elements after deleting at most one element.
    """
    n = len(nums)
    if n == 0:
        return 0

    max_sum = 0
    current_window_sum = 0
    left = 0
    seen_elements = {}

    for right in range(n):
        current_val = nums[right]

        while current_val in seen_elements and seen_elements[current_val] >= left:
            duplicate_val = nums[left]
            current_window_sum -= duplicate_val
            seen_elements[duplicate_val] = -1
            left += 1

        seen_elements[current_val] = right
        current_window_sum += current_val

        max_sum = max(max_sum, current_window_sum)

        if left < right:
            current_window_sum_minus_min = current_window_sum - min(nums[left:right+1])
            
            temp_sum = current_window_sum
            min_val_in_window = float('inf')
            
            for i in range(left, right + 1):
                if nums[i] < min_val_in_window:
                    min_val_in_window = nums[i]
            
            max_sum = max(max_sum, current_window_sum - min_val_in_window)

    return max_sum

def solve(nums: list[int]) -> int:
    """
    Args:
        nums: A list of integers.

    Returns:
        The maximum sum of a subarray with unique elements after deleting at most one element.
    """
    n = len(nums)
    if n == 0:
        return 0

    max_sum = 0
    left = 0
    current_sum = 0
    seen = {}
    
    import collections
    min_heap = [] 
    
    # To achieve O(n), we need to track the minimum element in the current unique window efficiently.
    # Since we only care about the maximum sum after deleting ONE element, 
    # we want to subtract the smallest element in the current unique window.
    # A sliding window with a monotonic queue or a segment tree could work, 
    # but for a single deletion, we can use a sliding window minimum approach.

    # Re-implementing with a more efficient approach for the "delete one" constraint.
    # We maintain a window [left, right] of unique elements.
    # For each window, we want max(sum(window), sum(window) - min(window)).
    # Since sum(window) - min(window) is only better if min(window) > 0, 
    # and we want to maximize the result, we actually want to subtract the smallest element 
    # if it helps, but the problem implies we *can* delete. If all elements are positive, 
    # deleting the smallest is optimal. If there are negatives, deleting the most negative is optimal.
    
    # Correct logic: For a unique window, the best sum is either the sum of all elements 
    # or the sum of all elements minus the minimum element in that window.
    
    from collections import deque

    seen = {}
    left = 0
    current_sum = 0
    max_total_sum = 0
    min_deque = deque() # Stores indices for sliding window minimum

    for right in range(n):
        val = nums[right]
        
        while val in seen and seen[val] >= left:
            old_idx = seen[val]
            # Shrink window from left
            while left <= old_idx:
                if min_deque and min_deque[0] == left:
                    min_deque.popleft()
                current_sum -= nums[left]
                left += 1
            # Note: we don't need to manually remove from min_deque here 
            # because the while loop handles the left pointer.
            # However, the 'seen' check is the primary driver.
            # We must ensure the min_deque is synchronized with 'left'.
            # The loop above handles 'left' moving past the duplicate.
            # But we need to re-sync the min_deque after the while loop.
            # Actually, the standard sliding window minimum logic is:
            # 1. Remove indices from front if they are < left.
            # 2. Remove indices from back if nums[idx] >= nums[right].
            # 3. Add right.
            
        # Re-syncing min_deque after potential left movement
        while min_deque and min_deque[0] < left:
            min_deque.popleft()

        seen[val] = right
        current_sum += val
        
        while min_deque and nums[min_deque[-1]] >= val:
            min_deque.pop()
        min_deque.append(right)

        # Calculate max sum for current unique window
        # Option 1: No deletion
        max_total_sum = max(max_total_sum, current_sum)
        
        # Option 2: Delete the minimum element in the current unique window
        if min_deque:
            min_val = nums[min_deque[0]]
            max_total_sum = max(max_total_sum, current_sum - min_val)

    return max_total_sum