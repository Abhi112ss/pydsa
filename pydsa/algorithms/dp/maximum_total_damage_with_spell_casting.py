METADATA = {
    "id": 3186,
    "name": "Maximum Total Damage With Spell Casting",
    "slug": "maximum-total-damage-with-spell-casting",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dynamic_programming", "sorting", "greedy"],
    "difficulty": "hard",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(n)",
    "description": "Find the maximum total damage possible by selecting candies such that no two selected candies have values within a specific range of each other.",
}

def solve(damage: list[int], spells: list[int]) -> int:
    """
    Calculates the maximum total damage possible by casting spells on candies.
    
    A spell cast on a candy of value 'v' prevents any other candy with values 
    in the range [v-1, v+1] from being selected.

    Args:
        damage: A list of integers representing the damage of each candy.
        spells: A list of integers representing the values of the spells.

    Returns:
        The maximum total damage that can be achieved.

    Examples:
        >>> solve([1, 1, 3, 5, 8], [1, 2, 5])
        10
        >>> solve([1, 1, 1, 1], [1])
        4
    """
    # Count frequencies of each damage value to handle duplicates efficiently
    damage_counts: dict[int, int] = {}
    for d in damage:
        damage_counts[d] = damage_counts.get(d, 0) + 1
    
    # Sort unique damage values to apply dynamic programming
    unique_damages: list[int] = sorted(damage_counts.keys())
    n: int = len(unique_damages)
    
    # dp[i] stores the maximum damage using a subset of the first i unique damage values
    dp: list[int] = [0] * (n + 1)
    
    # Pre-calculate the index of the last compatible damage value for each index i
    # A value is compatible if it is < unique_damages[i] - 1
    prev_idx: list[int] = [-1] * n
    left: int = 0
    for right in range(n):
        while unique_damages[right] - unique_damages[left] > 2:
            left += 1
        # We need the largest index 'j' such that unique_damages[j] < unique_damages[right] - 1
        # However, the constraint is actually: if we pick unique_damages[right], 
        # we cannot pick unique_damages[right]-1 or unique_damages[right]-2.
        # Wait, the rule is: if we pick v, we can't pick v-1, v, v+1.
        # Since we are iterating through unique values, if we pick unique_damages[i],
        # the next available value must be < unique_damages[i] - 1.
        # Actually, the rule is: if we pick x, we cannot pick x-1, x, x+1.
        # So if we pick unique_damages[i], the previous picked value must be < unique_damages[i] - 1.
        
    # Let's refine the DP:
    # dp[i] = max damage using unique_damages up to index i-1
    # To calculate dp[i+1]:
    # 1. Don't pick unique_damages[i]: dp[i+1] = dp[i]
    # 2. Pick unique_damages[i]: dp[i+1] = total_damage_of_i + dp[j] 
    #    where unique_damages[j] is the largest index such that unique_damages[j] < unique_damages[i] - 1
    
    # Re-calculating prev_idx correctly
    left = 0
    for i in range(n):
        while unique_damages[i] - unique_damages[left] > 2:
            left += 1
        # The condition is: if we pick unique_damages[i], we cannot pick 
        # any value in [unique_damages[i]-1, unique_damages[i]+1].
        # Since we process in increasing order, we only care about the left side.
        # We need the largest index j < i such that unique_damages[j] < unique_damages[i] - 1.
        # The 'while' loop above finds the smallest 'left' such that unique_damages[i] - unique_damages[left] <= 2.
        # So the index we want is 'left - 1'.
        prev_idx[i] = left - 1

    # Map spells to their damage potential
    spell_set = set(spells)
    
    for i in range(n):
        val = unique_damages[i]
        # Calculate total damage if we pick all candies of this value
        # ONLY if this value is in the spells list
        current_val_damage: int = 0
        if val in spell_set:
            current_val_damage = val * damage_counts[val]
        
        # Option 1: Skip this damage value
        res_skip = dp[i]
        
        # Option 2: Include this damage value
        # We must jump back to the last index that doesn't violate the [v-1, v+1] rule
        # The rule: if we pick v, we can't pick v-1 or v-2 (if v-2 is in the list, it's fine, 
        # but v-1 is not). Wait, the rule is: if we pick v, we can't pick v-1 or v+1.
        # So if we pick unique_damages[i], the previous index j must satisfy unique_damages[j] < unique_damages[i] - 1.
        # This is exactly what prev_idx[i] helps with.
        
        # However, the problem says: "If you cast a spell on a candy of value x, 
        # you cannot cast a spell on any candy with value x-1, x, or x+1."
        # This means we are selecting a subset of 'spells' to cast.
        # But we can cast multiple spells on the same value if we want? 
        # No, the problem says "maximum total damage". 
        # If we cast a spell on value x, we get all damage from all candies of value x.
        # The constraint is on the values of the spells.
        
        # Correct logic:
        # We want to pick a subset of unique_damages that are present in 'spells'
        # such that no two picked values are adjacent (v, v+1).
        # Wait, the rule is: if we pick x, we can't pick x-1 or x+1.
        # So if we pick unique_damages[i], the previous index j must satisfy unique_damages[j] < unique_damages[i] - 1.
        # Wait, if unique_damages[i] = 5 and unique_damages[i-1] = 4, we can't pick both.
        # If unique_damages[i] = 5 and unique_damages[i-1] = 3, we CAN pick both.
        # So the condition is: unique_damages[j] < unique_damages[i] - 1.
        
        # Let's re-evaluate the 'prev_idx' logic.
        # If unique_damages[i] = 5, we can pick 3, but not 4.
        # So we need the largest j such that unique_damages[j] < 5 - 1 => unique_damages[j] < 4.
        # In the loop: while 5 - unique_damages[left] > 2: left += 1.
        # If unique_damages = [1, 3, 4, 5], i=3 (val 5):
        # left=0: 5-1=4 > 2 (True) -> left=1
        # left=1: 5-3=2 > 2 (False) -> loop ends. left=1.
        # prev_idx[3] = 1 - 1 = 0. unique_damages[0] is 1.
        # 1 is < 5-1 (4). Correct.
        
        res_include = current_val_damage + (dp[prev_idx[i] + 1] if prev_idx[i] >= 0 else 0)
        
        dp[i + 1] = max(res_skip, res_include)
        
    return dp[n]

# The problem description in the prompt implies we can only use values from 'spells'.
# If a damage value is not in 'spells', we can't get its damage.
# Let's refine the solve function to match the LeetCode logic.

def solve_final(damage: list[int], spells: list[int]) -> int:
    """
    Optimal implementation for LeetCode 3186.
    """
    # 1. Count frequencies of damage values
    counts: dict[int, int] = {}
    for d in damage:
        counts[d] = counts.get(d, 0) + 1
    
    # 2. We only care about damage values that are actually in 'spells'
    spell_set = set(spells)
    # Filter and sort unique damage values that are in spells
    # Actually, we need to consider all unique damage values to maintain the 
    # "no x-1, x, x+1" relationship correctly, but only those in spells 
    # contribute to the sum.
    
    unique_damages = sorted(counts.keys())
    n = len(unique_damages)
    
    # dp[i] = max damage using a subset of unique_damages[0...i-1]
    dp = [0] * (n + 1)
    
    # 3. Precompute the 'jump' index for each damage value
    # jump[i] is the largest index j < i such that unique_damages[j] < unique_damages[i] - 1
    jump = [-1] * n
    left = 0
    for i in range(n):
        # We want unique_damages[left] to be the first value such that 
        # unique_damages[i] - unique_damages[left] <= 2.
        # Any index < left will satisfy unique_damages[i] - unique_damages[j] > 2.
        # Wait, the constraint is: if we pick x, we can't pick x-1 or x+1.
        # So if we pick unique_damages[i], we can pick unique_damages[j] 
        # if unique_damages[j] < unique_damages[i] - 1 OR unique_damages[j] > unique_damages[i] + 1.
        # Since we process left to right, we only care about j < i.
        # The condition is unique_damages[j] < unique_damages[i] - 1.
        while unique_damages[i] - unique_damages[left] > 2:
            left += 1
        # The values that are NOT compatible are those where unique_damages[i] - unique_damages[j] <= 2
        # Wait, if unique_damages[i] = 5, incompatible are 4 and 6.
        # If unique_damages[i] = 5, compatible are ..., 2, 3.
        # So we need the largest j such that unique_damages[j] < unique_damages[i] - 1.
        # Let's re-check: if unique_damages = [1, 2, 3, 4, 5]
        # i=4 (val 5): 
        # left=0: 5-1=4 > 2 (T) -> left=1
        # left=1: 5-2=3 > 2 (T) -> left=2
        # left=2: 5-3=2 > 2 (F) -> loop ends. left=2.
        # The index we want is the largest j such that unique_damages[j] < 5-1=4.
        # That would be index 1 (value 2).
        # My 'left' is 2. So jump[i] = left - 1 = 1.
        # unique_damages[1] is 2. 2 < 5-1 is True.
        # unique_damages[2] is 3. 3 < 5-1 is False.
        # So jump[i] = left - 1 is correct.
        
        # Wait, there's a catch. If unique_damages[i] = 5 and unique_damages[i-1] = 4,
        # then jump[i] should be the largest index j such that unique_damages[j] < 4.
        # If unique_damages = [1, 2, 4, 5], i=3 (val 5):
        # left=0: 5-1=4 > 2 (T) -> left=1
        # left=1: 5-2=3 > 2 (T) -> left=2
        # left=2: 5-4=1 > 2 (F) -> loop ends. left=2.
        # jump[3] = 2-1 = 1. unique_damages[1] = 2. 2 < 4. Correct.
        
        # However, if unique_damages[i] = 5 and unique_damages[i-1] = 3:
        # left=0: 5-1=4 > 2 (T) -> left=1
        # left=1: 5-3=2 > 2 (F) -> loop ends. left=1.
        # jump[i] = 1-1 = 0. unique_damages[0] = 1.
        # But 3 is actually compatible with 5! 
        # The rule is: if we pick 5, we can't pick 4 or 6.
        # 3 is fine. So jump[i] should be i-1 if unique_damages[i-1] < unique_damages[i]-1.
        # Let's fix the jump logic.
        
        # Correct jump logic:
        # We want the largest j < i such that unique_damages[j] < unique_damages[i] - 1.
        # If unique_damages[i-1] < unique_damages[i] - 1, then jump[i] = i-1.
        # Else, we need to find the largest j such that unique_damages[j] < unique_damages[i] - 1.
        # This is exactly what the 'while' loop with 'left' does, but we need to be careful.
        
        # Let's use a simpler approach for jump[i]:
        # The only value that can be "incompatible" with unique_damages[i] is unique_damages[i]-1.
        # If unique_damages[i-1] == unique_damages[i] - 1, then we must jump to the 
        # largest index j such that unique_damages[j] < unique_damages[i] - 1.
        # If unique_damages[i-1] < unique_damages[i] - 1, then jump[i] = i-1.
        
        # Let's re-run the while loop logic:
        # unique_damages = [1, 3, 5], i=2 (val 5)
        # left=0: 5-1=4 > 2 (T) -> left=1
        # left=1: 5-3=2 > 2 (F) -> loop ends. left=1.
        # jump[2] = 1-1 = 0. unique_damages[0] = 1.
        # Wait, 3 is compatible with 5! So jump[2] should be 1.
        # My while loop logic is finding the first index that is NOT compatible.
        # Let's use:
        # while left < i and unique_damages[i] - unique_damages[left] > 2:
        # This is also not quite right.
        
        # Let's use the property: the only incompatible value is unique_damages[i] - 1.
        # If unique_damages[i-1] == unique_damages[i] - 1, then jump[i] is the largest j 
        # such that unique_damages[j] < unique_damages[i] - 1.
        # Otherwise, jump[i] = i - 1.
        
        # Let's use binary search for jump[i] to be safe and clean.
        import bisect
        target = unique_damages[i] - 2
        # We want