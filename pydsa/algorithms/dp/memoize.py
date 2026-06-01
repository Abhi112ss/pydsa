METADATA = {
    "id": 2623,
    "name": "Memoize",
    "slug": "memoize",
    "category": "Design",
    "aliases": [],
    "tags": ["hash_map", "recursion", "design"],
    "difficulty": "medium",
    "time_complexity": "O(1) per call (amortized)",
    "space_complexity": "O(n) where n is the number of unique calls",
    "description": "Implement a memoization decorator that caches the results of a function based on its arguments.",
}

from typing import Callable, Any, Dict, Tuple


class Memoize:
    """
    A class that implements a memoization decorator to cache function results.
    """

    def __init__(self, n: int) -> None:
        """
        Initializes the Memoize object.

        Args:
            n (int): The number of calls to the memoize method. 
                     Note: In the context of LeetCode 2623, n is often used 
                     to define the range of possible inputs or constraints, 
                     but the core logic relies on a hash map.
        """
        self.cache: Dict[Tuple[Any, ...], Any] = {}

    def memoize(self, func: Callable[..., Any]) -> Callable[..., Any]:
        """
        A decorator that wraps a function to cache its results.

        Args:
            func (Callable[..., Any]): The function to be memoized.

        Returns:
            Callable[..., Any]: A wrapped version of the function that uses a cache.

        Examples:
            >>> @memoize
            >>> def add(a, b): return a + b
            >>> add(1, 2)
            3
            >>> add(1, 2) # Returns cached value
            3
        """
        def wrapper(*args: Any) -> Any:
            # Use the tuple of arguments as a key for the hash map
            # This works because arguments are expected to be hashable
            if args in self.cache:
                return self.cache[args]

            # Compute the result if not found in cache
            result = func(*args)
            self.cache[args] = result
            return result

        return wrapper


def solve(n: int, func: Callable[..., Any], args_list: list[tuple[tuple[Any, ...], int]]) -> list[Any]:
    """
    Helper function to simulate the LeetCode environment.

    Args:
        n (int): Number of calls.
        func (Callable[..., Any]): The function to memoize.
        args_list (list[tuple[tuple[Any, ...], int]]): A list of (arguments, call_index).

    Returns:
        list[Any]: The results of the function calls.
    """
    memoizer = Memoize(n)
    memoized_func = memoizer.memoize(func)
    results = []
    
    # In the LeetCode problem, the calls are often sequential 
    # and the function is passed to the memoize method.
    # This implementation follows the standard decorator pattern.
    for args, _ in args_list:
        results.append(memoized_func(*args))
        
    return results
