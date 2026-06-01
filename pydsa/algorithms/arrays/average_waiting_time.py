METADATA = {
    "id": 1701,
    "name": "Average Waiting Time",
    "slug": "average-waiting-time",
    "category": "Simulation",
    "aliases": [],
    "tags": ["simulation", "array", "math"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Calculate the average time customers wait for their orders to be prepared, considering the chef's availability.",
}

def solve(customers: list[list[int]]) -> float:
    """
    Calculates the average waiting time for a series of customer orders.

    The waiting time for a customer is defined as the time from when the order 
    is placed until the food is ready. The chef can only work on one order 
    at a time.

    Args:
        customers: A list of lists where each sublist contains [arrival_time, time_to_cook].

    Returns:
        The average waiting time as a float.

    Examples:
        >>> solve([[1, 3], [2, 5]])
        5.0
        >>> solve([[1, 2], [2, 5], [4, 3]])
        5.333333333333333
    """
    total_waiting_time: int = 0
    current_time: int = 0

    for arrival_time, cook_time in customers:
        # The chef starts working either when the customer arrives 
        # or when the chef finishes the previous order, whichever is later.
        start_time = max(current_time, arrival_time)
        
        # The order is finished after the specified cook time.
        finish_time = start_time + cook_time
        
        # Waiting time = (finish time - arrival time)
        total_waiting_time += (finish_time - arrival_time)
        
        # Update the current time to when the chef becomes free again.
        current_time = finish_time

    return total_waiting_time / len(customers)
