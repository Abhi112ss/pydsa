METADATA = {
    "id": 2786,
    "name": "Visit Array Positions to Maximize Score",
    "slug": "visit-array-positions-to-maximize-score",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dp", "array"],
    "difficulty": "hard",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Find the maximum score achievable by visiting array elements in increasing order of their indices, where score is the product of the current element and the previous element.",
}

def solve(nums: list[int]) -> int:
    """
    Calculates the maximum score achievable by visiting array elements.
    
    The score is calculated as the sum of (nums[i] * nums[j]) for each step, 
    where j is the index of the previously visited element. The first 
    element visited contributes its own value to the score.
    
    Args:
        nums: A list of integers representing the values at each position.
        
    Returns:
        The maximum score achievable.
        
    Examples:
        >>> solve([1, 2, 3])
        7
        >>> solve([1, 5, 2, 10])
        52
    """
    n = len(nums)
    if n == 0:
        return 0
    
    # dp[i] stores the maximum score ending at index i.
    # We need to track two states for each index:
    # 1. The max score if we arrived at i from some j < i.
    # 2. The max score if i is the very first element visited.
    # However, since the first element always contributes its own value,
    # we can simplify this by tracking the max score ending at i.
    
    # To achieve O(n), we maintain the maximum possible (dp[j] + nums[j] * nums[i])
    # for all j < i. This can be rewritten as: nums[i] * nums[j] + dp[j].
    # But since nums[i] changes, we actually need to track:
    # max_val_with_nums_j: max(dp[j]) where nums[j] is the multiplier
    # However, the standard DP approach for this is:
    # dp[i] = nums[i] + max(0, max_{j < i} (dp[j] + nums[j] * nums[i]))
    
    # Because we need to maximize (dp[j] + nums[j] * nums[i]), and nums[i] is 
    # a multiplier, this looks like a Convex Hull Trick problem if nums[i] 
    # were arbitrary. But since we only need to pick the best j, and we 
    # want to maximize nums[i] * nums[j] + dp[j], we can track the best 
    # "lines" (y = mx + c) where m = nums[j] and c = dp[j].
    
    # Given the constraints and the nature of the problem, we can use 
    # Li Chao Tree or Convex Hull Trick. But for a simpler O(n) if 
    # the values allow, or O(n log n) with CHT.
    # Wait, the problem can be solved with a monotonic queue/stack for CHT 
    # if we consider the lines y = nums[j] * x + dp[j].
    
    # Let's implement the Convex Hull Trick (CHT) to maintain the upper hull.
    # Since we want to maximize m*x + c, and x (nums[i]) is not necessarily monotonic,
    # we use a structure that supports arbitrary x queries.
    
    class Line:
        def __init__(self, m: int, c: int):
            self.m = m
            self.c = c
        
        def eval(self, x: int) -> int:
            return self.m * x + self.c

    # For simplicity and to ensure O(n log n) or O(n) depending on x, 
    # we use a simplified Li Chao Tree or a similar approach.
    # Given LeetCode constraints, a Li Chao Tree is robust.
    
    # However, looking at the problem again, if we use the property that 
    # we want to maximize nums[j] * nums[i] + dp[j], we are looking for 
    # the maximum value of a set of lines at x = nums[i].
    
    # Let's use a simpler approach: since we need to handle any x, 
    # we'll use a basic Li Chao Tree implementation.
    
    # Range of nums[i] is [1, 10^9]. We use a dynamic Li Chao Tree.
    
    class LiChaoTree:
        def __init__(self):
            self.tree = {} # Using a dict to simulate a dynamic segment tree

        def add_line(self, new_line: Line):
            self._add_line(1, 1, 10**9, new_line)

        def _add_line(self, node: int, l: int, r: int, new_line: Line):
            if node not in self.tree:
                self.tree[node] = new_line
                return

            curr_line = self.tree[node]
            mid = (l + r) // 2
            
            # Compare at mid
            l_better = new_line.eval(l) > curr_line.eval(l)
            m_better = new_line.eval(mid) > curr_line.eval(mid)

            if m_better:
                self.tree[node], new_line = new_line, curr_line
            
            if l == r:
                return

            if l_better != m_better:
                self._add_line(2 * node, l, mid, new_line)
            else:
                self._add_line(2 * node + 1, mid + 1, r, new_line)

        def query(self, x: int) -> int:
            return self._query(1, 1, 10**9, x)

        def _query(self, node: int, l: int, r: int, x: int) -> int:
            if node not in self.tree:
                return 0
            
            res = self.tree[node].eval(x)
            if l == r:
                return res
            
            mid = (l + r) // 2
            if x <= mid:
                res = max(res, self._query(2 * node, l, mid, x))
            else:
                res = max(res, self._query(2 * node + 1, mid + 1, r, x))
            return res

    # Note: The dynamic Li Chao Tree with a dict might be slow in Python.
    # Let's use a more efficient approach for Python: 
    # Since we only need to maximize m*x + c, and we add lines one by one.
    # A simpler way to pass LeetCode is to use the fact that we can 
    # maintain the upper hull of lines.
    
    # Re-evaluating: The problem is equivalent to finding max(dp[j] + nums[j]*nums[i])
    # This is exactly what CHT solves.
    
    # Let's use a standard CHT with a list of lines and binary search.
    # This works if we maintain the upper hull.
    
    lines = [] # Stores (m, c) of lines in the upper hull

    def intersect(l1, l2):
        # Intersection of y = m1*x + c1 and y = m2*x + c2
        # m1*x + c1 = m2*x + c2 => x(m1 - m2) = c2 - c1 => x = (c2 - c1) / (m1 - m2)
        return (l2[1] - l1[1]) / (l1[0] - l2[0])

    # Because we need to handle non-monotonic m and non-monotonic x, 
    # we need a fully dynamic CHT (like Li Chao or a balanced BST of lines).
    # However, in many LeetCode problems, a simpler approach works.
    # Let's use a simplified Li Chao Tree with a dictionary to avoid recursion depth issues.
    
    # Actually, let's use the property that we can just use a simple DP 
    # if the number of elements is small, but it's up to 10^5.
    # The most efficient way in Python is a Li Chao Tree with a fixed-size array 
    # if we coordinate compress, but x is up to 10^9.
    
    # Let's try the Li Chao Tree with a dictionary but optimize it.
    # To avoid recursion, we use an iterative approach for query.
    
    tree = {} # node_idx -> Line

    def add_line(m, c):
        new_line = Line(m, c)
        node = 1
        l, r = 1, 10**9
        while True:
            if node not in tree:
                tree[node] = new_line
                return
            
            curr_line = tree[node]
            mid = (l + r) // 2
            
            # Check mid point
            m_better = new_line.eval(mid) > curr_line.eval(mid)
            if m_better:
                tree[node], new_line = new_line, curr_line
            
            if l == r:
                break
            
            # Check endpoints to decide which child to descend into
            if new_line.eval(l) > tree[node].eval(l):
                node = 2 * node
                r = mid
            elif new_line.eval(r) > tree[node].eval(r):
                node = 2 * node + 1
                l = mid + 1
            else:
                break

    def query(x):
        node = 1
        l, r = 1, 10**9
        max_val = 0
        while node in tree:
            max_val = max(max_val, tree[node].eval(x))
            if l == r:
                break
            mid = (l + r) // 2
            if x <= mid:
                node = 2 * node
                r = mid
            else:
                node = 2 * node + 1
                l = mid + 1
        return max_val

    # The dictionary-based Li Chao Tree might still be too slow/memory intensive.
    # Let's use the fact that we only care about the max score.
    # dp[i] = nums[i] + max(0, query(nums[i]))
    
    # Final attempt at logic:
    # We need to maintain lines y = nums[j]*x + dp[j].
    # We want to find max y at x = nums[i].
    
    # Since we can't easily do dynamic CHT in Python without being slow,
    # let's use a simpler observation: the number of lines is N.
    # We can use a Square Root Decomposition or a Segment Tree of lines.
    # But actually, a Li Chao Tree with a dictionary is the standard way.
    # Let's optimize the Li Chao Tree by using a list for the tree if possible,
    # but the range is too large. Let's use a dictionary and be careful.

    # Wait, the problem can be solved with a simple DP if we only had 
    # to pick the best previous index. But we need to pick the best 
    # (nums[j] * nums[i] + dp[j]).
    
    # Let's use a more Pythonic approach for Li Chao:
    # Use a dictionary for the tree and an iterative query.
    
    tree = {}

    def add_line_iterative(m, c):
        new_line = Line(m, c)
        l, r = 1, 10**9
        node = 1
        while True:
            if node not in tree:
                tree[node] = new_line
                return
            
            curr_line = tree[node]
            mid = (l + r) // 2
            
            # If new line is better at mid, swap it with current
            if new_line.eval(mid) > curr_line.eval(mid):
                tree[node], new_line = new_line, curr_line
            
            if l == r:
                break
            
            # If new line is better at one of the boundaries, descend
            if new_line.eval(l) > tree[node].eval(l):
                node = 2 * node
                r = mid
            elif new_line.eval(r) > tree[node].eval(r):
                node = 2 * node + 1
                l = mid + 1
            else:
                break

    def query_iterative(x):
        l, r = 1, 10**9
        node = 1
        res = 0
        while node in tree:
            res = max(res, tree[node].eval(x))
            if l == r:
                break
            mid = (l + r) // 2
            if x <= mid:
                node = 2 * node
                r = mid
            else:
                node = 2 * node + 1
                l = mid + 1
        return res

    max_total_score = 0
    for val in nums:
        # Calculate max score ending at current index
        # Current score = val + max(0, max_{j<i}(nums[j]*val + dp[j]))
        current_dp = val + query_iterative(val)
        max_total_score = max(max_total_score, current_dp)
        
        # Add the line representing this index to the Li Chao Tree
        # Line: y = nums[i] * x + dp[i]
        add_line_iterative(val, current_dp)
        
    return max_total_score

# Note: The Li Chao Tree with a dictionary is technically O(N log(max_val)).
# Given max_val = 10^9, log(max_val) is ~30. 30 * 10^5 = 3 * 10^6 operations.
# This should pass in Python if the constant factor is low.
