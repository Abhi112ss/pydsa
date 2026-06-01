METADATA = {
    "id": 1648,
    "name": "Sell Diminishing-Valued Colored Balls",
    "slug": "sell-diminishing-valued-colored-balls",
    "category": "Math",
    "aliases": [],
    "tags": ["math", "greedy", "heap"],
    "difficulty": "hard",
    "time_complexity": "O(K log K)",
    "space_complexity": "O(K)",
    "description": "Calculate the maximum profit from selling colored balls where the price decreases as you sell more of a specific color.",
}

def solve(colors: list[int], num_sales: int) -> int:
    """
    Calculates the maximum profit from selling colored balls using a greedy approach.
    
    The strategy is to always sell the ball with the highest current value. 
    Instead of a heap, we use a frequency-based approach with sorting to handle 
    large numbers of sales efficiently.

    Args:
        colors: A list of integers representing the count of balls of each color.
        num_sales: The total number of balls to be sold.

    Returns:
        The maximum profit possible, modulo 10^9 + 7.

    Examples:
        >>> solve([3, 5], 6)
        22
        >>> solve([1, 1], 1)
        1
    """
    MOD = 1_000_000_007

    # Sort colors in descending order to process the most frequent colors first
    sorted_colors = sorted(colors, reverse=True)
    # Add a zero to handle the boundary condition when all colors reach the same level
    sorted_colors.append(0)
    
    total_profit = 0
    current_num_colors = 0
    
    # We iterate through the sorted colors to find "levels" of ball counts.
    # We treat the counts as a staircase and fill the gaps between levels.
    for i in range(len(sorted_colors) - 1):
        current_num_colors += 1
        
        # The height difference between the current color count and the next highest
        height_diff = sorted_colors[i] - sorted_colors[i+1]
        
        if height_diff > 0:
            # Total balls available in this "level" across all current colors
            balls_in_level = height_diff * current_num_colors
            
            if num_sales >= balls_in_level:
                # We can sell all balls in this level.
                # Sum of arithmetic progression: (first + last) * count / 2
                # Here, we sell balls from value 'sorted_colors[i]' down to 'sorted_colors[i+1] + 1'
                # for each of the 'current_num_colors' colors.
                
                # Sum for one color: sum(range(low, high + 1))
                # Using formula: (high * (high + 1) // 2) - (low * (low - 1) // 2)
                high = sorted_colors[i]
                low = sorted_colors[i+1] + 1
                
                sum_one_color = (high * (high + 1) // 2) - (low * (low - 1) // 2)
                total_profit = (total_profit + sum_one_color * current_num_colors) % MOD
                num_sales -= balls_in_level
            else:
                # We can only sell some of the balls in this level.
                # num_sales // current_num_colors is how many full rows we can take.
                # num_sales % current_num_colors is the remainder.
                
                full_rows = num_sales // current_num_colors
                remainder = num_sales % current_num_colors
                
                # Calculate profit for the full rows
                high = sorted_colors[i]
                low = sorted_colors[i] - full_rows + 1
                sum_one_color = (high * (high + 1) // 2) - (low * (low - 1) // 2)
                total_profit = (total_profit + sum_one_color * current_num_colors) % MOD
                
                # Calculate profit for the remaining balls in the next row
                # These balls all have the value 'low - 1'
                remaining_val = low - 1
                total_profit = (total_profit + remainder * remaining_val) % MOD
                
                num_sales = 0
                break
                
        if num_sales == 0:
            break
            
    return total_profit % MOD
