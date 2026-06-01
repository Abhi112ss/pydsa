METADATA = {
    "id": 895,
    "name": "Maximum Frequency Stack",
    "slug": "maximum-frequency-stack",
    "category": "Design",
    "aliases": [],
    "tags": ["hash_map", "design", "stack"],
    "difficulty": "hard",
    "time_complexity": "O(1)",
    "space_complexity": "O(n)",
    "description": "Design a stack that supports push, pop, and top operations, where pop and top return the most frequent element.",
}

class FreqStack:
    def __init__(self) -> None:
        """
        Initializes the FreqStack data structure.
        """
        # Maps element value to its current frequency count
        self.freq_map: dict[int, int] = {}
        
        # Maps frequency count to a stack of elements having that frequency
        # This allows O(1) access to elements with the same max frequency
        self.group_map: dict[int, list[int]] = {}
        
        # Tracks the current maximum frequency present in the stack
        self.max_freq: int = 0

    def push(self, val: int) -> None:
        """
        Pushes an element onto the stack.

        Args:
            val: The integer value to be pushed.
        """
        # Update the frequency of the value
        current_freq = self.freq_map.get(val, 0) + 1
        self.freq_map[val] = current_freq

        # If this frequency is higher than the current max, update max_freq
        if current_freq > self.max_freq:
            self.max_freq = current_freq

        # Add the value to the stack corresponding to its current frequency
        if current_freq not in self.group_map:
            self.group_map[current_freq] = []
        self.group_map[current_freq].append(val)

    def pop(self) -> int:
        """
        Removes and returns the most frequent element. 
        If there is a tie, the element closest to the top of the stack is returned.

        Returns:
            The most frequent element.
        """
        # The most frequent element is at the top of the stack for max_freq
        popped_val = self.group_map[self.max_freq].pop()

        # Decrement the frequency of the popped element in the frequency map
        self.freq_map[popped_val] -= 1

        # If the stack for the current max_freq is empty, decrement max_freq
        if not self.group_map[self.max_freq]:
            self.max_freq -= 1

        return popped_val

    def top(self) -> int:
        """
        Returns the most frequent element without removing it.

        Returns:
            The most frequent element.
        """
        # The top element is always the last element added to the max_freq stack
        return self.group_map[self.max_freq][-1]


def solve() -> None:
    """
    Example usage of the FreqStack class.
    """
    freq_stack = FreqStack()
    freq_stack.push(5)
    freq_stack.push(7)
    freq_stack.push(5)
    freq_stack.push(7)
    freq_stack.push(4)
    freq_stack.push(5)
    
    # Expected: 5 (frequency 3)
    print(freq_stack.pop()) 
    # Expected: 5 (frequency 2, tie with 7, but 5 was pushed later/is higher in stack)
    print(freq_stack.pop()) 
    # Expected: 7 (frequency 2)
    print(freq_stack.pop()) 
    # Expected: 7 (frequency 1)
    print(freq_stack.pop()) 
    # Expected: 4 (frequency 1)
    print(freq_stack.pop())
