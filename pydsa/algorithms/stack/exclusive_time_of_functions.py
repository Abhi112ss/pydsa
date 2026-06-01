METADATA = {
    "id": 636,
    "name": "Exclusive Time of Functions",
    "slug": "exclusive-time-of-functions",
    "category": "Stack",
    "aliases": [],
    "tags": ["stack", "array", "simulation"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Calculate the total exclusive time spent in each function given a sequence of logs representing start and end events.",
}

def solve(n: int, logs: list[str]) -> list[int]:
    """
    Calculates the exclusive time spent in each function.

    Args:
        n: The number of unique functions (labeled 0 to n-1).
        logs: A list of log strings in the format "function_id:type:timestamp",
              where type is either "start" or "end".

    Returns:
        A list of integers where the i-th integer is the exclusive time spent in function i.

    Examples:
        >>> solve(2, ["0:start:0", "1:start:2", "1:end:5", "0:end:6"])
        [3, 4]
        >>> solve(1, ["0:start:0", "0:end:5"])
        [6]
    """
    result = [0] * n
    # The stack stores the IDs of functions currently being executed.
    stack: list[int] = []
    # Track the last timestamp when a state change occurred.
    prev_timestamp = 0

    for log in logs:
        # Parse the log entry
        func_id_str, event_type, timestamp_str = log.split(":")
        func_id = int(func_id_str)
        timestamp = int(timestamp_str)

        if event_type == "start":
            # If there is a function currently running, add the elapsed time 
            # to its exclusive time before pushing the new function.
            if stack:
                current_running_func = stack[-1]
                result[current_running_func] += timestamp - prev_timestamp
            
            stack.append(func_id)
            # The next interval starts at the current timestamp.
            prev_timestamp = timestamp
        else:
            # If it's an "end" event, the function is finishing.
            # The duration is (timestamp - prev_timestamp + 1) because 
            # the end timestamp is inclusive.
            current_running_func = stack.pop()
            result[current_running_func] += timestamp - prev_timestamp + 1
            
            # The next interval starts at the timestamp immediately after this end.
            prev_timestamp = timestamp + 1

    return result
