METADATA = {
    "id": 2627,
    "name": "Debounce",
    "slug": "debounce",
    "category": "design",
    "aliases": [],
    "tags": ["design", "timing"],
    "difficulty": "medium",
    "time_complexity": "O(1)",
    "space_complexity": "O(1)",
    "description": "Implement a debounce function that delays the execution of a function until a specified amount of time has passed since the last time it was invoked.",
}

import threading
import time

def solve(func: callable, wait: int) -> callable:
    """
    Args:
        func: The function to be debounced.
        wait: The delay in seconds.

    Returns:
        A debounced version of the function.
    """
    timer: threading.Timer = None

    def debounced(*args, **kwargs) -> None:
        nonlocal timer
        if timer is not None:
            timer.cancel()

        def execute_function():
            func(*args, **kwargs)

        timer = threading.Timer(wait, execute_function)
        timer.start()

    return debounced