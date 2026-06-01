METADATA = {
    "id": 2632,
    "name": "Curry",
    "slug": "curry",
    "category": "Functional Programming",
    "aliases": [],
    "tags": ["functional_programming", "recursion"],
    "difficulty": "medium",
    "time_complexity": "O(1)",
    "space_complexity": "O(n)",
    "description": "Implement a function that transforms a function with multiple arguments into a sequence of functions that each take a single argument.",
}

from typing import Callable, Any

def solve(fn: Callable, arity: int) -> Callable:
    """
    Transforms a function into a curried version.

    Args:
        fn: The original function to be curried.
        arity: The number of arguments the original function expects.

    Returns:
        A new function that, when called, returns either the result of fn 
        or another function to collect more arguments.

    Examples:
        >>> def add(a, b, c): return a + b + c
        >>> curried = solve(add, 3)
        >>> curried(1)(2)(3)
        6
    """
    
    def curried_wrapper(*args: Any) -> Any:
        # If the number of arguments collected so far matches or exceeds arity,
        # execute the original function.
        if len(args) >= arity:
            return fn(*args)
        
        # Otherwise, return a new function that accepts the next single argument.
        # We use a nested function to capture the current accumulated arguments.
        def next_step(next_arg: Any) -> Any:
            # Recursively call the wrapper with the combined arguments.
            return curried_wrapper(*(args + (next_arg,)))
            
        return next_step

    return curried_wrapper
