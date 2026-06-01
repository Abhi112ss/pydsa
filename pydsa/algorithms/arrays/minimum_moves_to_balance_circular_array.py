METADATA = {
    "id": 3776,
    "name": "Minimum Moves to Balance Circular Array",
    "slug": "minimum_moves_to_balance_circular_array",
    "category": "Math",
    "aliases": [],
    "tags": ["two_pointer", "math", "median"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Find the minimum moves to make all elements in a circular array equal by choosing a target value.",
}

def solve(nums: list[int]) -> int:
    """
    Calculates the minimum moves to make all elements in a circular array equal.
    
    The problem of minimizing the sum of absolute differences |x_i - target| 
    is solved by setting the target to the median of the array. Since the 
    array is circular, the relative distances remain the same for any 
    rotation, so we simply find the median of the given elements.

    Args:
        nums: A list of integers representing the circular array.

    Returns:
        The minimum number of moves required.

    Examples:
        >>> solve([1, 2, 3])
        2
        >>> solve([1, 10, 100])
        109
    """
    if not nums:
        return 0

    n = len(nums)
    
    # To find the median in O(n) time, we use the Quickselect algorithm.
    # However, for production-grade simplicity and to ensure O(n) average,
    # we can use a selection approach.
    
    def quickselect(arr: list[int], k: int) -> int:
        """Standard Quickselect algorithm to find the k-th smallest element."""
        if len(arr) == 1:
            return arr[0]
        
        pivot = arr[len(arr) // 2]
        lows = [x for x in arr if x < pivot]
        highs = [x for x in arr if x > pivot]
        pivots = [x for x in arr if x == pivot]
        
        if k < len(lows):
            return quickselect(lows, k)
        elif k < len(lows) + len(pivots):
            return pivots[0]
        else:
            return quickselect(highs, k - len(lows) - len(pivots))

    # The median minimizes the sum of absolute deviations.
    # For an odd number of elements, it's the middle one.
    # For an even number, any value between the two middle elements works.
    median_index = n // 2
    target = quickselect(nums, median_index)
    
    # Calculate the total moves: sum of |nums[i] - target|
    total_moves = 0
    for val in nums:
        total_moves += abs(val - target)
        
    return total_moves
