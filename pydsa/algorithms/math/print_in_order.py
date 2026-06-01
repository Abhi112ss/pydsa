METADATA = {
    "id": 1114,
    "name": "Print in Order",
    "slug": "print_in_order",
    "category": "concurrency",
    "aliases": [],
    "tags": ["concurrency", "synchronization", "multithreading"],
    "difficulty": "medium",
    "time_complexity": "O(1)",
    "space_complexity": "O(1)",
    "description": "Synchronize three methods so they print in the order first, second, third.",
}


from threading import Semaphore, Thread
from typing import Callable


class Foo:
    """Synchronize three actions to enforce the order first → second → third."""

    def __init__(self) -> None:
        # second can proceed only after first releases first_done
        self._first_done: Semaphore = Semaphore(0)
        # third can proceed only after second releases second_done
        self._second_done: Semaphore = Semaphore(0)

    def first(self, print_first: Callable[[], None]) -> None:
        """
        Execute the first action and signal that the first step is complete.

        Args:
            print_first: A callable that prints or otherwise performs the first step.
        """
        print_first()
        # Allow the second step to run
        self._first_done.release()

    def second(self, print_second: Callable[[], None]) -> None:
        """
        Execute the second action after the first action has completed.

        Args:
            print_second: A callable that prints or otherwise performs the second step.
        """
        # Wait until first step signals completion
        self._first_done.acquire()
        print_second()
        # Allow the third step to run
        self._second_done.release()

    def third(self, print_third: Callable[[], None]) -> None:
        """
        Execute the third action after the second action has completed.

        Args:
            print_third: A callable that prints or otherwise performs the third step.
        """
        # Wait until second step signals completion
        self._second_done.acquire()
        print_third()


def solve() -> None:
    """
    Demonstrates the Foo class by printing numbers 1, 2, 3 in order using three threads.

    Example:
        >>> solve()
        1
        2
        3
    """
    foo_instance = Foo()

    def print_one() -> None:
        print(1)

    def print_two() -> None:
        print(2)

    def print_three() -> None:
        print(3)

    # Create threads targeting each method
    thread_first = Thread(target=foo_instance.first, args=(print_one,))
    thread_second = Thread(target=foo_instance.second, args=(print_two,))
    thread_third = Thread(target=foo_instance.third, args=(print_three,))

    # Start threads in arbitrary order to prove synchronization works
    thread_third.start()
    thread_second.start()
    thread_first.start()

    # Wait for all threads to finish
    thread_first.join()
    thread_second.join()
    thread_third.join()