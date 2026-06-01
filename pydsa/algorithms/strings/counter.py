METADATA = {
    "id": 2620,
    "name": "Counter",
    "slug": "counter",
    "category": "Design",
    "aliases": [],
    "tags": ["javascript", "closures"],
    "difficulty": "easy",
    "time_complexity": "O(1)",
    "space_complexity": "O(1)",
    "description": "Design a Counter class supporting increment, decrement, reset, and get operations.",
}


class Counter:
    """Simple counter supporting increment, decrement, reset, and retrieval."""

    def __init__(self, initial: int = 0) -> None:
        """Initialize the counter with a starting value."""
        self._value: int = initial

    def inc(self) -> int:
        """Increase the counter by one and return the new value."""
        self._value += 1
        return self._value

    def dec(self) -> int:
        """Decrease the counter by one and return the new value."""
        self._value -= 1
        return self._value

    def reset(self) -> None:
        """Reset the counter to zero."""
        self._value = 0

    def get(self) -> int:
        """Return the current counter value."""
        return self._value


def solve() -> None:
    """Simulate a sequence of Counter operations.

    Args:
        Input is read from stdin and consists of three lines:
        1. An integer n, the number of operations.
        2. A JSON array of operation names (e.g., ["Counter","inc","get"]).
        3. A JSON array of argument lists for each operation.

    Returns:
        Prints a JSON array of results where constructor and void methods
        produce null, and other methods return their integer results.

    Example:
        Input:
            5
            ["Counter","inc","inc","reset","get"]
            [[10],[],[],[],[]]

        Output:
            [null,11,12,null,0]
    """
    import sys
    import json

    lines = sys.stdin.read().strip().splitlines()
    if not lines:
        return

    operation_count = int(lines[0].strip())
    operations = json.loads(lines[1])
    arguments = json.loads(lines[2])

    results: list[int | None] = []
    counter_instance: Counter | None = None

    for op_name, op_args in zip(operations, arguments):
        if op_name == "Counter":
            initial_value = op_args[0] if op_args else 0
            counter_instance = Counter(initial_value)
            results.append(None)  # constructor returns null
        elif op_name == "inc":
            results.append(counter_instance.inc())
        elif op_name == "dec":
            results.append(counter_instance.dec())
        elif op_name == "reset":
            counter_instance.reset()
            results.append(None)  # void method returns null
        elif op_name == "get":
            results.append(counter_instance.get())
        else:
            # Unsupported operation; append null for safety
            results.append(None)

    # Convert Python None to JSON null automatically
    sys.stdout.write(json.dumps(results))
