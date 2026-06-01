METADATA = {
    "id": 3086,
    "name": "Minimum Moves to Pick K Ones",
    "slug": "minimum-moves-to-pick-k-ones",
    "category": "Array",
    "aliases": [],
    "tags": ["sliding_window", "two_pointer", "arrays"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Find the minimum number of moves to pick k ones from an array where a move is defined as moving a pointer to an adjacent index.",
}

def solve(nums: list[int], k: int) -> int:
    """
    Calculates the minimum moves required to pick k ones from the given array.
    
    The problem is equivalent to finding k indices of '1's such that the sum of 
    distances to a central point is minimized. This central point is the median 
    of the chosen k indices.

    Args:
        nums: A list of integers where 1 represents a target element.
        k: The number of ones to pick.

    Returns:
        The minimum number of moves required.

    Examples:
        >>> solve([1, 0, 1, 0, 1], 2)
        1
        >>> solve([1, 1, 1, 1, 1], 3)
        0
    """
    # Extract the indices of all elements that are equal to 1
    one_indices = [i for i, val in enumerate(nums) if val == 1]
    n = len(one_indices)
    
    # We need to find a contiguous subarray of length k in one_indices
    # that minimizes the sum of absolute differences from its median.
    # Let the window be indices[i ... i+k-1].
    # The median is at index mid = i + k // 2.
    
    # Precompute prefix sums of the indices to calculate window sums in O(1)
    prefix_sums = [0] * (n + 1)
    for i in range(n):
        prefix_sums[i + 1] = prefix_sums[i] + one_indices[i]
        
    min_moves = float('inf')
    
    # Iterate through every possible window of size k
    for i in range(n - k + 1):
        # Window range in one_indices is [i, i + k - 1]
        left = i
        right = i + k - 1
        mid = i + k // 2
        
        # The median index in the original one_indices list
        median_val = one_indices[mid]
        
        # Sum of distances for elements to the left of the median:
        # sum(median_val - one_indices[j]) for j in [left, mid-1]
        # = (count_left * median_val) - sum(one_indices[left...mid-1])
        count_left = mid - left
        sum_left = prefix_sums[mid] - prefix_sums[left]
        dist_left = (count_left * median_val) - sum_left
        
        # Sum of distances for elements to the right of the median:
        # sum(one_indices[j] - median_val) for j in [mid+1, right]
        # = sum(one_indices[mid+1...right]) - (count_right * median_val)
        count_right = right - mid
        sum_right = prefix_sums[right + 1] - prefix_sums[mid + 1]
        dist_right = sum_right - (count_right * median_val)
        
        current_moves = dist_left + dist_right
        if current_moves < min_moves:
            min_moves = current_moves
            
    return int(min_moves)
