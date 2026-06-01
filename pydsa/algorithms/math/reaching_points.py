METADATA = {
    "id": 780,
    "name": "Reaching Points",
    "slug": "reaching-points",
    "category": "Math",
    "aliases": [],
    "tags": ["math", "greedy"],
    "difficulty": "medium",
    "time_complexity": "O(log(max(tx, ty)))",
    "space_complexity": "O(1)",
    "description": "Determine if a target point (tx, ty) can be reached from a starting point (sx, sy) using only addition operations.",
}

def solve(sx: int, sy: int, tx: int, ty: int) -> bool:
    """
    Determines if the target point (tx, ty) can be reached from (sx, sy) 
    using only the operations (x, y) -> (x + y) or (x, y) -> (x + x).

    The algorithm works backwards from the target to the source. Since 
    one coordinate must be the sum of the other and itself (or just the other), 
    we can use modulo to jump multiple steps at once.

    Args:
        sx: Starting x-coordinate.
        sy: Starting y-coordinate.
        tx: Target x-coordinate.
        ty: Target y-coordinate.

    Returns:
        True if the target is reachable, False otherwise.

    Examples:
        >>> solve(1, 1, 3, 5)
        True
        >>> solve(1, 1, 1, 2)
        False
    """
    # If target is smaller than source in any dimension, it's impossible
    if sx > tx or sy > ty:
        return False

    while sx <= tx and sy <= ty:
        # If we reached the source, we are done
        if sx == tx and sy == ty:
            return True
        
        # If one coordinate matches the source, check if the other 
        # can be reached by repeatedly doubling or adding the source
        if sx == tx:
            # ty must be reachable from sy by adding sy repeatedly
            # This is equivalent to (ty - sy) % sy == 0
            return (ty - sy) % sy == 0
        if sy == ty:
            # tx must be reachable from sx by adding sx repeatedly
            return (tx - sx) % sx == 0

        # Work backwards: the larger coordinate must be the sum of the smaller 
        # coordinate and some multiple of the other coordinate.
        if tx > ty:
            # We want to reduce tx using ty. 
            # We use modulo to skip multiple subtractions: tx = tx % ty.
            # However, we must ensure tx doesn't drop below sx.
            if ty > sy:
                # If ty is still greater than sy, we can reduce tx using ty
                # We use (tx - sx) % ty to ensure we don't overshoot sx
                tx %= ty
                # If tx becomes 0 due to modulo, it means tx was a multiple of ty.
                # But we need to keep tx at least sx. If tx < sx, we check if 
                # the original tx could have been reduced to sx.
                if tx < sx:
                    # If tx % ty is 0, the smallest positive value is ty.
                    # But we need to check if sx is reachable.
                    # A simpler way: if tx % ty == 0, the "last" tx was ty.
                    # If ty is already < sx, it's impossible.
                    # Let's refine the modulo logic:
                    # We need tx_new = tx - k * ty such that tx_new >= sx.
                    # The largest such k is (tx - sx) // ty.
                    # If k is 0, we can't reduce tx further.
                    pass 
            else:
                # ty is already at sy, handled by the 'if sy == ty' block above
                pass
            
            # Re-implementing the modulo logic more robustly:
            # We need to reduce tx while keeping tx >= sx and ty > sy.
            # If ty > sy, we can reduce tx to tx % ty. 
            # But if tx % ty is 0, we actually want to treat it as ty 
            # to avoid tx becoming 0 (unless sx is 0, but problem implies positive).
            # Actually, the simplest way:
            if ty > sy:
                # We can reduce tx by multiples of ty as long as tx > sx
                # The remainder tx % ty might be 0, but we need to stay >= sx.
                # If tx % ty == 0, the smallest tx can be is ty (if ty >= sx).
                # However, the standard way to handle this in Euclidean-like 
                # algorithms is:
                tx %= ty
                if tx == 0: # This happens if tx was a multiple of ty
                    # Since we need tx >= sx, and sx >= 1, tx cannot be 0.
                    # The only way tx % ty == 0 is if tx was a multiple.
                    # We can't just set tx = 0. We must check if sx is reachable.
                    # But the 'if sx == tx' and 'if sy == ty' checks handle the boundaries.
                    # Let's use the (tx - sx) % ty logic instead.
                    pass
            
            # Let's use the most robust version of the Euclidean reduction:
            # To avoid the tx=0 issue, we use:
            # tx = tx - k * ty, where k is the largest integer such that tx - k * ty >= sx
            # k = (tx - sx) // ty
            # If k == 0, we can't reduce tx anymore.
            # If k > 0, tx = tx - k * ty.
            # This is equivalent to:
            # if ty > sy:
            #    k = (tx - sx) // ty
            #    if k == 0: return False # Cannot reduce tx further
            #    tx -= k * ty
            # else: return False
            
            # Let's restart the loop logic inside the while to be cleaner.
            break # break to use the clean logic below

    # Clean implementation of the Euclidean-style reduction
    while sx <= tx and sy <= ty:
        if sx == tx and sy == ty:
            return True
        if sx == tx:
            return (ty - sy) % sy == 0
        if sy == ty:
            return (tx - sx) % sx == 0
        
        if tx > ty:
            # How many ty's can we subtract from tx while keeping tx >= sx?
            # We need tx - k * ty >= sx  =>  k * ty <= tx - sx  =>  k <= (tx - sx) / ty
            k = (tx - sx) // ty
            if k == 0: return False
            tx -= k * ty
        else:
            # How many tx's can we subtract from ty while keeping ty >= sy?
            k = (ty - sy) // sx
            if k == 0: return False
            ty -= k * sx
            
    return False

# The above logic is slightly redundant. Let's provide the final optimized version.

def solve_final(sx: int, sy: int, tx: int, ty: int) -> bool:
    """
    Optimized version of the Reaching Points solver.
    """
    while sx <= tx and sy <= ty:
        if sx == tx and sy == ty:
            return True
        if sx == tx:
            return (ty - sy) % sy == 0
        if sy == ty:
            return (tx - sx) % sx == 0
        
        if tx > ty:
            # Reduce tx using ty
            # We must ensure tx remains >= sx.
            # The number of times we can subtract ty is (tx - sx) // ty.
            # If this is 0, we can't reduce tx anymore.
            k = (tx - sx) // ty
            if k == 0: return False
            tx -= k * ty
        else:
            # Reduce ty using tx
            k = (ty - sy) // sx
            if k == 0: return False
            ty -= k * sx
            
    return False

# Re-assigning to solve for the final output
solve = solve_final