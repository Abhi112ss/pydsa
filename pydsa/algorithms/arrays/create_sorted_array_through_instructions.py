METADATA = {
    "id": 1649,
    "name": "Create Sorted Array through Instructions",
    "slug": "create-sorted-array-through-instructions",
    "category": "Hard",
    "aliases": [],
    "tags": ["binary_indexed_tree", "fenwick_tree", "binary_search"],
    "difficulty": "hard",
    "time_complexity": "O(n log M) where M is the maximum value in instructions",
    "space_complexity": "O(M)",
    "description": "Calculate the minimum cost to create a sorted array by summing the minimum of elements strictly less than and strictly greater than the current element being inserted.",
}

class FenwickTree:
    """A Fenwick Tree (Binary Indexed Tree) implementation for prefix sums."""

    def __init__(self, size: int):
        self.tree = [0] * (size + 1)
        self.size = size

    def update(self, index: int, delta: int) -> None:
        """Adds delta to the element at the given index."""
        while index <= self.size:
            self.tree[index] += delta
            index += index & (-index)

    def query(self, index: int) -> int:
        """Returns the prefix sum from 1 to index."""
        sum_val = 0
        while index > 0:
            sum_val += self.tree[index]
            index -= index & (-index)
        return sum_val

def solve(instructions: list[int]) -> int:
    """
    Calculates the minimum cost to create a sorted array using a Fenwick Tree.

    The cost for each insertion is defined as min(count(x < current), count(x > current)).
    We use a Fenwick Tree to maintain the frequency of elements seen so far to 
    perform these counts in logarithmic time.

    Args:
        instructions: A list of integers representing the sequence of insertions.

    Returns:
        The total minimum cost modulo 10^9 + 7.

    Examples:
        >>> solve([1, 3, 3, 2, 4, 3])
        4
        >>> solve([1, 2, 3, 4, 2, 1, 2])
        2
    """
    if not instructions:
        return 0

    MOD = 1_000_000_007
    max_val = max(instructions)
    bit = FenwickTree(max_val)
    total_cost = 0
    elements_seen = 0

    for x in instructions:
        # count_less is the number of elements strictly smaller than x
        # query(x-1) gives sum of frequencies from index 1 to x-1
        count_less = bit.query(x - 1)
        
        # count_greater is the number of elements strictly larger than x
        # Total elements seen so far minus elements <= x
        count_greater = elements_seen - bit.query(x)
        
        # The cost for this step is the minimum of the two counts
        total_cost = (total_cost + min(count_less, count_greater)) % MOD
        
        # Update the Fenwick Tree with the current element's frequency
        bit.update(x, 1)
        elements_seen += 1

    return total_cost
