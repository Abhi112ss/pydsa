METADATA = {
    "id": 1603,
    "name": "Design Parking System",
    "slug": "design_parking_system",
    "category": "Design",
    "aliases": [],
    "tags": ["design", "arrays"],
    "difficulty": "medium",
    "time_complexity": "O(1)",
    "space_complexity": "O(1)",
    "description": "Implements a parking system that tracks available spots for three car sizes.",
}


class ParkingSystem:
    """Parking system that tracks the number of available spots for big, medium, and small cars.

    The system supports constant‑time updates and queries.
    """

    def __init__(self, big: int, medium: int, small: int) -> None:
        """Initialize the parking system with the given number of spots for each car size.

        Args:
            big: Number of big car spots.
            medium: Number of medium car spots.
            small: Number of small car spots.
        """
        self._available_big = big
        self._available_medium = medium
        self._available_small = small

    def addCar(self, car_type: int) -> bool:
        """Attempt to park a car of the given type.

        Args:
            car_type: 1 for big, 2 for medium, 3 for small.

        Returns:
            True if a spot was available and the car was parked; otherwise False.
        """
        if car_type == 1:
            if self._available_big > 0:
                self._available_big -= 1
                return True
            return False
        if car_type == 2:
            if self._available_medium > 0:
                self._available_medium -= 1
                return True
            return False
        if car_type == 3:
            if self._available_small > 0:
                self._available_small -= 1
                return True
            return False
        # Invalid car type
        return False


def solve() -> None:
    """Demonstrates usage of the ParkingSystem class.

    Example:
        >>> parking = ParkingSystem(1, 1, 0)
        >>> parking.addCar(1)   # park a big car
        True
        >>> parking.addCar(2)   # park a medium car
        True
        >>> parking.addCar(3)   # park a small car (none available)
        False
        >>> parking.addCar(1)   # no big spots left
        False
    """
    # Example usage (not part of LeetCode submission)
    parking = ParkingSystem(1, 1, 0)
    print(parking.addCar(1))  # Expected: True
    print(parking.addCar(2))  # Expected: True
    print(parking.addCar(3))  # Expected: False
    print(parking.addCar(1))  # Expected: False
