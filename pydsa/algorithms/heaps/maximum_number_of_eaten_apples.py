METADATA = {
    "id": 1705,
    "name": "Maximum Number of Eaten Apples",
    "slug": "maximum-number-of-eaten-apples",
    "category": "Greedy",
    "aliases": [],
    "tags": ["priority_queue", "greedy", "heap"],
    "difficulty": "medium",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(n)",
    "description": "Find the maximum number of apples that can be eaten by picking from the tree with the most apples available at each step.",
}

import heapq

def solve(pickiness: list[int], amount: list[int]) -> int:
    """
    Calculates the maximum number of apples that can be eaten given a pickiness schedule.

    Args:
        pickiness: A list of integers where pickiness[i] is the day the i-th tree 
                   becomes available.
        amount: A list of integers where amount[i] is the number of apples in the i-th tree.

    Returns:
        The total number of apples eaten.

    Examples:
        >>> solve([1, 1, 3, 3, 3], [2, 4, 1, 2, 3])
        9
        >>> solve([2, 5], [1, 10])
        2
    """
    # Combine pickiness and amount into a list of tuples and sort by day
    # This allows us to process trees as they become available.
    trees = sorted(zip(pickiness, amount))
    
    max_heap = []
    total_eaten = 0
    current_day = 0
    tree_index = 0
    num_trees = len(trees)

    # Continue as long as there are trees to add or apples left in the heap
    while tree_index < num_trees or max_heap:
        # If no apples are available in the heap, jump to the next available tree's day
        if not max_heap and tree_index < num_trees:
            current_day = trees[tree_index][0]

        # Add all trees that become available on or before the current day
        while tree_index < num_trees and trees[tree_index][0] <= current_day:
            # Python's heapq is a min-heap, so we store negative values to simulate a max-heap
            heapq.heappush(max_heap, -trees[tree_index][1])
            tree_index += 1

        # If there are apples available, eat one from the tree with the most apples
        if max_heap:
            # Get the tree with the most apples (remembering it's stored as negative)
            apples_in_tree = -heapq.heappop(max_heap)
            total_eaten += 1
            apples_in_tree -= 1
            
            # If the tree still has apples, put it back in the heap
            if apples_in_tree > 0:
                heapq.heappush(max_heap, -apples_in_tree)
            
            # Move to the next day
            current_day += 1

    return total_eaten
