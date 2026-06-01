METADATA = {
    "id": 3845,
    "name": "Maximum Subarray XOR with Bounded Range",
    "slug": "maximum_subarray_xor_with_bounded_range",
    "category": "Bit Manipulation",
    "aliases": [],
    "tags": ["trie", "bit_manipulation", "prefix_xor"],
    "difficulty": "hard",
    "time_complexity": "O(n * log(max_val))",
    "space_complexity": "O(n * log(max_val))",
    "description": "Find the maximum XOR sum of a contiguous subarray such that the XOR sum falls within a given range [L, R].",
}

class TrieNode:
    """A node in the Binary Trie structure."""
    def __init__(self):
        self.children: dict[int, TrieNode] = {}
        self.count: int = 0

class Trie:
    """A Binary Trie to store prefix XOR values for efficient bitwise queries."""
    def __init__(self, max_bits: int):
        self.root = TrieNode()
        self.max_bits = max_bits

    def insert(self, val: int) -> None:
        """Inserts a value into the Trie."""
        current = self.root
        for i in range(self.max_bits, -1, -1):
            bit = (val >> i) & 1
            if bit not in current.children:
                current.children[bit] = TrieNode()
            current = current.children[bit]
            current.count += 1

    def query_max_less_than_or_equal(self, prefix_xor: int, limit: int) -> int:
        """
        Finds the maximum value 'v' in the Trie such that (prefix_xor ^ v) <= limit.
        Returns -1 if no such value exists.
        """
        # This is a specialized search. We want to find max (prefix_xor ^ v) 
        # subject to (prefix_xor ^ v) <= limit.
        # We traverse the Trie bit by bit.
        
        def dfs(node: TrieNode, bit_idx: int, current_xor: int) -> int:
            if bit_idx < 0:
                return current_xor
            
            res = -1
            p_bit = (prefix_xor >> bit_idx) & 1
            l_bit = (limit >> bit_idx) & 1
            
            # If l_bit is 1, we have two choices for the current bit of (prefix_xor ^ v):
            # 1. Set the bit of (prefix_xor ^ v) to 0. This is always < limit's current bit.
            #    Once we set a bit to 0 where limit has 1, all subsequent bits can be anything.
            #    To maximize the result, we'd want to greedily pick bits to make the XOR sum large.
            #    However, the constraint is on the total XOR sum.
            
            # Let's use a more standard approach: 
            # At each bit, if l_bit == 1:
            #    Option A: bit of (prefix_xor ^ v) is 0. This makes the whole XOR sum < limit.
            #              We then want to find the maximum possible XOR sum from this point.
            #    Option B: bit of (prefix_xor ^ v) is 1. This matches limit's bit.
            #              We must continue checking lower bits.
            # If l_bit == 0:
            #    Option A: bit of (prefix_xor ^ v) must be 0.
            #    Option B: bit of (prefix_xor ^ v) is 1. This is impossible as it would exceed limit.
            
            # To implement "find max XOR sum < limit", we need a helper to find max XOR 
            # in a subtree without constraints.
            return -1 # Placeholder for logic structure

        # Re-evaluating: The problem asks for max(subarray_xor) where L <= subarray_xor <= R.
        # This is equivalent to finding max(subarray_xor) in range [0, R] 
        # and then checking if that result is >= L. 
        # Wait, that's not quite right. We need the maximum value that is actually in [L, R].
        # The correct approach is to find the maximum XOR sum in the Trie that is <= R,
        # and if that value is < L, then no value in [L, R] exists.
        # Actually, the standard "Max XOR in range" is usually solved by finding 
        # the max XOR sum <= R and then checking if it's >= L.
        # But we need to find the maximum value in the set {prefix_xor[i] ^ prefix_xor[j]} 
        # that satisfies L <= val <= R.
        
        return -1

def solve(nums: list[int], L: int, R: int) -> int:
    """
    Finds the maximum subarray XOR sum that lies within the range [L, R].

    Args:
        nums: A list of integers.
        L: The lower bound of the allowed XOR sum.
        R: The upper bound of the allowed XOR sum.

    Returns:
        The maximum subarray XOR sum in [L, R], or -1 if none exists.

    Examples:
        >>> solve([1, 2, 3], 1, 2)
        2
        >>> solve([8, 1, 2, 12, 7, 6], 10, 15)
        15
    """
    n = len(nums)
    prefix_xors = [0] * (n + 1)
    for i in range(n):
        prefix_xors[i + 1] = prefix_xors[i] ^ nums[i]

    # To find max(P[i] ^ P[j]) such that L <= (P[i] ^ P[j]) <= R
    # We can iterate through each P[i] and find the best P[j] in the Trie.
    # The constraint is on the result of the XOR, not the values themselves.
    
    max_bits = max(max(prefix_xors), R)
    if max_bits < 0: max_bits = 0
    max_bits = max_bits.bit_length()

    trie_root = TrieNode()

    def trie_insert(val: int):
        curr = trie_root
        for i in range(max_bits, -1, -1):
            bit = (val >> i) & 1
            if bit not in curr.children:
                curr.children[bit] = TrieNode()
            curr = curr.children[bit]
            curr.count += 1

    def trie_query(p_xor: int, limit: int) -> int:
        """Finds the maximum (p_xor ^ v) such that (p_xor ^ v) <= limit."""
        # We use a recursive approach to explore the Trie.
        # At each bit, we decide whether to follow the path that matches the limit bit
        # or the path that makes the XOR sum strictly less than the limit.
        
        def find_max(node: TrieNode, bit_idx: int, current_xor: int, is_less: bool) -> int:
            if bit_idx < 0:
                return current_xor
            
            p_bit = (p_xor >> bit_idx) & 1
            l_bit = (limit >> bit_idx) & 1
            
            best = -1
            
            # If is_less is True, we are already strictly less than the limit.
            # We just want to maximize the XOR sum greedily.
            if is_less:
                # Try to pick bit that makes (p_bit ^ bit) == 1
                target_bit = 1 - p_bit
                if target_bit in node.children:
                    best = find_max(node.children[target_bit], bit_idx - 1, current_xor | (1 << bit_idx), True)
                elif p_bit in node.children:
                    best = find_max(node.children[p_bit], bit_idx - 1, current_xor, True)
                return best

            # If is_less is False, we are currently matching the limit's prefix.
            # We have two choices for the current bit of the XOR result:
            # 1. Result bit is 0.
            # 2. Result bit is 1.
            
            # Choice 1: Result bit is 0.
            # This is possible if:
            #    a) l_bit is 1 (then 0 < 1, so is_less becomes True)
            #    b) l_bit is 0 (then 0 == 0, so is_less remains False)
            
            # To get result bit 0, we need v_bit == p_bit
            if p_bit in node.children:
                new_is_less = is_less or (0 < l_bit)
                # If l_bit was 0 and we pick 0, we stay on the boundary.
                # If l_bit was 1 and we pick 0, we are now strictly less.
                if l_bit == 1 or 0 < l_bit: # This is just l_bit == 1
                    # If we pick 0 and l_bit is 1, we are now 'less'.
                    # We need to find the max possible XOR from here.
                    # To maximize, we greedily pick bits.
                    res = find_max_greedy(node.children[p_bit], bit_idx - 1, current_xor, True)
                    if res != -1: best = max(best, res)
                elif l_bit == 0:
                    # We pick 0, and l_bit is 0. We stay on the boundary.
                    res = find_max(node.children[p_bit], bit_idx - 1, current_xor, False)
                    if res != -1: best = max(best, res)

            # Choice 2: Result bit is 1.
            # This is possible only if l_bit is 1.
            # To get result bit 1, we need v_bit == 1 - p_bit
            if l_bit == 1:
                target_bit = 1 - p_bit
                if target_bit in node.children:
                    # We pick 1, and l_bit is 1. We stay on the boundary.
                    res = find_max(node.children[target_bit], bit_idx - 1, current_xor | (1 << bit_idx), False)
                    if res != -1: best = max(best, res)
            
            return best

        def find_max_greedy(node: TrieNode, bit_idx: int, current_xor: int, is_less: bool) -> int:
            # Standard max-xor query in a Trie
            curr = node
            for i in range(bit_idx, -1, -1):
                p_bit = (p_xor >> i) & 1
                target = 1 - p_bit
                if target in curr.children:
                    current_xor |= (1 << i)
                    curr = curr.children[target]
                elif p_bit in curr.children:
                    curr = curr.children[p_bit]
                else:
                    return -1
            return current_xor

        # The recursive approach is slightly complex. Let's simplify.
        # We want max(p_xor ^ v) s.t. (p_xor ^ v) <= limit.
        # We can use a simple iterative approach with a stack or recursion.
        
        return find_max(trie_root, max_bits, 0, False)

    # Corrected approach:
    # We need to find max(P[i] ^ P[j]) in [L, R].
    # Since we want the MAXIMUM, we can iterate through all P[i], 
    # and for each, find the largest P[j] in the Trie such that 
    # L <= (P[i] ^ P[j]) <= R.
    
    # However, "find max X in Trie such that L <= (X ^ P) <= R" is still tricky.
    # Let's use the property: max_{val \in [L, R]} (val)
    # We can find the maximum XOR sum <= R. If that value is < L, then no value in [L, R] exists.
    # Wait, that's only true if we are looking for the maximum value in the set.
    # If the set is {5, 15} and range is [10, 20], max is 15.
    # If the set is {5, 15} and range is [6, 14], max is -1.
    # So the logic is: find the maximum value in the set that is <= R. 
    # If that value is >= L, then it's our answer.
    
    # But there's a catch: the maximum value <= R might be 15, but if 15 is not in [L, R], 
    # we need to check if there's another value in [L, R].
    # Actually, the "maximum value <= R" is exactly what we want, 
    # provided we check if it's >= L.
    
    # Let's refine:
    # For each prefix_xor[i], we want to find max(prefix_xor[i] ^ prefix_xor[j]) 
    # such that prefix_xor[i] ^ prefix_xor[j] <= R.
    # Let this be `best_for_i`.
    # The global answer is max(best_for_i) for all i, but we must ensure best_for_i >= L.
    
    # Wait, if best_for_i is 15 and R is 20, but L is 16, then 15 is not a valid answer.
    # We need the largest value in the set that is <= R AND >= L.
    # This is equivalent to: find the largest value in the set that is <= R, 
    # and if that value is < L, then no value in [L, R] exists for this i.
    
    # Let's implement `find_max_xor_le(p_xor, limit)`:
    # This function returns the maximum (p_xor ^ v) such that (p_xor ^ v) <= limit.

    def find_max_xor_le(p_xor: int, limit: int) -> int:
        # Iterative approach to find max (p_xor ^ v) <= limit
        # We use a stack to simulate DFS to avoid recursion depth issues
        # Stack stores (node, bit_idx, current_xor, is_less)
        stack = [(trie_root, max_bits, 0, False)]
        max_found = -1
        
        while stack:
            node, bit_idx, current_xor, is_less = stack.pop()
            
            if bit_idx < 0:
                if current_xor >= 0: # current_xor is always >= 0 here
                    max_found = max(max_found, current_xor)
                continue
            
            if is_less:
                # Greedily pick the best bit
                p_bit = (p_xor >> bit_idx) & 1
                target = 1 - p_bit
                if target in node.children:
                    stack.append((node.children[target], bit_idx - 1, current_xor | (1 << bit_idx), True))
                elif p_bit in node.children:
                    stack.append((node.children[p_bit], bit_idx - 1, current_xor, True))
                else:
                    # This case shouldn't happen if the Trie is built correctly
                    max_found = max(max_found, current_xor)
            else:
                p_bit = (p_xor >> bit_idx) & 1
                l_bit = (limit >> bit_idx) & 1
                
                if l_bit == 1:
                    # Option 1: Result bit is 0. This makes is_less = True.
                    # To get result bit 0, we need v_bit = p_bit.
                    if p_bit in node.children:
                        stack.append((node.children[p_bit], bit_idx - 1, current_xor, True))
                    
                    # Option 2: Result bit is 1. This keeps is_less = False.
                    # To get result bit 1, we need v_bit = 1 - p_bit.
                    if (1 - p_bit) in node.children:
                        stack.append((node.children[1 - p_bit], bit_idx - 1, current_xor | (1 << bit_idx), False))
                else:
                    # l_bit == 0. Result bit MUST be 0 to stay <= limit.
                    # To get result bit 0, we need v_bit = p_bit.
                    if p_bit in node.children:
                        stack.append((node.children[p_bit], bit_idx - 1, current_xor, False))
        
        return max_found

    ans = -1
    # Insert