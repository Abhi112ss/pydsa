METADATA = {
    "id": 3849,
    "name": "Maximum Bitwise XOR After Rearrangement",
    "slug": "maximum-bitwise-xor-after-rearrangement",
    "category": "Greedy",
    "aliases": [],
    "tags": ["greedy", "bit_manipulation", "trie"],
    "difficulty": "medium",
    "time_complexity": "O(n * log(max_val))",
    "space_complexity": "O(n * log(max_val))",
    "description": "Find the maximum possible bitwise XOR sum of a rearranged array by greedily selecting elements using a Trie.",
}

def solve(nums: list[int]) -> int:
    """
    Args:
        nums: A list of integers.

    Returns:
        The maximum bitwise XOR sum achievable by rearranging the array.
    """
    if not nums:
        return 0

    max_val = max(nums)
    bit_length = max_val.bit_length()
    if bit_length == 0:
        bit_length = 1

    trie = {}

    def insert(val: int) -> None:
        current_node = trie
        for i in range(bit_length - 1, -1, -1):
            bit = (val >> i) & 1
            if bit not in current_node:
                current_node[bit] = {}
            current_node = current_node[bit]
        current_node["value"] = val

    def find_best_match(val: int) -> int:
        current_node = trie
        for i in range(bit_length - 1, -1, -1):
            bit = (val >> i) & 1
            desired_bit = 1 - bit
            if desired_bit in current_node:
                current_node = current_node[desired_bit]
            else:
                current_node = current_node[bit]
        return current_node["value"]

    for num in nums:
        insert(num)

    used = [False] * len(nums)
    num_to_idx = {val: i for i, val in enumerate(nums)}
    
    # Note: The problem logic for "rearrangement" to maximize XOR sum 
    # usually implies pairing elements (a_i, a_j) such that sum(a_i ^ a_j) is max.
    # However, standard LeetCode interpretation for this specific prompt 
    # involves a greedy matching approach.
    
    # Since the prompt asks for a greedy approach with a Trie:
    # We treat this as finding pairs.
    
    total_xor_sum = 0
    visited = [False] * len(nums)
    
    # To handle duplicates correctly in a Trie-based greedy approach, 
    # we use a frequency map or a Trie that tracks counts.
    
    count_trie = {}

    def insert_with_count(val: int) -> None:
        current_node = count_trie
        for i in range(bit_length - 1, -1, -1):
            bit = (val >> i) & 1
            if bit not in current_node:
                current_node[bit] = {"count": 0}
            current_node = current_node[bit]
            current_node["count"] += 1
        current_node["val"] = val
        current_node["count"] += 1

    # Re-implementing with frequency tracking to allow "removal"
    trie_nodes = [{"children": {}, "count": 0}]

    def trie_insert(val: int) -> None:
        node_idx = 0
        trie_nodes[node_idx]["count"] += 1
        for i in range(bit_length - 1, -1, -1):
            bit = (val >> i) & 1
            if bit not in trie_nodes[node_idx]["children"]:
                trie_nodes[node_idx]["children"][bit] = len(trie_nodes)
                trie_nodes.append({"children": {}, "count": 0})
            node_idx = trie_nodes[node_idx]["children"][bit]
            trie_nodes[node_idx]["count"] += 1

    def trie_remove(val: int) -> None:
        node_idx = 0
        trie_nodes[node_idx]["count"] -= 1
        for i in range(bit_length - 1, -1, -1):
            bit = (val >> i) & 1
            node_idx = trie_nodes[node_idx]["children"][bit]
            trie_nodes[node_idx]["count"] -= 1

    def trie_find_max_xor(val: int) -> int:
        node_idx = 0
        for i in range(bit_length - 1, -1, -1):
            bit = (val >> i) & 1
            desired_bit = 1 - bit
            if desired_bit in trie_nodes[node_idx]["children"]:
                next_idx = trie_nodes[node_idx]["children"][desired_bit]
                if trie_nodes[next_idx]["count"] > 0:
                    node_idx = next_idx
                    continue
            node_idx = trie_nodes[node_idx]["children"][bit]
        
        # Reconstruct value from path
        res_val = 0
        temp_idx = 0
        # This is inefficient, let's store value at leaf
        return None # placeholder

    # Corrected Greedy Approach:
    # 1. Build Trie with counts.
    # 2. For each number, if not used, find its best XOR partner in Trie.
    # 3. Add XOR to sum, mark both as used (decrement counts).

    trie_nodes = [{"children": {}, "count": 0, "val": None}]

    def insert_v2(val: int) -> None:
        curr = 0
        trie_nodes[curr]["count"] += 1
        for i in range(bit_length - 1, -1, -1):
            bit = (val >> i) & 1
            if bit not in trie_nodes[curr]["children"]:
                trie_nodes[curr]["children"][bit] = len(trie_nodes)
                trie_nodes.append({"children": {}, "count": 0, "val": None})
            curr = trie_nodes[curr]["children"][bit]
            trie_nodes[curr]["count"] += 1
        trie_nodes[curr]["val"] = val

    def remove_v2(val: int) -> None:
        curr = 0
        trie_nodes[curr]["count"] -= 1
        for i in range(bit_length - 1, -1, -1):
            bit = (val >> i) & 1
            curr = trie_nodes[curr]["children"][bit]
            trie_nodes[curr]["count"] -= 1

    def query_v2(val: int) -> int:
        curr = 0
        for i in range(bit_length - 1, -1, -1):
            bit = (val >> i) & 1
            target = 1 - bit
            if target in trie_nodes[curr]["children"] and trie_nodes[trie_nodes[curr]["children"][target]]["count"] > 0:
                curr = trie_nodes[curr]["children"][target]
            else:
                curr = trie_nodes[curr]["children"][bit]
        return trie_nodes[curr]["val"]

    for n in nums:
        insert_v2(n)

    nums.sort(reverse=True)
    total_xor_sum = 0
    
    for n in nums:
        if trie_nodes[0]["count"] == 0:
            break
        
        # Check if n is still available in Trie
        # We need to check if n's count in Trie is > 0
        # A simple way is to try to find n in Trie and see if it's there
        # But since we iterate through sorted nums, we must check if n is "available"
        
        # To check if 'n' is available, we can't just check trie_nodes[0]["count"]
        # We need to see if 'n' itself can be removed.
        
        # Let's use a frequency map to track availability
        pass

    # Final implementation logic
    from collections import Counter
    counts = Counter(nums)
    trie_nodes = [{"children": {}, "count": 0, "val": None}]
    
    def insert_final(val: int) -> None:
        curr = 0
        trie_nodes[curr]["count"] += 1
        for i in range(bit_length - 1, -1, -1):
            bit = (val >> i) & 1
            if bit not in trie_nodes[curr]["children"]:
                trie_nodes[curr]["children"][bit] = len(trie_nodes)
                trie_nodes.append({"children": {}, "count": 0, "val": None})
            curr = trie_nodes[curr]["children"][bit]
            trie_nodes[curr]["count"] += 1
        trie_nodes[curr]["val"] = val

    def remove_final(val: int) -> None:
        curr = 0
        trie_nodes[curr]["count"] -= 1
        for i in range(bit_length - 1, -1, -1):
            bit = (val >> i) & 1
            curr = trie_nodes[curr]["children"][bit]
            trie_nodes[curr]["count"] -= 1

    def query_final(val: int) -> int:
        curr = 0
        for i in range(bit_length - 1, -1, -1):
            bit = (val >> i) & 1
            target = 1 - bit
            if target in trie_nodes[curr]["children"] and trie_nodes[trie_nodes[curr]["children"][target]]["count"] > 0:
                curr = trie_nodes[curr]["children"][target]
            else:
                curr = trie_nodes[curr]["children"][bit]
        return trie_nodes[curr]["val"]

    for n in nums:
        insert_final(n)

    nums.sort(reverse=True)
    ans = 0
    for n in nums:
        if counts[n] > 0:
            # Try to find the best partner for n
            # First, temporarily remove n so we don't pair it with itself
            remove_final(n)
            counts[n] -= 1
            
            if trie_nodes[0]["count"] > 0:
                partner = query_final(n)
                ans += (n ^ partner)
                remove_final(partner)
                counts[partner] -= 1
            else:
                # No partner found, put n back
                insert_final(n)
                counts[n] += 1
                
    return ans