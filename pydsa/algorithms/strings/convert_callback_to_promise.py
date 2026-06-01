METADATA = {
    "id": 2776,
    "name": "Convert Callback Based Function to Promise Based Function",
    "slug": "convert-callback-based-function-to-promise-based-function",
    "category": "Design",
    "aliases": [],
    "tags": ["asynchronous", "javascript"],
    "difficulty": "easy",
    "time_complexity": "O(1)",
    "space_complexity": "O(1)",
    "description": "Create a wrapper function that converts a callback-based function into one that returns a Promise.",
}

def solve(fn: callable) -> callable:
    """
    Converts a callback-based function into a function that returns a Promise.

    In a real Python environment, we simulate the 'Promise' behavior using 
    a wrapper that returns a result or raises an exception, mimicking the 
    asynchronous resolution/rejection pattern.

    Args:
        fn: A function that takes a callback as its last argument. 
            The callback follows the (error, result) convention.

    Returns:
        A new function that, when called, returns a result or raises an error,
        simulating the behavior of a resolved or rejected Promise.

    Examples:
        >>> def callback_fn(x, callback):
        ...     if x < 0: callback(ValueError("Negative"), None)
        ...     else: callback(None, x * 2)
        >>> promise_fn = solve(callback_fn)
        >>> promise_fn(5)
        10
        >>> promise_fn(-1)
        Traceback (most recent call last):
            ...
        ValueError: Negative
    """

    def promise_wrapper(*args: any) -> any:
        """
        The wrapper function that simulates the Promise resolution.
        """
        # This list will capture the result from the callback
        # We use a list to allow the inner callback to modify the outer scope
        captured_result = []
        captured_error = []

        def callback(error: any, result: any) -> None:
            """
            The executor callback passed to the original function.
            """
            if error is not None:
                captured_error.append(error)
            else:
                captured_result.append(result)

        # Call the original function with the provided arguments 
        # and append our custom callback at the end.
        fn(*args, callback)

        # Simulate the 'await' or '.then()' behavior of a Promise.
        # If the callback captured an error, we raise it (rejection).
        if captured_error:
            raise captured_error[0]
        
        # If the callback captured a result, we return it (resolution).
        return captured_result[0]

    return promise_wrapper
