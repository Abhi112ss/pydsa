METADATA = {
    "id": 937,
    "name": "Reorder Data in Log Files",
    "slug": "reorder-data-in-log-files",
    "category": "String",
    "aliases": [],
    "tags": ["sorting", "string"],
    "difficulty": "medium",
    "time_complexity": "O(n log n * m)",
    "space_complexity": "O(n * m)",
    "description": "Reorder log files such that letter-logs come before digit-logs, and letter-logs are sorted lexicographically by their contents.",
}

def solve(logs: list[str]) -> list[str]:
    """
    Reorders log files according to specific rules:
    1. Letter-logs come before digit-logs.
    2. Letter-logs are sorted lexicographically by their content.
    3. If contents are identical, letter-logs are sorted by their identifiers.
    4. Digit-logs maintain their original relative order.

    Args:
        logs: A list of strings representing the log files.

    Returns:
        A list of strings representing the reordered log files.

    Examples:
        >>> solve(["dig1 8 1 5 1", "let1 art can", "dig2 3 6 7"])
        ['let1 art can', 'dig1 8 1 5 1', 'dig2 3 6 7']
        >>> solve(["a1 t1", "a2 t1", "a3 t2"])
        ['a1 t1', 'a2 t1', 'a3 t2']
    """
    
    def get_sort_key(log: str):
        # Split the log into identifier and the rest of the content
        # We use maxsplit=1 because the content itself can contain spaces
        parts = log.split(" ", 1)
        identifier = parts[0]
        content = parts[1]

        # Check if the content starts with a digit
        # If it's a digit-log, we return a tuple that places it after letter-logs
        # The first element 1 indicates a digit-log, the second is the original index
        # to ensure stable sorting (though Python's sort is stable by default).
        if content[0].isdigit():
            return (1, 0, 0)  # Type 1: Digit-log
        
        # If it's a letter-log, we return a tuple that places it before digit-logs
        # The first element 0 indicates a letter-log.
        # The second element is the content for lexicographical comparison.
        # The third element is the identifier for tie-breaking.
        return (0, content, identifier)

    # Python's sort is Timsort, which is stable. 
    # This stability is crucial for maintaining the relative order of digit-logs.
    # We use a custom key to handle the two distinct types of logs.
    
    # To strictly maintain digit-log order without including index in key, 
    # we can separate them or rely on the fact that digit-logs will have 
    # the same key (1, 0, 0) and Timsort preserves order for equal keys.
    
    # However, to be explicit and robust, we can use a key that distinguishes 
    # letter-logs (type 0) from digit-logs (type 1).
    
    def sorting_logic(log: str):
        parts = log.split(" ", 1)
        identifier = parts[0]
        content = parts[1]
        
        if content[0].isdigit():
            # Digit logs: type 1, content/id don't matter for sorting relative to each other
            # because stability handles their original order.
            return (1,)
        else:
            # Letter logs: type 0, then content, then identifier
            return (0, content, identifier)

    return sorted(logs, key=sorting_logic)
