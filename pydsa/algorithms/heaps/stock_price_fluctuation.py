METADATA = {
    "id": 2034,
    "name": "Stock Price Fluctuation",
    "slug": "stock-price-fluctuation",
    "category": "Heap",
    "aliases": [],
    "tags": ["heap", "hash_map", "priority_queue"],
    "difficulty": "medium",
    "time_complexity": "O(q log q)",
    "space_complexity": "O(q)",
    "description": "Design a system to track stock price changes and retrieve the maximum and minimum prices efficiently.",
}

import heapq

class StockPriceTracker:
    def __init__(self, initial_price: int):
        """
        Initializes the tracker with an initial price.
        
        Args:
            initial_price (int): The starting price of the stock.
        """
        self.current_price = initial_price
        self.price_map = {1: initial_price}
        
        # Max-heap stores (-price, timestamp) to simulate max behavior
        self.max_heap = [(-initial_price, 1)]
        # Min-heap stores (price, timestamp)
        self.min_heap = [(initial_price, 1)]

    def update(self, timestamp: int, price: int) -> None:
        """
        Updates the stock price at a given timestamp.

        Args:
            timestamp (int): The time of the update.
            price (int): The new price.
        """
        self.current_price = price
        self.price_map[timestamp] = price
        
        # Push new price into both heaps
        heapq.heappush(self.max_heap, (-price, timestamp))
        heapq.heappush(self.min_heap, (price, timestamp))

    def current() -> int:
        """
        Returns the current price.
        Note: This is a placeholder for the solve structure; 
        the actual logic is handled within the class.
        """
        pass

    def maximum() -> int:
        """
        Returns the maximum price currently in the system.
        """
        pass

    def minimum() -> int:
        """
        Returns the minimum price currently in the system.
        """
        pass

def solve(queries: list[list[int]]) -> list[int]:
    """
    Processes a list of queries for stock price fluctuations.

    Args:
        queries (list[list[int]]): A list of queries where:
            - queries[i][0] is the type (1: update, 2: current, 3: maximum, 4: minimum)
            - queries[i][1] is the timestamp (for type 1)
            - queries[i][2] is the price (for type 1)

    Returns:
        list[int]: The results of the queries (only for types 2, 3, and 4).

    Examples:
        >>> solve([[1, 1, 10], [2, 0, 0], [2, 0, 0], [3, 0, 0], [4, 0, 0], [1, 2, 5], [2, 0, 0], [3, 0, 0], [4, 0, 0]])
        [10, 10, 10, 5, 5]
    """
    # The problem description implies the first update is always at timestamp 1.
    # However, the input format for LeetCode is a list of queries.
    # We need to handle the initial price logic carefully.
    
    # Since the problem states the first query is always an update at timestamp 1,
    # we initialize the tracker with a dummy value or handle the first update.
    # Actually, the standard LeetCode problem starts with an initial price.
    # Let's assume the first query is always an update at timestamp 1.
    
    # To match LeetCode's specific input structure:
    # queries[i] = [type, timestamp, price] or [type, timestamp]
    
    # We'll use a dummy initial price and update it with the first query.
    # But the problem says: "The first query is always an update at timestamp 1."
    # Let's initialize with a value that will be overwritten.
    
    tracker = None
    results = []

    for query in queries:
        q_type = query[0]
        
        if q_type == 1:
            timestamp, price = query[1], query[2]
            if tracker is None:
                tracker = StockPriceTracker(price)
                # Since the first query is an update, we don't want to double-add.
                # But the constructor adds it. Let's adjust.
                # A cleaner way:
                tracker = StockPriceTracker(0) 
                # Overwrite the initial 0 with the first update
                tracker.update(timestamp, price)
            else:
                tracker.update(timestamp, price)
        
        elif q_type == 2:
            results.append(tracker.current_price)
            
        elif q_type == 3:
            # Lazy deletion: remove elements from max_heap if they don't match price_map
            while tracker.max_heap:
                neg_price, timestamp = tracker.max_heap[0]
                if -neg_price == tracker.price_map.get(timestamp, -1):
                    break
                heapq.heappop(tracker.max_heap)
            results.append(-tracker.max_heap[0][0])
            
        elif q_type == 4:
            # Lazy deletion: remove elements from min_heap if they don't match price_map
            while tracker.min_heap:
                price, timestamp = tracker.min_heap[0]
                if price == tracker.price_map.get(timestamp, -1):
                    break
                heapq.heappop(tracker.min_heap)
            results.append(tracker.min_heap[0][0])

    return results

# Redefining the class and solve to be more robust for the specific LeetCode input
class StockPrice:
    def __init__(self, initial_price: int):
        self.price_map = {1: initial_price}
        self.current_timestamp = 1
        self.current_price = initial_price
        self.max_heap = [(-initial_price, 1)]
        self.min_heap = [(initial_price, 1)]

    def update(self, timestamp: int, price: int) -> None:
        self.current_timestamp = timestamp
        self.current_price = price
        self.price_map[timestamp] = price
        heapq.heappush(self.max_heap, (-price, timestamp))
        heapq.heappush(self.min_heap, (price, timestamp))

    def current(self) -> int:
        return self.current_price

    def maximum(self) -> int:
        # Clean up max_heap: remove stale prices (where timestamp price != current price at that timestamp)
        while -self.max_heap[0][0] != self.price_map[self.max_heap[0][1]]:
            heapq.heappop(self.max_heap)
        return -self.max_heap[0][0]

    def minimum(self) -> int:
        # Clean up min_heap: remove stale prices
        while self.min_heap[0][0] != self.price_map[self.min_heap[0][1]]:
            heapq.heappop(self.min_heap)
        return self.min_heap[0][0]

def solve_final(initial_price: int, queries: list[list[int]]) -> list[int]:
    """
    The actual implementation logic for the LeetCode problem.
    
    Args:
        initial_price (int): The starting price.
        queries (list[list[int]]): The list of operations.
        
    Returns:
        list[int]: Results of queries.
    """
    tracker = StockPrice(initial_price)
    results = []
    
    for q in queries:
        if q[0] == 1:
            tracker.update(q[1], q[2])
        elif q[0] == 2:
            results.append(tracker.current())
        elif q[0] == 3:
            results.append(tracker.maximum())
        elif q[0] == 4:
            results.append(tracker.minimum())
            
    return results

# Note: The LeetCode problem structure usually provides the class definition.
# The solve() function below is a wrapper to fit the requested format.

def solve(queries: list[list[int]]) -> list[int]:
    """
    Wrapper for the StockPrice class to process queries.
    Note: LeetCode #2034 provides an initial price separately.
    In the context of this single-file solver, we assume the first query 
    is the update that sets the initial price or we extract it.
    """
    # Based on LeetCode's test cases, the first query is always an update at timestamp 1.
    # We'll initialize with the price from the first query.
    first_query = queries[0]
    tracker = StockPrice(first_query[2])
    
    # If the first query was an update, we've already processed it.
    # But we must skip it in the loop.
    results = []
    for i in range(1, len(queries)):
        q = queries[i]
        if q[0] == 1:
            tracker.update(q[1], q[2])
        elif q[0] == 2:
            results.append(tracker.current())
        elif q[0] == 3:
            results.append(tracker.maximum())
        elif q[0] == 4:
            results.append(tracker.minimum())
    return results

# Correcting the solve function to handle the standard LeetCode input format 
# where the class is instantiated with an initial price.
# Since the prompt asks for a single solve() function, I will implement 
# the logic inside solve() assuming queries[0] is the first update.

def solve(queries: list[list[int]]) -> list[int]:
    """
    Processes stock price queries.
    
    Args:
        queries (list[list[int]]): List of queries.
            Type 1: [1, timestamp, price]
            Type 2: [2, timestamp] (timestamp is ignored)
            Type 3: [3, timestamp] (timestamp is ignored)
            Type 4: [4, timestamp] (timestamp is ignored)

    Returns:
        list[int]: Results of queries 2, 3, and 4.
    """
    # The problem states: "The first query is always an update at timestamp 1."
    # We use this to initialize our tracker.
    initial_price = queries[0][2]
    tracker = StockPrice(initial_price)
    
    results = []
    # Start from index 1 because index 0 was used for initialization
    for i in range(1, len(queries)):
        q = queries[i]
        op = q[0]
        
        if op == 1:
            tracker.update(q[1], q[2])
        elif op == 2:
            results.append(tracker.current())
        elif op == 3:
            results.append(tracker.maximum())
        elif op == 4:
            results.append(tracker.minimum())
            
    return results