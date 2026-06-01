METADATA = {
    "id": 421,
    "name": "Maximum XOR of Two Numbers in an Array",
    "slug": "maximum-xor-of-two-numbers-in-an-array",
    "category": "Bit Manipulation",
    "aliases": [],
    "tags": ["trie", "bit_manipulation", "greedy"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Find the maximum result of XORing two numbers in an integer array using a Trie-based greedy approach.",
}

class TrieNode:
    """A node in the prefix tree representing bits."""
    def __init__(self) -> None:
        self.children: dict[int, TrieNode] = {}

class Solution:
    def findMaximumXOR(self, nums: list[int]) -> int:
        """
        Finds the maximum XOR value possible from any two numbers in the input array.

        Args:
            nums: A list of non-negative integers.

        Returns:
            The maximum XOR value found.

        Examples:
            >>> Solution().findMaximumXOR([3, 10, 5, 25, 2, 8])
            28
            >>> Solution().findMaximumXOR([14, 70, 5, 8, 19])
            12
        """
        if not nums:
            return 0

        root = TrieNode()
        # Determine the maximum bit length needed based on the largest number
        max_num = max(nums)
        L = max_num.bit_length()

        # Build the Trie by inserting the binary representation of each number
        for num in nums:
            current_node = root
            for i in range(L - 1, -1, -1):
                bit = (num >> i) & 1
                if bit not in current_node.children:
                    current_node.children[bit] = TrieNode()
                current_node = current_node.children[bit]

        max_xor = 0
        for num in nums:
            current_node = root
            current_xor = 0
            # For each number, try to traverse the Trie by picking the opposite bit
            for i in range(L - 1, -1, -1):
                bit = (num >> i) & 1
                toggled_bit = 1 - bit
                
                # If the opposite bit exists, we take it to maximize the XOR at this position
                if toggled_bit in current_node.children:
                    current_xor |= (1 << i)
                    current_node = current_node.children[toggled_bit]
                else:
                    # Otherwise, we must follow the same bit
                    current_node = current_node.children[bit]
            
            max_xor = max(max_xor, current_xor)

        return max_xor

def solve(nums: list[int]) -> int:
    """Helper function to call the solution."""
    return Solution().findMaximumXOR(nums)
