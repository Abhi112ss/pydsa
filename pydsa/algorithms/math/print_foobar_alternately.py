METADATA = {
    "id": 1115,
    "name": "Print FooBar Alternately",
    "slug": "print-foobar-alternately",
    "category": "Concurrency",
    "aliases": [],
    "tags": ["threading", "semaphore", "synchronization"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Implement two threads that print 'foo' and 'bar' alternately in a specific sequence.",
}

import threading

class FooBar:
    """
    A class to control the alternating printing of 'foo' and 'bar' using semaphores.
    """

    def __init__(self, n: int):
        """
        Initializes the FooBar object.

        Args:
            n (int): The number of times to print the 'fooBar' sequence.
        """
        self.n = n
        # foo_sem starts at 1 so the first call to foo() can proceed immediately.
        self.foo_sem = threading.Semaphore(1)
        # bar_sem starts at 0 so the first call to bar() must wait for foo().
        self.bar_sem = threading.Semaphore(0)

    def foo(self) -> None:
        """
        Prints 'foo' to stdout.
        """
        for _ in range(self.n):
            # Wait for the signal that it is 'foo's turn
            self.foo_sem.acquire()
            print("foo", end="")
            # Signal that it is now 'bar's turn
            self.bar_sem.release()

    def bar(self) -> None:
        """
        Prints 'bar' to stdout.
        """
        for _ in range(self.n):
            # Wait for the signal that it is 'bar's turn
            self.bar_sem.acquire()
            print("bar", end="")
            # Signal that it is now 'foo's turn
            self.foo_sem.release()

def solve() -> None:
    """
    Demonstrates the functionality of the FooBar class.
    """
    import sys
    
    # Example usage:
    n = 5
    fb = FooBar(n)
    
    t1 = threading.Thread(target=fb.foo)
    t2 = threading.Thread(target=fb.bar)
    
    t1.start()
    t2.start()
    
    t1.join()
    t2.join()
    print()  # New line after sequence
