METADATA = {
    "id": 2780,
    "name": "Minimum Index of a Valid Split",
    "slug": "minimum-index-of-a-valid-split",
    "category": "Hash Table",
    "aliases": [],
    "tags": ["hash_map", "prefix_sum", "array"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Find the minimum index such that the elements before the index and after the index have no common elements.",
}

def solve(nums: list[int]) -> int:
    """
    Finds the minimum index such that the elements in the left part [0, index] 
    and the right part [index + 1, n-1] have no common elements.

    Args:
        nums: A list of integers.

    Returns:
        The minimum index of a valid split. Returns -1 if no such split exists.

    Examples:
        >>> solve([1, 2, 3, 4, 5])
        0
        >>> solve([1, 2, 1, 2, 3])
        3
        >>> solve([1, 2, 3, 1, 2, 3])
        -1
    """
    n = len(nums)
    if n < 2:
        return -1

    # Frequency map for the right side (suffix)
    # Initially, all elements are in the right side
    right_counts: dict[int, int] = {}
    for num in nums:
        right_counts[num] = right_counts.get(num, 0) + 1

    # Frequency map for the left side (prefix)
    left_counts: dict[int, int] = {}

    # Iterate through the array to find the split point
    # The split occurs AFTER index 'i', so the left part is nums[0...i]
    # and the right part is nums[i+1...n-1]
    # We need to check if the set of elements in left_counts and right_counts are disjoint.
    # However, the problem defines split at index 'i' such that left is [0, i] and right is [i+1, n-1].
    # Wait, the problem says: "the elements in the left part and the elements in the right part 
    # have no common elements."
    # A split at index 'i' means left is nums[0...i] and right is nums[i+1...n-1].
    # The constraint is that the set of elements in left and right must be disjoint.
    
    # To optimize, we track how many elements in the current 'left' set 
    # are also present in the 'right' set.
    
    # Let's refine: A split is valid if for every element in left, its count in right is 0.
    # Since we move index by index, we can maintain the 'right_counts' and 'left_counts'.
    
    # We iterate up to n-2 because the right part must have at least one element.
    for i in range(n - 1):
        current_val = nums[i]
        
        # Add current element to the left side
        left_counts[current_val] = left_counts.get(current_val, 0) + 1
        
        # Remove current element from the right side
        right_counts[current_val] -= 1
        if right_counts[current_val] == 0:
            del right_counts[current_val]
            
        # A split is valid if the intersection of keys in left_counts and right_counts is empty.
        # However, checking intersection every time is O(unique_elements), making it O(N^2) worst case.
        # Optimization: Instead of checking intersection, we can track the number of 
        # 'common' elements. But since we only care if ANY element from left is in right,
        # we can use a counter for how many unique elements in 'left' exist in 'right'.
        # Actually, a simpler way: A split is valid if for all x in left_counts, 
        # right_counts[x] is 0.
        # Even simpler: The split is valid if the number of unique elements in the 
        # whole array is equal to (unique elements in left) + (unique elements in right).
        # But that's only true if they are disjoint.
        
        # Let's use the property: The split is valid if for every element in left_counts,
        # it does not exist in right_counts.
        # To do this in O(1) per step, we track 'common_elements_count'.
        # But 'common_elements_count' is tricky because an element might be in both 
        # but its count in right becomes 0.
        
        # Let's use a different approach: 
        # A split at index i is valid if for all x in left_counts, right_counts.get(x, 0) == 0.
        # This is equivalent to saying: the set of keys in left_counts and right_counts are disjoint.
        # We can maintain a variable `overlap_count` which is the number of unique elements 
        # that are present in BOTH left_counts and right_counts.
        
        # Let's restart the loop logic with overlap tracking.
        pass

    # Re-implementing with overlap tracking for O(n)
    right_counts = {}
    for x in nums:
        right_counts[x] = right_counts.get(x, 0) + 1
    
    left_counts = {}
    overlap_count = 0
    
    for i in range(n - 1):
        val = nums[i]
        
        # 1. Add val to left
        if val in left_counts:
            # val is already in left. If it was in right, it's still in right (unless count was 1)
            # But we need to check if it WAS in right and now it's in both.
            # Actually, if it's already in left, adding it doesn't change the 'set' of keys.
            left_counts[val] += 1
        else:
            left_counts[val] = 1
            # If this new element from left is also in right, overlap increases
            if right_counts.get(val, 0) > 0:
                overlap_count += 1
        
        # 2. Remove val from right
        if right_counts[val] == 1:
            # val is about to be removed from right. 
            # If it was in left, the overlap decreases.
            if val in left_counts:
                overlap_count -= 1
            del right_counts[val]
        else:
            right_counts[val] -= 1
            
        # 3. Check validity
        if overlap_count == 0:
            return i
            
    return -1

class Solution:
    def minimumIndex(self, nums: list[int]) -> int:
        """
        Wrapper class for LeetCode compatibility.
        """
        return solve(nums)
