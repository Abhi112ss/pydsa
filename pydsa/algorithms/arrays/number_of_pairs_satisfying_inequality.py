METADATA = {
    "id": 2426,
    "name": "Number of Pairs Satisfying Inequality",
    "slug": "number-of-pairs-satisfying-inequality",
    "category": "Math",
    "aliases": [],
    "tags": ["binary_search", "sorting", "math"],
    "difficulty": "medium",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(1)",
    "description": "Count pairs (i, j) such that i < j and nums[i] / (nums[i] + 1) >= nums[j] / (nums[j] + 1).",
}

def solve(nums: list[int]) -> int:
    """
    Counts the number of pairs (i, j) such that i < j and 
    nums[i] / (nums[i] + 1) >= nums[j] / (nums[j] + 1).

    The inequality f(x) = x / (x + 1) is strictly increasing for x >= 0.
    Therefore, nums[i] / (nums[i] + 1) >= nums[j] / (nums[j] + 1) 
    is equivalent to nums[i] >= nums[j].
    However, the problem asks for pairs (i, j) where i < j.
    Wait, the actual mathematical property is:
    x / (x + 1) >= y / (y + 1)  <=>  x(y + 1) >= y(x + 1)
    <=> xy + x >= yx + y
    <=> x >= y.
    
    So the problem is equivalent to counting pairs (i, j) with i < j and nums[i] >= nums[j].
    This is the definition of counting inversions (specifically, non-strict inversions).
    
    Args:
        nums: A list of integers.

    Returns:
        The number of pairs (i, j) satisfying the condition.

    Examples:
        >>> solve([1, 1, 1])
        3
        >>> solve([2, 1, 3])
        1
    """
    # The problem simplifies to counting pairs (i, j) where i < j and nums[i] >= nums[j].
    # This is equivalent to the number of inversions in the array if we consider 
    # the condition as nums[i] >= nums[j].
    
    def count_inversions_and_sort(arr: list[int]) -> tuple[int, list[int]]:
        """Helper function using merge sort to count inversions."""
        if len(arr) <= 1:
            return 0, arr
        
        mid = len(arr) // 2
        left_count, left_sorted = count_inversions_and_sort(arr[:mid])
        right_count, right_sorted = count_inversions_and_sort(arr[mid:])
        
        merged = []
        count = left_count + right_count
        i = 0
        j = 0
        
        # Merge step: count how many elements from the left side are >= elements from the right side
        while i < len(left_sorted) and j < len(right_sorted):
            # If left_sorted[i] >= right_sorted[j], then all elements from i to end 
            # in left_sorted are also >= right_sorted[j] because left_sorted is sorted.
            # Wait, the standard inversion count is for strictly greater. 
            # For nums[i] >= nums[j], we count when left[i] >= right[j].
            if left_sorted[i] >= right_sorted[j]:
                # This logic is slightly different for non-strict.
                # Let's use the standard merge sort inversion logic:
                # If we want to count i < j where nums[i] >= nums[j]:
                # In a sorted merge, if left[i] < right[j], no inversion.
                # If left[i] >= right[j], then right[j] is smaller than all remaining in left.
                # Actually, it's easier to count how many elements in the left are >= right[j].
                pass
            
            # Let's re-implement standard merge sort inversion counting for nums[i] >= nums[j]
            # To handle >=, we count how many elements in left are >= right[j].
            # Standard inversion (i < j, nums[i] > nums[j]) is easier.
            # Let's use the property: Total pairs - pairs where nums[i] < nums[j].
            # But that's not quite right. Let's just do the merge correctly.
            break

        # Re-implementing merge sort to count pairs (i, j) with i < j and nums[i] >= nums[j]
        return 0, []

    # Since the problem is equivalent to counting pairs (i, j) with i < j and nums[i] >= nums[j],
    # we can use a Fenwick tree (Binary Indexed Tree) or Merge Sort.
    # Given the constraints and the nature of the problem, Merge Sort is O(n log n).
    
    def merge_sort_count(data: list[int]) -> int:
        if len(data) <= 1:
            return 0
        
        mid = len(data) // 2
        left = data[:mid]
        right = data[mid:]
        
        count = merge_sort_count(left) + merge_sort_count(right)
        
        # Sort left and right to use two pointers
        left.sort()
        right.sort()
        
        # For each element in right, find how many elements in left are >= it
        # Since left is sorted, we can use two pointers or binary search.
        # Using two pointers:
        l_idx = 0
        for r_val in right:
            while l_idx < len(left) and left[l_idx] < r_val:
                l_idx += 1
            # All elements from l_idx to len(left)-1 are >= r_val
            count += (len(left) - l_idx)
            
        # Note: The above logic is slightly flawed because merge_sort_count 
        # needs to actually sort the array to work recursively.
        return count

    # Corrected Merge Sort approach
    def count_non_strict_inversions(arr: list[int]) -> tuple[int, list[int]]:
        if len(arr) <= 1:
            return 0, arr
        
        mid = len(arr) // 2
        left_inv, left_sorted = count_non_strict_inversions(arr[:mid])
        right_inv, right_sorted = count_non_strict_inversions(arr[mid:])
        
        merged = []
        total_inv = left_inv + right_inv
        
        # Two pointers to count pairs (i, j) where left_sorted[i] >= right_sorted[j]
        i = 0
        for j in range(len(right_sorted)):
            while i < len(left_sorted) and left_sorted[i] < right_sorted[j]:
                i += 1
            # Every element from i to the end of left_sorted is >= right_sorted[j]
            total_inv += (len(left_sorted) - i)
            
        # Standard merge to keep the array sorted for the parent caller
        i = 0
        j = 0
        while i < len(left_sorted) and j < len(right_sorted):
            if left_sorted[i] <= right_sorted[j]:
                merged.append(left_sorted[i])
                i += 1
            else:
                merged.append(right_sorted[j])
                j += 1
        merged.extend(left_sorted[i:])
        merged.extend(right_sorted[j:])
        
        return total_inv, merged

    # The problem asks for i < j and nums[i] >= nums[j].
    # The merge sort approach above counts exactly that.
    # However, the merge step in the code above is slightly redundant 
    # because we call .sort() or do a manual merge.
    # Let's use a cleaner version.
    
    def solve_recursive(arr: list[int]) -> tuple[int, list[int]]:
        if len(arr) <= 1:
            return 0, arr
        
        mid = len(arr) // 2
        left_count, left_sorted = solve_recursive(arr[:mid])
        right_count, right_sorted = solve_recursive(arr[mid:])
        
        merged = []
        count = left_count + right_count
        
        # Count pairs (i, j) such that left_sorted[i] >= right_sorted[j]
        # Since both are sorted, we can use two pointers.
        l_ptr = 0
        for r_ptr in range(len(right_sorted)):
            while l_ptr < len(left_sorted) and left_sorted[l_ptr] < right_sorted[r_ptr]:
                l_ptr += 1
            # All elements from l_ptr to end of left_sorted are >= right_sorted[r_ptr]
            count += (len(left_sorted) - l_ptr)
            
        # Standard merge for sorting
        i = 0
        j = 0
        while i < len(left_sorted) and j < len(right_sorted):
            if left_sorted[i] <= right_sorted[j]:
                merged.append(left_sorted[i])
                i += 1
            else:
                merged.append(right_sorted[j])
                j += 1
        merged.extend(left_sorted[i:])
        merged.extend(right_sorted[j:])
        
        return count, merged

    result, _ = solve_recursive(nums)
    return result
