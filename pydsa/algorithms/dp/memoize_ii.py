METADATA = {
    "id": 2630,
    "name": "Memoize II",
    "slug": "memoize_ii",
    "category": "Design",
    "aliases": [],
    "tags": ["hash_map", "design", "decorator"],
    "difficulty": "medium",
    "time_complexity": "O(1) per call (amortized, depending on key generator)",
    "space_complexity": "O(n) where n is the number of unique argument combinations",
    "description": "Implement a decorator that caches the results of a function using a custom key generator.",
}

from typing import Callable, Any, Dict


class Memoize:
    """
    A class to implement a memoization decorator with a custom key generator.
    """

    def __init__(self, fn: Callable, key_generator: Callable[..., str]):
        """
        Initializes the Memoize instance.

        Args:
            fn: The function to be memoized.
            key_generator: A function that takes the same arguments as fn 
                           and returns a string representing the unique key.
        """
        self.fn = fn
        self.key_generator = key_generator
        self.cache: Dict[str, Any] = {}

    def __call__(self, *args: Any, **kwargs: Any) -> Any:
        """
        Executes the function or returns the cached result if the key exists.

        Args:
            *args: Positional arguments for the function.
            **kwargs: Keyword arguments for the function.

        Returns:
            The result of the function call.

        Examples:
            >>> def add(a, b): return a + b
            >>> def gen(a, b): return f"{a},{b}"
            >>> memoized_add = Memoize(add, gen)
            >>> memoized_add(1, 2)
            3
            >>> memoized_add(1, 2)
            3
        """
        # Generate a unique string key using the provided key_generator
        key = self.key_generator(*args, **kwargs)

        # Check if the result is already in the cache
        if key in self.cache:
            return self.cache[key]

        # Compute the result, store it in the cache, and return it
        result = self.fn(*args, **kwargs)
        self.cache[key] = result
        return result


def solve(fn: Callable, key_generator: Callable[..., str]) -> Callable:
    """
    A wrapper function that returns a Memoize instance.

    Args:
        fn: The function to be memoized.
        key_generator: A function that generates a string key for the arguments.

    Returns:
        A memoized version of the input function.
    """
    return Memoize(fn, key_generator)