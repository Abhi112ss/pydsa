METADATA = {
    "id": 1195,
    "name": "Fizz Buzz Multithreaded",
    "slug": "fizz-buzz-multithreaded",
    "category": "Concurrency",
    "aliases": [],
    "tags": ["concurrency", "multithreading", "synchronization"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Print numbers from 1 to n in order, replacing multiples of 3 with 'Fizz', 5 with 'Buzz', and both with 'FizzBuzz', using multiple threads.",
}

import threading

class FizzBuzz:
    def __init__(self, n: int):
        """
        Args:
            n (int): The upper limit of the sequence.
        """
        self.n = n
        self.current_number = 1
        self.lock = threading.Lock()
        self.condition = threading.Condition(self.lock)

    def fizz(self, printFizz: callable) -> None:
        """
        Args:
            printFizz (callable): Function to print "Fizz".
        """
        while True:
            with self.condition:
                while self.current_number <= self.n and not (self.current_number % 3 == 0 and self.current_number % 5 != 0):
                    self.condition.wait()
                
                if self.current_number > self.n:
                    return
                
                printFizz()
                self.current_number += 1
                self.condition.notify_all()

    def buzz(self, printBuzz: callable) -> None:
        """
        Args:
            printBuzz (callable): Function to print "Buzz".
        """
        while True:
            with self.condition:
                while self.current_number <= self.n and not (self.current_number % 5 == 0 and self.current_number % 3 != 0):
                    self.condition.wait()
                
                if self.current_number > self.n:
                    return
                
                printBuzz()
                self.current_number += 1
                self.condition.notify_all()

    def fizzbuzz(self, printFizzBuzz: callable) -> None:
        """
        Args:
            printFizzBuzz (callable): Function to print "FizzBuzz".
        """
        while True:
            with self.condition:
                while self.current_number <= self.n and not (self.current_number % 3 == 0 and self.current_number % 5 == 0):
                    self.condition.wait()
                
                if self.current_number > self.n:
                    return
                
                printFizzBuzz()
                self.current_number += 1
                self.condition.notify_all()

    def number(self, printNumber: callable) -> None:
        """
        Args:
            printNumber (callable): Function to print the number.
        """
        while True:
            with self.condition:
                while self.current_number <= self.n and (self.current_number % 3 == 0 or self.current_number % 5 == 0):
                    self.condition.wait()
                
                if self.current_number > self.n:
                    return
                
                printNumber(self.current_number)
                self.current_number += 1
                self.condition.notify_all()