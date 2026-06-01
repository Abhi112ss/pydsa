METADATA = {
    "id": 2303,
    "name": "Calculate Amount Paid in Taxes",
    "slug": "calculate-amount-paid-in-taxes",
    "category": "Math",
    "aliases": [],
    "tags": ["math", "simulation"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Calculate the total tax paid by iterating through income brackets and applying the corresponding tax rate to the portion of income within each bracket.",
}

def solve(income: int, tax_brackets: list[list[int]]) -> int:
    """
    Calculates the total amount of tax paid based on income and tax brackets.

    Args:
        income: The total income of the individual.
        tax_brackets: A list of lists where each sub-list contains [upper_bound, tax_rate].
            The upper_bound is the maximum income for that bracket.
            The tax_rate is the percentage (0-100) applied to the income in that bracket.

    Returns:
        The total tax amount paid, rounded down to the nearest integer.

    Examples:
        >>> solve(50000, [[10000, 10], [50000, 20]])
        9000
        >>> solve(10000, [[5000, 10], [10000, 20]])
        1500
    """
    total_tax = 0.0
    previous_upper_bound = 0

    for upper_bound, tax_rate in tax_brackets:
        # Determine the portion of income that falls into the current bracket
        # The bracket range is (previous_upper_bound, upper_bound]
        current_bracket_limit = min(income, upper_bound)
        
        # If the income is less than or equal to the previous bound, no more tax is owed
        if current_bracket_limit <= previous_upper_bound:
            break
            
        # Calculate the amount of income within this specific bracket
        taxable_amount_in_bracket = current_bracket_limit - previous_upper_bound
        
        # Apply the tax rate to the amount in this bracket
        total_tax += taxable_amount_in_bracket * (tax_rate / 100.0)
        
        # Update the previous bound for the next iteration
        previous_upper_bound = upper_bound

    # Return the floor of the total tax as an integer
    return int(total_tax)
