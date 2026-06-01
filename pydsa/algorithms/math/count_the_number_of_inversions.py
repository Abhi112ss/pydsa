METADATA = {
    "id": 3193,
    "name": "Count the Number of Inversions",
    "slug": "count-the-number-of-inversions",
    "category": "Hard",
    "aliases": [],
    "tags": ["merge_sort", "fenwick_tree", "segment_tree", "counting"],
    "difficulty": "hard",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(n)",
    "description": "Count the number of pairs (i, j) such that i < j and nums[i] > nums[j].",
}

def solve(nums: list[int]) -> int:
    """
    Counts the number of inversions in an array using a Fenwick Tree (Binary Indexed Tree).
    
    An inversion is a pair (i, j) such that i < j and nums[i] > nums[j].
    To handle large values in nums, we use coordinate compression to map 
    the values to a range [1, N].

    Args:
        nums: A list of integers.

    Returns:
        The total number of inversions in the list.

    Examples:
        >>> solve([5, 4, 3, 2, 1])
        10
        >>> solve([1, 2, 3, 4, 5])
        0
        >>> solve([2, 4, 1, 3, 5])
        3
    """
    n = len(nums)
    if n <= 1:
        return 0

    # Coordinate Compression:
    # Fenwick Tree requires indices to be positive integers.
    # We map the unique values in nums to their rank (1 to M).
    sorted_unique_elements = sorted(list(set(nums)))
    rank_map = {val: i + 1 for i, val in enumerate(sorted_unique_elements)}
    
    # BIT (Binary Indexed Tree) implementation
    # bit[i] stores the frequency of elements with rank i
    bit_size = len(sorted_unique_elements)
    bit = [0] * (bit_size + 1)

    def update(index: int, delta: int) -> None:
        """Adds delta to the frequency of the element at the given rank index."""
        while index <= bit_size:
            bit[index] += delta
            index += index & (-index)

    def query(index: int) -> int:
        """Returns the prefix sum up to the given rank index."""
        s = 0
        while index > 0:
            s += bit[index]
            index -= index & (-index)
        return s

    inversion_count = 0
    
    # Traverse the array from right to left.
    # For each element, count how many elements to its right are strictly smaller.
    # Alternatively, traverse left to right and count how many elements seen 
    # so far are strictly greater than the current element.
    for i in range(n):
        current_rank = rank_map[nums[i]]
        
        # Number of elements already seen that are greater than current_rank
        # is (total elements seen so far) - (elements <= current_rank)
        elements_seen_so_far = i
        elements_less_than_or_equal = query(current_rank)
        
        inversion_count += (elements_seen_so_far - elements_less_than_or_equal)
        
        # Add the current element to the BIT
        update(current_rank, 1)

    return inversion_count
