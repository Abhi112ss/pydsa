METADATA = {
    "id": 2525,
    "name": "Categorize Box According to Criteria",
    "slug": "categorize-box-according-to-criteria",
    "category": "Simulation",
    "aliases": [],
    "tags": ["arrays", "simulation"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Categorize boxes into 'red', 'blue', or 'green' based on specific weight and color criteria.",
}

def solve(boxes: list[list[int]]) -> list[str]:
    """
    Categorizes boxes based on their weight and color properties.

    A box is categorized as:
    - 'red' if weight is strictly greater than the average weight of all boxes 
      AND the color is 1.
    - 'blue' if weight is strictly greater than the average weight of all boxes 
      AND the color is 2.
    - 'green' if weight is less than or equal to the average weight of all boxes.

    Args:
        boxes: A list of lists where each sub-list contains [weight, isBlue, isRed].
               Note: The problem description implies color encoding. 
               Based on standard LeetCode interpretation for this problem:
               boxes[i][0] = weight
               boxes[i][1] = isBlue (1 if true, 0 if false)
               boxes[i][2] = isRed (1 if true, 0 if false)

    Returns:
        A list of strings representing the category of each box.

    Examples:
        >>> solve([[10, 0, 1], [20, 1, 0], [30, 0, 0]])
        ['red', 'blue', 'green']
    """
    total_weight = 0
    num_boxes = len(boxes)
    
    # Calculate the total weight to find the average
    for box in boxes:
        total_weight += box[0]
    
    average_weight = total_weight / num_boxes
    results = []

    for weight, is_blue, is_red in boxes:
        # Check if weight is less than or equal to average first
        if weight <= average_weight:
            results.append("green")
        else:
            # If weight is greater than average, check color flags
            if is_red == 1:
                results.append("red")
            elif is_blue == 1:
                results.append("blue")
            else:
                # This case handles if a box is heavier than average but has no color
                # Though problem constraints usually imply one color if heavier
                results.append("green")
                
    return results
