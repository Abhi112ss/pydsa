METADATA = {
    "id": 1152,
    "name": "Analyze User Website Visit Pattern",
    "slug": "analyze-user-website-visit-pattern",
    "category": "Hash Table",
    "aliases": [],
    "tags": ["hash_map", "sorting", "brute_force"],
    "difficulty": "hard",
    "time_complexity": "O(U * V^3)",
    "space_complexity": "O(U * V^3)",
    "description": "Find the most frequent 3-sequence of website visits across all users, prioritizing the one with the smallest first and second elements in case of ties.",
}

from collections import defaultdict

def solve(users: list[list[int]], visits: list[list[int]]) -> list[int]:
    """
    Analyzes website visit patterns to find the most frequent 3-sequence.

    Args:
        users: A list of lists where users[i] contains the IDs of users who visited the websites.
        visits: A list of lists where visits[i] contains [timestamp, user_id, website_id].

    Returns:
        A list of three integers representing the most frequent 3-sequence [web1, web2, web3].

    Examples:
        >>> users = [[0, 1, 2], [0, 1], [2, 1, 0], [1, 0], [0, 1]]
        >>> visits = [[1, 0, 5], [2, 1, 5], [3, 2, 5], [4, 1, 5], [5, 0, 5], [6, 1, 5], [7, 2, 5], [8, 0, 5], [9, 1, 5], [10, 2, 5]]
        >>> solve(users, visits)
        [5, 5, 5]
    """
    # Map user_id to a sorted list of (timestamp, website_id)
    user_history = defaultdict(list)
    for timestamp, user_id, website_id in visits:
        user_history[user_id].append((timestamp, website_id))

    # Sort each user's history by timestamp to ensure chronological order
    for user_id in user_history:
        user_history[user_id].sort()

    # Map user_id to a list of website_ids in chronological order
    user_websites = defaultdict(list)
    for user_id, history in user_history.items():
        user_websites[user_id] = [web_id for _, web_id in history]

    # Global frequency map for 3-sequences
    sequence_counts = defaultdict(int)

    # Iterate through each user to find all unique 3-sequences they visited
    for user_id in user_websites:
        websites = user_websites[user_id]
        n = len(websites)
        if n < 3:
            continue
        
        # Use a set to ensure we only count a specific 3-sequence once per user
        user_unique_sequences = set()
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    user_unique_sequences.add((websites[i], websites[j], websites[k]))
        
        # Increment global counts for sequences found for this user
        for seq in user_unique_sequences:
            sequence_counts[seq] += 1

    # Find the best sequence based on frequency, then lexicographical order
    # We want max frequency, then min web1, then min web2, then min web3
    # We can achieve this by sorting with a custom key
    best_sequence = []
    max_freq = -1

    # Sort keys to handle tie-breaking: frequency descending, then web1, web2, web3 ascending
    # Python's sort is stable, but we can use a single key for efficiency
    for seq, freq in sequence_counts.items():
        if freq > max_freq:
            max_freq = freq
            best_sequence = list(seq)
        elif freq == max_freq:
            # Tie-breaking logic: compare elements one by one
            if list(seq) < best_sequence:
                best_sequence = list(seq)

    return best_sequence
