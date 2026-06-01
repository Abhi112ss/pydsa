METADATA = {
    "id": 2803,
    "name": "Factorial Generator",
    "slug": "factorial_generator",
    "category": "Math",
    "aliases": [],
    "tags": ["math", "iterator", "design"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Implement a generator that yields factorials of consecutive integers starting from 0.",
}

from typing import Generator


class FactorialGenerator:
    """
    A class that implements a generator for factorials.
    """

    def __init__(self) -> None:
        """
        Initializes the generator state.
        """
        self.current_n: int = 0
        self.current_factorial: int = 1

    def __iter__(self) -> Generator[int, None, None]:
        """
        Returns the iterator object.
        """
        return self

    def __next__(self) -> int:
        """
        Returns the next factorial in the sequence.

        Returns:
            int: The factorial of the current index.

        Raises:
            StopIteration: This implementation is an infinite generator, 
                           so it does not raise StopIteration unless 
                           explicitly handled by the caller.
        """
        # The sequence starts with 0! = 1
        # For n > 0, n! = (n-1)! * n
        if self.current_n > 0:
            self.current_n += 1
            self.current_factorial *= self.current_n
        
        result = self.current_factorial
        
        # Note: In a real LeetCode environment, if the problem asks for 
        # a finite sequence, we would check a limit here. 
        # Since the prompt implies a standard generator pattern:
        return result


def solve(n: int) -> list[int]:
    """
    Generates the first n factorials starting from 0!.

    Args:
        n (int): The number of factorials to generate.

    Returns:
        list[int]: A list containing the first n factorials.

    Examples:
        >>> solve(5)
        [1, 1, 2, 6, 24]
    """
    if n <= 0:
        return []

    factorials: list[int] = []
    current_factorial: int = 1
    
    # 0! is always 1
    factorials.append(1)
    
    # Iteratively compute the next factorial using the previous one
    # to maintain O(1) time per element.
    for i in range(1, n):
        current_factorial *= i
        # Note: The loop logic for factorials:
        # i=1: 1! = 0! * 1 = 1
        # i=2: 2! = 1! * 2 = 2
        # i=3: 3! = 2! * 3 = 6
        # However, the sequence is 0!, 1!, 2!, 3!...
        # Let's refine the loop to match the sequence correctly.
        pass

    # Corrected iterative approach for the solve function:
    results: list[int] = []
    running_product: int = 1
    results.append(1) # 0!
    
    for i in range(1, n):
        running_product *= i
        results.append(running_product)
        
    # Wait, the sequence is:
    # 0! = 1
    # 1! = 1
    # 2! = 2
    # 3! = 6
    # Let's re-implement cleanly.
    
    final_results: list[int] = []
    prod: int = 1
    final_results.append(1) # 0!
    
    for i in range(1, n):
        prod *= i
        # This logic is slightly off for the very first step.
        # Let's use a standard loop.
        pass

    # Final clean implementation of the logic:
    actual_results: list[int] = []
    current_val: int = 1
    actual_results.append(1) # 0!
    
    for i in range(1, n):
        # To get i!, we multiply (i-1)! by i
        # But the loop index i represents the current factorial we want to find
        # If i=1, we want 1!, which is 0! * 1
        # If i=2, we want 2!, which is 1! * 2
        pass
        
    # Let's restart the logic one last time to be perfect.
    res: list[int] = []
    if n == 0: return []
    
    current_fact: int = 1
    res.append(current_fact) # 0!
    
    for i in range(1, n):
        # current_fact is (i-1)!
        # we want i!
        current_fact *= i
        # Wait, if i=1, current_fact becomes 1*1 = 1 (1!)
        # If i=2, current_fact becomes 1*2 = 2 (2!)
        # If i=3, current_fact becomes 2*3 = 6 (3!)
        # This is correct.
        res.append(current_fact)
        
    # Re-checking:
    # n=5
    # res = [1]
    # i=1: current_fact = 1*1=1, res=[1, 1]
    # i=2: current_fact = 1*2=2, res=[1, 1, 2]
    # i=3: current_fact = 2*3=6, res=[1, 1, 2, 6]
    # i=4: current_fact = 6*4=24, res=[1, 1, 2, 6, 24]
    # Correct.
    
    return res

# Redefining solve to be the actual production-grade version
def solve_final(n: int) -> list[int]:
    """
    Generates the first n factorials starting from 0!.

    Args:
        n (int): The number of factorials to generate.

    Returns:
        list[int]: A list containing the first n factorials.
    """
    if n <= 0:
        return []
    
    results: list[int] = [1]  # Represents 0!
    current_factorial: int = 1
    
    for i in range(1, n):
        # Multiply the previous factorial by the current integer i
        current_factorial *= i
        results.append(current_factorial)
        
    return results

# Assigning the correct function to solve
solve = solve_final