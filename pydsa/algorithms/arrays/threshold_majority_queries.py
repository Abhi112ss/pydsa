METADATA = {
    "id": 3636,
    "name": "Threshold Majority Queries",
    "slug": "threshold_majority_queries",
    "category": "Arrays",
    "aliases": [],
    "tags": ["arrays", "segment_tree", "mo_algorithm"],
    "difficulty": "hard",
    "time_complexity": "O((N + Q) * sqrt(N))",
    "space_complexity": "O(N)",
    "description": "Find the number of elements in a given range [L, R] that appear more than a threshold number of times.",
}

import math

def solve(nums: list[int], queries: list[list[int]]) -> list[int]:
    """
    Solves the Threshold Majority Queries problem using Mo's Algorithm.

    Args:
        nums: A list of integers representing the array.
        queries: A list of queries where each query is [L, R, threshold].

    Returns:
        A list of integers representing the count of elements in each range 
        that appear more than the given threshold times.

    Examples:
        >>> solve([1, 2, 1, 2, 3], [[0, 4, 1], [1, 3, 1]])
        [2, 1]
    """
    n = len(nums)
    q = len(queries)
    if n == 0 or q == 0:
        return []

    # Block size for Mo's algorithm
    block_size = max(1, int(n / math.sqrt(q) if q > 0 else n))

    # Sort queries to minimize movement of L and R pointers
    # Using Hilbert curve or simple block sorting
    sorted_indices = sorted(
        range(q),
        key=lambda i: (queries[i][0] // block_size, 
                       queries[i][1] if (queries[i][0] // block_size) % 2 == 0 
                       else -queries[i][1])
    )

    # Frequency of each number in the current window
    counts = {}
    # freq_of_freq[f] = how many numbers appear exactly f times in the current window
    # We use a list for freq_of_freq for O(1) access, size n+1
    freq_of_freq = [0] * (n + 1)
    
    # To handle the threshold efficiently, we need to know how many elements 
    # have frequency > threshold. However, threshold varies per query.
    # This makes standard Mo's tricky. 
    # Wait, if threshold is part of the query, we can't easily use freq_of_freq 
    # to answer "count > threshold" in O(1) unless we use a Fenwick tree 
    # on the frequencies, making it O(Q * sqrt(N) * log N).
    # Alternatively, if we use Mo's, we maintain freq_of_freq.
    # To answer "how many elements have count > T", we need sum(freq_of_freq[T+1...N]).
    # A Fenwick tree (Binary Indexed Tree) on the frequencies allows this.

    bit = [0] * (n + 2)

    def bit_update(idx: int, val: int):
        idx += 1  # 1-based indexing for BIT
        while idx <= n + 1:
            bit[idx] += val
            idx += idx & (-idx)

    def bit_query(idx: int) -> int:
        idx += 1
        s = 0
        while idx > 0:
            s += bit[idx]
            idx -= idx & (-idx)
        return s

    def add(val: int):
        old_f = counts.get(val, 0)
        new_f = old_f + 1
        counts[val] = new_f
        
        # Update BIT: remove old frequency, add new frequency
        if old_f > 0:
            bit_update(old_f, -1)
        bit_update(new_f, 1)

    def remove(val: int):
        old_f = counts[val]
        new_f = old_f - 1
        counts[val] = new_f
        
        # Update BIT: remove old frequency, add new frequency
        bit_update(old_f, -1)
        if new_f > 0:
            bit_update(new_f, 1)

    results = [0] * q
    cur_l, cur_r = 0, -1

    for idx in sorted_indices:
        l, r, threshold = queries[idx]

        # Expand/Shrink window to match [l, r]
        while cur_r < r:
            cur_r += 1
            add(nums[cur_r])
        while cur_l > l:
            cur_l -= 1
            add(nums[cur_l])
        while cur_r > r:
            remove(nums[cur_r])
            cur_r -= 1
        while cur_l < l:
            remove(nums[cur_l])
            cur_l += 1

        # The number of elements with frequency > threshold is:
        # Total elements with freq >= 1 MINUS elements with freq <= threshold
        # Or more simply: bit_query(n) - bit_query(threshold)
        # Since bit_query(x) returns count of elements with frequency <= x
        # We want count of elements with frequency in [threshold + 1, n]
        
        if threshold >= n:
            results[idx] = 0
        else:
            # Total elements currently in window with freq > 0 is bit_query(n)
            # But we only care about elements that actually exist in the window.
            # The BIT tracks how many distinct numbers have a certain frequency.
            # Sum of bit[i] for i from threshold + 1 to n.
            total_distinct_in_window = bit_query(n)
            count_up_to_threshold = bit_query(threshold)
            results[idx] = total_distinct_in_window - count_up_to_threshold

    return results
