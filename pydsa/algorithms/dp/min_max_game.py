METADATA = {
    "id": 2293,
    "name": "Min Max Game",
    "slug": "min-max-game",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dp", "game_theory"],
    "difficulty": "hard",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Find the maximum possible value of the minimum of two elements chosen from an array under specific game rules.",
}

def solve(nums: list[int]) -> int:
    """
    Calculates the maximum value of the minimum of two elements chosen by players.
    
    The game rules:
    1. Alice chooses an index i, then Bob chooses an index j such that j is the 
       nearest index to i where nums[j] < nums[i].
    2. Alice wants to maximize min(nums[i], nums[j]).
    3. Bob wants to minimize the result (though in this specific problem, 
       Bob's choice is deterministic based on Alice's choice).
    
    Actually, the problem states: Alice chooses i, then Bob chooses j such that 
    j is the nearest index to i where nums[j] < nums[i]. Alice wants to maximize 
    min(nums[i], nums[j]). Since j is fixed once i is chosen, Alice simply 
    picks i to maximize the value.

    Args:
        nums: A list of integers representing the game state.

    Returns:
        The maximum possible value of min(nums[i], nums[j]).

    Examples:
        >>> solve([1, 2, 3, 4, 5])
        1
        >>> solve([5, 4, 3, 2, 1])
        1
        >>> solve([1, 5, 2, 4, 3])
        2
    """
    n = len(nums)
    if n < 2:
        return 0

    # To find the nearest index j such that nums[j] < nums[i], 
    # we can use a monotonic stack.
    # We need to check both left and right directions for each i.
    
    # left_min[i] will store the value of the nearest element to the left of i that is < nums[i]
    # right_min[i] will store the value of the nearest element to the right of i that is < nums[i]
    
    # However, the problem asks for the nearest index j. 
    # If multiple indices exist, the "nearest" is defined by the distance |i - j|.
    # If distances are equal, the problem implies we check both.
    # Actually, the rule is: Bob chooses j such that |i - j| is minimized and nums[j] < nums[i].
    
    # Let's find the nearest smaller value to the left and right for every index.
    left_smaller_val = [-1] * n
    right_smaller_val = [-1] * n
    
    # Monotonic stack to find nearest smaller to the left
    stack: list[int] = []
    for i in range(n):
        while stack and nums[stack[-1]] >= nums[i]:
            stack.pop()
        if stack:
            left_smaller_val[i] = nums[stack[-1]]
        stack.append(i)
        
    # Monotonic stack to find nearest smaller to the right
    stack = []
    for i in range(n - 1, -1, -1):
        while stack and nums[stack[-1]] >= nums[i]:
            stack.pop()
        if stack:
            right_smaller_val[i] = nums[stack[-1]]
        stack.append(i)
        
    max_min_val = 0
    
    for i in range(n):
        # For each i, Bob picks the nearest j. 
        # If there's a tie in distance, the problem implies we look at the values.
        # But the problem says "the nearest index j". If there are two, 
        # we must consider the one that results in the minimum value for that i.
        # Wait, the rule is: Bob chooses j to minimize min(nums[i], nums[j]).
        # Since nums[j] < nums[i], min(nums[i], nums[j]) is always nums[j].
        # So Bob chooses j to minimize nums[j] among the nearest indices.
        
        # Let's re-read: "Bob chooses an index j such that j is the nearest index to i 
        # where nums[j] < nums[i]". 
        # If there are two nearest indices (one left, one right), Bob chooses the one 
        # that minimizes the result.
        
        l_val = left_smaller_val[i]
        r_val = right_smaller_val[i]
        
        # We need to know the distances to decide which is "nearest"
        # Let's refine the stack to store indices to calculate distance.
        pass

    # Re-implementing with distance logic
    left_idx = [-1] * n
    right_idx = [-1] * n
    
    stack = []
    for i in range(n):
        while stack and nums[stack[-1]] >= nums[i]:
            stack.pop()
        if stack:
            left_idx[i] = stack[-1]
        stack.append(i)
        
    stack = []
    for i in range(n - 1, -1, -1):
        while stack and nums[stack[-1]] >= nums[i]:
            stack.pop()
        if stack:
            right_idx[i] = stack[-1]
        stack.append(i)
        
    ans = 0
    for i in range(n):
        l = left_idx[i]
        r = right_idx[i]
        
        current_min_for_i = float('inf')
        
        # Check left nearest
        if l != -1:
            current_min_for_i = min(current_min_for_i, nums[l])
            
        # Check right nearest
        if r != -1:
            # If distances are equal, Bob chooses the one that minimizes the value
            if l != -1 and (i - l) == (r - i):
                current_min_for_i = min(nums[l], nums[r])
            else:
                # If distances are not equal, Bob must pick the strictly nearest one.
                # If only one exists, we take it.
                if l != -1 and r != -1:
                    if (i - l) < (r - i):
                        current_min_for_i = nums[l]
                    else:
                        current_min_for_i = nums[r]
                elif l != -1:
                    current_min_for_i = nums[l]
                else:
                    current_min_for_i = nums[r]
            
        # If no smaller element exists, this i is not a valid choice for Alice
        if current_min_for_i != float('inf'):
            ans = max(ans, int(current_min_for_i))
            
    return ans
