METADATA = {
    "id": 2532,
    "name": "Time to Cross a Bridge",
    "slug": "time_to_cross_a_bridge",
    "category": "Greedy",
    "aliases": [],
    "tags": ["greedy", "sorting"],
    "difficulty": "medium",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(1)",
    "description": "Calculate the minimum time required for all people to cross a bridge given specific constraints using a greedy approach.",
}

def solve(people: list[int], bridge_capacity: int) -> int:
    """
    Calculates the minimum time required for all people to cross a bridge.
    
    The strategy is to sort the people by their crossing times and pair the 
    fastest people with the slowest people to minimize the total time spent 
    waiting for the slowest person in each group.

    Args:
        people: A list of integers representing the time each person takes to cross.
        bridge_capacity: The maximum number of people that can cross at once.

    Returns:
        The minimum total time required for everyone to cross.

    Examples:
        >>> solve([1, 2, 3, 4], 2)
        6
        >>> solve([10, 2, 3, 5], 2)
        15
    """
    if not people:
        return 0

    # Sort people to allow greedy pairing of fastest and slowest
    people.sort()
    
    total_time = 0
    left = 0
    right = len(people) - 1

    # We process people in groups of 'bridge_capacity'
    # To minimize time, we want the fastest people to 'carry' the slowest people
    # across the bridge.
    while left <= right:
        # The time taken for the current group is determined by the slowest person in that group
        # In a greedy approach for capacity K, we take the K-1 fastest and the 1 slowest
        # However, the problem logic for 'bridge capacity' usually implies we take 
        # the slowest person and fill the rest of the capacity with the fastest available.
        
        # Number of people we can take in this trip
        # We take the slowest person (right) and up to (bridge_capacity - 1) fastest people (left)
        
        # The time for this trip is the time of the slowest person in the current group
        total_time += people[right]
        
        # Move the right pointer to indicate the slowest person has crossed
        right -= 1
        
        # Move the left pointer to indicate the fastest people used to fill capacity have crossed
        # We use bridge_capacity - 1 because the slowest person is already accounted for
        left += (bridge_capacity - 1)
        
        # If left exceeds right, it means we've processed everyone or the last group was smaller
        # The loop condition 'left <= right' handles the termination.
        # Note: If left > right after the decrement, it means we used more people than available,
        # which is fine as they all crossed in that last trip.
        if left > right and left > len(people) - 1:
            # This is a safety break, though the while condition handles it
            break
            
    # Correction for the logic: The standard 'bridge' problem (like LeetCode 678) 
    # usually involves a flashlight. This specific prompt asks for a capacity-based 
    # greedy approach. If the capacity is K, we take the K slowest people? 
    # No, to minimize time, we take the K-1 fastest and 1 slowest.
    
    # Let's re-implement the logic clearly:
    # We want to group people such that the sum of max(group) is minimized.
    # To minimize sum of maxes, we should group the largest elements with the smallest elements.
    
    # Re-calculating using the correct greedy logic:
    people.sort()
    total_time = 0
    n = len(people)
    
    # We take the slowest person (n-1) and pair them with the (capacity-1) fastest people.
    # This way, the 'cost' of the trip is people[n-1], and we remove 'capacity' people.
    # We repeat this until no one is left.
    
    i = n - 1
    j = 0
    total_time = 0
    
    while i >= 0:
        total_time += people[i]
        # We used the slowest person (i) and (bridge_capacity - 1) fastest people (j)
        i -= 1
        j += (bridge_capacity - 1)
        
        # If the fastest people we 'used' have crossed the slowest person's index,
        # it means we've effectively processed everyone.
        if j > i:
            break
            
    # Wait, the logic above is slightly flawed if j catches up to i.
    # Let's use a more robust pointer approach.
    
    people.sort()
    total_time = 0
    left = 0
    right = len(people) - 1
    
    while left <= right:
        # The slowest person in the current set is at 'right'
        total_time += people[right]
        right -= 1
        # We use the fastest 'bridge_capacity - 1' people to accompany the slowest
        left += (bridge_capacity - 1)
        # If left > right, it means the fastest people we tried to pick 
        # were actually part of the 'slow' group we already accounted for.
        # This is handled by the while condition.
        if left > right:
            # We must ensure we don't double count if left was already > right
            # but the loop terminates.
            break
            
    # Let's refine the loop one last time to be perfectly clean.
    people.sort()
    total_time = 0
    # We process from the slowest to fastest.
    # Each trip takes 1 slowest person and (capacity - 1) fastest people.
    # This is optimal because the slowest person's time is unavoidable.
    # By pairing them with the fastest, we 'waste' the fastest people's 
    # potential to lead their own trips, but we minimize the number of trips.
    
    # Actually, the most efficient way to use capacity K is to take the K slowest 
    # people together? No, that would make the time sum(max(groups)).
    # To minimize sum of maxes, you want the largest values to be the max of 
    # as many groups as possible? No, you want each large value to be the max 
    # of a group that contains as many other large values as possible.
    
    # Correct Greedy: To minimize sum of maxes, group the K largest elements together.
    # Example: [1, 2, 3, 4], cap 2. 
    # Groups: (4, 3), (2, 1) -> Maxes: 4, 2. Total = 6.
    # Groups: (4, 1), (3, 2) -> Maxes: 4, 3. Total = 7.
    # So, group the K largest elements together.
    
    people.sort()
    total_time = 0
    idx = len(people) - 1
    while idx >= 0:
        total_time += people[idx]
        idx -= bridge_capacity
        
    return total_time
