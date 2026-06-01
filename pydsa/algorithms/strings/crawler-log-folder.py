METADATA = {
    "id": 1598,
    "name": "Crawler Log Folder",
    "slug": "crawler-log-folder",
    "category": "String",
    "aliases": [],
    "tags": ["string", "sorting"],
    "difficulty": "medium",
    "time_complexity": "O(n log n * k)",
    "space_complexity": "O(n * k)",
    "description": "Sort a list of log messages where each message starts with a severity level followed by a numeric ID and a message string, comparing numeric parts numerically.",
}

import re
from functools import cmp_to_key

def solve(logs: list[str]) -> list[str]:
    """
    Sorts log messages based on custom rules:
    1. Compare severity levels (error < info < warning).
    2. If severity is the same, compare numeric IDs numerically.
    3. If IDs are also the same, compare the message strings lexicographically.

    Args:
        logs: A list of log strings in the format "[severity] [id] [message]".

    Returns:
        A list of sorted log strings.

    Examples:
        >>> solve(["[warning] [10] [a]", "[error] [2] [b]", "[info] [1] [c]"])
        ['[error] [2] [b]', '[info] [1] [c]', '[warning] [10] [a]']
    """
    
    # Severity priority mapping
    severity_order = {
        "error": 0,
        "info": 1,
        "warning": 2
    }

    def compare_logs(log_a: str, log_b: str) -> int:
        """
        Custom comparator for two log strings.
        """
        # Split the log into components: [severity], [id], and the rest of the message
        # We use a regex or manual split to isolate the first three parts
        # Format: "[severity] [id] message"
        
        parts_a = log_a.split(" ", 2)
        parts_b = log_b.split(" ", 2)

        # 1. Compare Severity
        # Strip brackets from "[error]" -> "error"
        sev_a = parts_a[0][1:-1]
        sev_b = parts_b[0][1:-1]
        
        if sev_a != sev_b:
            return severity_order[sev_a] - severity_order[sev_b]

        # 2. Compare Numeric IDs
        # Strip brackets from "[10]" -> "10"
        id_a = int(parts_a[1][1:-1])
        id_b = int(parts_b[1][1:-1])
        
        if id_a != id_b:
            return id_a - id_b

        # 3. Compare Message Strings Lexicographically
        # The message is the third part (index 2)
        msg_a = parts_a[2]
        msg_b = parts_b[2]
        
        if msg_a < msg_b:
            return -1
        elif msg_a > msg_b:
            return 1
        else:
            return 0

    # Use cmp_to_key to convert our comparator into a key function for sort()
    # The complexity is O(N log N) comparisons, where each comparison is O(K)
    # where K is the length of the log string.
    return sorted(logs, key=cmp_to_key(compare_logs))
