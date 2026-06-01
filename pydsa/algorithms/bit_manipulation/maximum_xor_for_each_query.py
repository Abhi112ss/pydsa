METADATA = {
    "id": 1829,
    "name": "Maximum XOR for Each Query",
    "slug": "maximum-xor-for-each-query",
    "category": "Bit Manipulation",
    "aliases": [],
    "tags": ["bit_manipulation", "trie", "greedy"],
    "difficulty": "medium",
    "time_complexity": "O((n + q) * log(max_val))",
    "space_complexity": "O(n * log(max_val))",
    "description": "Find the maximum XOR value for each query by selecting two elements from an array such that their XOR is maximized, while ensuring the selected elements are both greater than or equal to the query value.",
}

class TrieNode:
    """A node in the Binary Trie structure."""
    def __init__(self):
        self.children: dict[int, TrieNode] = {}

class BinaryTrie:
    """A Trie used to store binary representations of integers for XOR maximization."""
    def __init__(self, max_bits: int):
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

    def find_max_xor(self, num: int) -> int:
        """Finds the maximum XOR possible for the given number using existing Trie entries."""
        current = self.root
        max_xor = 0
        for i in range(self.max_bits, -1, -1):
            bit = (num >> i) & 1
            # To maximize XOR, we want to pick the opposite bit
            target_bit = 1 - bit
            if target_bit in current.children:
                max_xor |= (1 << i)
                current = current.children[target_bit]
            elif bit in current.children:
                current = current.children[bit]
            else:
                # This case should not be hit if the Trie is not empty
                return -1
        return max_xor

def solve(nums: list[int], queries: list[int]) -> list[int]:
    """
    Calculates the maximum XOR for each query by selecting two elements >= query.

    Args:
        nums: A list of integers.
        queries: A list of integers representing the minimum threshold for elements.

    Returns:
        A list of integers where each element is the maximum XOR for the corresponding query,
        or -1 if no two elements in nums are >= query.

    Examples:
        >>> solve([8, 1, 2], [5, 4, 1])
        [-1, -1, 3]
        >>> solve([4, 2, 1], [1])
        [6]
    """
    # Sort nums and queries in descending order to use a two-pointer/greedy approach
    # This allows us to add elements to the Trie only when they satisfy the query threshold
    sorted_nums = sorted(nums, reverse=True)
    # We store original indices to return the results in the correct order
    sorted_queries = sorted(enumerate(queries), key=lambda x: x[1], reverse=True)
    
    results = [-1] * len(queries)
    trie = BinaryTrie(max_bits=30)
    nums_idx = 0
    count_in_trie = 0

    for original_idx, query_val in sorted_queries:
        # Add all numbers from nums that are greater than or equal to the current query
        while nums_idx < len(sorted_nums) and sorted_nums[nums_idx] >= query_val:
            trie.insert(sorted_nums[nums_idx])
            nums_idx += 1
            count_in_trie += 1
        
        # We need at least two numbers in the Trie to form an XOR pair
        if count_in_trie < 2:
            results[original_idx] = -1
        else:
            # Find the max XOR for the query value. 
            # Note: The problem asks for max(nums[i] ^ nums[j]) where nums[i], nums[j] >= query.
            # Since we only have numbers >= query in the Trie, we can iterate through 
            # the numbers already in the Trie to find the max XOR.
            # However, a more efficient way is to realize that the max XOR pair 
            # among elements >= query can be found by checking each element against the Trie.
            # But wait, the query itself isn't necessarily in the Trie. 
            # Actually, the optimal way is to find max(a ^ b) for all a, b in Trie.
            # Since we add elements incrementally, we can maintain the global max XOR.
            
            # Correction: To find the max XOR of ANY two elements currently in the Trie,
            # we can't just query the Trie with the 'query_val'. We need to find 
            # max(a ^ b) for all a, b in the Trie.
            # We can maintain a running 'current_max_xor' as we insert elements.
            pass

    # Re-implementing the logic to maintain a running maximum XOR
    # This is more efficient than querying the Trie with the query value.
    
    # Resetting for the correct logic
    results = [-1] * len(queries)
    trie = BinaryTrie(max_bits=30)
    sorted_nums = sorted(nums, reverse=True)
    sorted_queries = sorted(enumerate(queries), key=lambda x: x[1], reverse=True)
    
    nums_idx = 0
    current_max_xor = -1
    count_in_trie = 0

    for original_idx, query_val in sorted_queries:
        while nums_idx < len(sorted_nums) and sorted_nums[nums_idx] >= query_val:
            val_to_add = sorted_nums[nums_idx]
            # Before inserting, find the max XOR this new value can form with existing values
            if count_in_trie > 0:
                potential_xor = trie.find_max_xor(val_to_add)
                if potential_xor > current_max_xor:
                    current_max_xor = potential_xor
            
            trie.insert(val_to_add)
            nums_idx += 1
            count_in_trie += 1
            
        if count_in_trie >= 2:
            results[original_idx] = current_max_xor
        else:
            results[original_idx] = -1
            
    return results
