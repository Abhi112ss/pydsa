METADATA = {
    "id": 2693,
    "name": "Call Function with Custom Context",
    "slug": "call-function-with-custom-context",
    "category": "Design",
    "aliases": [],
    "tags": ["design_patterns", "javascript-equivalent"],
    "difficulty": "easy",
    "time_complexity": "O(1)",
    "space_complexity": "O(1)",
    "description": "Implement a mechanism to call a function with a specific context and arguments, mimicking JavaScript's Function.prototype.call.",
}

from typing import Any, Callable


class FunctionCaller:
    """
    A class that simulates the behavior of calling a function with a 
    specific context (this) and a list of arguments.
    """

    def __init__(self, func: Callable) -> None:
        """
        Initializes the FunctionCaller with a target function.

        Args:
            func: The function to be called.
        """
        self.func = func

    def call(self, context: Any, *args: Any) -> Any:
        """
        Executes the stored function using the provided context and arguments.

        In Python, to simulate 'this' context, we pass the context as the 
        first argument if the function is designed to accept it, or we 
        wrap the function. However, the standard way to implement this 
        pattern in a generic way is to treat the context as the first 
        argument of the function call.

        Args:
            context: The object to be used as the context (the 'this' value).
            *args: Variable length argument list to pass to the function.

        Returns:
            The result of the function execution.

        Examples:
            >>> def greet(name):
            ...     return f"Hello, {name}"
            >>> caller = FunctionCaller(greet)
            >>> caller.call(None, "Alice")
            'Hello, Alice'
        """
        # In Python, 'context' is typically passed as the first argument 
        # to simulate the 'self' or 'this' binding in a functional way.
        # We unpack the args and prepend the context.
        return self.func(context, *args)


def solve() -> None:
    """
    Example usage of the FunctionCaller class.
    """
    # Example 1: A function that uses the context
    def identity_with_context(context: dict, value: int) -> int:
        # The context is used to store or retrieve data
        context["last_value"] = value
        return value

    context_obj = {}
    caller = FunctionCaller(identity_with_context)
    
    # Call the function with context_obj and the argument 10
    result = caller.call(context_obj, 10)
    
    print(f"Result: {result}")  # Expected: 10
    print(f"Context: {context_obj}")  # Expected: {'last_value': 10}
