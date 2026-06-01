METADATA = {
    "id": 2964,
    "name": "Number of Divisible Triplet Sums",
    "slug": "number_of_divisible_triplet_sums",
    "category": "Math",
    "aliases": [],
    "tags": ["math", "hash_map", "prefix_sum"],
    "difficulty": "medium",
    "time_complexity": "O(n + k^2)",
    "space_complexity": "O(k)",
    "description": "Count the number of triplets whose sum is divisible by k using remainder frequencies.",
}

def solve(nums: list[int], k: int) -> int:
    """
    Calculates the number of triplets (i, j, l) such that 0 <= i < j < l < n 
    and (nums[i] + nums[j] + nums[l]) % k == 0.

    Args:
        nums: A list of integers.
        k: The divisor.

    Returns:
        The total count of triplets whose sum is divisible by k.

    Examples:
        >>> solve([3, 3, 3, 3], 3)
        4
        >>> solve([1, 2, 3, 4, 5], 3)
        4
    """
    # Count the frequency of each remainder when elements are divided by k
    remainder_counts: dict[int, int] = {}
    for num in nums:
        rem = num % k
        remainder_counts[rem] = remainder_counts.get(rem, 0) + 1

    # We extract the counts into a list for easier indexing, 
    # ensuring all possible remainders [0, k-1] are represented.
    counts = [remainder_counts.get(i, 0) for i in range(k)]
    total_triplets = 0

    # Case 1: All three elements have the same remainder 'r'
    # (r + r + r) % k == 0  =>  3r % k == 0
    for r in range(k):
        if (3 * r) % k == 0:
            n_r = counts[r]
            if n_r >= 3:
                # Combination nCr: n! / (r!(n-r)!) -> n*(n-1)*(n-2)/6
                total_triplets += (n_r * (n_r - 1) * (n_r - 2)) // 6

    # Case 2: Two elements have the same remainder 'r1', and one has 'r2'
    # (2*r1 + r2) % k == 0, where r1 != r2
    for r1 in range(k):
        for r2 in range(k):
            if r1 != r2 and (2 * r1 + r2) % k == 0:
                n1 = counts[r1]
                n2 = counts[r2]
                if n1 >= 2:
                    # Combination: (n1 choose 2) * n2
                    total_triplets += (n1 * (n1 - 1) // 2) * n2

    # Case 3: All three elements have different remainders 'r1', 'r2', 'r3'
    # (r1 + r2 + r3) % k == 0, where r1 < r2 < r3
    for r1 in range(k):
        for r2 in range(r1 + 1, k):
            # Calculate required r3 such that (r1 + r2 + r3) % k == 0
            # r3 % k = (-r1 - r2) % k
            r3 = (k - (r1 + r2) % k) % k
            
            # To avoid double counting and ensure r1 < r2 < r3, 
            # we only process if r3 is greater than r2
            if r3 > r2:
                n1 = counts[r1]
                n2 = counts[r2]
                n3 = counts[r3]
                total_triplets += n1 * n2 * n3

    return total_triplets
