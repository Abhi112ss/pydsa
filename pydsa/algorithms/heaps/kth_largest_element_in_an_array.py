METADATA = {
    "id": 215,
    "name": "Kth Largest Element in an Array",
    "slug": "kth_largest_element_in_an_array",
    "category": "Algorithms",
    "aliases": ["find kth largest", "kth largest"],
    "tags": ["heap", "quickselect", "sorting"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Find the kth largest element in an unsorted array.",
}

import random

def solve(nums: list[int], k: int) -> int:
    """Find the kth largest element in an unsorted array using Quickselect algorithm.
    
    Args:
        nums: List of integers to search through.
        k: The position of the largest element to find (1-indexed).
    
    Returns:
        The kth largest element.
    
    Examples:
        >>> solve([3, 2, 1, 5, 6, 4], 2)
        5
        >>> solve([3, 2, 3, 1, 2, 4, 5, 5, 6], 4)
        4
    """
    # Quickselect algorithm: partition around a random pivot
    target_index = len(nums) - k  # Convert kth largest to index in sorted order
    
    def quickselect(left: int, right: int) -> int:
        # Choose random pivot to avoid worst-case O(n^2)
        pivot_index = random.randint(left, right)
        pivot_value = nums[pivot_index]
        
        # Move pivot to the end
        nums[pivot_index], nums[right] = nums[right], nums[pivot_index]
        
        # Partition: elements < pivot go to the left
        store_index = left
        for index in range(left, right):
            if nums[index] < pivot_value:
                nums[store_index], nums[index] = nums[index], nums[store_index]
                store_index += 1
        
        # Move pivot to its final position
        nums[store_index], nums[right] = nums[right], nums[store_index]
        
        # Recurse into the correct partition
        if store_index == target_index:
            return nums[store_index]
        elif store_index < target_index:
            return quickselect(store_index + 1, right)
        else:
            return quickselect(left, store_index - 1)
    
    return quickselect(0, len(nums) - 1)