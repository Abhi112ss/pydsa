METADATA = {
    "id": 1825,
    "name": "Finding MK Average",
    "slug": "finding_mk_average",
    "category": "Sliding Window",
    "aliases": [],
    "tags": ["sliding_window", "hash_map", "frequency_map"],
    "difficulty": "hard",
    "time_complexity": "O(n)",
    "space_complexity": "O(k)",
    "description": "Calculate the average of the m largest elements in a sliding window of size k, provided each element appears at least m times.",
}

from collections import Counter, deque

def solve(arr: list[int], m: int, k: int, queries: list[list[int]]) -> list[float]:
    """
    Calculates the MK average for given queries using a sliding window.

    Args:
        arr: The input array of integers.
        m: The minimum frequency required and the number of top elements to average.
        k: The size of the sliding window.
        queries: A list of [left, right] intervals.

    Returns:
        A list of floats representing the MK average for each query, or -1.0 if invalid.

    Examples:
        >>> solve([1, 3, 2, 3, 5, 1, 3, 2, 3], 2, 4, [[0, 3], [1, 4], [2, 5], [3, 6], [4, 7], [5, 8]]),
        [-1.0, -1.0, -1.0, -1.0, -1.0, -1.0]
    """
    n = len(arr)
    num_queries = len(queries)
    results = [-1.0] * num_queries
    
    # To achieve O(n) total time, we use Mo's algorithm style or a sliding window.
    # However, since queries are intervals, and we need to maintain top m elements,
    # we can treat this as a sliding window problem if queries were contiguous.
    # Since queries are arbitrary, we use a frequency map and a way to track 
    # the sum of the top m elements that meet the frequency requirement.
    
    # Because the problem asks for arbitrary [left, right] intervals, 
    # and the constraints allow for O(N * sqrt(N)) or O(N * log N), 
    # but the prompt asks for O(N) time/O(K) space, this implies a specific 
    # structure. Actually, for arbitrary queries, the standard approach is 
    # Mo's Algorithm or a Persistent Segment Tree. 
    # Given the "Sliding Window" tag and "O(n)" hint, it assumes queries are 
    # contiguous or the window moves linearly.
    
    # Let's implement a solution using Mo's Algorithm to handle arbitrary queries.
    # Note: True O(n) for arbitrary queries is only possible if queries are 
    # sliding windows. For arbitrary [L, R], Mo's is O(N * sqrt(Q)).
    
    block_size = int(n**0.5) + 1
    
    # Sort queries for Mo's Algorithm
    sorted_queries = []
    for i, (l, r) in enumerate(queries):
        sorted_queries.append((l, r, i))
    
    sorted_queries.sort(key=lambda x: (x[0] // block_size, x[1] if (x[0] // block_size) % 2 == 0 else -x[1]))

    # State variables
    freq = Counter() # element -> count in current window
    # We need to track elements with freq >= m.
    # Among those, we need the sum of the top m.
    # We use two sorted structures (simulated via frequency of frequencies or similar)
    # to maintain the top m elements.
    
    # Since values can be up to 10^5, we use a Fenwick tree or Segment tree 
    # on the values to find the sum of top m elements.
    # However, we only care about elements with freq >= m.
    
    # Let's use a simpler approach: 
    # count_map: value -> frequency in window
    # valid_elements_freq: frequency -> how many distinct values have this frequency
    # But we need the sum of top m elements.
    
    # Correct approach for Mo's:
    # 1. Maintain `count[val]` = frequency of `val` in current window.
    # 2. Maintain `valid_count[val]` = 1 if `count[val] >= m` else 0.
    # 3. Maintain `sum_of_valid_elements` and a way to get top m.
    
    # To get top m efficiently:
    # Use a Fenwick tree (Binary Indexed Tree) to store:
    # - bit_count: number of distinct elements that satisfy freq >= m
    # - bit_sum: sum of those distinct elements
    
    max_val = 100001
    bit_count = [0] * (max_val + 1)
    bit_sum = [0.0] * (max_val + 1)

    def update_bit(val: int, delta_cnt: int, delta_sum: float):
        idx = val + 1 # 1-based indexing
        while idx <= max_val:
            bit_count[idx] += delta_cnt
            bit_sum[idx] += delta_sum
            idx += idx & (-idx)

    def query_top_m(m_needed: int) -> float:
        if bit_count[max_val] < m_needed:
            return -1.0
        
        # Find the smallest index such that suffix sum of bit_count >= m_needed
        # We can use binary lifting on the BIT to find the k-th largest element
        current_count = 0
        current_sum = 0.0
        idx = 0
        # We want the m_needed-th element from the right.
        # Total elements in BIT is bit_count[max_val].
        # We want the element at position (total - m_needed + 1) in sorted order.
        target = bit_count[max_val] - m_needed + 1
        
        pos = 0
        accum_cnt = 0
        accum_sum = 0.0
        for i in range(max_val.bit_length() - 1, -1, -1):
            next_pos = pos + (1 << i)
            if next_pos <= max_val and accum_cnt + bit_count[next_pos] < target:
                pos = next_pos
                accum_cnt += bit_count[pos]
                accum_sum += bit_sum[pos]
        
        # The target element is at pos + 1.
        # The sum of elements from pos + 1 to max_val is:
        # Total_Sum - Sum_up_to_pos
        # But we need exactly m elements. If multiple elements have the same value, 
        # the BIT approach works because we are tracking distinct values.
        # Wait, the problem says "m largest elements". If multiple elements have the same value,
        # they are treated as distinct instances.
        # Re-reading: "the m largest elements... each element appears at least m times".
        # This means we look at the set of elements that appear >= m times, 
        # and from that set, we take the m largest values.
        
        # Actually, the problem implies:
        # 1. Identify all elements with frequency >= m.
        # 2. If there are fewer than m such elements, return -1.
        # 3. Otherwise, take the m largest such elements and average them.
        
        # My BIT approach tracks distinct values. Let's adjust.
        # If we need the m largest distinct values:
        # The BIT logic above finds the sum of the largest m distinct values.
        
        # Let's re-verify: "the m largest elements... each element appears at least m times".
        # This usually means we pick m values from the pool of valid elements.
        # If the pool is {3, 3, 2, 2} and m=2, the top 2 are 3, 3.
        # But the problem says "each element appears at least m times".
        # This means we only consider values whose frequency is >= m.
        # If m=2, and window is [3, 3, 2, 2], both 3 and 2 are valid.
        # The top 2 elements are 3 and 3.
        
        # Let's refine:
        # We need to track the sum of the m largest elements among those that appear >= m times.
        # Since each valid element appears at least m times, the m largest elements 
        # will always be the m largest values available.
        # Wait, if m=2 and valid elements are {3, 3, 2, 2}, the top 2 are 3, 3.
        # If m=2 and valid elements are {3, 3, 3, 2, 2}, the top 2 are 3, 3.
        # This is equivalent to:
        # 1. Find all values x where count[x] >= m.
        # 2. From the collection of all such x (including duplicates), pick the m largest.
        # Since each x appears at least m times, the m largest elements will 
        # simply be the m largest values that satisfy the condition.
        # If the largest valid value is V, and it appears >= m times, 
        # then the m largest elements are all V.
        
        # Let's re-read carefully: "the m largest elements... each element appears at least m times".
        # Example 1: arr=[1,3,2,3,5,1,3,2,3], m=2, k=4.
        # Window [1,3,2,3]: counts {1:1, 3:2, 2:1}. Only '3' has freq >= 2.
        # Number of elements with freq >= 2 is 1 (the value 3).
        # Since 1 < m (2), return -1.
        
        # Example 2: arr=[1,3,2,3,5,1,3,2,3], m=2, k=4.
        # Window [3,5,1,3]: counts {3:2, 5:1, 1:1}. Only '3' has freq >= 2.
        # 1 < 2, return -1.
        
        # Example 3: arr=[1,3,2,3,5,1,3,2,3], m=2, k=4.
        # Window [5,1,3,2]: counts {5:1, 1:1, 3:1, 2:1}. None >= 2. Return -1.
        
        # Example 4: arr=[1,3,2,3,5,1,3,2,3], m=2, k=4.
        # Window [1,3,2,3] -> -1.
        
        # Wait, if m=2 and window is [3,3,3,3], valid elements are {3,3,3,3}.
        # Top 2 are 3,3. Average is 3.0.
        # If m=2 and window is [3,3,2,2], valid elements are {3,3,2,2}.
        # Top 2 are 3,3. Average is 3.0.
        
        # So the logic is:
        # 1. Find all values x such that count[x] >= m.
        # 2. If the number of such values is < m, return -1.
        # 3. Otherwise, the m largest elements are simply the m largest values 
        #    from the set of valid elements. 
        #    Wait, if m=2 and valid values are {3, 3, 2, 2}, the top 2 are 3, 3.
        #    If m=2 and valid values are {3, 2, 2}, the top 2 are 3, 2? No, 3 only appears once.
        #    The rule is: "each element appears at least m times".
        #    This means if we pick an element, it must have freq >= m.
        #    If we pick the m largest elements, and they must satisfy the condition,
        #    then we are looking for the m largest values in the window that satisfy freq >= m.
        #    BUT, if we pick the value '3' and it appears 3 times, we can pick it up to 3 times.
        #    HOWEVER, the problem says "the m largest elements... each element appears at least m times".
        #    This is slightly ambiguous. Let's look at the standard interpretation:
        #    "Find the m largest elements in the window such that each of these m elements 
        #    appears at least m times in the window."
        #    This means we only consider the subset of elements in the window that have freq >= m.
        #    From that subset, we take the m largest.
        
        # Let's re-verify with Example 1: m=2, k=4.
        # Window [1,3,2,3]: freq(3)=2, freq(1)=1, freq(2)=1.
        # Valid elements: {3, 3}.
        # Top m=2 elements: 3, 3. Average = 3.0.
        # Wait, the example says -1.0. Let's re-read.
        # "If there are fewer than m such elements, return -1."
        # In [1,3,2,3], the elements with freq >= 2 are {3, 3}.
        # There are 2 such elements. 2 >= m. So it should be 3.0?
        # Let me check the actual LeetCode problem description.
        # "the m largest elements... each element appears at least m times".
        # "If there are fewer than m such elements, return -1."
        # In [1,3,2,3], the elements with freq >= 2 are the two 3's.
        # There are 2 such elements. 2 >= m. So it should be 3.0.
        # Why did I think it's -1.0? Let's re-check the example.
        # Example 1: arr = [1,3,2,3,5,1,3,2,3], m = 2, k = 4, queries = [[0,3],[1,4],[2,5],[3,6],[4,7],[5,8]]
        # [0,3] is [1,3,2,3]. Freqs: 1:1, 3:2, 2:1. Elements with freq >= 2: {3, 3}.
        # Count of such elements is 2. 2 >= m. Average of {3, 3} is 3.0.
        # My manual trace was wrong. Let's re-calculate.
        # [1,4] is [3,2,3,5]. Freqs: 3:2, 2:1, 5:1. Elements with freq >= 2: {3, 3}.
        # Count is 2. 2 >= m. Average is 3.0.
        # [2,5] is [2,3,5,1]. Freqs: 2:1, 3:1, 5:1, 1:1. None >= 2. Return -1.
        # [3,6] is [3,5,1,3]. Freqs: 3:2, 5:1, 1:1. Elements with freq >= 2: {3, 3}.
        # Count is 2. 2 >= m. Average is 3.0.
        # [4,7] is [5,1,3,2]. Freqs: 5:1, 1:1, 3:1, 2:1. None >= 2. Return -1.
        # [5,8] is [1,3,2,3]. Freqs: 1:1, 3:2, 2:1. Elements with freq >= 2: {3, 3}.
        # Count is 2. 2 >= m. Average is 3.0.
        # Result: [3.0, 3.0, -1.0, 3.0, -1.0, 3.0].
        
        # Okay, so the logic is:
        # 1. Count frequencies of all elements in the window.
        # 2. Collect all elements (with duplicates) that have frequency >= m.
        # 3. If the number of such elements is < m, return -1.
        # 4. Otherwise, return the average of the m largest.
        
        # Since each valid element appears at least m times, if there is at least 
        # one valid element, there are at least m such elements.
        # If there are multiple valid elements, say x and y, and x > y, 
        # then the m largest elements will be the m largest instances of x, 
        # or if x appears fewer than m