METADATA = {
    "id": 1066,
    "name": "Campus Bikes II",
    "slug": "campus-bikes-ii",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dynamic_programming", "bitmask", "backtracking"],
    "difficulty": "hard",
    "time_complexity": "O(n * 2^m)",
    "space_complexity": "O(2^m)",
    "description": "Find the minimum total distance to assign unique bikes to workers using bitmask DP.",
}

def solve(worker_locations: list[list[int]], bike_locations: list[list[int]]) -> int:
    """
    Calculates the minimum total distance to assign one unique bike to each worker.

    Args:
        worker_locations: A list of [x, y] coordinates for each worker.
        bike_locations: A list of [x, y] coordinates for each bike.

    Returns:
        The minimum total distance required to assign bikes to all workers.

    Examples:
        >>> solve([[0,0],[2,2]], [[3,3],[1,1]])
        4
        >>> solve([[1,2],[1,0]], [[0,0],[2,2]])
        4
    """
    num_workers = len(worker_locations)
    num_bikes = len(bike_locations)
    
    # dp[mask] stores the minimum distance to satisfy the first 'k' workers,
    # where 'k' is the number of set bits in 'mask', and 'mask' represents 
    # the set of bikes already assigned.
    # Initialize with infinity.
    dp = [float('inf')] * (1 << num_bikes)
    dp[0] = 0

    # Precompute distances to avoid repeated calculations
    # dists[i][j] is the distance between worker i and bike j
    dists = []
    for w_x, w_y in worker_locations:
        row = []
        for b_x, b_y in bike_locations:
            row.append(abs(w_x - b_x) + abs(w_y - b_y))
        dists.append(row)

    # Iterate through each possible state (mask)
    for mask in range(1 << num_bikes):
        # The number of set bits in the mask tells us which worker we are currently assigning
        # e.g., if mask is 0101 (binary), 2 bits are set, so we are assigning the 3rd worker (index 2)
        worker_idx = bin(mask).count('1')
        
        if worker_idx >= num_workers:
            continue

        # Try assigning every available bike to the current worker
        for bike_idx in range(num_bikes):
            # Check if the bike is NOT yet in the mask
            if not (mask & (1 << bike_idx)):
                new_mask = mask | (1 << bike_idx)
                # Update the DP state for the new mask with the minimum distance found
                new_dist = dp[mask] + dists[worker_idx][bike_idx]
                if new_dist < dp[new_mask]:
                    dp[new_mask] = new_dist

    # The answer is the minimum distance in any mask that has exactly 'num_workers' bits set
    # However, since we iterate worker by worker, the result will naturally propagate 
    # to masks with 'num_workers' bits. We need to find the minimum among all masks 
    # that have 'num_workers' bits set.
    
    min_total_distance = float('inf')
    for mask in range(1 << num_bikes):
        if bin(mask).count('1') == num_workers:
            min_total_distance = min(min_total_distance, dp[mask])

    return int(min_total_distance)
