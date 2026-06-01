METADATA = {
    "id": 681,
    "name": "Next Closest Time",
    "slug": "next-closest-time",
    "category": "Simulation",
    "aliases": [],
    "tags": ["string", "simulation", "brute force"],
    "difficulty": "medium",
    "time_complexity": "O(1)",
    "space_complexity": "O(1)",
    "description": "Find the smallest time that is greater than the given time and uses only the digits present in the input.",
}

def solve(time: str) -> str:
    """
    Finds the next closest time using only the digits present in the input string.

    The algorithm simulates time minute by minute, checking each subsequent 
    minute to see if all its digits are contained within the set of digits 
    provided in the original time string.

    Args:
        time: A string representing time in "HH:MM" format.

    Returns:
        A string representing the next closest time in "HH:MM" format.

    Examples:
        >>> solve("19:34")
        '19:34' # This is not possible, it would be '19:39' if 9 is allowed
        >>> solve("19:34")
        '19:39'
        >>> solve("23:59")
        '22:22'
    """
    # Extract the digits available in the input time
    allowed_digits = {char for char in time if char != ':'}
    
    # Convert current time to total minutes from 00:00
    hours, minutes = map(int, time.split(':'))
    current_total_minutes = hours * 60 + minutes
    
    # There are 1440 minutes in a day (24 * 60)
    # We check every minute starting from the next one
    for increment in range(1, 1441):
        # Calculate the next minute, wrapping around using modulo 1440
        next_total_minutes = (current_total_minutes + increment) % 1440
        
        # Convert back to HH:MM format
        next_hours = next_total_minutes // 60
        next_minutes = next_total_minutes % 60
        
        # Format as string with leading zeros
        candidate_time = f"{next_hours:02d}:{next_minutes:02d}"
        
        # Check if all digits in the candidate time are in the allowed set
        # We skip the colon during the check
        is_valid = True
        for char in candidate_time:
            if char != ':' and char not in allowed_digits:
                is_valid = False
                break
        
        if is_valid:
            return candidate_time
            
    return time # Fallback, though the loop will always find a result (e.g., same digits)
