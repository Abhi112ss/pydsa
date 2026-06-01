METADATA = {
    "id": 719,
    "name": "Find K-th Smallest Pair Distance",
    "slug": "find-k-th-smallest-pair-distance",
    "category": "Binary Search",
    "aliases": [],
    "tags": ["binary_search", "two_pointer", "sorting"],
    "difficulty": "hard",
    "time_complexity": "O(n log n + n log W)",
    "space_complexity": "O(1)",
    "description": "Find the k-th smallest distance among all possible pairs in an array using binary search on the answer range.",
}

def solve(nums: list[int], k: int) -> int:
    """
    Finds the k-th smallest distance among all pairs in the input array.

    Args:
        nums: A list of integers.
        k: The rank of the distance to find (1-indexed).

    Returns:
        The k-th smallest distance.

    Examples:
        >>> solve([1, 3, 1], 1)
        0
        >>> solve([1, 1, 1], 2)
        0
        >>> solve([1, 6, 1], 3)
        5
    """
    nums.sort()
    n = len(nums)
    
    # The range of possible distances is [0, max_element - min_element]
    low = 0
    high = nums[-1] - nums[0]

    def count_pairs_with_distance_le(mid: int) -> int:
        """Counts how many pairs have a distance <= mid using a sliding window."""
        count = 0
        left = 0
        # Use two pointers (sliding window) to find pairs (left, right) 
        # such that nums[right] - nums[left] <= mid
        for right in range(n):
            while nums[right] - nums[left] > mid:
                left += 1
            count += (right - left)
        return count

    # Binary search on the distance value
    while low < high:
        mid = (low + high) // 2
        # If the number of pairs with distance <= mid is at least k,
        # then the k-th smallest distance is mid or smaller.
        if count_pairs_with_distance_le(mid) >= k:
            high = mid
        else:
            low = mid + 1
            
    return low
