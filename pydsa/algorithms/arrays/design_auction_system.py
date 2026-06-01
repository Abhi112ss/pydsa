METADATA = {
    "id": 3815,
    "name": "Design Auction System",
    "slug": "design_auction_system",
    "category": "Design",
    "aliases": [],
    "tags": ["heap", "hash_map", "design"],
    "difficulty": "medium",
    "time_complexity": "O(log N)",
    "space_complexity": "O(N)",
    "description": "Design a system to manage auction bids with real-time updates and retrieval of the highest bidder.",
}

import heapq

class AuctionSystem:
    """
    A system to manage auction bids using a max-heap for efficient retrieval
    of the highest bid and a hash map for tracking user-specific bid status.
    """

    def __init__(self):
        # Max-heap stores tuples: (-bid_amount, auction_id, user_id, timestamp)
        # We use negative bid_amount to simulate a max-heap using Python's min-heap.
        self.heap: list[tuple[float, int, int, int]] = []
        
        # Maps user_id -> current_highest_bid_for_that_user
        # This allows us to perform "lazy deletion" from the heap.
        self.user_bids: dict[int, float] = {}
        
        # Counter to provide unique, increasing timestamps for tie-breaking
        self.timer: int = 0

    def place_bid(self, user_id: int, auction_id: int, amount: float) -> bool:
        """
        Places a bid for a specific user on an auction.
        
        Args:
            user_id: The unique identifier of the bidder.
            auction_id: The unique identifier of the auction.
            amount: The bid amount.

        Returns:
            bool: True if the bid is valid (higher than the user's previous bid), False otherwise.
        """
        self.timer += 1
        
        # Check if this is a valid increase for the user
        current_max = self.user_bids.get(user_id, -1.0)
        if amount <= current_max:
            return False
        
        # Update user's record and push to heap
        self.user_bids[user_id] = amount
        # We use -amount for max-heap behavior. 
        # auction_id and timer are used as tie-breakers.
        heapq.heappush(self.heap, (-amount, auction_id, user_id, self.timer))
        return True

    def get_highest_bidder(self, auction_id: int) -> tuple[int, float] | None:
        """
        Retrieves the highest bidder for a specific auction.
        
        Args:
            auction_id: The ID of the auction to query.

        Returns:
            A tuple of (user_id, amount) or None if no valid bids exist for this auction.
        """
        # Lazy removal: Clean the top of the heap if the bid is no longer the user's highest
        # or if the auction_id doesn't match the query.
        # Note: In a real-world multi-auction system, the heap would likely be 
        # partitioned by auction_id or we would filter by auction_id.
        # For this implementation, we assume the heap contains all bids.
        
        # Since the problem asks for the highest bidder *for a specific auction*,
        # a single global heap requires us to iterate or use multiple heaps.
        # To maintain O(log N) for place_bid, we use a dictionary of heaps.
        # Let's refine the implementation logic below.
        return None

class AuctionSystemOptimized:
    """
    Refined implementation using a dictionary of heaps to support 
    O(log N) per auction queries.
    """

    def __init__(self):
        # Maps auction_id -> max-heap of (-amount, user_id, timestamp)
        self.auctions: dict[int, list[tuple[float, int, int]]] = {}
        # Maps (auction_id, user_id) -> current_max_bid
        self.user_auction_bids: dict[tuple[int, int], float] = {}
        self.timer: int = 0

    def place_bid(self, user_id: int, auction_id: int, amount: float) -> bool:
        """
        Places a bid for a specific user on an auction.
        """
        self.timer += 1
        key = (auction_id, user_id)
        current_max = self.user_auction_bids.get(key, -1.0)
        
        if amount <= current_max:
            return False
        
        self.user_auction_bids[key] = amount
        if auction_id not in self.auctions:
            self.auctions[auction_id] = []
            
        # Push to the specific auction's heap
        heapq.heappush(self.auctions[auction_id], (-amount, user_id, self.timer))
        return True

    def get_highest_bidder(self, auction_id: int) -> tuple[int, float] | None:
        """
        Retrieves the highest bidder for a specific auction.
        """
        if auction_id not in self.auctions:
            return None
        
        heap = self.auctions[auction_id]
        
        # Lazy removal: Pop elements from the heap that are no longer valid
        # (i.e., the user has placed a higher bid since this one was added)
        while heap:
            neg_amount, user_id, timestamp = heap[0]
            actual_amount = -neg_amount
            
            # Check if this bid is still the user's current highest for this auction
            if self.user_auction_bids.get((auction_id, user_id)) == actual_amount:
                return (user_id, actual_amount)
            else:
                heapq.heappop(heap)
                
        return None

def solve():
    """
    Example usage of the AuctionSystemOptimized.
    """
    auction = AuctionSystemOptimized()
    
    # Test Case 1: Basic bidding
    assert auction.place_bid(1, 101, 50.0) is True
    assert auction.place_bid(2, 101, 60.0) is True
    assert auction.place_bid(1, 101, 70.0) is True  # User 1 increases bid
    assert auction.place_bid(1, 101, 65.0) is False # User 1 tries to lower bid
    
    # Test Case 2: Retrieval
    # Highest for auction 101 should be User 1 with 70.0
    assert auction.get_highest_bidder(101) == (1, 70.0)
    
    # Test Case 3: Different auctions
    assert auction.place_bid(3, 102, 100.0) is True
    assert auction.get_highest_bidder(101) == (1, 70.0)
    assert auction.get_highest_bidder(102) == (3, 100.0)
    
    # Test Case 4: Empty auction
    assert auction.get_highest_bidder(999) is None
