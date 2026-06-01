METADATA = {
    "id": 519,
    "name": "Random Flip Matrix",
    "slug": "random_flip_matrix",
    "category": "Design",
    "aliases": [],
    "tags": ["randomization", "hash_map", "design"],
    "difficulty": "medium",
    "time_complexity": "O(1)",
    "space_complexity": "O(k)",
    "description": "Design a data structure that simulates a matrix of zeros and ones, allowing for flipping elements and generating random elements in O(1) time.",
}

import random

class RandomFlipMatrix:
    """
    A data structure that simulates a matrix of zeros and ones.
    
    It supports flipping elements (0 to 1 or 1 to 0) and generating 
    a random element from the matrix in constant time.
    """

    def __init__(self, rows: int, cols: int):
        """
        Initializes the matrix with all zeros.

        Args:
            rows (int): Number of rows in the matrix.
            cols (int): Number of columns in the matrix.
        """
        self.rows = rows
        self.cols = cols
        self.total_elements = rows * cols
        
        # Stores the indices of elements that are currently 1.
        # We treat the 2D matrix as a flattened 1D array of size rows * cols.
        self.ones_indices = []
        
        # Maps a 1D index to its current position in the ones_indices list.
        # This allows O(1) lookup and removal.
        self.index_to_pos = {}

    def flip(self, r: int, c: int) -> None:
        """
        Flips the element at (r, c) from 0 to 1 or 1 to 0.

        Args:
            r (int): Row index.
            c (int): Column index.
        """
        flat_index = r * self.cols + c
        
        if flat_index in self.index_to_pos:
            # Element is currently 1, so we flip it to 0.
            # To remove in O(1), swap the element to be removed with the last element in the list.
            pos_to_remove = self.index_to_pos[flat_index]
            last_element_index = self.ones_indices[-1]
            
            # Move the last element to the position of the element we are removing
            self.ones_indices[pos_to_remove] = last_element_index
            self.index_to_pos[last_element_index] = pos_to_remove
            
            # Remove the last element
            self.ones_indices.pop()
            del self.index_to_pos[flat_index]
        else:
            # Element is currently 0, so we flip it to 1.
            # Append the index to the end of the list and record its position.
            self.index_to_pos[flat_index] = len(self.ones_indices)
            self.ones_indices.append(flat_index)

    def getRandom(self) -> int:
        """
        Returns a random element (0 or 1) from the matrix.

        Returns:
            int: A random element from the matrix.
        """
        # The probability of picking a 1 is (number of ones) / (total elements).
        # We pick a random integer in the range [0, total_elements - 1].
        # If the random integer is less than the count of ones, we return 1.
        # Otherwise, we return 0.
        if random.randrange(self.total_elements) < len(self.ones_indices):
            return 1
        return 0

def solve():
    """
    Example usage of the RandomFlipMatrix class.
    """
    matrix = RandomFlipMatrix(2, 2)
    matrix.flip(0, 0)
    matrix.flip(1, 1)
    print(matrix.getRandom())  # Should be 0 or 1
    matrix.flip(0, 0)
    print(matrix.getRandom())  # Should be 0 or 1
    matrix.flip(1, 1)
    print(matrix.getRandom())  # Should be 0 or 1
