METADATA = {
    "id": 2931,
    "name": "Maximum Spending After Buying Items",
    "slug": "maximum-spending-after-buying-items",
    "category": "Greedy",
    "aliases": [],
    "tags": ["greedy", "sorting"],
    "difficulty": "medium",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(1)",
    "description": "Maximize total spending by selecting items such that the sum of costs of items bought on day i is less than or equal to the sum of costs of items bought on day i+1.",
}

def solve(costs: list[int], days: int) -> int:
    """
    Calculates the maximum total spending possible given a list of item costs 
    and a fixed number of days, following the rule that the sum of costs 
    on day i must be less than or equal to the sum of costs on day i+1.

    Args:
        costs: A list of integers representing the cost of each item.
        days: The number of days available to distribute the items.

    Returns:
        The maximum total spending possible. Returns -1 if it's impossible 
        to distribute items such that the condition is met.

    Examples:
        >>> solve([1, 2, 3, 4, 5], 3)
        15
        >>> solve([1, 1, 1], 2)
        3
    """
    n = len(costs)
    # If we have more days than items, we can't satisfy the condition 
    # unless we assume empty days are allowed, but typically in these 
    # problems, every day must have at least one item or we distribute 
    # all items. Based on the constraint: sum(day_i) <= sum(day_i+1).
    # To maximize total sum, we just need to ensure a valid partition exists.
    
    # Sort costs to facilitate a greedy approach. 
    # However, the problem asks for the maximum spending. 
    # Since we must use ALL items (implied by "spending after buying items"),
    # the total spending is always sum(costs) if a valid partition exists.
    # If the problem implies we can choose a subset, the logic changes.
    # Re-reading standard LeetCode patterns for this type: 
    # Usually, we must use all items. If we must use all items, 
    # the total sum is constant. The challenge is checking if a partition exists.
    
    # Wait, if the goal is to maximize spending and we can pick a subset, 
    # we want to pick as many items as possible. 
    # But if we use all items, the sum is fixed. 
    # Let's assume the problem asks for the maximum sum of a subset 
    # that can be partitioned into 'days' groups satisfying the condition.
    
    # Correct Greedy Strategy for "Maximum Spending":
    # To satisfy sum(day_i) <= sum(day_i+1), we want the sums to be 
    # as close as possible or increasing.
    # Actually, if we can pick any subset, we should pick all items 
    # and check if they can be partitioned.
    
    # Given the prompt's hint: "Sort items by cost and use a greedy approach 
    # to pick the most expensive items first", this implies we might not 
    # use all items.
    
    # Let's refine: We want to pick a subset of items such that they can 
    # be partitioned into 'days' non-empty sets where sum(S_i) <= sum(S_{i+1}).
    
    # To maximize the sum, we try to include as many items as possible.
    # The most restrictive condition is the first day (must be <= second day).
    # The easiest way to satisfy the condition is to have the first day 
    # be very small and subsequent days be larger.
    
    # If we use all items, the total sum is sum(costs).
    # If we can't use all items, we want the largest sum.
    
    # Let's sort costs ascending.
    costs.sort()
    total_sum = sum(costs)
    
    # If we can partition all items, return total_sum.
    # A partition exists if we can pick 'days-1' items to be the first 'days-1' days,
    # and the remaining items form the last day, such that 
    # cost[0] <= cost[1] <= ... <= sum(remaining).
    # This is always possible if we have at least 'days' items 
    # by picking the smallest items for the first days.
    
    if n < days:
        return -1

    # The prompt implies a specific greedy logic. 
    # Let's implement the logic: Sort costs, and try to satisfy the 
    # condition using the largest possible items.
    
    # If the problem is: "Find max sum of a subset that can be partitioned"
    # and we must have 'days' groups.
    # The most efficient way to satisfy the condition is to have 
    # days-1 groups with 1 item each (the smallest ones) 
    # and 1 group with all other items.
    
    # However, if the prompt says "pick most expensive items first", 
    # it suggests we might be limited by the "sum(i) <= sum(i+1)" rule 
    # when picking large items.
    
    # Let's assume the standard interpretation: 
    # We want to pick a subset of items to maximize sum.
    # To satisfy the condition, the smallest sum must be <= the next.
    # The best way to maximize the sum is to use all items.
    # If we use all items, we just need to check if there exists 
    # a partition. A partition exists if we can pick 'days' groups.
    # The simplest partition is:
    # Day 1: costs[0]
    # Day 2: costs[1]
    # ...
    # Day days-1: costs[days-2]
    # Day days: sum(costs[days-1:])
    # This is valid if costs[0] <= costs[1] <= ... <= sum(costs[days-1:]).
    # Since costs is sorted, costs[i] <= costs[i+1] is true.
    # We only need to check if costs[days-2] <= sum(costs[days-1:]).
    
    # If the prompt implies we can't use all items, we'd use a 
    # different approach. But usually, "Maximum spending" with 
    # "all items" is a check.
    
    # Let's follow the prompt's specific hint: "Sort items... pick most expensive".
    # This usually applies to problems where you have a budget or a constraint.
    # If the constraint is the partition, and we want to maximize sum:
    # We can always include all items if n >= days and the partition exists.
    
    # Let's implement the partition check for all items.
    # If it fails, we'd need to remove items. But removing the smallest 
    # items is counter-productive to the sum. Removing the largest 
    # items might help satisfy the condition? No, that's backwards.
    
    # Let's re-read: "Maximum spending after buying items".
    # If we can't use all items, we want the largest subset.
    # If we can't satisfy the condition with all items, we must 
    # remove items until we can.
    # To keep the sum maximum, we should remove the smallest items? 
    # No, removing small items makes the "sum(i) <= sum(i+1)" harder 
    # to satisfy if the small items were the "base".
    # Actually, removing the largest items makes the sum(i+1) smaller.
    
    # Wait, if we have [10, 10, 10] and days=2. 
    # Day 1: 10, Day 2: 10. Sum = 20. (We didn't use the third 10).
    # If we used all: Day 1: 10, Day 2: 20. Sum = 30.
    
    # Let's use the logic: 
    # 1. Sort costs ascending.
    # 2. The total sum is maximized by using all items.
    # 3. A partition exists if we can find 'days' sums.
    # 4. The most flexible partition is (1 item, 1 item, ..., rest).
    # 5. If costs[days-2] > sum(costs[days-1:]), we must remove items.
    # To keep sum max, we should remove the smallest items? 
    # No, if we remove costs[0], the new costs[days-2] is the old costs[days-1].
    # This is getting complex. Let's stick to the most likely intended 
    # greedy: The total sum is sum(costs) if we can partition.
    # If we can't, we remove the smallest items until we can.
    
    # Actually, the most common version of this problem is:
    # You want to pick a subset of items.
    # The condition is sum(day_i) <= sum(day_i+1).
    # To maximize sum, we want to include as many items as possible.
    # If we include all items, we check the partition.
    # If we can't, we try removing the smallest item and check again.
    
    # Let's try the "all items" approach first.
    if n < days:
        return -1
    
    costs.sort()
    
    # Check if all items can be used
    # Smallest possible sums for first days-1 days are the smallest items.
    # The last day will have the sum of all remaining items.
    # We need costs[0] <= costs[1] <= ... <= costs[days-2] <= sum(costs[days-1:])
    
    # Since costs is sorted, costs[i] <= costs[i+1] is guaranteed.
    # We only need to check if costs[days-2] <= sum(costs[days-1:])
    
    current_sum_last_day = sum(costs[days-1:])
    if costs[days-2] <= current_sum_last_day:
        return sum(costs)
    
    # If not, we must remove items. To keep sum max, we remove the smallest.
    # But removing the smallest might not help if the bottleneck is 
    # costs[days-2] being too large.
    # Actually, if costs[days-2] > sum(costs[days-1:]), we need to 
    # either increase the last day's sum (by adding more items, but we used all)
    # or decrease costs[days-2] (by removing it).
    
    # If we remove costs[0], the new 'days-2' index is the old 'days-1'.
    # This is equivalent to saying we use a subset of size k.
    # For a fixed subset of size k, the best partition is 
    # (1, 1, ..., 1, k - (days-1)).
    # The condition is costs[days-2] <= sum(costs[days-1:k]).
    
    # Let's iterate on the number of items 'k' from n down to days.
    # For a fixed k, we pick the k largest items to maximize sum.
    # Then check if costs_subset[days-2] <= sum(costs_subset[days-1:k]).
    
    # Wait, if we pick the k largest items, the condition is 
    # harder to satisfy because costs[days-2] is larger.
    # So we should pick the k largest items AND check the condition.
    # If it fails, we try k-1.
    
    # Let's refine:
    # For k in range(n, days - 1, -1):
    #    subset = costs[n-k:] # k largest items
    #    if subset[days-2] <= sum(subset[days-1:]):
    #        return sum(subset)
    # return -1
    
    # This is O(n^2) in worst case. Let's optimize to O(n log n) or O(n).
    # The condition is: costs[n-k + days-2] <= sum(costs[n-k + days-1 : n])
    # Let's use prefix sums to make the sum check O(1).
    
    prefix_sums = [0] * (n + 1)
    for i in range(n):
        prefix_sums[i+1] = prefix_sums[i] + costs[i]
        
    def get_sum(l, r): # sum of costs[l:r]
        return prefix_sums[r] - prefix_sums[l]

    # We want to find the largest k such that:
    # costs[n - k + days - 2] <= get_sum(n - k + days - 1, n)
    
    # Since we want to maximize sum, and costs are positive, 
    # larger k is generally better.
    # However, the condition is not monotonic with k.
    # As k increases, the left side (costs[...]) increases and 
    # the right side (sum) increases.
    
    # Let's just iterate k from n down to days.
    for k in range(n, days - 1, -1):
        # The k largest items are costs[n-k : n]
        # The (days-1)-th item in this subset is at index (n-k) + (days-2)
        # The remaining items start at index (n-k) + (days-1)
        idx_threshold = n - k + days - 2
        idx_start_last_day = n - k + days - 1
        
        if costs[idx_threshold] <= get_sum(idx_start_last_day, n):
            return get_sum(n - k, n)
            
    return -1
