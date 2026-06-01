METADATA = {
    "id": 1803,
    "name": "Count Pairs With XOR in a Range",
    "slug": "count-pairs-with-xor-in-a-range",
    "category": "Bit Manipulation",
    "aliases": [],
    "tags": ["trie", "bit_manipulation"],
    "difficulty": "hard",
    "time_complexity": "O(n * log(max_val))",
    "space_complexity": "O(n * log(max_val))",
    "description": "Count the number of pairs (i, j) such that 0 <= i < j < n and lower <= nums[i] ^ nums[j] <= upper.",
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

    def count_less_than(self, num: int, limit: int) -> int:
        """
        Counts how many numbers currently in the Trie, when XORed with 'num',
        result in a value strictly less than 'limit'.
        """
        current = self.root
        count = 0
        for i in range(self.max_bits, -1, -1):
            if not current:
                break
            
            bit_num = (num >> i) & 1
            bit_limit = (limit >> i) & 1

            if bit_limit == 1:
                # If the limit bit is 1, then if we choose the path that makes 
                # the XOR bit 0, all numbers in that subtree will be < limit.
                # The path that makes XOR bit 0 is the same as bit_num.
                if bit_num in current.children:
                    count += current.children[bit_num].count
                
                # Then we must move to the path that makes the XOR bit 1 
                # to continue checking lower bits.
                current = current.children.get(1 - bit_num)
            else:
                # If the limit bit is 0, we MUST choose the path that makes 
                # the XOR bit 0 to stay potentially < limit.
                current = current.children.get(bit_num)
        
        return count

def solve(nums: list[int], lower: int, upper: int) -> int:
    """
    Counts the number of pairs (i, j) such that lower <= nums[i] ^ nums[j] <= upper.

    Args:
        nums: A list of integers.
        lower: The lower bound of the XOR range (inclusive).
        upper: The upper bound of the XOR range (inclusive).

    Returns:
        The total count of pairs satisfying the condition.

    Examples:
        >>> solve([1, 4, 2, 7], 2, 6)
        1
        >>> solve([1, 2, 3, 4, 5], 1, 2)
        2
    """
    # Determine the maximum number of bits needed based on the largest value
    # or the constraints (usually 20 bits for 10^6).
    max_val = max(max(nums), upper)
    max_bits = max_val.bit_length()

    trie = BinaryTrie(max_bits)
    total_pairs = 0

    for num in nums:
        # The number of pairs (i, j) where lower <= nums[i] ^ nums[j] <= upper
        # is equivalent to: (count where XOR < upper + 1) - (count where XOR < lower)
        # However, we process elements one by one to ensure i < j.
        # We calculate count(XOR < upper + 1) - count(XOR < lower) for the current num
        # against all elements already inserted in the Trie.
        
        count_upper = trie.count_less_than(num, upper + 1)
        count_lower = trie.count_less_than(num, lower)
        
        total_pairs += (count_upper - count_lower)
        
        # Insert current number into Trie for future comparisons
        trie.insert(num)

    return total_pairs
