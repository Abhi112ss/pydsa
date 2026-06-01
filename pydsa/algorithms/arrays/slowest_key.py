METADATA = {
    "id": 1629,
    "name": "Slowest Key",
    "slug": "slowest-key",
    "category": "Array",
    "aliases": [],
    "tags": ["arrays", "sorting"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Find the key that took the longest time to press, using lexicographical order as a tie-breaker.",
}

def solve(releaseTimes: list[int], keysPressed: list[str]) -> str:
    """
    Finds the key that took the longest time to press. 
    In case of a tie in duration, the lexicographically larger key is chosen.

    Args:
        releaseTimes: A list of integers representing the time each key was released.
        keysPressed: A list of strings representing the keys pressed.

    Returns:
        The key string that had the maximum duration.

    Examples:
        >>> solve([2, 5, 6, 7], ["a", "b", "c", "d"])
        'b'
        >>> solve([3, 10, 15], ["a", "z", "b"])
        'z'
    """
    max_duration = -1
    slowest_key = ""

    # The first key's duration is simply its release time (assuming start at time 0)
    # However, the problem implies duration is releaseTimes[i] - releaseTimes[i-1]
    # We can handle the first element by treating releaseTimes[-1] as 0.
    
    previous_time = 0
    
    for i in range(len(releaseTimes)):
        current_time = releaseTimes[i]
        current_key = keysPressed[i]
        
        # Calculate how long the current key was held
        duration = current_time - previous_time
        
        # Update if we found a longer duration, 
        # or if the duration is equal but the key is lexicographically larger
        if duration > max_duration:
            max_duration = duration
            slowest_key = current_key
        elif duration == max_duration:
            if current_key > slowest_key:
                slowest_key = current_key
        
        # Move the pointer forward for the next iteration
        previous_time = current_time

    return slowest_key
