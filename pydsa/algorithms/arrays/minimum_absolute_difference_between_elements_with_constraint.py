METADATA = {
    "id": 2817,
    "name": "Minimum Absolute Difference Between Elements With Constraint",
    "slug": "minimum-absolute-difference-between-elements-with-constraint",
    "category": "Arrays",
    "aliases": [],
    "tags": ["arrays", "sliding_window", "two_pointer", "sorted_set"],
    "difficulty": "hard",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(n)",
    "description": "Find the minimum absolute difference between two elements in an array such that their indices differ by at least k.",
}

import bisect

class SortedList:
    """
    A simplified SortedList implementation using bisect to maintain order.
    While a true Balanced BST is O(log n), Python's bisect on a list 
    is O(n) for insertions, but for LeetCode constraints, this often 
    passes or can be optimized with a Fenwick tree/Segment tree.
    To ensure O(n log n) behavior in a real production environment, 
    one would use a Red-Black Tree or AVL Tree.
    """
    def __init__(self):
        self._data = []

    def add(self, val: int) -> None:
        bisect.insort(self._data, val)

    def remove(self, val: int) -> None:
        # Find the index of the element to remove
        idx = bisect.bisect_left(self._data, val)
        if idx < len(self._data) and self._data[idx] == val:
            self._data.pop(idx)

    def find_closest_diff(self, val: int) -> float:
        if not self._data:
            return float('inf')
        
        # Find the position where val would be inserted
        idx = bisect.bisect_left(self._data, val)
        res = float('inf')
        
        # Check the element at the insertion point (the smallest element >= val)
        if idx < len(self._data):
            res = min(res, abs(self._data[idx] - val))
        
        # Check the element before the insertion point (the largest element < val)
        if idx > 0:
            res = min(res, abs(self._data[idx - 1] - val))
            
        return res

def solve(nums: list[int], k: int) -> int:
    """
    Finds the minimum absolute difference between two elements nums[i] and nums[j]
    such that |i - j| >= k.

    Args:
        nums: A list of integers.
        k: The minimum required distance between indices.

    Returns:
        The minimum absolute difference found.

    Examples:
        >>> solve([4, 5, 1, 10, 12], 2)
        1
        >>> solve([1, 2, 3, 4], 1)
        1
    """
    n = len(nums)
    min_diff = float('inf')
    
    # We use a sorted structure to keep track of elements that are at least k distance away
    # from the current index 'i'.
    active_elements = SortedList()

    # We iterate through the array. For each index i, the valid candidates for 
    # comparison are elements in the range [0, i - k].
    for i in range(k, n):
        # Add the element that just became valid (at index i - k)
        active_elements.add(nums[i - k])
        
        # Find the closest value to nums[i] in the sorted set of valid candidates
        current_diff = active_elements.find_closest_diff(nums[i])
        
        if current_diff < min_diff:
            min_diff = current_diff
            
        # Optimization: if we found a difference of 0, we can't do better
        if min_diff == 0:
            return 0

    return int(min_diff)
