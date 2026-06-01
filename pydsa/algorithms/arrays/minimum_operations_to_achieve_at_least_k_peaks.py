METADATA = {
    "id": 3892,
    "name": "Minimum Operations to Achieve At Least K Peaks",
    "slug": "minimum-operations-to-achieve-at-least-k-peaks",
    "category": "Greedy",
    "aliases": [],
    "tags": ["greedy", "arrays", "priority queue"],
    "difficulty": "medium",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(n)",
    "description": "Calculate the minimum operations required to ensure the array contains at least k peaks.",
}

import heapq

def solve(nums: list[int], k: int) -> int:
    """
    Args:
        nums: A list of integers representing the array.
        k: The target number of peaks required.

    Returns:
        The minimum number of operations to achieve at least k peaks.
    """
    n = len(nums)
    if k <= 0:
        return 0

    existing_peaks = 0
    for i in range(1, n - 1):
        if nums[i] > nums[i - 1] and nums[i] > nums[i + 1]:
            existing_peaks += 1

    if existing_peaks >= k:
        return 0

    needed = k - existing_peaks
    costs = []

    for i in range(1, n - 1):
        if not (nums[i] > nums[i - 1] and nums[i] > nums[i + 1]):
            left_neighbor = nums[i - 1]
            right_neighbor = nums[i + 1]
            target_height = max(left_neighbor, right_neighbor) + 1
            cost = target_height - nums[i]
            
            is_adjacent_to_peak = False
            if i > 1 and nums[i - 1] > nums[i - 2] and nums[i - 1] > nums[i]:
                is_adjacent_to_peak = True
            if i < n - 2 and nums[i + 1] > nums[i] and nums[i + 1] > nums[i + 2]:
                is_adjacent_to_peak = True
            
            if not is_adjacent_to_peak:
                costs.append(cost)

    costs.sort()
    
    total_operations = 0
    for i in range(min(needed, len(costs))):
        total_operations += costs[i]
        
    return total_operations