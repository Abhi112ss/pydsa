METADATA = {
    "id": 1116,
    "name": "Print Zero Even Odd",
    "slug": "print-zero-even-odd",
    "category": "Concurrency",
    "aliases": [],
    "tags": ["threading", "semaphore", "synchronization"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Implement a class that prints 0, then alternating odd and even numbers up to n in a specific sequence using three threads.",
}

import threading

class ZeroEvenOdd:
    """
    A class to control the printing order of 0, followed by alternating odd and even numbers.
    
    The sequence follows: 0, 1, 0, 2, 0, 3, 0, 4... up to n.
    """

    def __init__(self, n: int) -> None:
        """
        Initializes the synchronization primitives and the target number.

        Args:
            n (int): The upper limit of the sequence.
        """
        self.n = n
        # semaphore_zero starts at 1 to allow the first print (0)
        self.semaphore_zero = threading.Semaphore(1)
        # semaphore_odd starts at 0 to wait for the first odd number
        self.semaphore_odd = threading.Semaphore(0)
        # semaphore_even starts at 0 to wait for the first even number
        self.semaphore_even = threading.Semaphore(0)

    def zero(self, print_fn: callable) -> None:
        """
        Prints 0 and then signals either the odd or even thread.

        Args:
            print_fn (callable): Function to print the number.
        """
        for i in range(1, self.n + 1):
            self.semaphore_zero.acquire()
            print_fn(0)
            # If the current number we are about to process is odd, signal odd thread
            # Otherwise, signal the even thread.
            if i % 2 == 1:
                self.semaphore_odd.release()
            else:
                self.semaphore_even.release()
        
        # After the loop, we need to handle the final zero if n is even/odd logic requires it.
        # However, the problem sequence is 0, 1, 0, 2... 
        # The loop logic above handles n iterations of '0' being printed.
        # If n=5, sequence is 0, 1, 0, 2, 0, 3, 0, 4, 0, 5. Total 5 zeros.
        # The loop range(1, n+1) ensures exactly n zeros are printed.
        pass

    def even(self, print_fn: callable) -> None:
        """
        Prints even numbers.

        Args:
            print_fn (callable): Function to print the number.
        """
        for i in range(2, self.n + 1, 2):
            self.semaphore_even.acquire()
            print_fn(i)
            # After printing an even number, signal the zero thread to print next
            self.semaphore_zero.release()

    def odd(self, print_fn: callable) -> None:
        """
        Prints odd numbers.

        Args:
            print_fn (callable): Function to print the number.
        """
        for i in range(1, self.n + 1, 2):
            self.semaphore_odd.acquire()
            print_fn(i)
            # After printing an odd number, signal the zero thread to print next
            self.semaphore_zero.release()

def solve(n: int) -> None:
    """
    Helper function to execute the ZeroEvenOdd logic.

    Args:
        n (int): The upper limit.

    Examples:
        >>> solve(5)
        0102030405
    """
    obj = ZeroEvenOdd(n)
    
    # Using a list to capture output for testing purposes in a real environment,
    # but here we follow the LeetCode requirement of calling print_fn.
    def print_fn(x: int) -> None:
        print(x, end="")

    t1 = threading.Thread(target=obj.zero, args=(print_fn,))
    t2 = threading.Thread(target=obj.even, args=(print_fn,))
    t3 = threading.Thread(target=obj.odd, args=(print_fn,))

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()
    print() # New line after sequence