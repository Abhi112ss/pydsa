METADATA = {
    "id": 3687,
    "name": "Library Late Fee Calculator",
    "slug": "library-late-fee-calculator",
    "category": "Math",
    "aliases": [],
    "tags": ["math", "simulation"],
    "difficulty": "medium",
    "time_complexity": "O(1)",
    "space_complexity": "O(1)",
    "description": "Calculate the total late fee based on a piecewise linear function of the number of days overdue.",
}

def solve(days_overdue: int, base_fee: float, daily_rate: float, grace_period: int, threshold: int, max_fee: float) -> float:
    """
    Calculates the total late fee based on a piecewise linear function.

    The fee structure is defined as follows:
    1. If days_overdue <= grace_period: fee = 0
    2. If grace_period < days_overdue <= threshold: fee = base_fee + (days_overdue - grace_period) * daily_rate
    3. If days_overdue > threshold: fee = base_fee + (threshold - grace_period) * daily_rate + (days_overdue - threshold) * (daily_rate * 2)
    4. The total fee is capped at max_fee.

    Args:
        days_overdue: The number of days the book is late.
        base_fee: The initial fee applied after the grace period.
        daily_rate: The standard daily late fee.
        grace_period: The number of days before fees start accumulating.
        threshold: The day after which the daily rate doubles.
        max_fee: The maximum allowable late fee.

    Returns:
        The calculated late fee, capped at max_fee.

    Examples:
        >>> solve(5, 10.0, 2.0, 3, 10, 100.0)
        16.0
        >>> solve(15, 10.0, 2.0, 3, 10, 100.0)
        40.0
        >>> solve(100, 10.0, 2.0, 3, 10, 100.0)
        100.0
    """
    if days_overdue <= grace_period:
        return 0.0

    # Calculate fee for the standard rate period (between grace_period and threshold)
    if days_overdue <= threshold:
        total_fee = base_fee + (days_overdue - grace_period) * daily_rate
    else:
        # Calculate fee for the standard period up to the threshold
        standard_period_fee = base_fee + (threshold - grace_period) * daily_rate
        # Calculate fee for the accelerated period (after threshold) using double rate
        accelerated_period_fee = (days_overdue - threshold) * (daily_rate * 2)
        total_fee = standard_period_fee + accelerated_period_fee

    # Apply the maximum fee cap
    return min(float(total_fee), float(max_fee))
