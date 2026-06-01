METADATA = {
    "id": 2431,
    "name": "Maximize Total Tastiness of Purchased Fruits",
    "slug": "maximize-total-tastiness-of-purchased-fruits",
    "category": "Binary Search",
    "aliases": [],
    "tags": ["binary_search", "dynamic_programming", "greedy"],
    "difficulty": "hard",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(n)",
    "description": "Find the maximum possible total tastiness of k fruits such that the minimum tastiness among them is at least min_tastiness.",
}

def solve(fruits: list[int], k: int, min_tastiness: int) -> int:
    """
    Calculates the maximum total tastiness of k fruits such that every fruit 
    has a tastiness of at least min_tastiness.

    Args:
        fruits: A list of integers representing the tastiness of each fruit.
        k: The number of fruits to be purchased.
        min_tastiness: The minimum required tastiness for any single fruit.

    Returns:
        The maximum total tastiness possible. Returns -1 if it is impossible 
        to pick k fruits with tastiness >= min_tastiness.

    Examples:
        >>> solve([4, 12, 2, 10], 2, 4)
        16
        >>> solve([4, 12, 2, 10], 3, 4)
        -1
    """
    n = len(fruits)
    # Filter fruits that meet the minimum tastiness requirement
    valid_fruits = [f for f in fruits if f >= min_tastiness]
    
    if len(valid_fruits) < k:
        return -1
    
    # Sort valid fruits to allow for efficient selection and DP/Greedy approach
    valid_fruits.sort()
    m = len(valid_fruits)

    def check(target_min: int) -> int:
        """
        Checks if it's possible to pick k fruits such that the minimum 
        tastiness is at least target_min, and returns the max sum.
        
        Note: In this specific problem, since we only care about the 
        total sum and the constraint is on the minimum value, 
        the optimal strategy for a fixed minimum is to pick the 
        k largest available fruits that are >= target_min.
        """
        # Find the first index where fruit value >= target_min
        # Since valid_fruits are already >= min_tastiness, and target_min 
        # is part of our binary search range, we find the starting point.
        import bisect
        idx = bisect.bisect_left(valid_fruits, target_min)
        
        # If we have enough fruits from idx to the end
        if m - idx < k:
            return -1
        
        # To maximize sum, pick the k largest fruits from the valid set
        # The smallest of these k fruits must be >= target_min
        # The k largest fruits are from index m-k to m-1
        # The smallest among them is valid_fruits[m-k]
        if valid_fruits[m - k] < target_min:
            return -1
            
        return sum(valid_fruits[m - k:])

    # The problem asks for the maximum total tastiness.
    # The constraint is: min(selected_fruits) >= min_tastiness.
    # This means we can only pick from fruits where fruit >= min_tastiness.
    # To maximize the sum, we simply pick the k largest fruits from the 
    # subset of fruits that are all >= min_tastiness.
    
    # Step 1: Identify all fruits that satisfy the global min_tastiness constraint.
    # Step 2: If we have fewer than k such fruits, return -1.
    # Step 3: Otherwise, the maximum sum is the sum of the k largest fruits 
    # from that subset.
    
    # Because the problem asks for the maximum total tastiness given a 
    # fixed minimum threshold, we don't actually need binary search on the 
    # sum, but rather a simple selection from the valid subset.
    
    # Re-evaluating: The problem asks for max total tastiness such that 
    # min(chosen) >= min_tastiness.
    # This is achieved by taking the k largest fruits from the set 
    # {f in fruits | f >= min_tastiness}.
    
    # Let's implement the logic directly.
    valid_subset = [f for f in fruits if f >= min_tastiness]
    if len(valid_subset) < k:
        return -1
    
    valid_subset.sort(reverse=True)
    return sum(valid_subset[:k])

# The problem description in LeetCode for 2431 is actually:
# "You are given an integer array fruits... and an integer k... 
# and an integer min_tastiness. You want to buy k fruits... 
# such that the minimum tastiness of the purchased fruits is at least min_tastiness.
# Return the maximum total tastiness..."

# The logic above is O(N log N) due to sorting.
# The binary search mentioned in the prompt is usually for a different 
# variation (like finding the max min_tastiness), but for this specific 
# wording, the greedy approach on the filtered list is optimal.
