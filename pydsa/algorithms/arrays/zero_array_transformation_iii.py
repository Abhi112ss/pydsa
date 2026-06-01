METADATA = {
    "id": 3362,
    "name": "Zero Array Transformation III",
    "slug": "zero-array-transformation-iii",
    "category": "Greedy",
    "aliases": [],
    "tags": ["greedy", "difference_array", "sliding_window"],
    "difficulty": "hard",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(n)",
    "description": "Determine the minimum number of operations to make all elements in a target array zero using given ranges and values.",
}

def solve(nums: list[int], ranges: list[list[int]], values: list[int]) -> int:
    """
    Args:
        nums: A list of integers representing the target array.
        ranges: A list of lists where each sub-list contains [start, end] indices.
        values: A list of integers representing the amount to subtract from the range.

    Returns:
        The minimum number of operations required to make all elements in nums zero, or -1 if impossible.
    """
    n = len(nums)
    events = []
    for i in range(len(ranges)):
        start, end = ranges[i]
        val = values[i]
        events.append((start, 1, val, i))
        events.append((end + 1, -1, val, i))
    
    events.sort()
    
    available_ops = []
    current_diff = 0
    event_idx = 0
    used_count = 0
    
    import heapq

    for i in range(n):
        while event_idx < len(events) and events[event_idx][0] <= i:
            pos, type, val, op_id = events[event_idx]
            if type == 1:
                heapq.heappush(available_ops, (-val, op_id))
            else:
                pass
            event_idx += 1
        
        current_diff += 0 
        
        while nums[i] > 0:
            while available_ops and any(e[3] == available_ops[0][1] and e[0] > i for e in events if e[1] == -1):
                heapq.heappop(available_ops)

            if not available_ops:
                return -1
            
            val_neg, op_id = heapq.heappop(available_ops)
            val = -val_neg
            
            nums[i] -= val
            used_count += 1
            
            if nums[i] > 0:
                heapq.heappush(available_ops, (val_neg, op_id))
            else:
                pass

    return used_count

def solve(nums: list[int], ranges: list[list[int]], values: list[int]) -> int:
    """
    Args:
        nums: A list of integers representing the target array.
        ranges: A list of lists where each sub-list contains [start, end] indices.
        values: A list of integers representing the amount to subtract from the range.

    Returns:
        The minimum number of operations required to make all elements in nums zero, or -1 if impossible.
    """
    import heapq

    n = len(nums)
    m = len(values)
    
    starts = [[] for _ in range(n)]
    ends = [[] for _ in range(n)]
    
    for i in range(m):
        l, r = ranges[i]
        starts[l].append((values[i], i))
        if r + 1 < n:
            ends[r + 1].append((values[i], i))
            
    available_heap = []
    active_ops = set()
    used_ops = set()
    total_used = 0
    
    current_coverage = 0
    
    # We need to track the actual values applied to the current index.
    # Since we want minimum operations, we use a greedy approach with a priority queue.
    # However, a simple difference array doesn't work with greedy selection.
    # We use a Fenwick tree or Segment tree to manage the current values applied to nums.
    # But since we only move forward, we can use a priority queue of (value, end_index).
    
    # Correct Greedy: At index i, if nums[i] > 0, pick the available operation 
    # that covers i and has the largest value and extends furthest.
    # Actually, the standard greedy for this is: pick the operation that covers i 
    # and has the largest value to reduce nums[i] as much as possible.
    # To ensure we don't reuse, we track used indices.
    
    # Re-evaluating: The problem asks for minimum operations. 
    # This is equivalent to: at each index i, if nums[i] > 0, we must pick operations 
    # that cover i. To be most efficient for future indices, we should pick 
    # operations that cover i and end as late as possible.
    # Wait, the value also matters. If values are different, it's a variation of 
    # the interval covering problem.
    
    # Let's use: At index i, if nums[i] > 0, we need to pick operations covering i.
    # To satisfy nums[i], we pick operations that cover i and have the largest 'value'.
    # Among those with the same value, pick the one that ends latest.
    # Actually, the most robust greedy: At index i, if nums[i] > 0, pick the 
    # operation that covers i and has the largest value. If there's a tie, 
    # pick the one that ends latest.
    
    # But we can use an operation multiple times? No, "minimum number of operations".
    # Each operation in the list can be used at most once.
    
    # Let's refine:
    # 1. Store operations as (start, end, value).
    # 2. At index i, add all operations starting at i to a priority queue.
    # 3. Remove operations from the priority queue that end before i.
    # 4. While nums[i] > 0:
    #    a. If PQ is empty, return -1.
    #    b. Pick the operation from PQ with the largest value.
    #    c. If there's a tie in value, pick the one with the largest end index.
    #    d. Subtract its value from nums[i] and all subsequent nums[j] in its range.
    #    e. To do (d) efficiently, use a Fenwick tree or Segment tree.
    
    # Wait, the problem says "minimum number of operations". 
    # If we use an operation, we use its full value.
    
    # Let's use a Segment Tree to maintain the current values of nums.
    # Since we only need to subtract from a range and query a point, 
    # a Fenwick tree (Binary Indexed Tree) on the difference array is perfect.
    
    bit = [0] * (n + 2)
    
    def update(idx: int, val: int):
        idx += 1
        while idx <= n:
            bit[idx] += val
            idx += idx & (-idx)
            
    def query(idx: int) -> int:
        idx += 1
        s = 0
        while idx > 0:
            s += bit[idx]
            idx -= idx & (-idx)
        return s

    # We need to track the current value of nums[i] after operations.
    # current_nums[i] = original_nums[i] - query(i)
    
    # Priority Queue stores (-value, -end_index, op_id)
    pq = []
    ops_started = [[] for _ in range(n)]
    for idx in range(m):
        l, r = ranges[idx]
        ops_started[l].append((-values[idx], -ranges[idx][1], idx))
        
    used_count = 0
    for i in range(n):
        for item in ops_started[i]:
            heapq.heappush(pq, item)
            
        while pq:
            # Check if the top operation is still valid (ends >= i)
            neg_val, neg_end, op_id = pq[0]
            if -neg_end < i:
                heapq.heappop(pq)
                continue
            break
            
        current_val = nums[i] - query(i)
        
        while current_val > 0:
            if not pq:
                return -1
            
            neg_val, neg_end, op_id = heapq.heappop(pq)
            val = -neg_val
            end = -neg_end
            
            # Use this operation
            update(i, val)
            update(end + 1, -val)
            used_count += 1
            current_val = nums[i] - query(i)
            
            # We don't put it back because each operation is used once.
            # But wait, if we use it, it might not be enough to make nums[i] zero.
            # If it's not enough, we need to pick the NEXT best operation.
            # The current operation is now "used".
            
    # Final check
    for i in range(n):
        if nums[i] - query(i) > 0:
            return -1
            
    return used_count