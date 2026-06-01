METADATA = {
    "id": 1396,
    "name": "Design Underground System",
    "slug": "design_underground_system",
    "category": "Design",
    "aliases": [],
    "tags": ["design", "hash_map"],
    "difficulty": "medium",
    "time_complexity": "O(1) for all operations",
    "space_complexity": "O(S + P) where S is number of stations and P is number of station pairs",
    "description": "Design a system to track travel times between subway stations.",
}

class UndergroundSystem:
    def __init__(self) -> None:
        """
        Initializes the underground system.
        
        Attributes:
            check_ins (dict): Maps station_id to (time, station_id) for active trips.
            travel_times (dict): Maps (start_station, end_station) to [total_time, count].
        """
        # Maps station_id -> (check_in_time, start_station_id)
        self.check_ins: dict[int, tuple[int, int]] = {}
        # Maps (start_station_id, end_station_id) -> [cumulative_duration, trip_count]
        self.travel_times: dict[tuple[int, int], list[int]] = {}

    def check_in(self, id: int, station_id: int, t: int) -> None:
        """
        Checks in a customer at a specific station at a specific time.

        Args:
            id (int): Unique ID of the customer.
            station_id (int): The station where the customer checks in.
            t (int): The time of check-in.
        """
        self.check_ins[id] = (t, station_id)

    def check_out(self, id: int, station_id: int, t: int) -> None:
        """
        Checks out a customer at a specific station at a specific time.

        Args:
            id (int): Unique ID of the customer.
            station_id (int): The station where the customer checks out.
            t (int): The time of check-out.
        """
        # Retrieve check-in info and remove from active check-ins
        check_in_time, start_station_id = self.check_ins.pop(id)
        duration = t - check_in_time
        route = (start_station_id, station_id)

        # Update the cumulative travel time and count for this specific route
        if route not in self.travel_times:
            self.travel_times[route] = [0, 0]
        
        self.travel_times[route][0] += duration
        self.travel_times[route][1] += 1

    def complete_request(self, start_station_id: int, end_station_id: int) -> float:
        """
        Returns the average time taken for all completed trips between two stations.

        Args:
            start_station_id (int): The starting station ID.
            end_station_id (int): The ending station ID.

        Returns:
            float: The average travel time.

        Examples:
            >>> system.complete_request(1, 2)
            30.0
        """
        total_duration, count = self.travel_times[(start_station_id, end_station_id)]
        return total_duration / count

def solve():
    """
    Example usage of the UndergroundSystem class.
    """
    system = UndergroundSystem()
    system.check_in(1, 1, 10)
    system.check_in(2, 1, 15)
    system.check_out(1, 2, 20)
    print(system.complete_request(1, 2))  # Expected: 10.0
    system.check_out(2, 2, 35)
    print(system.complete_request(1, 2))  # Expected: 15.0
