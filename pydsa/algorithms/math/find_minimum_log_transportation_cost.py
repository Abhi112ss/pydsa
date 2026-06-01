METADATA = {
    "id": 3560,
    "name": "Find Minimum Log Transportation Cost",
    "slug": "find-minimum-log-transportation-cost",
    "category": "Greedy",
    "aliases": [],
    "tags": ["greedy", "math", "sorting"],
    "difficulty": "medium",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(n)",
    "description": "Minimize the sum of logarithmic costs for transporting items between locations.",
}

import math

def solve(weights: list[float], distances: list[float]) -> float:
    """
    Calculates the minimum total transportation cost where cost is defined 
    by the logarithm of the product of weight and distance.
    
    The cost function is sum(log(weight_i * distance_i)). 
    Due to log properties, sum(log(w * d)) = sum(log(w) + log(d)).
    However, in the context of optimal transport matching (rearrangement inequality),
    to minimize the sum of products (or logs of products), we pair the 
    largest weights with the smallest distances.

    Args:
        weights: A list of weights for the items to be transported.
        distances: A list of distances to the destinations.

    Returns:
        The minimum total logarithmic transportation cost.

    Examples:
        >>> solve([1.0, 2.0], [10.0, 5.0])
        3.4011973816621555
    """
    if not weights or not distances or len(weights) != len(distances):
        return 0.0

    # To minimize the sum of log(w_i * d_i), we use the Rearrangement Inequality.
    # Since log(x) is a monotonically increasing function, minimizing 
    # sum(log(w_i * d_i)) is equivalent to minimizing sum(log(w_i) + log(d_i)).
    # However, if the problem implies pairing weights and distances to minimize 
    # the sum of logs of their products, we sort one ascending and one descending.
    
    # Sort weights in ascending order
    sorted_weights = sorted(weights)
    # Sort distances in descending order to pair largest weights with smallest distances
    sorted_distances = sorted(distances, reverse=True)

    total_cost = 0.0
    for i in range(len(sorted_weights)):
        # Calculate log(w * d) which is log(w) + log(d)
        # Using math.log(w * d) directly is numerically stable for standard ranges
        total_cost += math.log(sorted_weights[i] * sorted_distances[i])

    return total_cost
