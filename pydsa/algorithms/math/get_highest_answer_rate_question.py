METADATA = {
    "id": 578,
    "name": "Get Highest Answer Rate Question",
    "slug": "get-highest-answer-rate-question",
    "category": "SQL",
    "aliases": [],
    "tags": ["sql", "math"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Find the question ID with the highest answer rate, defined as the ratio of 'answer' actions to 'show' actions.",
}

from collections import defaultdict

def solve(actions: list[dict]) -> int:
    """
    Calculates the question ID with the highest answer rate.
    
    The answer rate is defined as (number of 'answer' actions) / (number of 'show' actions).
    In case of a tie, the question with the smallest ID is returned.

    Args:
        actions: A list of dictionaries where each dictionary represents an action.
                 Each dictionary contains 'question_id' (int) and 'action' (str).
                 Example: [{'question_id': 1, 'action': 'show'}, {'question_id': 1, 'action': 'answer'}]

    Returns:
        The question_id with the highest answer rate.

    Examples:
        >>> actions = [{'question_id': 1, 'action': 'show'}, {'question_id': 1, 'action': 'answer'}, {'question_id': 2, 'action': 'show'}]
        >>> solve(actions)
        1
    """
    # counts[question_id] = [show_count, answer_count]
    counts = defaultdict(lambda: [0, 0])

    # Aggregate counts for each question in a single pass
    for action_entry in actions:
        q_id = action_entry['question_id']
        action_type = action_entry['action']
        
        if action_type == 'show':
            counts[q_id][0] += 1
        elif action_type == 'answer':
            counts[q_id][1] += 1

    best_question_id = -1
    max_rate = -1.0

    # Iterate through aggregated data to find the maximum rate
    # We sort keys to handle the tie-breaking rule (smallest ID) naturally if needed,
    # but a simple comparison logic is more efficient.
    for q_id in sorted(counts.keys()):
        show_count, answer_count = counts[q_id]
        
        # Avoid division by zero; though problem constraints usually imply show_count > 0
        if show_count > 0:
            current_rate = answer_count / show_count
            
            # Update if we find a strictly higher rate. 
            # Because we iterate through sorted keys, the first occurrence of a max_rate
            # will naturally be the smallest ID.
            if current_rate > max_rate:
                max_rate = current_rate
                best_question_id = q_id

    return best_question_id
