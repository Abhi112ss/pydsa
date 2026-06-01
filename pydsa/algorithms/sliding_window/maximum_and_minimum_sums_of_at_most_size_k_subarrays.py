METADATA = {
    "id": 3430,
    "name": "Maximum and Minimum Sums of at Most Size K Subarrays",
    "slug": "maximum-and-minimum-sums-of-at-most-size-k-subarrays",
    "category": "Array",
    "aliases": [],
    "tags": ["sliding_window", "array", "deque", "prefix_sum"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Find the maximum and minimum possible sums of subarrays with length at most K.",
}

from collections import deque

def solve(nums: list[int], k: int) -> list[int]:
    """
    Calculates the maximum and minimum sums of subarrays with length at most K.

    Args:
        nums: A list of integers representing the input array.
        k: The maximum allowed length of a subarray.

    Returns:
        A list containing two integers: [maximum_sum, minimum_sum].

    Examples:
        >>> solve([1, -2, 3, -4, 5], 2)
        [5, -4]
        >>> solve([1, 2, 3], 1)
        [3, 1]
    """
    n = len(nums)
    
    # Calculate prefix sums to transform subarray sum problem into 
    # difference of prefix sums: sum(i, j) = prefix_sum[j+1] - prefix_sum[i]
    prefix_sums = [0] * (n + 1)
    for i in range(n):
        prefix_sums[i + 1] = prefix_sums[i] + nums[i]

    def get_extreme_sums(find_max: bool) -> int:
        """
        Helper to find either the max or min subarray sum using a monotonic queue.
        To find max sum: max(prefix_sums[j] - prefix_sums[i]) where 0 <= j-i <= k.
        This is equivalent to prefix_sums[j] - min(prefix_sums[i]) for i in [j-k, j-1].
        """
        extreme_val = float('-inf') if find_max else float('inf')
        # deque stores indices of prefix_sums to maintain monotonicity
        # For max sum, we want to subtract the smallest possible prefix_sum in the window
        # For min sum, we want to subtract the largest possible prefix_sum in the window
        dq = deque()

        for j in range(n + 1):
            # 1. Remove indices that are out of the window of size K
            if dq and dq[0] < j - k:
                dq.popleft()

            # 2. Calculate the current subarray sum ending at j-1
            # We skip j=0 because a subarray must have at least one element (length >= 1)
            # However, the problem asks for "at most size K", and the prefix sum logic
            # naturally handles the range. We check if dq is not empty to ensure a valid i exists.
            if dq:
                if find_max:
                    # To maximize: current_prefix - min_prefix_in_window
                    current_sum = prefix_sums[j] - prefix_sums[dq[0]]
                    extreme_val = max(extreme_val, current_sum)
                else:
                    # To minimize: current_prefix - max_prefix_in_window
                    current_sum = prefix_sums[j] - prefix_sums[dq[0]]
                    extreme_val = min(extreme_val, current_sum)

            # 3. Maintain the monotonic property of the deque
            # If finding max: we want dq[0] to be the index of the minimum prefix_sum
            # If finding min: we want dq[0] to be the index of the maximum prefix_sum
            if find_max:
                while dq and prefix_sums[dq[-1]] >= prefix_sums[j]:
                    dq.pop()
            else:
                while dq and prefix_sums[dq[-1]] <= prefix_sums[j]:
                    dq.pop()
            
            dq.append(j)

        return int(extreme_val)

    # Note: The logic above calculates max(P[j] - min(P[i])) for max sum
    # and min(P[j] - max(P[i])) for min sum.
    # We must ensure we don't pick j=i (which would be sum 0, length 0).
    # The loop structure handles this by calculating sum BEFORE adding current j to dq.
    
    # Re-implementing slightly cleaner to ensure length >= 1
    def get_max_sum() -> int:
        res = float('-inf')
        dq = deque() # stores indices of minimum prefix sums
        for j in range(1, n + 1):
            # Add the prefix_sum[j-1] to the window before calculating sum for j
            # This ensures the subarray length is at least 1
            prev_idx = j - 1
            while dq and prefix_sums[dq[-1]] >= prefix_sums[prev_idx]:
                dq.pop()
            dq.append(prev_idx)
            
            if dq[0] < j - k:
                dq.popleft()
            
            res = max(res, prefix_sums[j] - prefix_sums[dq[0]])
        return int(res)

    def get_min_sum() -> int:
        res = float('inf')
        dq = deque() # stores indices of maximum prefix sums
        for j in range(1, n + 1):
            prev_idx = j - 1
            while dq and prefix_sums[dq[-1]] <= prefix_sums[prev_idx]:
                dq.pop()
            dq.append(prev_idx)
            
            if dq[0] < j - k:
                dq.popleft()
                
            res = min(res, prefix_sums[j] - prefix_sums[dq[0]])
        return int(res)

    return [get_max_sum(), get_min_sum()]
