METADATA = {
    "id": 1534,
    "name": "Count Good Triplets",
    "slug": "count-good-triplets",
    "category": "Array",
    "aliases": [],
    "tags": ["brute_force", "array"],
    "difficulty": "medium",
    "time_complexity": "O(n^3)",
    "space_complexity": "O(1)",
    "description": "Count the number of triplets (i, j, k) such that 0 <= i < j < k < arr.length and |arr[i] - arr[j]| < arr[k], |arr[j] - arr[k]| < arr[i], and |arr[k] - arr[i]| < arr[j].",
}

def solve(arr: list[int]) -> int:
    """
    Counts the number of 'good' triplets in the given array.
    
    A triplet (i, j, k) is good if:
    0 <= i < j < k < len(arr)
    |arr[i] - arr[j]| < arr[k]
    |arr[j] - arr[k]| < arr[i]
    |arr[k] - arr[i]| < arr[j]

    Args:
        arr: A list of integers.

    Returns:
        The total count of good triplets.

    Examples:
        >>> solve([1, 1, 1, 2, 3])
        4
        >>> solve([1, 2, 3, 4, 5])
        0
    """
    n = len(arr)
    good_triplet_count = 0

    # Iterate through all possible combinations of i, j, k where i < j < k
    for i in range(n):
        for j in range(i + 1, n):
            # Optimization: Pre-calculate the first condition to prune the search
            diff_ij = abs(arr[i] - arr[j])
            
            for k in range(j + 1, n):
                # Check all three conditions required for a 'good' triplet
                # 1. |arr[i] - arr[j]| < arr[k]
                # 2. |arr[j] - arr[k]| < arr[i]
                # 3. |arr[k] - arr[i]| < arr[j]
                if (diff_ij < arr[k] and 
                    abs(arr[j] - arr[k]) < arr[i] and 
                    abs(arr[k] - arr[i]) < arr[j]):
                    good_triplet_count += 1

    return good_triplet_count
