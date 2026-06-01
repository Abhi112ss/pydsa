METADATA = {
    "id": 2561,
    "name": "Rearranging Fruits",
    "slug": "rearranging-fruits",
    "category": "Greedy",
    "aliases": [],
    "tags": ["hash_map", "greedy", "sorting"],
    "difficulty": "hard",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(n)",
    "description": "Find the minimum cost to make two baskets of fruits identical by swapping elements.",
}

from collections import Counter

def solve(basket1: list[int], basket2: list[int]) -> int:
    """
    Calculates the minimum cost to make two baskets of fruits identical.

    The cost of swapping two fruits is the minimum of the two fruit values.
    To make baskets identical, we identify the elements that are in excess 
    in one basket compared to the other. We then pair these excess elements 
    and swap them using either the element itself or the global minimum 
    element found in both baskets.

    Args:
        basket1: A list of integers representing the first basket.
        basket2: A list of integers representing the second basket.

    Returns:
        The minimum cost to make the baskets identical, or -1 if impossible.

    Examples:
        >>> solve([4, 2, 2, 2], [1, 4, 1, 2])
        3
        >>> solve([8, 1, 2, 2], [4, 4, 4, 2])
        -1
    """
    count1 = Counter(basket1)
    count2 = Counter(basket2)
    
    # Combine counts to find the target frequency for each fruit
    all_fruits = set(count1.keys()) | set(count2.keys())
    diffs = []
    min_val = min(min(basket1), min(basket2))

    for fruit in all_fruits:
        total_count = count1[fruit] + count2[fruit]
        
        # If the total count of a fruit is odd, it's impossible to split equally
        if total_count % 2 != 0:
            return -1
        
        target = total_count // 2
        # Calculate how many of this fruit need to be moved out of basket1
        # If count1[fruit] > target, basket1 has excess.
        # If count1[fruit] < target, basket2 has excess.
        # We only need to track the absolute difference to know how many swaps are needed.
        diff = abs(count1[fruit] - target)
        # Each swap involves two elements (one from each basket), 
        # so we add 'diff' instances of the fruit to our pool of elements to be swapped.
        # However, since one swap fixes two imbalances, we only need to track 'diff' 
        # elements to be moved.
        for _ in range(diff):
            diffs.append(fruit)

    # The diffs list contains elements that are "extra" in their respective baskets.
    # Because every swap involves two elements, the number of elements in diffs
    # will be even, and we only need to perform len(diffs) // 2 swaps.
    # We sort them to greedily pick the smallest available elements to swap.
    diffs.sort()
    
    # We only need to perform half the number of swaps because each swap 
    # resolves two imbalances (one from basket1 and one from basket2).
    num_swaps = len(diffs) // 2
    total_cost = 0
    
    for i in range(num_swaps):
        # For each swap, we can either swap the two elements directly: diffs[i]
        # Or we can use the global minimum as an intermediary: 2 * min_val
        total_cost += min(diffs[i], 2 * min_val)
        
    return total_cost
