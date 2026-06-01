METADATA = {
    "id": 3885,
    "name": "Design Event Manager",
    "slug": "design_event_manager",
    "category": "Design",
    "aliases": [],
    "tags": ["heap", "design", "priority_queue"],
    "difficulty": "medium",
    "time_complexity": "O(log n)",
    "space_complexity": "O(n)",
    "description": "Design a system to manage events with priorities and timestamps, allowing for efficient retrieval and removal of the highest priority event.",
}

import heapq

class EventManager:
    """
    A system to manage events based on priority and timestamp.
    
    The system supports adding events, removing specific events, and 
    retrieving the event with the highest priority. If priorities are equal,
    the event with the earlier timestamp is prioritized.
    """

    def __init__(self) -> None:
        """Initializes the EventManager."""
        # Max-heap for priority. Python's heapq is a min-heap, 
        # so we store priority as negative.
        # Format: (-priority, timestamp, event_id)
        self.heap: list[tuple[int, int, int]] = []
        
        # Dictionary to track valid event_ids and their current priority/timestamp.
        # This allows for "lazy removal" from the heap.
        self.valid_events: dict[int, tuple[int, int]] = {}

    def add_event(self, event_id: int, priority: int, timestamp: int) -> None:
        """
        Adds a new event or updates an existing event.

        Args:
            event_id: Unique identifier for the event.
            priority: Priority level (higher value means higher priority).
            timestamp: The time the event was created.
        """
        self.valid_events[event_id] = (priority, timestamp)
        # We use -priority to simulate a max-heap using Python's min-heap.
        # We use timestamp as the second element to handle tie-breaking.
        heapq.heappush(self.heap, (-priority, timestamp, event_id))

    def remove_event(self, event_id: int) -> None:
        """
        Removes an event from the manager.

        Args:
            event_id: The unique identifier of the event to remove.
        """
        if event_id in self.valid_events:
            del self.valid_events[event_id]

    def get_highest_priority_event(self) -> int | None:
        """
        Retrieves the event_id of the highest priority event.

        Returns:
            The event_id of the highest priority event, or None if no events exist.
        """
        # Lazy removal: Clean the top of the heap if the event is no longer valid
        # or if the priority/timestamp in the heap doesn't match the current state.
        while self.heap:
            neg_priority, timestamp, event_id = self.heap[0]
            
            if event_id in self.valid_events:
                current_priority, current_timestamp = self.valid_events[event_id]
                # Check if the heap entry is the most recent version of this event
                if -neg_priority == current_priority and timestamp == current_timestamp:
                    return event_id
            
            # If the top element is invalid or outdated, pop it.
            heapq.heappop(self.heap)
            
        return None

def solve() -> None:
    """
    Example usage of the EventManager.
    """
    manager = EventManager()
    
    # Add events
    manager.add_event(1, 10, 100)
    manager.add_event(2, 20, 50)
    manager.add_event(3, 20, 30)  # Same priority as 2, but earlier timestamp
    
    # Highest priority should be event 3 (priority 20, timestamp 30)
    print(f"Highest priority: {manager.get_highest_priority_event()}") # Expected: 3
    
    # Remove event 3
    manager.remove_event(3)
    print(f"Highest priority after removal: {manager.get_highest_priority_event()}") # Expected: 2
    
    # Update event 1 to higher priority
    manager.add_event(1, 30, 150)
    print(f"Highest priority after update: {manager.get_highest_priority_event()}") # Expected: 1
