METADATA = {
    "id": 1570,
    "name": "Dot Product of Two Sparse Vectors",
    "slug": "dot-product-of-two-sparse-vectors",
    "category": "Design",
    "aliases": [],
    "tags": ["two_pointer", "hash_map", "design"],
    "difficulty": "medium",
    "time_complexity": "O(N + M) for construction and dot product, where N and M are non-zero elements",
    "space_complexity": "O(N + M) to store non-zero elements",
    "description": "Design a class that computes the dot product of two sparse vectors.",
}

class SparseVector:
    """
    A class representing a sparse vector optimized for dot product calculations.
    
    Instead of storing all elements (including zeros), this implementation 
    stores only non-zero elements as (index, value) pairs to save space 
    and time during computation.
    """

    def __init__(self, nums: list[int]) -> None:
        """
        Initializes the SparseVector with a list of integers.

        Args:
            nums: A list of integers representing the vector.
        """
        # Store non-zero elements as a list of tuples (index, value)
        # This allows for efficient two-pointer traversal.
        self.non_zero_elements: list[tuple[int, int]] = []
        for index, value in enumerate(nums):
            if value != 0:
                self.non_zero_elements.append((index, value))

    def dotProduct(self, vec: 'SparseVector') -> int:
        """
        Computes the dot product of this vector and another sparse vector.

        Args:
            vec: Another SparseVector instance.

        Returns:
            The dot product of the two vectors.

        Examples:
            >>> v1 = SparseVector([1, 0, 0, 2, 3])
            >>> v2 = SparseVector([0, 3, 0, 4, 0])
            >>> v1.dotProduct(v2)
            8
        """
        dot_product = 0
        ptr_a = 0
        ptr_b = 0
        
        list_a = self.non_zero_elements
        list_b = vec.non_zero_elements
        len_a = len(list_a)
        len_b = len(list_b)

        # Use two pointers to traverse both lists of non-zero elements
        while ptr_a < len_a and ptr_b < len_b:
            index_a, val_a = list_a[ptr_a]
            index_b, val_b = list_b[ptr_b]

            if index_a == index_b:
                # Indices match, multiply values and add to result
                dot_product += val_a * val_b
                ptr_a += 1
                ptr_b += 1
            elif index_a < index_b:
                # Index in A is smaller, move pointer A forward
                ptr_a += 1
            else:
                # Index in B is smaller, move pointer B forward
                ptr_b += 1
                
        return dot_product

def solve() -> None:
    """
    Example usage of the SparseVector class.
    """
    v1 = SparseVector([1, 0, 0, 2, 3])
    v2 = SparseVector([0, 3, 0, 4, 0])
    print(f"Dot Product: {v1.dotProduct(v2)}")  # Expected: 8
