METADATA = {
    "id": 2966,
    "name": "Divide Array Into Arrays With Max Difference",
    "slug": "divide-array-into-arrays-with-max-difference",
    "category": "Array",
    "aliases": [],
    "tags": ["greedy", "sorting", "arrays"],
    "difficulty": "easy",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(n)",
    "description": "Divide an array into subarrays of size k such that the difference between the maximum and minimum element in each subarray is at most max_difference.",
}

def solve(nums: list[int], max_difference: int, k: int) -> list[list[int]]:
    """
    Divides the array into subarrays of size k where the difference between 
    the max and min element in each subarray is <= max_difference.

    Args:
        nums: A list of integers to be divided.
        max_difference: The maximum allowed difference between max and min in a group.
        k: The required size of each subarray.

    Returns:
        A list of lists, where each inner list is a subarray of size k. 
        Returns an empty list if no such division is possible.

    Examples:
        >>> solve([1, 3, 2, 4, 5, 6], 1, 2)
        [[1, 2], [3, 4], [5, 6]]
        >>> solve([1, 3, 2, 4, 5, 6], 1, 3)
        []
    """
    # Sorting is the key: elements that are close in value will be adjacent.
    # This allows us to group elements greedily.
    nums.sort()
    
    n = len(nums)
    result: list[list[int]] = []
    
    # Iterate through the sorted array in steps of k
    for i in range(0, n, k):
        # The current group consists of elements from index i to i + k - 1
        group = nums[i : i + k]
        
        # Since the array is sorted, the min is the first element 
        # and the max is the last element of the group.
        if group[-1] - group[0] > max_difference:
            return []
        
        result.append(group)
        
    return result
