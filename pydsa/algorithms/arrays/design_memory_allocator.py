METADATA = {
    "id": 2502,
    "name": "Design Memory Allocator",
    "slug": "design-memory-allocator",
    "category": "Design",
    "aliases": [],
    "tags": ["array", "simulation"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Design a memory allocator that manages a fixed-size memory block and handles allocation and deallocation requests.",
}

class Allocator:
    def __init__(self, n: int):
        """
        Initializes the memory allocator with n units of memory.

        Args:
            n (int): The total size of the memory.
        """
        self.size = n
        # Initialize memory with 0 (representing free space)
        self.memory = [0] * n

    def allocate(self, blockSize: int, requestId: int) -> int:
        """
        Allocates a contiguous block of memory of size blockSize.

        Args:
            blockSize (int): The number of contiguous units required.
            requestId (int): The unique identifier for this allocation.

        Returns:
            int: The starting index of the allocated block, or -1 if no block is found.

        Examples:
            >>> allocator = Allocator(10)
            >>> allocator.allocate(1, 1)
            0
            >>> allocator.allocate(3, 2)
            1
            >>> allocator.allocate(6, 3)
            -1
        """
        consecutive_free = 0
        start_index = -1

        # Scan memory for the first available contiguous block of size blockSize
        for i in range(self.size):
            if self.memory[i] == 0:
                if consecutive_free == 0:
                    start_index = i
                consecutive_free += 1
                
                if consecutive_free == blockSize:
                    # Found a sufficient block, fill it with requestId
                    for j in range(start_index, start_index + blockSize):
                        self.memory[j] = requestId
                    return start_index
            else:
                # Reset counter if we hit an occupied unit
                consecutive_free = 0
                start_index = -1
        
        return -1

    def free(self, requestId: int) -> None:
        """
        Frees all memory blocks associated with the given requestId.

        Args:
            requestId (int): The unique identifier of the allocation to free.

        Examples:
            >>> allocator = Allocator(10)
            >>> allocator.allocate(3, 1)
            0
            >>> allocator.free(1)
            >>> allocator.allocate(3, 2)
            0
        """
        # Iterate through memory and reset units matching the requestId to 0
        for i in range(self.size):
            if self.memory[i] == requestId:
                self.memory[i] = 0

def solve():
    """
    Entry point for testing the implementation.
    """
    # Test Case 1
    allocator = Allocator(10)
    assert allocator.allocate(1, 1) == 0
    assert allocator.allocate(3, 2) == 1
    assert allocator.allocate(6, 3) == -1
    assert allocator.allocate(4, 4) == 4
    allocator.free(1)
    assert allocator.allocate(1, 5) == 0
    assert allocator.allocate(2, 6) == 0
    assert allocator.allocate(2, 7) == 7
    assert allocator.allocate(1, 8) == 9
    assert allocator.allocate(1, 9) == -1
