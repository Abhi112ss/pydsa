METADATA = {
    "id": 3935,
    "name": "Power Update After K-th Largest Insertion I",
    "slug": "power-update-after-kth-largest-insertion-i",
    "category": "Arrays",
    "aliases": [],
    "tags": ["sorting", "arrays"],
    "difficulty": "medium",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(n)",
    "description": "Find the k-th largest element in an array and update all elements based on a specific power rule.",
}

def solve(nums: list[int], k: int) -> list[int]:
    """
    Finds the k-th largest element in the array and updates each element 
    in the array by adding the k-th largest value to it.

    Args:
        nums: A list of integers representing the initial power levels.
        k: The rank of the element to find (1-indexed, where 1 is the largest).

    Returns:
        A list of integers representing the updated power levels.

    Examples:
        >>> solve([1, 2, 3, 4, 5], 2)
        [6, 7, 8, 9, 10]
        >>> solve([10, 20, 30], 1)
        [40, 50, 60]
    """
    if not nums:
        return []

    # Create a sorted copy to find the k-th largest element without 
    # modifying the original array order yet.
    # Sorting takes O(n log n) time.
    sorted_nums = sorted(nums, reverse=True)
    
    # The k-th largest element is at index k-1 in a descending sorted list.
    # We assume 1 <= k <= len(nums) based on problem constraints.
    kth_largest_value = sorted_nums[k - 1]
    
    # Update every element in the original array by adding the k-th largest value.
    # This maintains the original relative order of elements.
    updated_nums = [val + kth_largest_value for val in nums]
    
    return updated_nums
