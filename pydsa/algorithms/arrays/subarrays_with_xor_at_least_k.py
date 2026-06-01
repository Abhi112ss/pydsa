METADATA = {
    "id": 3632,
    "name": "Subarrays with XOR at Least K",
    "slug": "subarrays_with_xor_at_least_k",
    "category": "Bit Manipulation",
    "aliases": [],
    "tags": ["arrays", "bit_manipulation", "trie"],
    "difficulty": "hard",
    "time_complexity": "O(n * log(max_val))",
    "space_complexity": "O(n * log(max_val))",
    "description": "Count the number of subarrays whose XOR sum is greater than or equal to a given threshold K using a Binary Trie.",
}

class BinaryTrieNode:
    """A node in the Binary Trie representing bits of prefix XOR values."""
    def __init__(self):
        self.children: dict[int, BinaryTrieNode] = {}
        self.count: int = 0

class BinaryTrie:
    """A Binary Trie to store prefix XORs and perform range-based XOR queries."""
    def __init__(self, max_bits: int):
        self.root = BinaryTrieNode()
        self.max_bits = max_bits

    def insert(self, value: int) -> None:
        """Inserts a value into the Trie bit by bit."""
        current = self.root
        for i in range(self.max_bits, -1, -1):
            bit = (value >> i) & 1
            if bit not in current.children:
                current.children[bit] = BinaryTrieNode()
            current = current.children[bit]
            current.count += 1

    def count_greater_than_or_equal(self, prefix_xor: int, k: int) -> int:
        """
        Counts how many values 'v' in the Trie satisfy (v ^ prefix_xor) >= k.
        
        Args:
            prefix_xor: The current cumulative XOR sum.
            k: The threshold value.
            
        Returns:
            The number of elements in the trie that, when XORed with prefix_xor, 
            result in a value >= k.
        """
        current = self.root
        total_count = 0
        
        for i in range(self.max_bits, -1, -1):
            if not current:
                break
                
            bit_p = (prefix_xor >> i) & 1
            bit_k = (k >> i) & 1
            
            if bit_k == 0:
                # If the i-th bit of K is 0, then any path that results in a 1 
                # at this bit for (v ^ prefix_xor) will automatically make 
                # the total XOR > K.
                # The bit that results in 1 is (1 - bit_p).
                target_bit_for_one = 1 - bit_p
                if target_bit_for_one in current.children:
                    total_count += current.children[target_bit_for_one].count
                
                # We also need to explore the path where the i-th bit of (v ^ prefix_xor) is 0,
                # because that path might still satisfy the condition in lower bits.
                current = current.children.get(bit_p)
            else:
                # If the i-th bit of K is 1, we MUST take the path that results in a 1
                # at this bit for (v ^ prefix_xor) to have any chance of being >= K.
                target_bit_for_one = 1 - bit_p
                current = current.children.get(target_bit_for_one)
        
        # If we successfully traversed to the leaf, the value itself is equal to K
        if current:
            total_count += current.count
            
        return total_count

def solve(nums: list[int], k: int) -> int:
    """
    Calculates the number of subarrays with XOR sum >= k.

    Args:
        nums: A list of integers.
        k: The threshold value.

    Returns:
        The count of subarrays whose XOR sum is at least k.

    Examples:
        >>> solve([1, 2, 3], 2)
        3
        # Subarrays: [1,2] (XOR 3), [2] (XOR 2), [3] (XOR 3)
    """
    if not nums:
        return 0

    # Determine the number of bits needed based on the maximum possible XOR value.
    # A safe upper bound for 10^9 is 30 bits, but we calculate dynamically.
    max_val = k
    for x in nums:
        max_val |= x
    
    max_bits = max_val.bit_length()
    trie = BinaryTrie(max_bits)
    
    # Initial state: prefix XOR of 0 (empty subarray)
    trie.insert(0)
    
    current_xor = 0
    ans = 0
    
    for num in nums:
        current_xor ^= num
        # Query the Trie for all previous prefix_xors such that (current_xor ^ prev_xor) >= k
        ans += trie.count_greater_than_or_equal(current_xor, k)
        # Add the current prefix XOR to the Trie for future subarrays
        trie.insert(current_xor)
        
    return ans
