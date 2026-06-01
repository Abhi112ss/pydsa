METADATA = {
    "id": 3589,
    "name": "Count Prime-Gap Balanced Subarrays",
    "slug": "count-prime-gap-balanced-subarrays",
    "category": "Arrays",
    "aliases": [],
    "tags": ["arrays", "prefix_sum", "math"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Count the number of subarrays where the number of prime gaps equals a target value using prefix sums.",
}

def solve(nums: list[int], target_gap_count: int) -> int:
    """
    Counts the number of subarrays where the count of prime gaps equals target_gap_count.
    A prime gap is defined as the difference between two consecutive prime numbers.
    In the context of this problem, we identify indices i such that nums[i] and nums[i+1]
    are both prime, and we track the occurrences of these gaps.

    Args:
        nums: A list of integers.
        target_gap_count: The required number of prime gaps in a subarray.

    Returns:
        The total number of subarrays satisfying the condition.

    Examples:
        >>> solve([2, 3, 5, 7, 11], 2)
        3
        # Subarrays: [2, 3, 5], [3, 5, 7], [5, 7, 11] (each has 2 gaps)
    """
    n = len(nums)
    if n < 2:
        return 1 if target_gap_count == 0 else 0

    def is_prime(num: int) -> bool:
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    # Pre-calculate primality for all elements
    # Note: In a real production environment with large numbers, 
    # a Sieve of Eratosthenes would be used if the range is known.
    is_prime_arr = [is_prime(x) for x in nums]

    # Identify "gap" positions. 
    # A gap exists at index i if nums[i] and nums[i+1] are both prime.
    # We represent this as a binary array where 1 means a gap starts at i.
    gaps = [0] * (n - 1)
    for i in range(n - 1):
        if is_prime_arr[i] and is_prime_arr[i+1]:
            gaps[i] = 1

    # Use prefix sums to count gaps in any range [i, j].
    # The number of gaps in subarray nums[i...j] is the sum of gaps[k] 
    # for k from i to j-1.
    prefix_sum = [0] * n
    current_sum = 0
    for i in range(n - 1):
        current_sum += gaps[i]
        prefix_sum[i + 1] = current_sum

    # To find subarrays where prefix_sum[j] - prefix_sum[i] == target_gap_count,
    # we use a hash map to store the frequency of prefix sums encountered.
    # This is a standard technique for subarray sum problems.
    count_map = {0: 1}
    total_subarrays = 0
    
    # We iterate through the prefix sums. 
    # Note: prefix_sum[j] represents gaps in nums[0...j].
    # The number of gaps in nums[i...j] is prefix_sum[j] - prefix_sum[i].
    # However, since gaps are defined between elements, a subarray of length L
    # has L-1 potential gap positions.
    for j in range(1, n):
        # We want prefix_sum[j] - prefix_sum[i] == target_gap_count
        # where i is the starting index of the subarray.
        # The gaps in nums[i...j] are gaps[i] + ... + gaps[j-1].
        # This is exactly prefix_sum[j] - prefix_sum[i].
        needed = prefix_sum[j] - target_gap_count
        if needed in count_map:
            total_subarrays += count_map[needed]
        
        # Update map with the current prefix sum
        # We use prefix_sum[j] to represent the state after considering element j
        count_map[prefix_sum[j]] = count_map.get(prefix_sum[j], 0) + 1

    # Special case: if target_gap_count is 0, the logic above counts 
    # subarrays with 0 gaps. However, the prefix sum logic for 0-length 
    # gaps needs to be careful about the single-element subarrays.
    # The current logic handles subarrays of length >= 2.
    # Subarrays of length 1 always have 0 gaps.
    if target_gap_count == 0:
        total_subarrays += n

    return total_subarrays
