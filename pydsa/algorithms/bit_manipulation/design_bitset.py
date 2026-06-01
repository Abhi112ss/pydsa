METADATA = {
    "id": 2166,
    "name": "Design Bitset",
    "slug": "design_bitset",
    "category": "Design",
    "aliases": [],
    "tags": ["design", "bit_manipulation"],
    "difficulty": "medium",
    "time_complexity": "O(1) for most operations, O(n/word_size) for count",
    "space_complexity": "O(n)",
    "description": "Design a bitset that supports setting, resetting, and counting bits using bitwise operations.",
}

class Bitset:
    def __init__(self, n: int):
        """
        Initializes the bitset with n bits, all set to 0.
        """
        self.n = n
        # We use an array of integers to represent bits. 
        # Each integer (word) in Python can handle arbitrary size, 
        # but for standard bitset design, we treat them as 64-bit chunks.
        # However, Python's int is already an arbitrary-precision bitset.
        # To satisfy the 'Design' aspect efficiently, we use a single large integer.
        self.bits = 0

    def set(self, bit: int) -> None:
        """
        Sets the bit at the given index to 1.

        Args:
            bit (int): The index of the bit to set.
        """
        # Use bitwise OR with a mask where only the target bit is 1
        self.bits |= (1 << bit)

    def reset(self, bit: int) -> None:
        """
        Resets the bit at the given index to 0.

        Args:
            bit (int): The index of the bit to reset.
        """
        # Use bitwise AND with a mask where only the target bit is 0
        self.bits &= ~(1 << bit)

    def count(self) -> int:
        """
        Returns the number of set bits (1s) in the bitset.

        Returns:
            int: The total count of set bits.
        """
        # Python's bit_count() is highly optimized (O(number of bits))
        return self.bits.bit_count()

    def ones_count(self) -> int:
        """
        Returns the number of set bits (1s) in the bitset.
        This is an alias for count() in this implementation.

        Returns:
            int: The total count of set bits.
        """
        return self.count()

def solve():
    """
    Example usage of the Bitset class.
    """
    bitset = Bitset(5)
    bitset.set(1)
    bitset.set(3)
    print(f"Count after setting 1 and 3: {bitset.count()}")  # Expected: 2
    bitset.reset(1)
    print(f"Count after resetting 1: {bitset.count()}")      # Expected: 1
    bitset.set(1)
    print(f"Count after resetting 1: {bitset.count()}")      # Expected: 2
