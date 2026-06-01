METADATA = {
    "id": 799,
    "name": "Champagne Tower",
    "slug": "champagne-tower",
    "category": "Simulation",
    "aliases": [],
    "tags": ["simulation", "dynamic_programming"],
    "difficulty": "medium",
    "time_complexity": "O(R^2)",
    "space_complexity": "O(R)",
    "description": "Simulate the pouring of champagne into a pyramid of glasses to find how much liquid ends up in a specific glass.",
}

def solve(pour_amount: int, query_row: int, query_glass: int) -> float:
    """
    Simulates the champagne pouring process using a row-by-row DP approach.

    Args:
        pour_amount: The total amount of champagne poured into the top glass.
        query_row: The row index of the glass to query (0-indexed).
        query_glass: The glass index within the query row (0-indexed).

    Returns:
        The amount of champagne in the specified glass.

    Examples:
        >>> solve(2, 1, 1)
        0.0
        >>> solve(75, 2, 2)
        2.0
    """
    # We use a 1D array to represent the current row being processed.
    # This optimizes space from O(R^2) to O(R).
    # Initialize with 0.0. We need at most query_row + 2 elements to handle overflow.
    current_row = [0.0] * (query_row + 2)
    current_row[0] = float(pour_amount)

    # Iterate through each row up to the query_row
    for row_idx in range(query_row + 1):
        # Create a temporary row to store the state of the next row
        # to avoid using updated values from the same row iteration.
        next_row = [0.0] * (query_row + 2)
        
        for glass_idx in range(row_idx + 1):
            # Calculate how much champagne overflows from the current glass
            # Each glass can hold at most 1.0 unit.
            overflow = max(0.0, current_row[glass_idx] - 1.0)
            
            if overflow > 0:
                # Split the overflow equally into the two glasses below it
                # Glass (r, c) overflows into (r+1, c) and (r+1, c+1)
                next_row[glass_idx] += overflow / 2.0
                next_row[glass_idx + 1] += overflow / 2.0
            
            # If we are at the target row, we don't need to calculate overflow 
            # for the next row, but we need to keep track of the current glass's content.
            # However, the problem asks for the content of the glass, not the overflow.
            # To handle this cleanly, we'll store the actual content in a way that 
            # we can retrieve it.
            
        # If we just finished processing the query_row, the 'current_row' 
        # values are actually the amounts poured into those glasses.
        # But wait, the overflow logic above calculates what goes into the NEXT row.
        # Let's refine: current_row[glass_idx] is the total amount that entered the glass.
        
        # To get the final answer, we need the amount in the glass, capped at 1.0.
        # Let's adjust the loop to update the current_row for the next iteration.
        if row_idx < query_row:
            current_row = next_row
            # We need to add the 'next_row' values to the current_row logic.
            # Actually, a simpler way: current_row stores the total amount that 
            # entered the glass in the current row.
            # Let's re-initialize current_row to represent the "incoming" liquid.
            pass

    # Re-implementing the logic more cleanly to ensure O(R) space and correct values.
    # Let's use the 'current_row' to represent the amount of liquid that enters each glass.
    
    row_amounts = [0.0] * (query_row + 2)
    row_amounts[0] = float(pour_amount)

    for r in range(query_row + 1):
        next_row_amounts = [0.0] * (query_row + 2)
        for c in range(r + 1):
            # amount_in_glass is the total liquid that reached this glass
            amount_in_glass = row_amounts[c]
            overflow = max(0.0, amount_in_glass - 1.0)
            
            if r < query_row:
                # Distribute overflow to the next row
                next_row_amounts[c] += overflow / 2.0
                next_row_amounts[c + 1] += overflow / 2.0
            
            # If this is our target glass, we capture its total incoming amount
            if r == query_row and c == query_glass:
                return min(1.0, amount_in_glass)
        
        row_amounts = next_row_amounts

    return 0.0
