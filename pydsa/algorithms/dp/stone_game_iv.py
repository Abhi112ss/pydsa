METADATA = {
    "id": 1510,
    "name": "Stone Game IV",
    "slug": "stone-game-iv",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dp", "bit_manipulation", "game_theory"],
    "difficulty": "hard",
    "time_complexity": "O(2^n)",
    "space_complexity": "O(2^n)",
    "description": "Determine if the first player can win a game where players remove trailing stones and the remaining stones are split into two groups.",
}

def solve(stones: list[int]) -> bool:
    """
    Determines if the first player can win the stone game.

    The game involves players choosing to remove all trailing stones or 
    splitting the remaining stones into two groups. A player wins if 
    they can make a move that leaves the opponent in a losing state.

    Args:
        stones: A list of integers representing the stones.

    Returns:
        True if the first player can win, False otherwise.

    Examples:
        >>> solve([1, 1, 1, 1])
        True
        >>> solve([1, 1, 1])
        True
        >>> solve([1, 1])
        True
    """
    n = len(stones)
    # memo stores whether a specific configuration of stones (represented by a bitmask)
    # is a winning state for the player whose turn it is.
    memo: dict[int, bool] = {}

    def can_win(mask: int) -> bool:
        """
        Recursive helper using bitmasking to represent the current set of stones.
        
        Args:
            mask: An integer where the i-th bit is 1 if the i-th stone is present.
        """
        if mask == 0:
            return False
        
        if mask in memo:
            return memo[mask]

        # Option 1: Remove all trailing stones.
        # Find the index of the rightmost set bit.
        rightmost_index = 0
        temp_mask = mask
        while temp_mask > 0 and not (temp_mask & 1):
            temp_mask >>= 1
            rightmost_index += 1
        
        # Create a new mask by removing all stones from rightmost_index to the end.
        # This is done by masking with a value that has 1s only up to rightmost_index - 1.
        # However, the problem says "remove all trailing stones", meaning if stones are 
        # [1, 1, 1, 1], removing trailing stones leaves [1, 1, 1].
        # Actually, the rule is: remove all stones from the right end that are the same.
        # But the problem simplifies this: "remove all trailing stones" means 
        # if the stones are [1, 1, 1, 1], you can remove the last 1, or last two, etc.
        # Wait, the rule is: "remove all trailing stones" OR "split the remaining".
        # Let's re-read: "remove all trailing stones" means if stones are [1, 1, 1, 1], 
        # you can remove the last 1, or the last two, etc. 
        # Actually, the standard interpretation for this problem is:
        # 1. Remove all stones from the right end that are identical.
        # 2. Split the remaining stones into two groups.
        
        # Let's find the actual trailing stones.
        # The mask represents the current stones. We need to find how many 
        # consecutive stones at the end of the current mask are identical.
        
        # Find the index of the last stone (rightmost bit set)
        last_stone_idx = -1
        for i in range(n):
            if (mask >> i) & 1:
                last_stone_idx = i
        
        # Find how many identical stones are at the end
        count = 0
        current_val = -1
        # We iterate backwards from the last_stone_idx
        for i in range(last_stone_idx, -1, -1):
            if (mask >> i) & 1:
                if current_val == -1:
                    current_val = stones[i]
                
                if stones[i] == current_val:
                    count += 1
                else:
                    break
            else:
                # If the bit is 0, it's not part of the current game state
                continue
        
        # Move 1: Remove 'k' trailing stones where 1 <= k <= count
        # If any of these moves leads to a state where the opponent cannot win, we win.
        for k in range(1, count + 1):
            # New mask: remove k stones from the end
            # We need to find the index of the stone that is 'k' positions from the end
            # of the current active stones.
            
            # To simplify: the mask represents the indices of stones currently in play.
            # Let's find the indices of the stones currently in the mask.
            active_indices = [i for i in range(n) if (mask >> i) & 1]
            
            # Option 1: Remove k trailing stones
            # The trailing stones are the last k elements in active_indices
            new_mask_remove = mask
            for j in range(k):
                new_mask_remove &= ~(1 << active_indices[-(j + 1)])
            
            if not can_win(new_mask_remove):
                memo[mask] = True
                return True
            
            # Option 2: Split the remaining stones into two groups
            # The remaining stones are active_indices[:-k]
            # We split them at every possible position 'p'
            remaining_indices = active_indices[:len(active_indices) - k]
            if remaining_indices:
                for p in range(1, len(remaining_indices)):
                    # Group 1: remaining_indices[:p], Group 2: remaining_indices[p:]
                    # The problem says "the remaining stones are split into two groups"
                    # This means the new state is the bitwise OR of the two groups? 
                    # No, it means the new state is the set of stones in BOTH groups.
                    # Wait, the rule is: "the remaining stones are split into two groups... 
                    # the next player chooses one of the two groups".
                    # This means the new mask is either the mask of Group 1 or Group 2.
                    
                    mask_group1 = 0
                    for idx in remaining_indices[:p]:
                        mask_group1 |= (1 << idx)
                    
                    mask_group2 = 0
                    for idx in remaining_indices[p:]:
                        mask_group2 |= (1 << idx)
                        
                    if not can_win(mask_group1) or not can_win(mask_group2):
                        memo[mask] = True
                        return True
        
        # If no move leads to an opponent's loss, current player loses.
        memo[mask] = False
        return False

    # The logic above is slightly inefficient due to list creation. 
    # Let's optimize the bitmasking approach.
    
    memo = {}

    def solve_recursive(mask: int) -> bool:
        if mask == 0:
            return False
        if mask in memo:
            return memo[mask]
        
        # Get indices of set bits
        indices = []
        for i in range(n):
            if (mask >> i) & 1:
                indices.append(i)
        
        # 1. Remove trailing stones
        # Find how many trailing stones have the same value
        last_idx = indices[-1]
        val = stones[last_idx]
        count = 0
        for i in range(len(indices) - 1, -1, -1):
            if stones[indices[i]] == val:
                count += 1
            else:
                break
        
        # Try removing k trailing stones
        for k in range(1, count + 1):
            # New mask after removing k stones
            new_mask = mask
            for i in range(k):
                new_mask &= ~(1 << indices[-(i + 1)])
            
            if not solve_recursive(new_mask):
                memo[mask] = True
                return True
            
            # 2. Split the remaining stones into two groups
            # The remaining stones are indices[:len(indices)-k]
            rem_indices = indices[:len(indices) - k]
            if len(rem_indices) >= 2:
                for p in range(1, len(rem_indices)):
                    # Group 1
                    m1 = 0
                    for idx in rem_indices[:p]:
                        m1 |= (1 << idx)
                    if not solve_recursive(m1):
                        memo[mask] = True
                        return True
                    
                    # Group 2
                    m2 = 0
                    for idx in rem_indices[p:]:
                        m2 |= (1 << idx)
                    if not solve_recursive(m2):
                        memo[mask] = True
                        return True
                        
        memo[mask] = False
        return False

    # The actual problem constraints and rules:
    # "remove all trailing stones" -> if stones are [1,1,1,1], you can remove 1, 2, 3, or 4 stones.
    # "split the remaining stones" -> if you have [1,1,1] left, you can split into [1] and [1,1] 
    # or [1,1] and [1].
    
    # Let's use a more direct approach for the bitmask.
    memo = {}
    
    def dp(mask: int) -> bool:
        if mask == 0:
            return False
        if mask in memo:
            return memo[mask]
        
        # Find indices of stones currently in the game
        current_indices = [i for i in range(n) if (mask >> i) & 1]
        
        # Option 1: Remove k trailing stones
        # Find how many stones at the end of current_indices have the same value
        last_val = stones[current_indices[-1]]
        trailing_count = 0
        for i in range(len(current_indices) - 1, -1, -1):
            if stones[current_indices[i]] == last_val:
                trailing_count += 1
            else:
                break
        
        # Try removing k stones (1 to trailing_count)
        for k in range(1, trailing_count + 1):
            # New mask is current mask minus the last k indices
            new_mask = mask
            for i in range(1, k + 1):
                new_mask &= ~(1 << current_indices[-i])
            
            if not dp(new_mask):
                memo[mask] = True
                return True
            
            # Option 2: Split the remaining stones into two groups
            # The remaining stones are current_indices[:len(current_indices)-k]
            remaining = current_indices[:len(current_indices) - k]
            if len(remaining) >= 2:
                for split_point in range(1, len(remaining)):
                    # Group 1
                    m1 = 0
                    for idx in remaining[:split_point]:
                        m1 |= (1 << idx)
                    if not dp(m1):
                        memo[mask] = True
                        return True
                    
                    # Group 2
                    m2 = 0
                    for idx in remaining[split_point:]:
                        m2 |= (1 << idx)
                    if not dp(m2):
                        memo[mask] = True
                        return True
                        
        memo[mask] = False
        return False

    return dp((1 << n) - 1)
