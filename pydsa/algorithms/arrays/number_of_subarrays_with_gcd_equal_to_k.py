METADATA = {
    "id": 2447,
    "name": "Number of Subarrays With GCD Equal to K",
    "slug": "number-of-subarrays-with-gcd-equal-to-k",
    "category": "Math",
    "aliases": [],
    "tags": ["math", "sliding_window", "hash-table"],
    "difficulty": "medium",
    "time_complexity": "O(n * log(max_val))",
    "space_complexity": "O(log(max_val))",
    "description": "Count the number of subarrays whose greatest common divisor is equal to a given integer k.",
}

import math

def solve(nums: list[int], k: int) -> int:
    """
    Calculates the number of subarrays in nums that have a GCD equal to k.

    Args:
        nums: A list of integers.
        k: The target greatest common divisor.

    Returns:
        The total count of subarrays whose GCD is exactly k.

    Examples:
        >>> solve([4, 4, 4], 4)
        6
        >>> solve([1, 1, 1, 1, 1], 1)
        15
        >>> solve([12, 6, 9], 3)
        3
    """
    total_count = 0
    # current_gcd_counts stores {gcd_value: frequency} for all subarrays 
    # ending at the previous index.
    current_gcd_counts: dict[int, int] = {}

    for num in nums:
        # If num is not divisible by k, no subarray ending here can have GCD k.
        # However, we still need to reset the tracking to avoid carrying over 
        # GCDs that cannot possibly result in k.
        if num % k != 0:
            current_gcd_counts = {}
            continue

        new_gcd_counts: dict[int, int] = {num: 1}

        # For every GCD value achieved by subarrays ending at the previous index,
        # calculate the new GCD including the current number.
        for prev_gcd, count in current_gcd_counts.items():
            new_gcd = math.gcd(prev_gcd, num)
            # We only care about GCDs that are multiples of k.
            # If new_gcd % k != 0, it can never become k by adding more numbers.
            if new_gcd % k == 0:
                new_gcd_counts[new_gcd] = new_gcd_counts.get(new_gcd, 0) + count

        # Add the count of subarrays ending at the current index that have GCD == k.
        total_count += new_gcd_counts.get(k, 0)
        current_gcd_counts = new_gcd_counts

    return total_count
