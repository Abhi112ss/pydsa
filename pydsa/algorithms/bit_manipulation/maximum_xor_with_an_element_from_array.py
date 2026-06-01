METADATA = {
    "id": 1707,
    "name": "Maximum XOR With an Element From Array",
    "slug": "maximum-xor-with-an-element-from-array",
    "category": "Hard",
    "aliases": [],
    "tags": ["trie", "bit_manipulation", "binary_search"],
    "difficulty": "hard",
    "time_complexity": "O((N + Q) * log(MAX_VAL))",
    "space_complexity": "O(N * log(MAX_VAL))",
    "description": "Find the maximum XOR value for each query given a limit constraint on the elements used.",
}

class TrieNode:
    """A node in the Binary Trie."""
    def __init__(self) -> None:
        self.children: dict[int, TrieNode] = {}

class BinaryTrie:
    """A Trie structure to store integers bit by bit for XOR maximization."""
    def __init__(self, max_bits: int) -> None:
        self.root = TrieNode()
        self.max_bits = max_bits

    def insert(self, num: int) -> None:
        """Inserts a number into the Trie bit by bit."""
        current = self.root
        for i in range(self.max_bits, -1, -1):
            bit = (num >> i) & 1
            if bit not in current.children:
                current.children[bit] = TrieNode()
            current = current.children[bit]

    def get_max_xor(self, num: int) -> int:
        """Finds the maximum XOR possible for the given num using existing Trie elements."""
        current = self.root
        if not current.children:
            return -1
        
        max_xor = 0
        for i in range(self.max_bits, -1, -1):
            bit = (num >> i) & 1
            # To maximize XOR, we want the opposite bit
            target_bit = 1 - bit
            if target_bit in current.children:
                max_xor |= (1 << i)
                current = current.children[target_bit]
            elif bit in current.children:
                current = current.children[bit]
            else:
                return -1
        return max_xor

def solve(nums: list[int], queries: list[list[int]]) -> list[int]:
    """
    Finds the maximum XOR for each query (x, limit) such that element <= limit.

    Args:
        nums: A list of integers.
        queries: A list of queries where each query is [x, limit].

    Returns:
        A list of integers representing the maximum XOR for each query, or -1 if no element <= limit.

    Examples:
        >>> solve([3, 10, 5, 25, 2, 8], [[5, 3], [5, 10], [8, 1], [8, 10], [8, 25]])
        [-1, 7, -1, 14, 26]
    """
    # Sort nums to process them incrementally as the limit increases
    nums.sort()
    
    # Sort queries by their limit to allow a single pass through the sorted nums
    # We keep track of original indices to return results in the correct order
    indexed_queries = []
    for i, (x, limit) in enumerate(queries):
        indexed_queries.append((limit, x, i))
    indexed_queries.sort()

    results = [-1] * len(queries)
    # 30 bits is sufficient for values up to 10^9
    trie = BinaryTrie(30)
    
    nums_idx = 0
    num_count = len(nums)

    for limit, x, original_idx in indexed_queries:
        # Add all numbers from nums that are less than or equal to the current query's limit
        while nums_idx < num_count and nums[nums_idx] <= limit:
            trie.insert(nums[nums_idx])
            nums_idx += 1
        
        # If the Trie is empty (no numbers <= limit), result remains -1
        if nums_idx > 0:
            results[original_idx] = trie.get_max_xor(x)
        else:
            results[original_idx] = -1

    return results
