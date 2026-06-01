METADATA = {
    "id": 364,
    "name": "Nested List Weight Sum II",
    "slug": "nested-list-weight-sum-ii",
    "category": "Dynamic Programming / BFS",
    "aliases": [],
    "tags": ["dfs", "bfs", "recursion", "depth-first-search", "breadth-first-search"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Calculate the sum of integers in a nested list where each integer is multiplied by the sum of its depth and the depths of all subsequent levels.",
}

from typing import List, Union

class NestedInteger:
    """
    This is the interface that allows for accessing an element in a nested list.
    You should not implement it, or speculate about its implementation.
    """
    def isInteger(self) -> bool:
        """@return True if this NestedInteger holds a single integer, rather than a nested list."""
        pass

    def getInteger(self) -> int:
        """@return the integer if this NestedInteger holds a single integer, rather than a nested list."""
        pass

    def getList(self) -> List['NestedInteger']:
        """@return the nested list if this NestedInteger holds a nested list, rather than a single integer."""
        pass


def solve(nestedList: List[NestedInteger]) -> int:
    """
    Calculates the weighted sum of integers in a nested list.
    The weight of an integer is the sum of its depth and the depths of all subsequent levels.
    This is equivalent to: (sum of integers at level 1) * (total levels) + (sum of integers at level 2) * (total levels - 1) ...
    Or more simply: we maintain a running sum of all integers encountered so far and add that sum 
    to the total result every time we move down a level.

    Args:
        nestedList: A list of NestedInteger objects.

    Returns:
        The calculated weighted sum.

    Examples:
        >>> # Example 1: [[1,1],2,[1,1]]
        >>> # Level 0: [1, 1, 2, 1, 1] -> sum is 6.
        >>> # Level 1: [1, 1] -> sum is 2.
        >>> # Result: 6 + 2 = 8 (Wait, the logic is: sum of all integers at current level + previous running sum)
        >>> # Correct logic: 
        >>> # Level 0: 1, 1, 2, 1, 1. 
        >>> # Level 1: 1, 1.
        >>> # Total = (1+1+2+1+1) + (1+1) = 6 + 2 = 8.
        >>> return 8
    """
    total_sum = 0
    current_level_sum = 0
    queue = nestedList

    while queue:
        next_level_queue = []
        # current_level_sum tracks the sum of all integers found in all levels processed so far
        for nested_item in queue:
            if nested_item.isInteger():
                # If it's an integer, add it to the running sum of integers encountered
                val = nested_item.getInteger()
                current_level_sum += val
            else:
                # If it's a list, prepare to process its contents in the next iteration
                next_level_queue.extend(nested_item.getList())
        
        # The key insight: adding the current_level_sum to total_sum at each level 
        # effectively multiplies each integer by its 'remaining' depth.
        total_sum += current_level_sum
        queue = next_level_queue

    return total_sum

# Note: The solve function above implements the BFS approach which is optimal for this problem.
# The logic: 
# Level 0: sum_0 = integers_at_0. total = sum_0.
# Level 1: sum_1 = sum_0 + integers_at_1. total = sum_0 + (sum_0 + integers_at_1) = 2*sum_0 + integers_at_1.
# This is not quite right for the standard definition. Let's refine the logic:
# The problem asks for: sum(val * (depth + remaining_depths))
# Which is equivalent to: sum(val * depth) + sum(val * remaining_depths)
# A simpler way: 
# Let S_i be the sum of integers at level i.
# Total = S_0 * (depth_count) + S_1 * (depth_count - 1) ... is not it.
# The actual formula is: Total = S_0 + S_1 + ... + S_n (where S_i is the sum of all integers at level i AND all levels above it).
# Wait, the standard way to solve this is:
# Total = (Sum of integers at level 0) + (Sum of integers at level 1) + ...
# No, the weight is (depth + remaining_depths).
# Let's use the property: Weight(x) = depth(x) + (total_depths - depth(x)) = total_depths.
# Actually, the most robust way is:
# total_sum = 0, running_sum = 0
# For each level:
#   level_sum = sum of integers at this level
#   running_sum += level_sum
#   total_sum += running_sum
# This way, an integer at level 0 is added to total_sum in every iteration (depth times).
# An integer at level 1 is added to total_sum in every iteration from level 1 onwards.
# This matches the requirement.
