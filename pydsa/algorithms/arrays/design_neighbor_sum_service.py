METADATA = {
    "id": 3242,
    "name": "Design Neighbor Sum Service",
    "slug": "design-neighbor-sum-service",
    "category": "Design",
    "aliases": [],
    "tags": ["design", "array", "prefix_sum"],
    "difficulty": "medium",
    "time_complexity": "O(1) per query, O(n) initialization",
    "space_complexity": "O(n)",
    "description": "Design a service that allows updating elements in an array and querying the sum of an element and its neighbors.",
}

class NeighborSumService:
    def __init__(self, nums: list[int]):
        """
        Initializes the service with the given array.
        
        Args:
            nums: A list of integers representing the initial state.
        """
        self.nums = nums
        self.n = len(nums)
        # Precompute the neighbor sums for all indices to allow O(1) queries.
        # neighbor_sums[i] stores nums[i-1] + nums[i] + nums[i+1] (with boundary checks).
        self.neighbor_sums = [0] * self.n
        self._compute_all_neighbor_sums()

    def _compute_all_neighbor_sums(self) -> None:
        """Helper to compute initial neighbor sums for the entire array."""
        for i in range(self.n):
            current_sum = self.nums[i]
            if i > 0:
                current_sum += self.nums[i - 1]
            if i < self.n - 1:
                current_sum += self.nums[i + 1]
            self.neighbor_sums[i] = current_sum

    def update(self, index: int, val: int) -> None:
        """
        Updates the value at the given index and updates affected neighbor sums.
        
        Args:
            index: The index to update.
            val: The new value to be placed at the index.
        """
        diff = val - self.nums[index]
        self.nums[index] = val
        
        # The update at 'index' affects the neighbor sum of:
        # 1. The index itself
        # 2. The left neighbor (index - 1)
        # 3. The right neighbor (index + 1)
        for i in range(index - 1, index + 2):
            if 0 <= i < self.n:
                self.neighbor_sums[i] += diff

    def get(self, index: int) -> int:
        """
        Returns the sum of the element at index and its neighbors.
        
        Args:
            index: The index to query.
            
        Returns:
            The sum of nums[index-1], nums[index], and nums[index+1].
        """
        return self.neighbor_sums[index]

def solve():
    """
    Example usage of the NeighborSumService.
    """
    nums = [1, 2, 3, 4, 5]
    service = NeighborSumService(nums)
    
    # Initial sums: [1+2, 1+2+3, 2+3+4, 3+4+5, 4+5] -> [3, 6, 9, 12, 9]
    assert service.get(0) == 3
    assert service.get(2) == 9
    
    service.update(1, 10) 
    # nums becomes [1, 10, 3, 4, 5]
    # index 0 sum: 1 + 10 = 11
    # index 1 sum: 1 + 10 + 3 = 14
    # index 2 sum: 10 + 3 + 4 = 17
    assert service.get(0) == 11
    assert service.get(1) == 14
    assert service.get(2) == 17
