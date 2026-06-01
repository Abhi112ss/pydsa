METADATA = {
    "id": 2512,
    "name": "Reward Top K Students",
    "slug": "reward_top_k_students",
    "category": "Array",
    "aliases": [],
    "tags": ["sorting", "hash_map"],
    "difficulty": "medium",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(n)",
    "description": "Assign rewards to students based on their scores, where higher scores receive higher rewards, and the top k unique scores receive specific incremental rewards.",
}

def solve(student_scores: list[int], k: int) -> list[int]:
    """
    Assigns rewards to students based on their scores.
    
    The reward logic:
    1. Find all unique scores and sort them in descending order.
    2. The top k unique scores receive rewards: 
       - The highest unique score gets reward k.
       - The second highest gets k-1, and so on, down to 1.
    3. All other scores receive a reward of 0.

    Args:
        student_scores: A list of integers representing each student's score.
        k: The number of top unique scores to reward.

    Returns:
        A list of integers representing the rewards for each student in the original order.

    Examples:
        >>> solve([10, 20, 30, 40, 50], 2)
        [0, 0, 1, 2, 0] (Wait, logic check: top 2 unique are 50 and 40. 50->2, 40->1)
        Actually, if scores are [10, 20, 30, 40, 50] and k=2:
        Unique sorted: [50, 40, 30, 20, 10]
        Rewards: 50->2, 40->1, others->0.
        Result: [0, 0, 0, 1, 2]
    """
    # Get unique scores and sort them in descending order
    unique_scores = sorted(list(set(student_scores)), reverse=True)
    
    # Map each of the top k unique scores to its corresponding reward
    # The highest score gets reward k, the next gets k-1, ..., the k-th gets 1
    reward_map: dict[int, int] = {}
    for i in range(min(k, len(unique_scores))):
        score = unique_scores[i]
        reward_map[score] = k - i
        
    # Construct the result list by looking up each student's score in the reward map
    # If the score is not in the map, the reward is 0
    rewards = [reward_map.get(score, 0) for score in student_scores]
    
    return rewards
