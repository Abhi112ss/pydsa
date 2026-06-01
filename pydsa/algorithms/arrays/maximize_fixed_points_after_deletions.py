METADATA = {
    "id": 3920,
    "name": "Maximize Fixed Points After Deletions",
    "slug": "maximize-fixed-points-after-deletions",
    "category": "Array",
    "aliases": [],
    "tags": ["greedy", "arrays"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Maximize the number of elements that match their index after performing deletions.",
}

def solve(nums: list[int]) -> int:
    """
    Calculates the maximum number of fixed points (nums[i] == i) possible 
    after deleting any number of elements from the array.

    A fixed point is achieved if an element's value equals its index in the 
    resulting array. Since deleting elements shifts subsequent elements to 
    the left, an element 'v' can become a fixed point if and only if 
    v >= 0 and there are at most 'v' elements before it in the original array.

    Args:
        nums: A list of integers representing the original array.

    Returns:
        The maximum number of fixed points possible.

    Examples:
        >>> solve([0, 2, 2, 2])
        2
        >>> solve([1, 1, 1])
        1
        >>> solve([0, 1, 2, 3])
        4
    """
    # To maximize fixed points, we want to pick elements such that 
    # for each chosen element 'v', its new index is 'v'.
    # This is possible if the number of elements we keep before 'v' is exactly 'v'.
    # Therefore, for an element 'v' to be a fixed point, it must satisfy:
    # 1. v >= 0
    # 2. v <= current_index_in_original_array
    # 3. We must be able to pick exactly 'v' elements from the elements 
    #    appearing before it in the original array.
    
    # However, the problem simplifies to: how many distinct values 'v' can we 
    # pick such that each 'v' is at an index >= v in the original array?
    # Actually, the constraint is more specific: if we pick a set of values 
    # {v1, v2, ..., vk} to be fixed points, they must be able to occupy 
    # indices {v1, v2, ..., vk}. This is only possible if all v_i are distinct 
    # and for every v_i, there are at least v_i elements available to its left.
    
    # Since we want to maximize the count, and each fixed point 'v' requires 
    # exactly 'v' elements to its left, we can only have one element for each 
    # unique value 'v'. If we pick value 'v', it will occupy index 'v'.
    # The condition for 'v' to be a valid fixed point is that there are at 
    # least 'v' elements in the original array at indices <= the original 
    # index of 'v' that can serve as the 'v' elements before it.
    
    # Correct Greedy Strategy:
    # An element with value 'v' can be a fixed point if its original index 'i' 
    # satisfies i >= v. To maximize the number of fixed points, we can 
    # pick one instance of each unique value 'v' that satisfies i >= v.
    
    possible_values = set()
    
    for original_index, value in enumerate(nums):
        # If the value is greater than its current index, it can never 
        # be a fixed point because even if we delete everything before it, 
        # its index will still be at most its original index.
        # Wait, that's wrong. If we delete elements, the index decreases.
        # If original index is 5 and value is 2, we can delete 3 elements 
        # to make the index 2.
        # If original index is 2 and value is 5, we can't make the index 5.
        # So the condition is: value <= original_index.
        
        if value <= original_index:
            # We can potentially make this 'value' a fixed point.
            # We use a set to ensure we only count each unique value once,
            # because each index in the final array can only hold one value.
            possible_values.add(value)
            
    # However, there is a catch: if we pick values {0, 1, 5}, 
    # we need to ensure we have enough elements to fill the gaps.
    # But the problem allows deleting ANY elements. 
    # If we want to have fixed points at indices 0, 1, and 5, 
    # we need at least 6 elements in total.
    # The set of values we pick must satisfy: 
    # for every v in our set, v < total_elements_kept.
    # Since we want to maximize the size of the set, and the largest 
    # value 'v' in our set requires at least 'v+1' elements to exist,
    # we must ensure that if we pick a set of values S, 
    # then for all v in S, v < len(nums) is not enough; 
    # we need to be able to pick 'v' elements to be at indices 0...v-1.
    
    # Let's refine: We can pick a value 'v' if there exists an index 'i' 
    # such that nums[i] == v and i >= v.
    # Let the set of such values be V.
    # We want to pick a subset of V such that we can actually form the indices.
    # If we pick values {v1, v2, ..., vk}, we can form them if 
    # we can arrange them such that each vi is at index vi.
    # This is possible if we have enough elements to fill the indices.
    # The number of elements needed to support the largest value 'max(V_subset)'
    # is max(V_subset) + 1.
    # So we need: max(V_subset) + 1 <= len(nums).
    # Since all v in V satisfy v <= original_index < len(nums), 
    # then v + 1 <= len(nums) is always true for any v in V.
    # Thus, we can always pick all unique values in V.
    
    return len(possible_values)
