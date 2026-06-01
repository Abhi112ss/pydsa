METADATA = {
    "id": 3567,
    "name": "Minimum Absolute Difference in Sliding Submatrix",
    "slug": "minimum_absolute_difference_in_sliding_submatrix",
    "category": "Sliding Window",
    "aliases": [],
    "tags": ["sliding_window", "heap", "sorted_list"],
    "difficulty": "hard",
    "time_complexity": "O(N * M * log(K))",
    "space_complexity": "O(K)",
    "description": "Find the minimum absolute difference between any two elements in all possible submatrices of size KxK within an N x M matrix.",
}

from bisect import bisect_left, insort

class SortedList:
    """
    A simple implementation of a sorted list using bisect to maintain order.
    In a production environment, a Fenwick tree or a Balanced BST would be used.
    """
    def __init__(self):
        self.data = []

    def add(self, val: int) -> None:
        insort(self.data, val)

    def remove(self, val: int) -> None:
        idx = bisect_left(self.data, val)
        if idx < len(self.data) and self.data[idx] == val:
            self.data.pop(idx)

    def get_min_diff(self) -> float:
        if len(self.data) < 2:
            return float('inf')
        # The minimum difference in a sorted list must be between adjacent elements
        # However, since we need to find the global min diff of the window, 
        # we track it externally or recalculate. For this problem, we need 
        # to efficiently update the min diff as elements enter/leave.
        # To keep O(log K) per operation, we use a secondary structure.
        return 0.0 # Placeholder for logic handled in solve()

def solve(matrix: list[list[int]], k: int) -> int:
    """
    Finds the minimum absolute difference between any two elements in any KxK submatrix.

    Args:
        matrix: A 2D list of integers representing the input grid.
        k: The dimension of the square submatrix.

    Returns:
        The minimum absolute difference found across all KxK submatrices.

    Examples:
        >>> solve([[1, 5, 9], [10, 2, 8], [3, 7, 4]], 2)
        1
    """
    rows = len(matrix)
    cols = len(matrix[0])
    
    # We use a SortedList to maintain elements in the current KxK window.
    # To find the minimum difference efficiently, we use a second SortedList 
    # to store the differences between adjacent elements in the first SortedList.
    from bisect import insort, bisect_left

    class WindowManager:
        def __init__(self):
            self.elements = []  # Sorted list of elements in window
            self.diffs = []     # Sorted list of differences between adjacent elements

        def add(self, val: int) -> None:
            idx = bisect_left(self.elements, val)
            
            # If there are elements, calculate new differences
            prev_val = self.elements[idx - 1] if idx > 0 else None
            next_val = self.elements[idx] if idx < len(self.elements) else None
            
            if prev_val is not None and next_val is not None:
                # Remove the old difference between prev and next
                old_diff = next_val - prev_val
                self.diffs.remove(old_diff)
            
            if prev_val is not None:
                insort(self.diffs, val - prev_val)
            if next_val is not None:
                insort(self.diffs, next_val - val)
                
            insort(self.elements, val)

        def remove(self, val: int) -> None:
            idx = bisect_left(self.elements, val)
            # Ensure we are removing the correct instance
            if idx >= len(self.elements) or self.elements[idx] != val:
                return

            prev_val = self.elements[idx - 1] if idx > 0 else None
            next_val = self.elements[idx + 1] if idx + 1 < len(self.elements) else None
            
            # Remove differences associated with the element being removed
            if prev_val is not None:
                self.diffs.remove(val - prev_val)
            if next_val is not None:
                self.diffs.remove(next_val - val)
            
            # If there were neighbors, a new difference is created between them
            if prev_val is not None and next_val is not None:
                insort(self.diffs, next_val - prev_val)
                
            self.elements.pop(idx)

        def get_min_diff(self) -> int:
            return self.diffs[0] if self.diffs else float('inf')

    min_global_diff = float('inf')
    
    # Sliding window approach:
    # 1. Iterate through rows using a sliding window of height K.
    # 2. For each row-set, use a sliding window of width K.
    # However, a 2D sliding window is better handled by:
    # For each row, maintain a sliding window of width K.
    # Then, for each column, maintain a sliding window of height K.
    # But since we need the KxK submatrix, we can use a 2D sliding window.
    
    # Optimization: We can treat this as a 1D sliding window problem over 
    # "rows of windows".
    
    for r in range(rows - k + 1):
        # For a fixed set of K rows, we slide a window of width K across columns
        manager = WindowManager()
        
        # Initialize the first KxK window for this row set
        for i in range(r, r + k):
            for j in range(k):
                manager.add(matrix[i][j])
        
        min_global_diff = min(min_global_diff, manager.get_min_diff())
        
        # Slide the window to the right
        for c in range(1, cols - k + 1):
            # Remove the leftmost column of the previous window
            for i in range(r, r + k):
                manager.remove(matrix[i][c - 1])
            # Add the rightmost column of the new window
            for i in range(r, r + k):
                manager.add(matrix[i][c + k - 1])
            
            min_global_diff = min(min_global_diff, manager.get_min_diff())
            
            if min_global_diff == 0:
                return 0

    return int(min_global_diff)
