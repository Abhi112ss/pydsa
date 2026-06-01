METADATA = {
    "id": 2783,
    "name": "Flight Occupancy and Waitlist Analysis",
    "slug": "flight-occupancy-and-waitlist-analysis",
    "category": "Simulation",
    "aliases": [],
    "tags": ["simulation", "array", "greedy"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Simulate a flight booking process to determine the final occupancy and waitlist size.",
}

def solve(capacity: int, bookings: list[int]) -> tuple[int, int]:
    """
    Simulates the flight booking process to find final occupancy and waitlist size.

    Args:
        capacity: The maximum number of passengers the flight can hold.
        bookings: A list of integers representing the number of passengers 
            attempting to book in each time interval.

    Returns:
        A tuple containing (final_occupancy, final_waitlist_size).

    Examples:
        >>> solve(10, [5, 3, 4, 2])
        (10, 4)
        >>> solve(5, [2, 2, 2])
        (5, 1)
    """
    current_occupancy = 0
    waitlist_size = 0

    for new_bookings in bookings:
        # Calculate how many people can actually fit in the plane
        available_seats = capacity - current_occupancy
        
        if new_bookings <= available_seats:
            # All new bookings fit into the plane
            current_occupancy += new_bookings
        else:
            # Some or all new bookings must go to the waitlist
            # First, fill the remaining seats
            current_occupancy = capacity
            # The rest of the new bookings are added to the existing waitlist
            waitlist_size += (new_bookings - available_seats)
            
        # Note: In this specific problem variation, we assume people on the 
        # waitlist do not board until seats become available, but since 
        # capacity only increases via 'bookings' and we are tracking 
        # cumulative occupancy, we simply track the overflow.
        # However, if the problem implies waitlisted people board as soon 
        # as seats open, the logic would differ. Based on the prompt 
        # 'tracking current capacity and queue length', we treat 
        # occupancy as a ceiling.

    # Re-evaluating the logic for a standard simulation:
    # If the problem implies that 'bookings' are people arriving, 
    # and 'capacity' is the limit:
    
    # Resetting for a clean simulation approach
    occupancy = 0
    waitlist = 0
    
    for incoming in bookings:
        # 1. Try to fill existing waitlist first if seats were to open? 
        # (Not applicable here as no one is leaving)
        
        # 2. Add incoming people to the plane if seats exist
        can_fit = max(0, capacity - occupancy)
        if incoming <= can_fit:
            occupancy += incoming
        else:
            # Fill the plane and put the rest in waitlist
            occupancy = capacity
            waitlist += (incoming - can_fit)
            
    return occupancy, waitlist

# The logic above is slightly redundant due to the reset. 
# Let's provide the optimized single-pass version.

def solve_optimized(capacity: int, bookings: list[int]) -> tuple[int, int]:
    """
    Simulates the flight booking process to find final occupancy and waitlist size.

    Args:
        capacity: The maximum number of passengers the flight can hold.
        bookings: A list of integers representing the number of passengers 
            attempting to book in each time interval.

    Returns:
        A tuple containing (final_occupancy, final_waitlist_size).
    """
    occupancy = 0
    waitlist = 0

    for incoming in bookings:
        # Calculate how many seats are currently empty
        empty_seats = capacity - occupancy
        
        if incoming <= empty_seats:
            # All incoming passengers can be seated
            occupancy += incoming
        else:
            # Fill the remaining seats and move the rest to the waitlist
            occupancy = capacity
            waitlist += (incoming - empty_seats)
            
    return occupancy, waitlist

# Re-assigning to the required function name
solve = solve_optimized