METADATA = {
    "id": 2935,
    "name": "Maximum Strong Pair XOR II",
    "slug": "maximum-strong-pair-xor-ii",
    "category": "Bit Manipulation",
    "aliases": [],
    "tags": ["trie", "sliding_window", "bit_manipulation"],
    "difficulty": "hard",
    "time_complexity": "O(n * log(max_val))",
    "space_complexity": "O(n * log(max_val))",
    "description": "Find the maximum XOR value of a pair (x, y) such that |x - y| <= min(x, y).",
}

class TrieNode:
    """A node in the Binary Trie."""
    def __init__(self):
        self.children: dict[int, TrieNode] = {}
        self.count: int = 0

class BinaryTrie:
    """A Trie implementation for bitwise operations."""
    def __init__(self, max_bits: int):
        self.root = TrieNode()
        self.max_bits = max_bits

    def insert(self, num: int) -> None:
        """Inserts a number into the Trie."""
        current = self.root
        for i in range(self.max_bits, -1, -1):
            bit = (num >> i) & 1
            if bit not in current.children:
                current.children[bit] = TrieNode()
            current = current.children[bit]
            current.count += 1

    def remove(self, num: int) -> None:
        """Removes a number from the Trie by decrementing counts."""
        current = self.root
        for i in range(self.max_bits, -1, -1):
            bit = (num >> i) & 1
            current = current.children[bit]
            current.count -= 1

    def query_max_xor(self, num: int) -> int:
        """Finds the maximum XOR possible for the given number in the Trie."""
        current = self.root
        max_xor = 0
        for i in range(self.max_bits, -1, -1):
            bit = (num >> i) & 1
            desired_bit = 1 - bit
            # Check if the desired bit exists and has at least one active number
            if desired_bit in current.children and current.children[desired_bit].count > 0:
                max_xor |= (1 << i)
                current = current.children[desired_bit]
            elif bit in current.children and current.children[bit].count > 0:
                current = current.children[bit]
            else:
                # This case should not be reached if Trie is managed correctly
                return 0
        return max_xor

def solve(nums: list[int]) -> int:
    """
    Calculates the maximum XOR of a strong pair (x, y) where |x - y| <= min(x, y).
    
    The condition |x - y| <= min(x, y) is equivalent to saying that for a sorted 
    array, if we pick x and y (where x <= y), then y - x <= x, which simplifies 
    to y <= 2x.

    Args:
        nums: A list of integers.

    Returns:
        The maximum XOR value found among all valid strong pairs.

    Examples:
        >>> solve([1, 4, 2, 7])
        3
        >>> solve([10, 15, 20, 25])
        13
    """
    if not nums:
        return 0

    # Sort to use sliding window: for a fixed y, we need x such that x >= y/2
    nums.sort()
    
    # Determine the number of bits needed based on the maximum value
    max_val = nums[-1]
    max_bits = max_val.bit_length()
    
    trie = BinaryTrie(max_bits)
    max_xor_result = 0
    left_pointer = 0

    # Iterate through nums as the 'y' in the pair (x, y)
    for right_pointer in range(len(nums)):
        current_y = nums[right_pointer]
        
        # Maintain sliding window: remove elements that violate y <= 2x
        # i.e., remove elements where x < y/2 (or 2x < y)
        while left_pointer < right_pointer and 2 * nums[left_pointer] < current_y:
            trie.remove(nums[left_pointer])
            left_pointer += 1
        
        # Query the Trie for the best x in the current valid window [left, right-1]
        if left_pointer < right_pointer:
            max_xor_result = max(max_xor_result, trie.query_max_xor(current_y))
        
        # Add the current number to the Trie for future queries
        trie.insert(current_y)

    return max_xor_result
