METADATA = {
    "id": 303,
    "name": "Range Sum Query - Immutable",
    "slug": "range_sum_query_immutable",
    "category": "Design",
    "aliases": ["NumArray"],
    "tags": ["prefix_sum"],
    "difficulty": "easy",
    "time_complexity": "O(1)",
    "space_complexity": "O(n)",
    "description": "Design a data structure to efficiently compute the sum of elements between two indices in an immutable array.",
}

class NumArray:
    def __init__(self, nums: list[int]):
        """
        Initializes the NumArray object with the given list of integers.
        
        Args:
            nums: The input list of integers.
        
        Examples:
            >>> obj = NumArray([1, 2, 3, 4, 5])
        """
        # Precompute prefix sums: prefix[i] = sum of nums[0..i-1]
        self.prefix = [0] * (len(nums) + 1)
        for i in range(len(nums)):
            self.prefix[i + 1] = self.prefix[i] + nums[i]

    def sumRange(self, left: int, right: int) -> int:
        """
        Returns the sum of elements between indices left and right (inclusive).
        
        Args:
            left: The starting index (0-indexed).
            right: The ending index (0-indexed).
        
        Returns:
            The sum of elements from index left to right.
        
        Examples:
            >>> obj = NumArray([1, 2, 3, 4, 5])
            >>> obj.sumRange(1, 3)
            9
        """
        # The sum from left to right is prefix[right+1] - prefix[left]
        return self.prefix[right + 1] - self.prefix[left]


def solve(nums: list[int], queries: list[tuple[int, int]]) -> list[int]:
    """
    Processes multiple range sum queries on an immutable array.
    
    Args:
        nums: The input list of integers.
        queries: A list of tuples (left, right) representing range queries.
    
    Returns:
        A list of sums corresponding to each query.
    
    Examples:
        >>> solve([1, 2, 3, 4, 5], [(0, 2), (1, 3), (2, 4)])
        [6, 9, 12]
        >>> solve([-2, 0, 3, -5, 2, -1], [(0, 2), (2, 5), (0, 5)])
        [1, -1, -3]
    """
    obj = NumArray(nums)
    results = []
    for left, right in queries:
        results.append(obj.sumRange(left, right))
    return results