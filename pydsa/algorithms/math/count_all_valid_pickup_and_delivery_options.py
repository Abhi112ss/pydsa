METADATA = {
    "id": 1359,
    "name": "Count All Valid Pickup and Delivery Options",
    "slug": "count-all-valid-pickup-and-delivery-options",
    "category": "Math",
    "aliases": [],
    "tags": ["combinatorics", "dynamic_programming"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Calculate the number of ways to arrange pickup and delivery locations such that each pickup occurs before its corresponding delivery.",
}

def solve(n: int, modulo: int) -> int:
    """
    Args:
        n: The number of orders.
        modulo: The modulo value for the result.

    Returns:
        The total number of valid pickup and delivery sequences modulo the given value.
    """
    total_ways = 1
    for i in range(1, n + 1):
        total_ways = (total_ways * (2 * i - 1) * i) % modulo
    return total_ways