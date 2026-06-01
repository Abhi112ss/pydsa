METADATA = {
    "id": 1126,
    "name": "Active Businesses",
    "slug": "active_businesses",
    "category": "Aggregation",
    "aliases": [],
    "tags": ["hash table", "counting", "math"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Count how many event types per business exceed the average occurrences per event type across all businesses.",
}

def solve(business_id: list[int], event_type: list[int]) -> int:
    """
    Calculates the number of event types for each business that occur more 
    frequently than the global average occurrence of that event type.

    Args:
        business_id: A list of business identifiers for each event.
        event_type: A list of event type identifiers for each event.

    Returns:
        The total count of (business, event_type) pairs where the count 
        for that specific business and event type is greater than the 
        average count of that event type across all businesses.

    Examples:
        >>> solve([1, 1, 2, 2, 2], [10, 10, 10, 20, 20])
        2
        # Event 10 occurs 3 times total. Avg for 10 = 3 / 2 businesses = 1.5.
        # Business 1 has two 10s (2 > 1.5) -> +1
        # Business 2 has one 10 (1 < 1.5) -> +0
        # Event 20 occurs 2 times total. Avg for 20 = 2 / 2 businesses = 1.0.
        # Business 1 has zero 20s (0 < 1.0) -> +0
        # Business 2 has two 20s (2 > 1.0) -> +1
        # Total = 1 + 1 = 2
    """
    if not business_id:
        return 0

    # Map to store: event_type -> {business_id -> count}
    # This allows us to track how many times a business performs a specific event
    event_to_business_counts: dict[int, dict[int, int]] = {}
    
    # Map to store: event_type -> total_occurrences
    event_total_counts: dict[int, int] = {}

    # Map to store: event_type -> number_of_unique_businesses_that_performed_it
    # This is needed to calculate the average: total_occurrences / unique_businesses
    event_unique_business_count: dict[int, int] = {}

    # Single pass to aggregate all necessary statistics
    for b_id, e_type in zip(business_id, event_type):
        if e_type not in event_to_business_counts:
            event_to_business_counts[e_type] = {}
            event_total_counts[e_type] = 0
            event_unique_business_count[e_type] = 0
        
        # Update business-specific event count
        if b_id not in event_to_business_counts[e_type]:
            event_to_business_counts[e_type][b_id] = 0
            event_unique_business_count[e_type] += 1
        
        event_to_business_counts[e_type][b_id] += 1
        event_total_counts[e_type] += 1

    active_count = 0

    # Iterate through each event type to compare business counts against the average
    for e_type, business_map in event_to_business_counts.items():
        total_occurrences = event_total_counts[e_type]
        # The average is defined as total occurrences of the event type 
        # divided by the number of businesses that performed that event type.
        num_businesses = event_unique_business_count[e_type]
        average_occurrence = total_occurrences / num_businesses

        # Check each business that participated in this event type
        for b_id, count in business_map.items():
            if count > average_occurrence:
                active_count += 1

    return active_count
