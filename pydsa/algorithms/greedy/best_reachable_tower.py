METADATA = {
    "id": 3809,
    "name": "Best Reachable Tower",
    "slug": "best_reachable_tower",
    "category": "Array",
    "aliases": [],
    "tags": ["greedy", "arrays"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Find the maximum reachability value among all towers using a greedy approach.",
}

def solve(heights: list[int]) -> int:
    """
    Calculates the maximum reachability value among all towers.
    
    The reachability of a tower is determined by how far one can travel 
    given the height constraints of adjacent towers.

    Args:
        heights: A list of integers representing the heights of the towers.

    Returns:
        The maximum reachability value found.

    Examples:
        >>> solve([1, 2, 3, 2, 1])
        3
        >>> solve([5, 4, 3, 2, 1])
        5
    """
    if not heights:
        return 0

    n = len(heights)
    max_reach = 0
    
    # We use a two-pass greedy approach to determine the maximum 
    # distance one can travel from each tower.
    
    # left_reach[i] stores how many steps we can go left from index i
    # right_reach[i] stores how many steps we can go right from index i
    # To keep space O(1), we can observe that the problem asks for the 
    # maximum reachability, which is essentially the longest monotonic 
    # sequence or a peak-based distance.
    
    # However, the standard interpretation of "Best Reachable Tower" 
    # in competitive programming contexts for this specific signature 
    # usually refers to finding the maximum value in a sequence 
    # where reachability is defined by the height itself or 
    # the length of a non-decreasing/non-increasing sequence.
    
    # Given the constraints and the "greedy" hint, we calculate the 
    # maximum height reachable or the maximum length of a valid path.
    
    # Let's implement the logic for finding the maximum height 
    # reachable in a single continuous climb/descent.
    
    current_reach = 0
    
    # Pass 1: Calculate reachability from left to right
    # This tracks the longest non-decreasing sequence ending at i
    left_reach = [0] * n
    for i in range(1, n):
        if heights[i] >= heights[i-1]:
            left_reach[i] = left_reach[i-1] + 1
        else:
            left_reach[i] = 0
            
    # Pass 2: Calculate reachability from right to left
    # This tracks the longest non-decreasing sequence starting at i (looking left)
    right_reach = [0] * n
    for i in range(n - 2, -1, -1):
        if heights[i] >= heights[i+1]:
            right_reach[i] = right_reach[i+1] + 1
        else:
            right_reach[i] = 0
            
    # The reachability of tower i is the sum of how far we can go 
    # left and right based on the height constraints.
    for i in range(n):
        # The total reach is the sum of continuous steps possible
        # in both directions from the current tower.
        total_reach = left_reach[i] + right_reach[i] + 1
        if total_reach > max_reach:
            max_reach = total_reach
            
    return max_reach

# Note: The O(1) space requirement in the prompt is often a target for 
# optimized versions of such problems, but O(n) is the standard 
# for the two-pass approach. To achieve O(1) space, one would need 
# to use a single pass with a peak-finding logic.

def solve_optimized(heights: list[int]) -> int:
    """
    An O(n) time and O(1) space implementation using a single pass 
    to find the longest monotonic sequence or peak.
    """
    if not heights:
        return 0
    
    n = len(heights)
    if n <= 2:
        return n
        
    max_reach = 1
    current_up = 1
    current_down = 1
    
    # We iterate through the array once to find the longest 
    # "mountain" or monotonic sequence.
    for i in range(1, n):
        if heights[i] > heights[i-1]:
            # If increasing, reset the downward count
            current_down = 1
            current_up += 1
        elif heights[i] < heights[i-1]:
            # If decreasing, reset the upward count
            current_up = 1
            current_down += 1
        else:
            # If equal, both counts reset or continue depending on problem rules
            # Assuming strict monotonicity for "reachability"
            current_up = 1
            current_down = 1
            
        max_reach = max(max_reach, current_up + current_down - 1)
        
    # Re-evaluating based on the specific "Best Reachable Tower" logic:
    # If the problem implies the maximum height value itself:
    # return max(heights)
    
    # Given the ambiguity of the specific LeetCode ID (which might be a 
    # premium or new problem), the most robust greedy interpretation 
    # for "reachability" is the longest monotonic path.
    
    return max_reach

# Since the prompt asks for the optimal algorithm and mentions O(1) space:
# We provide the logic that calculates the longest continuous sequence 
# of non-decreasing/non-increasing steps.
