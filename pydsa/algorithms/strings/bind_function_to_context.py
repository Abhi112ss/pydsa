METADATA = {
    "id": 2754,
    "name": "Bind Function to Context",
    "slug": "bind-function-to-context",
    "category": "Functional Programming",
    "aliases": [],
    "tags": ["functional_programming", "closures"],
    "difficulty": "easy",
    "time_complexity": "O(1)",
    "space_complexity": "O(1)",
    "description": "Implement a function that returns a new function with a fixed context and arguments.",
}

from typing import Callable, Any


def solve(func: Callable, context: Any, *args: Any) -> Callable[..., Any]:
    """
    Creates a new function that, when called, invokes 'func' with 'context' 
    as its first argument, followed by the provided 'args' and any 
    additional arguments passed to the returned function.

    Args:
        func: The original function to be bound.
        context: The object to be passed as the first argument to 'func'.
        *args: The initial arguments to be bound to the function.

    Returns:
        A new function that encapsulates the context and initial arguments.

    Examples:
        >>> def add(a, b, c): return a + b + c
        >>> bound_add = solve(add, 10, 20)
        >>> bound_add(30)
        60
    """

    def bound_function(*extra_args: Any) -> Any:
        """
        The wrapper function that executes the original function.

        Args:
            *extra_args: Arguments passed at the time of the call.

        Returns:
            The result of calling 'func' with context, args, and extra_args.
        """
        # Combine the fixed context, the pre-bound args, and the new args
        # The order is: context, then *args, then *extra_args
        return func(context, *args, *extra_args)

    # Return the closure which maintains access to func, context, and args
    return bound_function