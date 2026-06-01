METADATA = {
    "id": 3736,
    "name": "Minimum Moves to Equal Array Elements III",
    "slug": "minimum-moves-to-equal-array-elements-iii",
    "category": "Math",
    "aliases": [],
    "tags": ["greedy", "math"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Find the minimum number of moves to make all elements in an array equal, where a move consists of incrementing or decrementing an element by 1.",
}

def solve(nums: list[int]) -> int:
    """
    Calculates the minimum number of moves to make all elements in the array equal.
    A move is defined as incrementing or decrementing an element by 1.
    The optimal target value to minimize the sum of absolute differences is the median.

    Args:
        nums: A list of integers.

    Returns:
        The minimum number of moves required.

    Examples:
        >>> solve([1, 2, 3])
        2
        >>> solve([1, 10, 2, 9])
        16
    """
    if not nums:
        return 0

    # To find the median in O(n) time and O(1) space, we would ideally use 
    # Quickselect. However, since we need to return the result and the 
    # problem constraints usually allow for sorting in O(n log n) or 
    # require O(n) via Quickselect, we implement the logic for the median.
    # For the sake of a clean production implementation, we use the sorted median.
    
    # Note: In a strict O(n) requirement, one would use a selection algorithm.
    # Here we sort to find the median, which is O(n log n). 
    # To achieve true O(n), we use the Quickselect approach.
    
    def quickselect(arr: list[int], k: int) -> int:
        """Standard Quickselect algorithm to find the k-th smallest element."""
        left, right = 0, len(arr) - 1
        while left <= right:
            pivot_index = (left + right) // 2
            pivot_val = arr[pivot_index]
            
            # Partitioning
            arr[pivot_index], arr[right] = arr[right], arr[pivot_index]
            store_index = left
            for i in range(left, right):
                if arr[i] < pivot_val:
                    arr[i], arr[store_index] = arr[store_index], arr[i]
                    store_index += 1
            arr[store_index], arr[right] = arr[right], arr[store_index]
            
            if store_index == k:
                return arr[k]
            elif store_index < k:
                left = store_index + 1
            else:
                right = store_index - 1
        return arr[left]

    # Create a copy to avoid mutating the input if that's a requirement, 
    # though here we assume we can work on a local copy.
    nums_copy = list(nums)
    n = len(nums_copy)
    
    # The median is the element at index n // 2 in a sorted array.
    median = quickselect(nums_copy, n // 2)
    
    # The minimum moves is the sum of absolute differences from the median.
    total_moves = 0
    for num in nums:
        total_moves += abs(num - median)
        
    return total_moves
