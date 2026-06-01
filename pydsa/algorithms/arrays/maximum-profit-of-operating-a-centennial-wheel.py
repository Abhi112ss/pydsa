METADATA = {
    "id": 1599,
    "name": "Maximum Profit of Operating a Centennial Wheel",
    "slug": "maximum_profit_of_operating_a_centennial_wheel",
    "category": "array",
    "aliases": [],
    "tags": ["sliding_window", "greedy"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Find the maximum profit from operating a wheel over a consecutive interval of days.",
}


def max_profit(customers: list[int]) -> int:
    """Compute the maximum profit achievable by operating the wheel over a
    consecutive interval of days.

    Each day the wheel can serve at most 4 customers, generating a profit equal
    to the number of served customers. Operating the wheel incurs a fixed cost
    of 2 per day. The profit for a single day is therefore
    `min(customers[i], 4) - 2`. The goal is to select a contiguous sub‑array that
    maximizes the total profit (or return 0 if operating is never profitable).

    Args:
        customers: List of integers where customers[i] is the number of people
            wanting to ride on day i.

    Returns:
        The maximum total profit achievable (non‑negative integer).

    Examples:
        >>> max_profit([1, 4, 2, 3])
        2
        >>> max_profit([5, 5, 5, 5])
        8
        >>> max_profit([0, 0, 0])
        0
    """
    max_ending_here = 0
    max_so_far = 0

    for daily_customers in customers:
        # profit for the current day after accounting for capacity and cost
        daily_profit = min(daily_customers, 4) - 2

        # Kadane's update: either start new interval or extend previous one
        max_ending_here = max(daily_profit, max_ending_here + daily_profit)

        # Track the best profit seen so far
        max_so_far = max(max_so_far, max_ending_here)

    return max_so_far


def solve() -> None:
    """Read input, compute and print the maximum profit.

    Input format:
        n
        a1 a2 ... an

    where n is the number of days and ai is the number of customers on day i.
    """
    import sys

    data = sys.stdin.read().strip().split()
    if not data:
        return

    n = int(data[0])
    customers = list(map(int, data[1:1 + n]))
    result = max_profit(customers)
    print(result)