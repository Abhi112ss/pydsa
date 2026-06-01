METADATA = {
    "id": 2120,
    "name": "Execution of All Suffix Instructions Staying in a Grid",
    "slug": "execution_of_all_suffix_instructions_staying_in_a_grid",
    "category": "Simulation",
    "aliases": [],
    "tags": ["greedy", "simulation"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Find the maximum length of a suffix of instructions that can be executed without moving out of the grid boundaries.",
}

def solve(instructions: list[str], n: int) -> int:
    """
    Finds the maximum length of a suffix of instructions that can be executed 
    starting from (0, 0) without leaving the n x n grid.

    Args:
        instructions: A list of strings representing directions ('U', 'D', 'L', 'R').
        n: The size of the n x n grid.

    Returns:
        The length of the longest suffix of instructions that can be executed.

    Examples:
        >>> solve(["U", "R", "L", "D", "U", "R", "L", "D"], 3)
        4
        >>> solve(["U", "U", "U", "U"], 3)
        0
    """
    # Map directions to coordinate changes (row, col)
    direction_map = {
        'U': (-1, 0),
        'D': (1, 0),
        'L': (0, -1),
        'R': (0, 1)
    }

    # To find the longest suffix, we can iterate backwards from the end of the list.
    # However, the problem asks for the suffix starting from some index i to the end.
    # A suffix of length k means we start at index len(instructions) - k.
    # Since we need to know if the *entire* suffix is valid, we can simulate 
    # the movement from the end towards the beginning to see how far back we can go.
    
    # Actually, the simplest way to find the longest suffix is to check 
    # suffixes of decreasing length, but that's O(n^2).
    # To achieve O(n), we observe that if a suffix of length k is valid, 
    # it doesn't necessarily mean a suffix of length k-1 is valid (because the 
    # starting position for the suffix of length k-1 is different).
    
    # Wait, the problem states: "the suffix of instructions starting from index i".
    # If we start at index i, we start at (0,0).
    # Let's simulate the instructions from the end to the beginning.
    # If we start at index i, we follow instructions[i], instructions[i+1]...
    # This is equivalent to saying: if we start at index i, we must stay in bounds.
    
    # Let's use the property that we only care about the "worst" displacement.
    # For a suffix starting at i, the path is:
    # pos(i, j) = (0,0) + sum(dir[k] for k in range(i, j+1))
    # We need min_row >= 0, max_row < n, min_col >= 0, max_col < n for all j in [i, len-1].
    
    # Let's re-evaluate: The instructions are executed starting from (0,0).
    # If we pick suffix starting at index i, we start at (0,0) and follow instructions[i...end].
    
    # We can pre-calculate the total displacement of the suffix.
    # But a better way: Iterate from the end of the instructions.
    # Let's track the relative movement required to stay in bounds.
    # For a suffix starting at index i, let the path be P_i.
    # P_i[j] = P_{i+1}[j] + direction[i].
    # This is still slightly complex. Let's use the "backwards" approach.
    
    # Let's track the bounds of the path if we were to start at (0,0) 
    # and follow instructions from index i to the end.
    # Let's define:
    # min_r[i], max_r[i], min_c[i], max_c[i] as the bounds of the path 
    # starting from (0,0) using instructions from i to end.
    
    # To compute this in O(n), we iterate backwards:
    # If we add instruction i (dir) to the front of the suffix [i+1...end]:
    # The new path is: (0,0), (0,0)+dir, (0,0)+dir+dir_{i+1}, ...
    # The new bounds are:
    # new_min_r = min(0, dir_r + min_r[i+1])
    # new_max_r = max(0, dir_r + max_r[i+1])
    # ... and so on.
    
    num_instr = len(instructions)
    # current_min_r, current_max_r, current_min_c, current_max_c
    # represent the bounds of the path starting from (0,0) for the current suffix.
    curr_min_r, curr_max_r = 0, 0
    curr_min_c, curr_max_c = 0, 0
    
    # We also need to track the total displacement of the suffix to "shift" the bounds.
    # However, the logic above (new_min = min(0, dir + old_min)) 
    # correctly simulates starting at (0,0) and prepending a move.
    
    max_suffix_len = 0
    
    # Iterate backwards through the instructions
    for i in range(num_instr - 1, -1, -1):
        dr, dc = direction_map[instructions[i]]
        
        # If we prepend instructions[i], the entire previous path is shifted by (dr, dc)
        # and we add the new starting point (0,0).
        # The new bounds are the union of {0,0} and the shifted old bounds.
        
        # We must check if the suffix [i...end] is valid.
        # A suffix is valid if 0 <= min_r, max_r < n, 0 <= min_c, max_c < n.
        # Note: The bounds calculated here are relative to the start of the suffix.
        
        # Update bounds for the suffix starting at index i
        # We use the logic: new_path_bounds = {0} union {move + old_path_bounds}
        # But wait, the path is: (0,0), (0,0)+dir, (0,0)+dir+dir_next...
        # So the bounds are: min(0, dr + old_min_r), max(0, dr + old_max_r)
        
        # We need to be careful. The "old" bounds were for the suffix [i+1...end].
        # If we add instructions[i], the new path is:
        # Step 0: (0,0)
        # Step 1: (0,0) + (dr, dc)
        # Step 2: (0,0) + (dr, dc) + (dr_next, dc_next) ...
        # This is exactly: {0,0} union { (dr, dc) + path_of_suffix_i+1 }
        
        # However, the suffix [i+1...end] was already calculated starting from (0,0).
        # So we shift its bounds by (dr, dc) and include (0,0).
        
        # We need to track the bounds of the suffix [i...end]
        # Let's use a temporary variable to store the bounds of the suffix [i+1...end]
        # before updating them.
        
        # But there's a catch: the suffix [i+1...end] was valid if its bounds were in [0, n-1].
        # If we prepend instructions[i], the new bounds must also be in [0, n-1].
        
        # Let's refine the update:
        # The suffix [i...end] is valid if:
        # 0 <= min(0, dr + old_min_r) AND max(0, dr + old_max_r) < n
        # AND 0 <= min(0, dc + old_min_c) AND max(0, dc + old_max_c) < n
        
        # Wait, the "old_min_r" etc. are the bounds of the suffix [i+1...end] 
        # starting from (0,0).
        
        # Let's re-initialize for the very last instruction (i = num_instr - 1)
        if i == num_instr - 1:
            dr, dc = direction_map[instructions[i]]
            # Path is (0,0) -> (dr, dc)
            curr_min_r, curr_max_r = min(0, dr), max(0, dr)
            curr_min_c, curr_max_c = min(0, dc), max(0, dc)
        else:
            dr, dc = direction_map[instructions[i]]
            # The path for suffix [i...end] is (0,0) followed by 
            # (dr, dc) + (path for suffix [i+1...end])
            # So we shift the existing bounds by (dr, dc) and include (0,0)
            
            # We need to calculate the bounds of the suffix [i+1...end] 
            # relative to its own start (0,0).
            # Let's use the previous curr_min_r, etc.
            
            # To avoid using the updated values, we'd need a temp. 
            # But we can just update them directly.
            # The new bounds are:
            # min_r = min(0, dr + old_min_r)
            # max_r = max(0, dr + old_max_r)
            # ...
            
            # However, we need to know if the suffix [i+1...end] was valid 
            # to continue building the suffix [i...end].
            # Actually, we don't. We just need to know if the current suffix is valid.
            # If suffix [i+1...end] was invalid, suffix [i...end] is definitely invalid.
            
            # Let's use a flag or check the bounds.
            # If the previous suffix was already out of bounds, the current one is too.
            # But the bounds are relative to (0,0). If the previous suffix was 
            # out of bounds, it means its min_r < 0 or max_r >= n.
            # If we prepend a move, the new min_r could potentially become 0 
            # if dr was positive, but that's impossible because the path 
            # starts at (0,0). If the previous path went to -1, 
            # and we prepend a 'D' (dr=1), the new path goes 0 -> 1 -> 0.
            # So the new min_r is 0. 
            # This means a suffix can become valid by prepending moves!
            # Wait, the problem says: "the suffix of instructions starting from index i".
            # This means we ALWAYS start at (0,0) for any suffix we pick.
            # So my logic of prepending and shifting is correct.
            
            # Let's re-calculate the bounds for suffix [i...end]
            # Let S_i be the set of points in the path of suffix i.
            # S_i = {(0,0)} U { (dr_i, dc_i) + p | p in S_{i+1} }
            
            # This is correct. Let's implement it.
            
            # We need to keep track of whether the suffix [i+1...end] was valid.
            # Actually, we don't need to. We just need to check if the current 
            # suffix [i...end] is valid.
            
            # Let's use a flag `is_valid` for the suffix [i+1...end].
            # If suffix [i+1...end] was invalid, suffix [i...end] is also invalid.
            # Why? Because the path of suffix [i...end] contains a shifted 
            # version of the path of suffix [i+1...end].
            # If the path of [i+1...end] went out of bounds, then the path 
            # of [i...end] will also go out of bounds (just shifted).
            # Wait, that's only true if we consider the bounds relative to the start.
            # If the path [i+1...end] goes to -1, then the path [i...end] 
            # goes to (0,0) -> (dr, dc) -> (dr-1, dc).
            # If dr=1, the new path is 0 -> 1 -> 0. The -1 is gone!
            # So a suffix can become valid by prepending.
            
            # Let's re-read: "the suffix of instructions starting from index i".
            # This means for a fixed i, we start at (0,0) and follow instructions[i...end].
            # My "prepending" logic:
            # S_i = { (0,0) } U { (dr_i, dc_i) + p | p in S_{i+1} }
            # This is exactly what we need.
            
            # Let's trace: instructions = ["U", "U", "U"], n = 3
            # i=2: dir="U" (-1,0). S_2 = {(0,0), (-1,0)}. Bounds: r:[-1,0], c:[0,0]. Invalid.
            # i=1: dir="U" (-1,0). S_1 = {(0,0)} U {(-1,0) + S_2} 
            #      = {(0,0)} U {(-1,0), (-2,0)}. Bounds: r:[-2,0], c:[0,0]. Invalid.
            # i=0: dir="U" (-1,0). S_0 = {(0,0)} U {(-1,0) + S_1}
            #      = {(0,0)} U {(-1,0), (-2,0), (-3,0)}. Bounds: r:[-3,0], c:[0,0]. Invalid.
            
            # Trace: instructions = ["D", "D", "D"], n = 3
            # i=2: dir="D" (1,0). S_2 = {(0,0), (1,0)}. Bounds: r:[0,1], c:[0,0]. Valid.
            # i=1: dir="D" (1,0). S_1 = {(0,0)} U {(1,0) + S_2}
            #      = {(0,0), (1,0), (2,0)}. Bounds: r:[0,2], c:[0,0]. Valid.
            # i=0: dir="D" (1,0). S_0 = {(0,0)} U {(1,0) + S_1}
            #      = {(0,0), (1,0), (2,0), (3,0)}. Bounds: r:[0,3], c:[0,0]. Invalid.
            
            # This logic is O(n) and correct.
            
            # To implement:
            # We need to track the bounds of the suffix [i+1...end] 
            # and then update them to be the bounds of [i...end].
            # But we need to know if the suffix [i+1...end] was valid 
            # to know if we can continue? No, we just check the current bounds.
            # Wait, if suffix [i+1...end] was invalid, suffix [i...end] 
            # might still be valid? 
            # Let's check: S_2 = {(0,0), (-1,0)} (Invalid)
            # S_1 = {(0,0), (1,0) + (-1,0), (1,0) + (0,0)} = {(0,0), (0,0), (1,0)} = {(0,0), (1,0)} (Valid!)
            # Yes! So we cannot stop just because a suffix was invalid.
            # We must check every suffix.
            
            # BUT, if the suffix [i+1...end] was invalid, it means 
            # its bounds were outside [0, n-1].
            # If we prepend (dr, dc), the new bounds are min(0, dr + old_min) 
            # and max(0, dr + old_max).
            # If the suffix [i+1...end] was invalid, it means 
            # old_min < 0 or old_max >= n.
            # If old_min < 0, then dr + old_min could be >= 0 if dr is large.
            # However, dr is only -1, 0, or 1.
            # If old_min was -1, and dr is 1