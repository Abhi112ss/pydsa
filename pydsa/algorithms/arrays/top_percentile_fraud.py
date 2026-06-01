METADATA = {
    "id": 3055,
    "name": "Top Percentile Fraud",
    "slug": "top_percentile_fraud",
    "category": "Sorting",
    "aliases": [],
    "tags": ["sorting", "math"],
    "difficulty": "medium",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(n)",
    "description": "Identify the threshold score for the top percentile of fraud scores and return the count of users meeting or exceeding it.",
}

import math

def solve(fraud_scores: list[int], percentile: int) -> int:
    """
    Calculates how many users fall into the top 'percentile' of fraud scores.

    The threshold is determined by finding the score at the (100 - percentile)-th 
    percentile position. Specifically, we find the index in the sorted list 
    that represents the cutoff.

    Args:
        fraud_scores: A list of integers representing fraud scores of users.
        percentile: An integer representing the top percentile (e.g., 10 for top 10%).

    Returns:
        The number of users whose fraud score is greater than or equal to the 
        calculated threshold score.

    Examples:
        >>> solve([10, 20, 30, 40, 50], 20)
        1
        >>> solve([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10)
        1
    """
    if not fraud_scores:
        return 0

    # Sort scores in ascending order to easily find percentile positions
    sorted_scores = sorted(fraud_scores)
    n = len(sorted_scores)

    # The top P percentile means we want the top (P/100 * n) elements.
    # In many statistical definitions, the threshold index for the top P% 
    # is calculated based on the rank. 
    # For LeetCode style percentile problems, we find the rank index.
    # Rank = ceil((100 - percentile) / 100 * n)
    # However, a more robust way to find the 'top P%' threshold in a discrete set:
    # The number of elements to keep is k = ceil(n * percentile / 100).
    # But the problem usually defines the threshold as the value at a specific rank.
    
    # Let's use the standard rank-based approach:
    # The threshold is the value at index: floor((100 - percentile) / 100 * n)
    # Wait, let's refine: if percentile is 10, we want the top 10% of scores.
    # If n=10, top 10% is 1 element. The index would be 9 (the last element).
    # The threshold index is n - ceil(n * percentile / 100).
    
    # Correct logic for "Top P%":
    # We need to find the value such that at least P% of values are >= it.
    # The number of elements that constitute the top P% is:
    # count_needed = ceil(n * percentile / 100)
    
    count_needed = math.ceil((n * percentile) / 100)
    
    # The threshold score is the score at the position that leaves 
    # exactly 'count_needed' elements from the end.
    # Example: n=10, percentile=10 -> count_needed=1. Index = 10 - 1 = 9.
    # Example: n=5, percentile=20 -> count_needed=1. Index = 5 - 1 = 4.
    threshold_index = n - count_needed
    threshold_score = sorted_scores[threshold_index]

    # Count how many scores are >= threshold_score
    # Since the list is sorted, we can use binary search or a simple loop.
    # A simple loop is O(n), but we already spent O(n log n) sorting.
    
    fraud_count = 0
    for score in sorted_scores:
        if score >= threshold_score:
            fraud_count += 1
            
    # Note: If multiple users have the same score as the threshold, 
    # they all count towards the fraud group.
    # The problem asks for the count of users meeting or exceeding the threshold.
    
    # Re-evaluating: The problem asks for the count of users. 
    # If the threshold is 40, and scores are [10, 40, 40, 40, 50], 
    # all 40s and 50s are counted.
    
    # Let's re-verify the count logic.
    # If the threshold is determined by the value at the calculated index,
    # we simply count all elements >= that value.
    
    final_count = 0
    for i in range(n):
        if sorted_scores[i] >= threshold_score:
            final_count += (n - i)
            break
            
    # Actually, the loop above is slightly wrong. Let's just do:
    final_count = sum(1 for s in sorted_scores if s >= threshold_score)

    return final_count
