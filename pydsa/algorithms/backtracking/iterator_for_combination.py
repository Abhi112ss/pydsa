METADATA = {
    "id": 1286,
    "name": "Iterator for Combination",
    "slug": "iterator_for_combination",
    "category": "Design",
    "aliases": [],
    "tags": ["backtracking", "design", "bit_manipulation"],
    "difficulty": "medium",
    "time_complexity": "O(k) per next() call",
    "space_complexity": "O(k) to store current state",
    "description": "Implement an iterator that returns all possible combinations of k elements from a set of n elements.",
}

class CombinationIterator:
    """
    An iterator that generates all combinations of k elements from the set {1, 2, ..., n}.
    
    This implementation uses a lexicographical generation approach (Gosper's Hack 
    logic or similar pointer-based movement) to find the next combination in O(k) time.
    """

    def __init__(self, n: int, k: int):
        """
        Initializes the iterator with n and k.

        Args:
            n (int): The upper bound of the set {1, 2, ..., n}.
            k (int): The size of each combination.
        """
        self.n = n
        self.k = k
        # We store the current combination as a list of integers.
        # Using 1-based indexing as per problem description.
        self.current_combination: list[int] = list(range(1, k + 1))
        # If k > n, no combinations are possible.
        self.has_next = k <= n and k >= 0

    def next(self) -> list[int]:
        """
        Returns the next combination in lexicographical order.

        Returns:
            list[int]: The next combination.

        Raises:
            StopIteration: If there are no more combinations.
        """
        if not self.has_next:
            raise StopIteration()

        # Store the result to return
        result = list(self.current_combination)

        # Find the next lexicographical combination
        # 1. Find the rightmost element that can be incremented
        # An element at index i can be incremented if it is less than n - k + i + 1
        pivot_index = -1
        for i in range(self.k - 1, -1, -1):
            if self.current_combination[i] < self.n - self.k + i + 1:
                pivot_index = i
                break

        if pivot_index == -1:
            # No more combinations available
            self.has_next = False
        else:
            # 2. Increment the pivot element
            self.current_combination[pivot_index] += 1
            # 3. Reset all elements to the right of the pivot to be sequential
            for j in range(pivot_index + 1, self.k):
                self.current_combination[j] = self.current_combination[j - 1] + 1

        return result

    def has_next(self) -> bool:
        """
        Checks if there are more combinations available.

        Returns:
            bool: True if more combinations exist, False otherwise.
        """
        return self.has_next

def solve():
    """
    Example usage of the CombinationIterator.
    """
    # Example 1: n=4, k=2
    # Combinations: [1,2], [1,3], [1,4], [2,3], [2,4], [3,4]
    it = CombinationIterator(4, 2)
    results = []
    while it.has_next():
        results.append(it.next())
    print(f"n=4, k=2: {results}")

    # Example 2: n=5, k=3
    it2 = CombinationIterator(5, 3)
    results2 = []
    while it2.has_next():
        results2.append(it2.next())
    print(f"n=5, k=3: {results2}")
