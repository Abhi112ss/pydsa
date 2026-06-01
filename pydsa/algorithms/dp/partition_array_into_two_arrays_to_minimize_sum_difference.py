METADATA = {
    "id": 2035,
    "name": "Partition Array Into Two Arrays to Minimize Sum Difference",
    "slug": "partition-array-into-two-arrays-to-minimize-sum-difference",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["meet-in-the-middle", "bit-manipulation", "subset-sum"],
    "difficulty": "hard",
    "time_complexity": "O(2^(n/2) * n)",
    "space_complexity": "O(2^(n/2))",
    "description": "Partition an array of 2n integers into two arrays of size n such that the absolute difference of their sums is minimized.",
}

import bisect
from collections import defaultdict

def solve(nums: list[int]) -> int:
    """
    Partitions an array of 2n integers into two arrays of size n to minimize 
    the absolute difference between their sums using the meet-in-the-middle approach.

    Args:
        nums: A list of 2n integers.

    Returns:
        The minimum absolute difference between the sums of the two partitioned arrays.

    Examples:
        >>> solve([3, 9, 7, 3])
        2
        >>> solve([-36, 36])
        72
    """
    n_total = len(nums)
    n = n_total // 2
    total_sum = sum(nums)
    
    # Split the array into two halves
    left_half = nums[:n]
    right_half = nums[n:]
    
    # left_sums[k] stores all possible sums of exactly k elements from the left half
    left_sums = defaultdict(list)
    
    # Generate all subset sums for the left half using bit manipulation
    # There are 2^n possible subsets for each half
    for i in range(1 << n):
        current_sum = 0
        count = 0
        for j in range(n):
            if (i >> j) & 1:
                current_sum += left_half[j]
                count += 1
        left_sums[count].append(current_sum)
        
    # Sort the sums for each count to enable binary search
    for count in left_sums:
        left_sums[count].sort()
        
    min_diff = float('inf')
    
    # Generate all subset sums for the right half
    for i in range(1 << n):
        right_sum = 0
        right_count = 0
        for j in range(n):
            if (i >> j) & 1:
                right_sum += right_half[j]
                right_count += 1
        
        # To form a partition of size n, if we pick 'right_count' elements from the right,
        # we must pick 'n - right_count' elements from the left.
        needed_left_count = n - right_count
        target_left_sum = total_sum / 2 - right_sum
        
        # Use binary search to find the left sum that brings the total sum closest to total_sum / 2
        possible_left_sums = left_sums[needed_left_count]
        idx = bisect.bisect_left(possible_left_sums, target_left_sum)
        
        # Check the element at idx and idx-1 to find the closest sum to the target
        if idx < len(possible_left_sums):
            current_total = right_sum + possible_left_sums[idx]
            min_diff = min(min_diff, abs(total_sum - 2 * current_total))
            
        if idx > 0:
            current_total = right_sum + possible_left_sums[idx - 1]
            min_diff = min(min_diff, abs(total_sum - 2 * current_total))
            
        # Early exit if we found the perfect partition
        if min_diff == 0:
            return 0
            
    return int(min_diff)
