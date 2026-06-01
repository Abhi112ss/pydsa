METADATA = {
    "id": 1618,
    "name": "Maximum Font to Fit a Sentence in a Screen",
    "slug": "maximum-font-to-fit-a-sentence-in-a-screen",
    "category": "Binary Search",
    "aliases": [],
    "tags": ["binary_search", "strings"],
    "difficulty": "medium",
    "time_complexity": "O(N * log(max_font_size))",
    "space_complexity": "O(1)",
    "description": "Find the maximum font size such that a given sentence fits within a specified screen width, considering spaces between words.",
}

def solve(sentence: str, screen_width: int, font_size: list[int]) -> int:
    """
    Finds the maximum font size from the given list that allows the sentence 
    to fit within the screen width.

    Args:
        sentence: The string of words separated by single spaces.
        screen_width: The maximum width available on the screen.
        font_size: A list of available font sizes.

    Returns:
        The maximum font size that fits, or -1 if no font size fits.

    Examples:
        >>> solve("hello world", 10, [1, 2, 3])
        1
        >>> solve("hello world", 10, [1, 2, 3, 4, 5])
        -1
    """
    words = sentence.split(" ")
    
    def can_fit(size: int) -> bool:
        """Checks if the sentence fits in the screen with the given font size."""
        # Calculate total width: sum of (word_length * size) + (number_of_spaces * size)
        # Since spaces are also sized, we can treat the sentence as a single unit 
        # of length (len(sentence) * size)
        total_width = len(sentence) * size
        return total_width <= screen_width

    # Sort font sizes to enable binary search
    sorted_fonts = sorted(font_size)
    
    low = 0
    high = len(sorted_fonts) - 1
    result = -1

    # Binary search for the largest valid font size
    while low <= high:
        mid = (low + high) // 2
        current_size = sorted_fonts[mid]
        
        if can_fit(current_size):
            # If it fits, try a larger font size to maximize
            result = current_size
            low = mid + 1
        else:
            # If it doesn't fit, we must try smaller font sizes
            high = mid - 1
            
    return result
