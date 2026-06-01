METADATA = {
    "id": 1383,
    "name": "Maximum Performance of a Team",
    "slug": "maximum-performance-of-a-team",
    "category": "Heap",
    "aliases": [],
    "tags": ["heap", "greedy", "sorting"],
    "difficulty": "hard",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(n)",
    "description": "Find the maximum performance of a team given k members, where performance is the product of sum of speeds and average efficiency.",
}

import heapq

def solve(speed: list[int], efficiency: list[int], k: int) -> int:
    """
    Calculates the maximum performance of a team of size k.

    Performance is defined as (sum of speeds) * (minimum efficiency in the team).
    To maximize this, we sort engineers by efficiency in descending order and 
    use a min-heap to keep track of the k largest speeds encountered so far.

    Args:
        speed: A list of integers representing the speed of each engineer.
        efficiency: A list of integers representing the efficiency of each engineer.
        k: The required number of engineers in the team.

    Returns:
        The maximum performance possible, modulo 10^9 + 7.

    Examples:
        >>> solve([2, 10, 5, 10], [5, 4, 3, 2], 2)
        100
        >>> solve([5, 5, 5, 5], [1, 2, 3, 4], 2)
        30
    """
    MOD = 10**9 + 7
    
    # Combine speed and efficiency into pairs and sort by efficiency descending.
    # This allows us to treat the current efficiency as the 'minimum' efficiency
    # for all engineers processed so far.
    engineers = sorted(zip(efficiency, speed), key=lambda x: x[0], reverse=True)
    
    max_performance = 0
    current_speed_sum = 0
    # Min-heap to store the speeds of the engineers in the current team.
    # We use a min-heap so we can easily remove the smallest speed when the team exceeds size k.
    speed_heap = []
    
    for eff, spd in engineers:
        # Add current engineer's speed to the sum and the heap
        heapq.heappush(speed_heap, spd)
        current_speed_sum += spd
        
        # If the team size exceeds k, remove the engineer with the smallest speed
        # to maintain the highest possible speed sum for the current efficiency level.
        if len(speed_heap) > k:
            removed_speed = heapq.heappop(speed_heap)
            current_speed_sum -= removed_speed
            
        # If we have exactly k engineers, calculate the performance.
        # Since we sorted by efficiency descending, 'eff' is the minimum efficiency in the heap.
        if len(speed_heap) == k:
            max_performance = max(max_performance, current_speed_sum * eff)
            
    return max_performance % MOD
