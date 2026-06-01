METADATA = {
    "id": 2284,
    "name": "Sender With Largest Word Count",
    "slug": "sender-with-largest-word-count",
    "category": "Hash Table",
    "aliases": [],
    "tags": ["hash_map", "string_manipulation"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Find the sender with the largest word count, returning the sender with the smallest lexicographical name in case of ties.",
}

def solve(messages: list[list[str]]) -> list[str]:
    """
    Finds the sender with the largest word count. If there is a tie, 
    returns the sender with the smallest lexicographical name.

    Args:
        messages: A list of lists where each inner list contains [sender, message].

    Returns:
        A list containing [sender_with_max_words, max_word_count].

    Examples:
        >>> solve([["alice", "hello world"], ["bob", "hi"]])
        ['alice', 2]
        >>> solve([["alice", "hello"], ["bob", "hi"]])
        ['alice', 1]
    """
    # Map to store the total word count for each sender
    sender_word_counts: dict[str, int] = {}

    for sender, message in messages:
        # Split message by spaces to count words
        # Note: The problem guarantees messages are non-empty and words are space-separated
        word_count = len(message.split(" "))
        
        if sender in sender_word_counts:
            sender_word_counts[sender] += word_count
        else:
            sender_word_counts[sender] = word_count

    max_words = -1
    best_sender = ""

    # Iterate through the map to find the winner
    for sender, total_count in sender_word_counts.items():
        # Update if we find a higher count, or if count is equal but name is lexicographically smaller
        if total_count > max_words:
            max_words = total_count
            best_sender = sender
        elif total_count == max_words:
            if sender < best_sender:
                best_sender = sender

    return [best_sender, max_words]
