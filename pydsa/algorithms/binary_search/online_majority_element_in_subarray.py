METADATA = {
    "id": 1157,
    "name": "Online Majority Element In Subarray",
    "slug": "online-majority-element-in-subarray",
    "category": "Hard",
    "aliases": [],
    "tags": ["binary_search", "segment_tree", "randomization"],
    "difficulty": "hard",
    "time_complexity": "O(q log n)",
    "space_complexity": "O(n)",
    "description": "Given an array and queries for subarrays, find the majority element (appearing more than half the time) in each subarray.",
}

import collections
import bisect
import random

class OnlineMajorityElementSolver:
    """
    A solver for finding the majority element in subarrays using a randomized 
    sampling approach combined with binary search.
    """

    def __init__(self, nums: list[int]):
        """
        Initializes the solver by pre-processing the positions of each element.

        Args:
            nums: The input array of integers.
        """
        self.nums = nums
        self.n = len(nums)
        # Map each value to a sorted list of indices where it appears
        self.pos_map: dict[int, list[int]] = collections.defaultdict(list)
        for index, value in enumerate(nums):
            self.pos_map[value].append(index)

    def query(self, left: int, right: int) -> int:
        """
        Finds the majority element in the range [left, right].

        Args:
            left: The starting index of the subarray.
            right: The ending index of the subarray.

        Returns:
            The majority element if it exists, otherwise -1.

        Examples:
            >>> solver = OnlineMajorityElementSolver([1, 2, 1, 2, 1])
            >>> solver.query(0, 4)
            1
            >>> solver.query(0, 1)
            -1
        """
        subarray_len = right - left + 1
        threshold = subarray_len // 2

        # A majority element must occupy more than 50% of the subarray.
        # If we pick a random element from the subarray, the probability 
        # that we pick the majority element is > 1/2.
        # By checking 40 random samples, the probability of missing the 
        # majority element is < (1/2)^40, which is negligible.
        for _ in range(40):
            # Pick a random index within the range [left, right]
            random_idx = random.randint(left, right)
            candidate = self.nums[random_idx]

            # Use binary search to count occurrences of the candidate in [left, right]
            # bisect_right finds the first position after the target value
            # bisect_left finds the first position of the target value
            indices = self.pos_map[candidate]
            count = bisect.bisect_right(indices, right) - bisect.bisect_left(indices, left)

            if count > threshold:
                return candidate

        return -1

def solve(nums: list[int], queries: list[list[int]]) -> list[int]:
    """
    Processes multiple queries to find majority elements in subarrays.

    Args:
        nums: The input array of integers.
        queries: A list of queries, where each query is [left, right].

    Returns:
        A list of results for each query.

    Examples:
        >>> solve([1, 2, 1, 2, 1], [[0, 4], [0, 1]])
        [1, -1]
    """
    solver = OnlineMajorityElementSolver(nums)
    results = []
    for left, right in queries:
        results.append(solver.query(left, right))
    return results
