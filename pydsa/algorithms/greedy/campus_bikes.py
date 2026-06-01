METADATA = {
    "id": 1057,
    "name": "Campus Bikes",
    "slug": "campus-bikes",
    "category": "Greedy",
    "aliases": [],
    "tags": ["sorting", "greedy"],
    "difficulty": "medium",
    "time_complexity": "O(N*M log(N*M))",
    "space_complexity": "O(N*M)",
    "description": "Assign bikes to workers to minimize the total distance traveled using a greedy approach.",
}

def solve(workers: list[list[int]], bikes: list[list[int]]) -> int:
    """
    Assigns bikes to workers such that the total distance traveled is minimized.

    The strategy is to calculate all possible (distance, worker_index, bike_index) 
    triplets, sort them by distance, and greedily assign the smallest distances 
    to available workers and bikes.

    Args:
        workers: A list of lists where workers[i] = [position_i, worker_i].
        bikes: A list of lists where bikes[j] = [position_j, bike_j].

    Returns:
        The minimum total distance traveled.

    Examples:
        >>> solve([[1, 0], [2, 1]], [[10, 0], [5, 1]])
        11
        >>> solve([[1, 0], [2, 1]], [[2, 0], [3, 1]])
        1
    """
    # Create a list of all possible (distance, worker_id, bike_id) combinations
    all_triplets = []
    for worker_pos, worker_id in workers:
        for bike_pos, bike_id in bikes:
            distance = abs(worker_pos - bike_pos)
            all_triplets.append((distance, worker_id, bike_id))

    # Sort triplets by distance to enable greedy selection
    all_triplets.sort()

    num_workers = len(workers)
    num_bikes = len(bikes)
    
    # Track which workers and bikes have already been assigned
    worker_used = [False] * num_workers
    bike_used = [False] * num_bikes
    
    total_distance = 0
    assignments_made = 0

    for distance, worker_id, bike_id in all_triplets:
        # If both the worker and the bike are available, assign them
        if not worker_used[worker_id] and not bike_used[bike_id]:
            worker_used[worker_id] = True
            bike_used[bike_id] = True
            total_distance += distance
            assignments_made += 1
            
            # Optimization: Stop once all workers have a bike
            if assignments_made == num_workers:
                break

    return total_distance
