METADATA = {
    "id": 68,
    "name": "Text Justification",
    "slug": "text-justification",
    "category": "Simulation",
    "aliases": [],
    "tags": ["string", "simulation"],
    "difficulty": "hard",
    "time_complexity": "O(N)",
    "space_complexity": "O(N)",
    "description": "Given an array of strings, format the text such that each line has exactly maxWidth characters and is fully justified.",
}

def solve(words: list[str], maxWidth: int) -> list[str]:
    """
    Formats a list of words into lines of a specific width using full justification.

    Args:
        words: A list of strings representing the words to be formatted.
        maxWidth: The exact number of characters each line must contain.

    Returns:
        A list of strings where each string is a justified line.

    Examples:
        >>> solve(["This", "is", "an", "example", "of", "text", "justification."], 16)
        ['This    is    an', 'example  of text', 'justification.  ']
    """
    result = []
    current_line_words = []
    current_line_length = 0

    for word in words:
        # Check if adding this word (plus at least one space per existing word) exceeds maxWidth
        # current_line_length is the sum of lengths of words currently in the line
        # len(current_line_words) is the minimum number of spaces needed between words
        if current_line_length + len(word) + len(current_line_words) > maxWidth:
            # Process the completed line
            result.append(_format_line(current_line_words, current_line_length, maxWidth, False))
            current_line_words = []
            current_line_length = 0
        
        current_line_words.append(word)
        current_line_length += len(word)

    # Handle the last line: left-justified, single spaces between words, trailing spaces to fill width
    if current_line_words:
        result.append(_format_line(current_line_words, current_line_length, maxWidth, True))

    return result

def _format_line(words: list[str], words_len: int, maxWidth: int, is_last_line: bool) -> str:
    """
    Helper to construct a single justified line.

    Args:
        words: The words to be placed in the line.
        words_len: The sum of the lengths of the words.
        maxWidth: The target width of the line.
        is_last_line: Boolean indicating if this is the final line of the text.

    Returns:
        A single string representing the justified line.
    """
    num_words = len(words)
    num_spaces_needed = maxWidth - words_len

    # Case 1: Last line or a line with only one word (Left Justified)
    if is_last_line or num_words == 1:
        line = " ".join(words)
        # Pad the end with remaining spaces
        return line + " " * (maxWidth - len(line))

    # Case 2: Fully Justified
    # Calculate how many spaces go between each word gap
    num_gaps = num_words - 1
    spaces_per_gap = num_spaces_needed // num_gaps
    extra_spaces = num_spaces_needed % num_gaps

    line_parts = []
    for i in range(num_gaps):
        line_parts.append(words[i])
        # Distribute spaces: base amount + 1 extra if we are within the 'extra_spaces' count
        current_gap_size = spaces_per_gap + (1 if i < extra_spaces else 0)
        line_parts.append(" " * current_gap_size)
    
    # Add the final word
    line_parts.append(words[-1])
    
    return "".join(line_parts)
