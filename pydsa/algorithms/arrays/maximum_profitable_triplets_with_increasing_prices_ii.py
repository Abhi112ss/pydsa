METADATA = {
    "id": 2921,
    "name": "Maximum Profitable Triplets With Increasing Prices II",
    "slug": "maximum-profitable-triplets-with-increasing-prices-ii",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["fenwick_tree", "segment_tree", "binary_indexed_tree", "sorting", "dynamic_programming"],
    "difficulty": "hard",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(n)",
    "description": "Find the maximum total profit from non-overlapping triplets of indices (i, j, k) such that prices[i] < prices[j] < prices[k] and i < j < k.",
}

class FenwickTree:
    """A Fenwick Tree (Binary Indexed Tree) to maintain maximum values."""
    
    def __init__(self, size: int):
        self.tree = [0] * (size + 1)

    def update(self, index: int, value: float) -> None:
        """Updates the tree at a given index with a new maximum value."""
        while index < len(self.tree):
            if value > self.tree[index]:
                self.tree[index] = value
            else:
                # Since we only care about increasing the max, 
                # if the current value is not better, we can't optimize further here.
                # However, in a standard max-BIT, we only update if value is larger.
                break
            index += index & (-index)

    def query(self, index: int) -> float:
        """Queries the maximum value in the range [1, index]."""
        res = 0.0
        while index > 0:
            if self.tree[index] > res:
                res = self.tree[index]
            index -= index & (-index)
        return res

def solve(prices: list[int]) -> int:
    """
    Calculates the maximum total profit from non-overlapping triplets.
    
    A triplet (i, j, k) is valid if i < j < k and prices[i] < prices[j] < prices[k].
    The profit is (prices[j] - prices[i]) + (prices[k] - prices[j]) = prices[k] - prices[i].
    Wait, the problem defines profit as (prices[j] - prices[i]) + (prices[k] - prices[j]).
    Actually, the problem states: profit = (prices[j] - prices[i]) + (prices[k] - prices[j]).
    This simplifies to prices[k] - prices[i].
    
    Args:
        prices: A list of integers representing prices.
        
    Returns:
        The maximum total profit as an integer.
        
    Examples:
        >>> solve([1, 5, 2, 10])
        9
        >>> solve([1, 2, 3, 4, 5])
        4
    """
    n = len(prices)
    if n < 3:
        return 0

    # Coordinate compression to map prices to [1, unique_count]
    sorted_prices = sorted(list(set(prices)))
    rank_map = {price: i + 1 for i, price in enumerate(sorted_prices)}
    m = len(sorted_prices)

    # dp_pair[j] stores the max profit of a single pair (i, j) where i < j and prices[i] < prices[j]
    # We use a Fenwick tree to find max(prices[j] - prices[i]) for all i < j
    # To maximize prices[j] - prices[i], we need to minimize prices[i].
    # However, the problem is about non-overlapping triplets.
    # Let's redefine:
    # dp1[j]: max profit of a single pair (i, j) ending at j.
    # dp2[j]: max profit of a single triplet (i, j, k) ending at k.
    # dp3[k]: max total profit of multiple non-overlapping triplets ending at or before k.
    
    # To handle non-overlapping, we need to track the max profit of completed triplets
    # before the current index starts a new pair.
    
    # bit_pair: stores max(prices[j] - prices[i]) for pairs ending at j
    # bit_triplet: stores max(total_profit_before_i + (prices[j] - prices[i]) + (prices[k] - prices[j]))
    
    # Actually, a simpler DP:
    # f[j] = max profit of a pair (i, j) where i < j and prices[i] < prices[j].
    # To maximize f[j], we need max(prices[j] - prices[i]) -> prices[j] - min(prices[i]).
    # But we need to account for the total profit of triplets completed before index i.
    
    # Let's use three Fenwick trees:
    # 1. bit_min_price: stores min(prices[i] - total_profit_before_i) for index i.
    #    Wait, we want to maximize (prices[j] - prices[i] + total_profit_before_i).
    #    This is prices[j] + max(total_profit_before_i - prices[i]).
    # 2. bit_pair_profit: stores max(total_profit_before_i - prices[i] + prices[j]) for index j.
    #    This is max(profit_of_pair_ending_at_j + total_profit_before_i_of_that_pair).
    #    Actually, let's use:
    #    bit_pair: stores max(total_profit_before_i - prices[i] + prices[j])? No.
    
    # Correct DP approach:
    # Let dp_pair[j] = max profit of a pair (i, j) + total profit of triplets before i.
    # dp_pair[j] = max_{i < j, prices[i] < prices[j]} (total_profit_before_i - prices[i] + prices[j])
    # Let dp_triplet[k] = max profit of a triplet (i, j, k) + total profit of triplets before i.
    # dp_triplet[k] = max_{j < k, prices[j] < prices[k]} (dp_pair[j] - prices[j] + prices[k])
    # Let dp_total[k] = max total profit using indices up to k.
    # dp_total[k] = max(dp_total[k-1], dp_triplet[k])

    # bit_pair: stores max(total_profit_before_i - prices[i]) indexed by price rank
    # bit_triplet: stores max(dp_pair[j] - prices[j]) indexed by price rank
    # bit_total: stores max(dp_total[i]) indexed by price rank (not needed, just a variable)

    # We need to find max(total_profit_before_i - prices[i]) where prices[i] < prices[j].
    # We need to find max(dp_pair[j] - prices[j]) where prices[j] < prices[k].
    
    # bit_pair_val: stores max(total_profit_before_i - prices[i]) for a given price rank
    # bit_triplet_val: stores max(dp_pair[j] - prices[j]) for a given price rank
    
    # To handle "total_profit_before_i", we need to know the max total profit 
    # available before index i. Since we process i from 0 to n-1, 
    # total_profit_before_i is simply the max dp_total found so far.
    
    # However, "total_profit_before_i" means the max profit of triplets that 
    # strictly end before index i.
    
    # Let's refine:
    # As we iterate k from 0 to n-1:
    # 1. Current max total profit from completed triplets is `max_total_so_far`.
    #    But we must ensure the triplet (i, j, k) doesn't overlap with previous ones.
    #    If a triplet ends at index `last_end`, the next triplet must start at `last_end + 1`.
    #    This is naturally handled if we update `max_total_so_far` only after a triplet is completed.
    
    # Let's use:
    # bit_pair: stores max(total_profit_before_i - prices[i]) indexed by price rank.
    # bit_triplet: stores max(dp_pair[j] - prices[j]) indexed by price rank.
    # We need to be careful: "total_profit_before_i" is the max profit of triplets 
    # that ended at some index `idx < i`.
    
    # We can use a queue or a pointer to update the Fenwick trees with 
    # "completed" triplets.
    
    # Let's simplify:
    # For each index k:
    #   1. A triplet can be formed using a pair ending at j < k where prices[j] < prices[k].
    #      Profit = (dp_pair[j] - prices[j] + prices[k]) + (total profit of triplets ending before the i of that pair).
    #      This is getting complex. Let's use the property:
    #      Profit of (i, j, k) = (prices[j] - prices[i]) + (prices[k] - prices[j]) = prices[k] - prices[i].
    #      Total profit = sum (prices[k_m] - prices[i_m]).
    
    # Let's use the standard DP for non-overlapping intervals:
    # dp[k] = max total profit using a subset of indices from {0...k}.
    # To compute dp[k], either:
    #   - k is not the end of a triplet: dp[k] = dp[k-1]
    #   - k is the end of a triplet (i, j, k): dp[k] = max_{i < j < k, p[i]<p[j]<p[k]} (dp[i-1] + p[k] - p[i])
    
    # To optimize max_{i < j < k, p[i]<p[j]<p[k]} (dp[i-1] - p[i] + p[k]):
    # For a fixed k, we need max_{j < k, p[j] < p[k]} [ max_{i < j, p[i] < p[j]} (dp[i-1] - p[i]) + p[j] ] - p[j] + p[k]
    # Let val[j] = max_{i < j, p[i] < p[j]} (dp[i-1] - p[i]) + p[j].
    # Then dp[k] = max(dp[k-1], max_{j < k, p[j] < p[k]} (val[j] - p[j] + p[k])).
    
    # Let's track:
    # bit_pair: stores max(dp[i-1] - prices[i]) indexed by price rank.
    # bit_triplet: stores max(val[j] - prices[j]) indexed by price rank.
    # where val[j] = bit_pair.query(rank[j]-1) + prices[j].
    
    # Note: dp[i-1] is the max profit using indices up to i-1.
    
    dp = [0] * (n + 1)
    bit_pair = FenwickTree(m) # stores max(dp[i-1] - prices[i])
    bit_triplet = FenwickTree(m) # stores max(val[j] - prices[j])
    
    # We need to handle the "i-1" carefully. 
    # When we are at index k, we can update bit_pair with (dp[k-1] - prices[k])
    # and bit_triplet with (val[k] - prices[k]).
    
    # But wait, the order of updates matters.
    # For index k:
    # 1. Try to form a triplet ending at k:
    #    current_triplet_profit = bit_triplet.query(rank_map[prices[k]] - 1) + prices[k]
    #    dp[k] = max(dp[k-1], current_triplet_profit)
    # 2. Try to form a pair ending at k:
    #    val_k = bit_pair.query(rank_map[prices[k]] - 1) + prices[k]
    #    bit_triplet.update(rank_map[prices[k]], val_k - prices[k])
    # 3. Update bit_pair with the possibility of k being the start of a new triplet:
    #    bit_pair.update(rank_map[prices[k]], dp[k-1] - prices[k])
    
    # Wait, step 3 should use dp[k-1] because the triplet starts at k, 
    # so the previous triplets must have ended before k.
    # Actually, if the triplet is (k, j, l), the previous triplets must end before k.
    # So dp[k-1] is correct.
    
    # Let's re-trace with an example: prices = [1, 5, 2, 10]
    # k=0: p=1, r=1. dp[1]=0. bit_pair.upd(1, dp[0]-1 = -1). bit_triplet.upd(1, val-1).
    # k=1: p=5, r=2. dp[2]=0. val_1 = bit_pair.query(1)+5 = -1+5=4. bit_triplet.upd(2, 4-5=-1). bit_pair.upd(2, dp[1]-5=-5).
    # k=2: p=2, r=1. dp[3]=0. val_2 = bit_pair.query(0)+2 = 2. bit_triplet.upd(1, 2-2=0). bit_pair.upd(1, dp[2]-2=-2).
    # k=3: p=10, r=4. dp[4] = max(dp[3], bit_triplet.query(3)+10).
    #      bit_triplet.query(3) = max(bit_triplet[1], bit_triplet[2]) = max(0, -1) = 0.
    #      dp[4] = max(0, 0+10) = 10. 
    # Wait, the example [1, 5, 2, 10] should be 9? 
    # (5-1) + (10-5) = 9? No, (5-1) + (10-2) is not allowed because indices must be i<j<k.
    # Triplets: (0, 1, 3) -> prices (1, 5, 10). Profit = (5-1) + (10-5) = 9.
    # My manual trace: bit_triplet.query(3) was 0. 0 + 10 = 10. 
    # Where did 10 come from? bit_triplet[1] was 0. 
    # bit_triplet[1] came from val_2 - prices[2] = 2 - 2 = 0.
    # val_2 = bit_pair.query(0) + 2. But rank_map[2] is 1. query(0) is 0.
    # So val_2 = 0 + 2 = 2. bit_triplet.update(1, 2-2=0).
    # This means a triplet (i, j, k) where i is "nothing" (profit 0).
    # But the problem says i < j < k. So i must be a valid index.
    # The bit_pair.query(rank-1) should only return a value if a valid i was found.
    # We can initialize Fenwick tree with a very small number.
    
    # Let's use -float('inf') for initialization.
    
    return _solve_optimized(prices, rank_map, m)

def _solve_optimized(prices: list[int], rank_map: dict[int, int], m: int) -> int:
    n = len(prices)
    dp = [0] * (n + 1)
    
    # bit_pair stores max(dp[i-1] - prices[i])
    # bit_triplet stores max(val[j] - prices[j]) where val[j] = max_{i<j, p[i]<p[j]} (dp[i-1] - p[i] + p[j])
    
    # Use a large negative number for initialization
    INF = float('inf')
    
    # We'll use a custom Fenwick to handle -