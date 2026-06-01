METADATA = {
    "id": 1421,
    "name": "NPV Queries",
    "slug": "npv_queries",
    "category": "Math",
    "aliases": [],
    "tags": ["prefix_sum", "math", "array"],
    "difficulty": "medium",
    "time_complexity": "O(n + q)",
    "space_complexity": "O(n)",
    "description": "Calculate the Net Present Value (NPV) for multiple range queries given a sequence of cash flows and a discount rate.",
}

def solve(cash_flows: list[float], discount_rate: float, queries: list[list[int]]) -> list[float]:
    """
    Calculates the Net Present Value (NPV) for multiple range queries.
    
    The NPV for a range [L, R] is calculated as the sum of (cash_flow[i] / (1 + r)^i) 
    for i from L to R, where r is the discount rate.

    Args:
        cash_flows: A list of cash flows where cash_flows[i] is the amount at time i.
        discount_rate: The discount rate per period.
        queries: A list of queries, where each query is a list [L, R] representing 
                 the inclusive range of indices.

    Returns:
        A list of floats representing the NPV for each query.

    Examples:
        >>> solve([100.0, 100.0, 100.0], 0.1, [[0, 2], [1, 1]])
        [248.68462809917355, 90.9090909090909]
    """
    n = len(cash_flows)
    if n == 0:
        return [0.0] * len(queries)

    # Precompute the discount factor for each time step: 1 / (1 + r)^i
    # We use a prefix sum array of the discounted cash flows to answer range queries in O(1).
    discounted_prefix_sums = [0.0] * (n + 1)
    
    # current_discount_factor represents (1 / (1 + r)^i)
    current_discount_factor = 1.0
    divisor = 1.0 + discount_rate

    for i in range(n):
        # Calculate the discounted value for the current period
        discounted_value = cash_flows[i] * current_discount_factor
        # Build the prefix sum array
        discounted_prefix_sums[i + 1] = discounted_prefix_sums[i] + discounted_value
        # Update the discount factor for the next period: 1 / (1 + r)^(i+1)
        current_discount_factor /= divisor

    results = []
    for left, right in queries:
        # The NPV for range [L, R] is the sum of discounted values from L to R.
        # Using the prefix sum: Sum(L, R) = PrefixSum[R+1] - PrefixSum[L]
        # Note: This assumes the formula is sum(CF[i] / (1+r)^i). 
        # If the problem implies the range starts at time 0 relative to the query, 
        # one would need to multiply by (1+r)^L, but standard NPV queries 
        # usually refer to absolute time indices.
        npv = discounted_prefix_sums[right + 1] - discounted_prefix_sums[left]
        results.append(npv)

    return results
