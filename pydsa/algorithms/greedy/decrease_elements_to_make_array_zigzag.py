METADATA = {
    "id": 1144,
    "name": "Decrease Elements To Make Array Zigzag",
    "slug": "decrease-elements-to-make-array-zigzag",
    "category": "Array",
    "aliases": [],
    "tags": ["greedy", "arrays"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Find the minimum number of subtractions to make an array zigzag by either making even indices smaller than neighbors or odd indices smaller than neighbors.",
}

def solve(nums: list[int]) -> int:
    """
    Calculates the minimum number of subtractions needed to make the array zigzag.
    
    A zigzag array is one where elements at even indices are strictly smaller 
    than their neighbors, or elements at odd indices are strictly smaller 
    than their neighbors.

    Args:
        nums: A list of integers representing the input array.

    Returns:
        The minimum number of subtractions required.

    Examples:
        >>> solve([1, 2, 3])
        2
        >>> solve([9, 8, 1, 2, 1])
        2
    """
    n = len(nums)
    if n <= 1:
        return 0

    def get_cost(start_index: int) -> int:
        """
        Calculates the cost to make elements at start_index, start_index + 2, ...
        strictly smaller than their immediate neighbors.
        """
        total_subtractions = 0
        for i in range(start_index, n, 2):
            # Determine the value of the neighbors
            left_neighbor = nums[i - 1] if i > 0 else float('inf')
            right_neighbor = nums[i + 1] if i < n - 1 else float('inf')
            
            # The target value for nums[i] must be less than both neighbors
            target_max_val = min(left_neighbor, right_neighbor) - 1
            
            # If current element is not already smaller than target, calculate cost
            if nums[i] > target_max_val:
                total_subtractions += nums[i] - target_max_val
                
        return total_subtractions

    # Case 1: Even indices are the 'valleys' (smaller than neighbors)
    # Case 2: Odd indices are the 'valleys' (smaller than neighbors)
    # We take the minimum of these two strategies.
    return min(get_cost(0), get_cost(1))
