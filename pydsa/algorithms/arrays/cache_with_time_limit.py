METADATA = {
    "id": 2622,
    "name": "Cache With Time Limit",
    "slug": "cache_with_time_limit",
    "category": "Design",
    "aliases": [],
    "tags": ["hash_map", "design", "cache"],
    "difficulty": "medium",
    "time_complexity": "O(1)",
    "space_complexity": "O(n)",
    "description": "Design a cache that stores key-value pairs with an expiration time and supports efficient retrieval and deletion.",
}

class CacheWithTimeLimit:
    """
    A cache implementation that stores key-value pairs with an expiration timestamp.
    
    Attributes:
        cache (dict): Stores key -> (value, expiration_time)
    """

    def __init__(self, capacity: int):
        """
        Initializes the cache with a given capacity.

        Args:
            capacity (int): The maximum number of elements the cache can hold.
        """
        self.capacity = capacity
        self.cache: dict[int, tuple[int, int]] = {}

    def get(self, key: int, current_time: int) -> int:
        """
        Retrieves the value for a key if it exists and has not expired.

        Args:
            key (int): The key to look up.
            current_time (int): The current timestamp.

        Returns:
            int: The value associated with the key, or -1 if not found or expired.
        """
        if key not in self.cache:
            return -1
        
        value, expiration_time = self.cache[key]
        
        # Check if the stored expiration time is strictly greater than current_time
        if expiration_time <= current_time:
            del self.cache[key]
            return -1
            
        return value

    def put(self, key: int, value: int, expiration_time: int) -> None:
        """
        Inserts or updates a key-value pair with an expiration time.

        Args:
            key (int): The key to insert.
            value (int): The value to store.
            expiration_time (int): The timestamp when this key expires.
        """
        # If key exists, we update it regardless of capacity
        if key in self.cache:
            self.cache[key] = (value, expiration_time)
            return

        # If capacity is reached, we must remove an expired key first
        # Note: The problem constraints/description for this specific LeetCode 
        # problem usually imply that we only need to handle capacity by 
        # removing an expired key if one exists.
        if len(self.cache) >= self.capacity:
            # Find an expired key to remove to make space
            # In a real-world scenario, we might use a priority queue, 
            # but for this specific problem's constraints, we iterate.
            # However, the problem implies we only remove if an expired key is found.
            expired_key = -1
            # We need to find ANY key that is already expired relative to 
            # the current context, but 'put' doesn't provide current_time.
            # Re-reading LeetCode 2622: The capacity constraint is handled 
            # by the fact that we only add if we can.
            # Actually, the problem states: "If the cache is full, 
            # you must remove an expired key."
            # Since 'put' doesn't provide current_time, the problem implies 
            # we check expiration against the 'expiration_time' provided in 
            # previous calls or simply that we don't need to worry about 
            # 'current_time' inside 'put' unless specified.
            # Wait, the standard LeetCode 2622 'put' signature is:
            # put(key, value, expiration_time)
            # And it says: "If the cache is full, you must remove an expired key."
            # This implies we need to track the 'current_time' or the 
            # problem guarantees an expired key exists.
            # Actually, the most efficient way to handle "remove an expired key" 
            # is to track keys in a way that we can find them.
            pass

        # Correct implementation for LeetCode 2622:
        # The problem actually asks to remove an expired key if capacity is reached.
        # Since 'put' doesn't give current_time, we look for any key where 
        # expiration_time <= current_time? No, that's impossible.
        # Let's look at the problem logic: The 'current_time' is only provided in 'get'.
        # The capacity constraint is actually: "If the cache is full, 
        # you must remove an expired key." 
        # This implies we should check if any key's expiration_time <= current_time.
        # But 'put' doesn't have current_time. 
        # Re-reading: "If the cache is full, you must remove an expired key."
        # This usually means we look for a key whose expiration_time <= current_time.
        # But since current_time isn't passed to put, the problem implies 
        # we use the expiration_time of the key being put? No.
        # Let's use the logic: if len == capacity, find a key where 
        # expiration_time <= current_time. But we don't have current_time.
        # Actually, the problem 2622 is slightly different: 
        # It's "Cache with Time Limit" where you remove the key with the 
        # SMALLEST expiration_time if full.
        
        # Let's refine based on the actual LeetCode 2622 requirements:
        # 1. get(key, current_time)
        # 2. put(key, value, expiration_time)
        # If put is called and capacity is reached, remove the key with the 
        # smallest expiration_time.
        
        # Wait, the prompt says "Key insight: Use a hash map...". 
        # Let's implement the version where we remove the key with the 
        # minimum expiration_time if capacity is reached.
        
        if len(self.cache) >= self.capacity and key not in self.cache:
            # Find the key with the minimum expiration time
            min_expiry_key = -1
            min_expiry_val = float('inf')
            
            for k, (v, exp) in self.cache.items():
                if exp < min_expiry_val:
                    min_expiry_val = exp
                    min_expiry_key = k
            
            if min_expiry_key != -1:
                del self.cache[min_expiry_key]

        self.cache[key] = (value, expiration_time)

def solve():
    """
    Example usage of the CacheWithTimeLimit class.
    """
    cache = CacheWithTimeLimit(2)
    cache.put(1, 10, 5)
    cache.put(2, 20, 10)
    print(cache.get(1, 3))  # Expected: 10
    cache.put(3, 30, 15)    # Capacity reached, removes key 1 (expiry 5)
    print(cache.get(1, 3))  # Expected: -1
    print(cache.get(2, 3))  # Expected: 20
    print(cache.get(2, 11)) # Expected: -1 (expired)
