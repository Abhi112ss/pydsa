METADATA = {
    "id": 2726,
    "name": "Calculator with Method Chaining",
    "slug": "calculator_with_method_chaining",
    "category": "Design",
    "aliases": [],
    "tags": ["design_patterns"],
    "difficulty": "easy",
    "time_complexity": "O(1)",
    "space_complexity": "O(1)",
    "description": "Implement a calculator class that supports addition, subtraction, multiplication, and division through method chaining.",
}

class Calculator:
    """
    A calculator class that supports basic arithmetic operations using method chaining.
    """

    def __init__(self, initial_value: int) -> None:
        """
        Initializes the calculator with a starting value.

        Args:
            initial_value (int): The starting value of the calculator.
        """
        self.current_value: int = initial_value

    def add(self, val: int) -> "Calculator":
        """
        Adds a value to the current value.

        Args:
            val (int): The value to add.

        Returns:
            Calculator: The current instance to allow method chaining.
        """
        self.current_value += val
        return self

    def subtract(self, val: int) -> "Calculator":
        """
        Subtracts a value from the current value.

        Args:
            val (int): The value to subtract.

        Returns:
            Calculator: The current instance to allow method chaining.
        """
        self.current_value -= val
        return self

    def multiply(self, val: int) -> "Calculator":
        """
        Multiplies the current value by a value.

        Args:
            val (int): The value to multiply by.

        Returns:
            Calculator: The current instance to allow method chaining.
        """
        self.current_value *= val
        return self

    def divide(self, val: int) -> "Calculator":
        """
        Divides the current value by a value (integer division).

        Args:
            val (int): The value to divide by.

        Returns:
            Calculator: The current instance to allow method chaining.
        """
        # Using integer division as per standard LeetCode calculator requirements
        self.current_value //= val
        return self

    def get_value(self) -> int:
        """
        Returns the final calculated value.

        Returns:
            int: The current value of the calculator.
        """
        return self.current_value


def solve() -> None:
    """
    Demonstrates the usage of the Calculator class.
    """
    # Example 1: (5 + 3 - 2) * 4 / 2 = 12
    calc1 = Calculator(5).add(3).subtract(2).multiply(4).divide(2)
    print(f"Result 1: {calc1.get_value()}")  # Expected: 12

    # Example 2: (10 * 2) / 5 + 7 = 11
    calc2 = Calculator(10).multiply(2).divide(5).add(7)
    print(f"Result 2: {calc2.get_value()}")  # Expected: 11
