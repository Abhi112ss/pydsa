METADATA = {
    "id": 379,
    "name": "Design Phone Directory",
    "slug": "design-phone-directory",
    "category": "Design",
    "aliases": [],
    "tags": ["design", "hash_set", "queue"],
    "difficulty": "easy",
    "time_complexity": "O(1)",
    "space_complexity": "O(n)",
    "description": "Design a system that manages a pool of available phone numbers and allows for calling and returning numbers to the pool.",
}

class PhoneDirectory:
    """
    A system to manage a pool of available phone numbers.
    
    Attributes:
        available_numbers (set): A set containing all numbers currently in the pool.
        used_numbers (set): A set containing all numbers currently being used.
    """

    def __init__(self, phone_numbers: list[int]):
        """
        Initializes the PhoneDirectory with a list of available numbers.

        Args:
            phone_numbers (list[int]): A list of integers representing available phone numbers.
        """
        # We use sets for O(1) average time complexity for add, remove, and contains operations.
        self.available_numbers = set(phone_numbers)
        self.used_numbers = set()

    def call(self, number: int) -> bool:
        """
        Attempts to call a number. If the number is available, it is marked as used.

        Args:
            number (int): The phone number to call.

        Returns:
            bool: True if the number was available and successfully called, False otherwise.

        Examples:
            >>> pd = PhoneDirectory([1, 2, 3])
            >>> pd.call(1)
            True
            >>> pd.call(1)
            False
        """
        # Check if the number exists in the available pool
        if number in self.available_numbers:
            # Move the number from available to used
            self.available_numbers.remove(number)
            self.used_numbers.add(number)
            return True
        return False

    def uncall(self, number: int) -> None:
        """
        Returns a number to the available pool.

        Args:
            number (int): The phone number to return to the pool.

        Examples:
            >>> pd = PhoneDirectory([1, 2, 3])
            >>> pd.call(1)
            True
            >>> pd.uncall(1)
            >>> pd.call(1)
            True
        """
        # Check if the number is currently in the used pool
        if number in self.used_numbers:
            # Move the number from used back to available
            self.used_numbers.remove(number)
            self.available_numbers.add(number)

def solve():
    """
    Example usage of the PhoneDirectory class.
    """
    phone_numbers = [1, 2, 3]
    directory = PhoneDirectory(phone_numbers)
    
    print(directory.call(1))    # Expected: True
    print(directory.call(2))    # Expected: True
    print(directory.call(1))    # Expected: False (already called)
    directory.uncall(1)         # Returns 1 to pool
    print(directory.call(1))    # Expected: True (available again)
    print(directory.call(3))    # Expected: True
    print(directory.call(4))    # Expected: False (not in initial list)
