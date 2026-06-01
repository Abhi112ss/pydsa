METADATA = {
    "id": 262,
    "name": "Trips and Users",
    "slug": "trips-and-users",
    "category": "Database/Logic",
    "aliases": [],
    "tags": ["math", "logic"],
    "difficulty": "hard",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Calculate the cancellation rate of requests with unbanned users for a specific date.",
}

def solve(trips: list[dict], users: list[dict], target_date: str) -> float:
    """
    Calculates the cancellation rate of requests with unbanned users for a specific date.

    The cancellation rate is defined as the number of canceled requests (either by 
    driver or client) divided by the total number of requests made by unbanned 
    users on the target date.

    Args:
        trips: A list of dictionaries where each dict represents a trip.
               Keys: 'id', 'client_id', 'driver_id', 'cityId', 'status', 'request_at'.
        users: A list of dictionaries where each dict represents a user.
               Keys: 'id', 'banned' (0 or 1).
        target_date: The date string in 'YYYY-MM-DD' format to filter trips.

    Returns:
        float: The cancellation rate rounded to 2 decimal places.

    Examples:
        >>> trips = [
        ...     {"id": 1, "client_id": 1, "driver_id": 10, "status": "completed", "request_at": "2013-10-01"},
        ...     {"id": 2, "client_id": 2, "driver_id": 11, "status": "canceled_by_driver", "request_at": "2013-10-01"},
        ...     {"id": 3, "client_id": 1, "driver_id": 12, "status": "completed", "request_at": "2013-10-01"}
        ... ]
        >>> users = [{"id": 1, "banned": 0}, {"id": 2, "banned": 0}, {"id": 10, "banned": 0}, {"id": 11, "banned": 0}, {"id": 12, "banned": 0}]
        >>> solve(trips, users, "2013-10-01")
        0.33
    """
    # Create a set of banned user IDs for O(1) lookup
    banned_users = {user["id"] for user in users if user["banned"] == 1}
    
    total_valid_trips = 0
    canceled_valid_trips = 0

    for trip in trips:
        # Filter by the specific date requested
        if trip["request_at"] == target_date:
            client_id = trip["client_id"]
            driver_id = trip["driver_id"]

            # A trip is valid only if BOTH client and driver are not banned
            if client_id not in banned_users and driver_id not in banned_users:
                total_valid_trips += 1
                
                # Check if the trip status indicates a cancellation
                if trip["status"].startswith("canceled"):
                    canceled_valid_trips += 1

    # If no valid trips exist for the date, the rate is 0.00
    if total_valid_trips == 0:
        return 0.00

    # Calculate ratio and round to 2 decimal places
    cancellation_rate = canceled_valid_trips / total_valid_trips
    return round(cancellation_rate, 2)
