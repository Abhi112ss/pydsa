METADATA = {
    "id": 3741,
    "name": "Minimum Distance Between Three Equal Elements II",
    "slug": "minimum-distance-between-three-equal-elements-ii",
    "category": "Array",
    "aliases": [],
    "tags": ["sliding_window", "hash_map", "two_pointer"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Find the minimum distance between the first and last element of any triplet of equal elements in an array.",
}

def solve(nums: list[int]) -> int:
    """
    Finds the minimum distance between the first and last element of any 
    three equal elements in the given array.

    The distance for a triplet at indices i, j, k (where i < j < k) 
    is defined as k - i.

    Args:
        nums: A list of integers.

    Returns:
        The minimum distance k - i for any three indices i < j < k 
        such that nums[i] == nums[j] == nums[k]. 
        Returns -1 if no such triplet exists.

    Examples:
        >>> solve([1, 2, 1, 2, 1])
        4
        >>> solve([1, 1, 1, 1])
        2
        >>> solve([1, 2, 3, 4])
        -1
    """
    # Map each unique number to a list of its indices in the input array
    index_map: dict[int, list[int]] = {}
    for index, value in enumerate(nums):
        if value not in index_map:
            index_map[value] = []
        index_map[value].append(index)

    min_distance = float('inf')
    found_triplet = False

    # Iterate through the collected indices for each unique number
    for indices in index_map.values():
        # A triplet requires at least 3 occurrences of the same number
        if len(indices) < 3:
            continue
        
        found_triplet = True
        
        # Use a sliding window of size 3 on the list of indices.
        # For any three indices i, j, k (where i < j < k), 
        # the distance is indices[k] - indices[i].
        # To minimize this, we only need to check consecutive triplets.
        for i in range(len(indices) - 2):
            # distance = index of the 3rd occurrence - index of the 1st occurrence
            current_distance = indices[i + 2] - indices[i]
            if current_distance < min_distance:
                min_distance = current_distance

    return int(min_distance) if found_triplet else -1
