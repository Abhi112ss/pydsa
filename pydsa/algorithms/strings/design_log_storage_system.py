METADATA = {
    "id": 635,
    "name": "Design Log Storage System",
    "slug": "design-log-storage-system",
    "category": "Design",
    "aliases": [],
    "tags": ["design", "string", "sorting"],
    "difficulty": "medium",
    "time_complexity": "O(N) per query where N is the number of logs",
    "space_complexity": "O(N) to store the logs",
    "description": "Design a system that stores logs with timestamps and allows querying logs within a specific time range and granularity.",
}

class LogStorage:
    def __init__(self) -> None:
        """
        Initializes the log storage system.
        """
        self.logs: list[str] = []

    def append(self, timestamp: str, message: str) -> None:
        """
        Appends a log entry to the system.

        Args:
            timestamp (str): The timestamp of the log in format 'YYYYMMDDHHMMSS'.
            message (str): The log message.
        """
        self.logs.append(timestamp + message)

    def query(self, start: str, end: str, granularity: str) -> int:
        """
        Queries the number of logs within a specific time range and granularity.

        Args:
            start (str): The start of the time range.
            end (str): The end of the time range.
            granularity (str): The granularity of the range ('Year', 'Month', 'Day', 'Hour', 'Minute', 'Second').

        Returns:
            int: The number of logs that fall within the specified range.

        Examples:
            >>> storage = LogStorage()
            >>> storage.append("20190101000000", "error")
            >>> storage.append("20190101000100", "error")
            >>> storage.query("20190101000000", "20190101000059", "Second")
            1
        """
        # Map granularity to the number of characters to keep from the timestamp
        # YYYYMMDDHHMMSS -> 4, 6, 8, 10, 12, 14
        granularity_map = {
            "Year": 4,
            "Month": 6,
            "Day": 8,
            "Hour": 10,
            "Minute": 12,
            "Second": 14
        }
        
        length = granularity_map[granularity]
        
        # Truncate the start and end bounds to the required granularity
        # This allows us to use lexicographical string comparison
        start_prefix = start[:length]
        end_prefix = end[:length]
        
        count = 0
        for log in self.logs:
            # Extract the timestamp part of the log entry
            log_timestamp = log[:length]
            
            # Check if the truncated log timestamp falls within the inclusive range
            if start_prefix <= log_timestamp <= end_prefix:
                count += 1
                
        return count

def solve():
    """
    Example usage of the LogStorage class.
    """
    storage = LogStorage()
    storage.append("20190101000000", "error")
    storage.append("20190101000100", "error")
    storage.append("20190101000059", "error")
    
    # Querying for logs in the first minute of 2019
    print(storage.query("20190101000000", "20190101000059", "Minute")) # Expected: 2
