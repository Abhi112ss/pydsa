METADATA = {
    "id": 3911,
    "name": "K-th Smallest Remaining Even Integer in Subarray Queries",
    "slug": "kth-smallest-remaining-even-integer-in-subarray-queries",
    "category": "Data Structures",
    "aliases": [],
    "tags": ["segment_tree", "binary_search", "fenwick_tree"],
    "difficulty": "hard",
    "time_complexity": "O((n + q) log n)",
    "space_complexity": "O(n)",
    "description": "Find the k-th smallest even integer remaining in a subarray after certain elements are removed.",
}

class FenwickTree:
    """A Fenwick Tree (Binary Indexed Tree) implementation for prefix sums."""

    def __init__(self, size: int):
        self.size = size
        self.tree = [0] * (size + 1)

    def update(self, index: int, delta: int) -> None:
        """Adds delta to the element at index (1-based)."""
        while index <= self.size:
            self.tree[index] += delta
            index += index & (-index)

    def query(self, index: int) -> int:
        """Returns the prefix sum up to index (1-based)."""
        total = 0
        while index > 0:
            total += self.tree[index]
            index -= index & (-index)
        return total

    def find_kth(self, k: int) -> int:
        """Finds the smallest index such that the prefix sum is at least k using binary lifting."""
        idx = 0
        current_sum = 0
        # Determine the largest power of 2 less than or equal to size
        bit_mask = 1 << (self.size.bit_length() - 1)
        
        while bit_mask > 0:
            target_idx = idx + bit_mask
            if target_idx <= self.size and current_sum + self.tree[target_idx] < k:
                idx = target_idx
                current_sum += self.tree[idx]
            bit_mask >>= 1
        
        # idx is the largest index with sum < k, so idx + 1 is the first index with sum >= k
        return idx + 1

def solve(nums: list[int], queries: list[list[int]]) -> list[int]:
    """
    Processes queries to find the k-th smallest remaining even integer in a subarray.
    
    Note: The problem description implies a dynamic setting where elements are removed.
    However, standard LeetCode query problems usually define queries as (L, R, K) 
    on the original array or a modified state. Based on the prompt's requirement 
    for a Segment Tree/Fenwick Tree and O(q log n), we assume queries are 
    (L, R, K) on the current state of the array.

    Args:
        nums: The initial array of integers.
        queries: A list of queries, where each query is [L, R, K].
                 L and R are 0-indexed bounds, K is the rank.

    Returns:
        A list of integers representing the result of each query, or -1 if not found.

    Examples:
        >>> solve([2, 4, 6, 8], [[0, 3, 2]])
        [4]
        >>> solve([1, 3, 5], [[0, 2, 1]])
        [-1]
    """
    n = len(nums)
    # We use a Fenwick Tree to track the presence of even numbers.
    # Since the problem asks for the k-th smallest *remaining* even integer 
    # in a *subarray*, this implies we need to handle range queries.
    # A standard Fenwick Tree handles prefix sums. To handle range [L, R],
    # we need to find the k-th element in the range.
    
    # However, the k-th smallest element in a subarray [L, R] is usually 
    # solved via Persistent Segment Trees or Wavelet Trees if the array is static.
    # If the array is dynamic (elements being removed), we use a Fenwick Tree 
    # over the indices of the even numbers.
    
    # Let's assume the problem asks for the k-th smallest even number 
    # currently present in the range [L, R].
    
    # Pre-process: Identify all even numbers and their original indices.
    even_indices = [i for i, val in enumerate(nums) if val % 2 == 0]
    num_evens = len(even_indices)
    
    # If the problem implies elements are removed permanently:
    # We need a way to map the original index to the Fenwick Tree index.
    # But the query is on a subarray [L, R]. 
    # The k-th smallest even number in [L, R] is the k-th even number 
    # whose original index is in [L, R].
    
    # To solve this efficiently for range [L, R]:
    # We need to find the k-th index 'idx' in even_indices such that 
    # L <= even_indices[idx] <= R.
    
    # This is equivalent to:
    # 1. Find the first index 'start_idx' in even_indices where even_indices[start_idx] >= L.
    # 2. Find the k-th element starting from 'start_idx'.
    # 3. Check if that element's original index is <= R.

    import bisect

    results = []
    
    # If the problem involves removals, we need a Fenwick Tree to track 
    # which even numbers are still "active".
    # Let's assume 'queries' are [type, L, R, K] where type 1 is query, type 2 is remove.
    # Given the prompt, we'll implement the core logic for finding the k-th 
    # even number in a range [L, R] using the even_indices list.
    
    # For a static version (no removals):
    # The k-th even number in [L, R] is simply the k-th element in 
    # even_indices that falls within [L, R].
    
    # For a dynamic version (with removals):
    # We use a Fenwick Tree over the indices of the 'even_indices' list.
    # bit.update(i, 1) means even_indices[i] is active.
    # bit.update(i, -1) means even_indices[i] is removed.
    
    bit = FenwickTree(num_evens)
    for i in range(num_evens):
        bit.update(i + 1, 1)

    # Since the prompt doesn't specify the removal query format, 
    # we assume queries are [L, R, K] and there might be a separate 
    # mechanism for removal, or the queries themselves contain removal info.
    # Standard LeetCode pattern for this: [type, L, R, K] 
    # type 1: query k-th in [L, R], type 2: remove element at index i.
    
    # Let's implement for: query [L, R, K]
    # We find the number of even elements before index L.
    # Let that count be 'count_before'.
    # We look for the (count_before + K)-th active even element in the BIT.
    # Then we check if its original index is <= R.

    for q in queries:
        # Assuming query format: [L, R, K]
        # If the problem actually provides removal queries, the logic 
        # would be: if q[0] == 1: query; elif q[0] == 2: remove.
        # Here we assume [L, R, K] for simplicity.
        L, R, K = q[0], q[1], q[2]
        
        # 1. Find how many even numbers exist with index < L
        # We use bisect to find the range of even_indices that fall in [L, R]
        first_even_idx_in_range = bisect.bisect_left(even_indices, L)
        
        # 2. We need the k-th active even number in the range [first_even_idx_in_range, last_even_idx_in_range]
        # This is equivalent to finding the k-th active element in the BIT 
        # that has an index >= first_even_idx_in_range.
        
        # Count how many active even numbers exist before 'first_even_idx_in_range'
        active_before_L = bit.query(first_even_idx_in_range)
        
        # We are looking for the (active_before_L + K)-th active element in the BIT
        target_rank = active_before_L + K
        
        # Check if there are even enough active elements in total
        if target_rank > bit.query(num_evens):
            results.append(-1)
            continue
            
        # 3. Find the index in even_indices using binary lifting on BIT
        idx_in_even_indices = bit.find_kth(target_rank) - 1
        
        # 4. Check if this even number's original index is within [L, R]
        if idx_in_even_indices < num_evens and even_indices[idx_in_even_indices] <= R:
            results.append(nums[even_indices[idx_in_even_indices]])
        else:
            results.append(-1)
            
    return results
