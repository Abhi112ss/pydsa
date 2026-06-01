METADATA = {
    "id": 3907,
    "name": "Count Smaller Elements With Opposite Parity",
    "slug": "count-smaller-elements-with-opposite-parity",
    "category": "Array",
    "aliases": [],
    "tags": ["fenwick_tree", "segment_tree", "bit_manipulation", "counting"],
    "difficulty": "medium",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(n)",
    "description": "Count elements smaller than the current element that have a different parity.",
}

class FenwickTree:
    """A standard Fenwick Tree (Binary Indexed Tree) implementation."""
    
    def __init__(self, size: int):
        self.tree = [0] * (size + 1)

    def update(self, index: int, delta: int) -> None:
        """Adds delta to the element at index."""
        while index < len(self.tree):
            self.tree[index] += delta
            index += index & (-index)

    def query(self, index: int) -> int:
        """Returns the prefix sum up to index."""
        total = 0
        while index > 0:
            total += self.tree[index]
            index -= index & (-index)
        return total

def solve(nums: list[int]) -> list[int]:
    """
    Counts how many elements seen so far are smaller than the current element 
    and have a different parity (even vs odd).

    Args:
        nums: A list of integers.

    Returns:
        A list of integers where each element at index i is the count of 
        elements in nums[0...i-1] that are smaller than nums[i] and have 
        a different parity than nums[i].

    Examples:
        >>> solve([1, 2, 3, 4])
        [0, 1, 1, 2]
        >>> solve([5, 3, 2, 1])
        [0, 0, 1, 1]
    """
    if not nums:
        return []

    # Coordinate compression to handle large integer values in Fenwick Tree
    # We map all unique values to a range [1, unique_count]
    sorted_unique_elements = sorted(list(set(nums)))
    rank_map = {val: i + 1 for i, val in enumerate(sorted_unique_elements)}
    max_rank = len(sorted_unique_elements)

    # Two Fenwick trees: one for even numbers, one for odd numbers
    even_bit = FenwickTree(max_rank)
    odd_bit = FenwickTree(max_rank)
    
    results = []

    for num in nums:
        rank = rank_map[num]
        
        # If current number is even, we need to count smaller odd numbers
        # If current number is odd, we need to count smaller even numbers
        if num % 2 == 0:
            # Query the odd BIT for counts of elements with rank < current rank
            count = odd_bit.query(rank - 1)
            even_bit.update(rank, 1)
        else:
            # Query the even BIT for counts of elements with rank < current rank
            count = even_bit.query(rank - 1)
            odd_bit.update(rank, 1)
            
        results.append(count)

    return results
