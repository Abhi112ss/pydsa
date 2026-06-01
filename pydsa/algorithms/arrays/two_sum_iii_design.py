METADATA = {
    "id": 170,
    "name": "Two Sum III - Data structure design",
    "slug": "two_sum_iii_data_structure_design",
    "category": "design",
    "aliases": [],
    "tags": ["hash_map", "design"],
    "difficulty": "medium",
    "time_complexity": "O(1) add, O(n) find",
    "space_complexity": "O(n)",
    "description": "Design a data structure that supports adding new numbers and finding if there exists any pair of numbers which sum equals to a given value.",
}

class TwoSum:
    def __init__(self):
        # Use a dictionary to store number frequencies for O(1) lookups
        self.freq = {}

    def add(self, number: int) -> None:
        """Add a number to the data structure.
        
        Args:
            number: The integer to add.
        """
        # Update frequency count of the number
        self.freq[number] = self.freq.get(number, 0) + 1

    def find(self, value: int) -> bool:
        """Check if there exists any pair of numbers that sum to value.
        
        Args:
            value: The target sum to find.
            
        Returns:
            bool: True if a pair exists, False otherwise.
        """
        # Iterate through each unique number in the data structure
        for num in self.freq:
            complement = value - num
            # Check if complement exists in the dictionary
            if complement in self.freq:
                # Handle case where complement is the same as current number
                if complement == num:
                    # Need at least two occurrences of the number
                    if self.freq[num] >= 2:
                        return True
                else:
                    # Different numbers, one occurrence each is sufficient
                    return True
        return False