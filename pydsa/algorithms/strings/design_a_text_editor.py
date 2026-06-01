METADATA = {
    "id": 2296,
    "name": "Design a Text Editor",
    "slug": "design-a-text-editor",
    "category": "Design",
    "aliases": [],
    "tags": ["doubly_linked_list", "string_manipulation", "design"],
    "difficulty": "hard",
    "time_complexity": "O(1) average for most operations, O(L) for cursor movement/deletion where L is length",
    "space_complexity": "O(N) where N is the total number of characters stored",
    "description": "Design a text editor that supports adding text, deleting characters, moving the cursor, and retrieving substrings.",
}

class TextEditor:
    """
    A text editor implementation using two stacks to represent the text 
    before and after the cursor. This allows O(1) amortized time for 
    insertions and deletions at the cursor.
    """

    def __init__(self) -> None:
        """Initializes the text editor with two stacks."""
        # Characters to the left of the cursor
        self.left_stack: list[str] = []
        # Characters to the right of the cursor
        self.right_stack: list[str] = []

    def addText(self, text: str) -> None:
        """
        Adds text at the current cursor position.

        Args:
            text: The string to be inserted.
        """
        # Append characters to the left stack to place them before the cursor
        for char in text:
            self.left_stack.append(char)

    def deleteText(self, k: int) -> int:
        """
        Deletes k characters to the left of the cursor.

        Args:
            k: The number of characters to delete.

        Returns:
            The number of characters actually deleted.
        """
        count = 0
        # Delete characters from the left stack one by one up to k
        while count < k and self.left_stack:
            self.left_stack.pop()
            count += 1
        return count

    def cursorLeft(self, k: int) -> str:
        """
        Moves the cursor k positions to the left.

        Args:
            k: The number of positions to move.

        Returns:
            The current text visible in the editor (up to 10 chars before and after cursor).
        """
        # Move characters from left stack to right stack to simulate left movement
        for _ in range(min(k, len(self.left_stack))):
            self.right_stack.append(self.left_stack.pop())
        return self._get_view()

    def cursorRight(self, k: int) -> str:
        """
        Moves the cursor k positions to the right.

        Args:
            k: The number of positions to move.

        Returns:
            The current text visible in the editor (up to 10 chars before and after cursor).
        """
        # Move characters from right stack to left stack to simulate right movement
        for _ in range(min(k, len(self.right_stack))):
            self.left_stack.append(self.right_stack.pop())
        return self._get_view()

    def _get_view(self) -> str:
        """
        Helper to construct the view of the text around the cursor.
        The problem defines the view as up to 10 characters before and 10 after.

        Returns:
            A string representing the current view.
        """
        # Get up to 10 characters from the end of the left stack
        left_part = "".join(self.left_stack[-10:])
        # Get up to 10 characters from the start of the right stack
        # Since right_stack is a stack, the 'start' is the bottom of the stack.
        # However, in our implementation, the top of right_stack is the character 
        # immediately to the right of the cursor.
        # To get the first 10 characters of the right side, we need to look at 
        # the elements from the end of the list towards the bottom.
        # Actually, the top of right_stack is the character closest to the cursor.
        # So we take the last 10 elements of the right_stack reversed.
        
        # Correct logic: right_stack top is the char immediately right of cursor.
        # We need the first 10 chars of the right side.
        # Because we push to right_stack when moving left, the 'top' is the 
        # character closest to the cursor.
        # Let's re-evaluate:
        # cursorLeft: left -> right (top of right is closest to cursor)
        # cursorRight: right -> left (top of left is closest to cursor)
        # So the right side is stored in right_stack such that the top is the 
        # character immediately to the right of the cursor.
        # To get the 10 characters to the right, we take the top 10 of right_stack
        # and reverse them to maintain correct order.
        
        right_view_list = []
        count = 0
        # We iterate from the top of the right stack (the character closest to cursor)
        # but we need to return them in the order they appear in the text.
        # The right_stack top is the character at index cursor + 1.
        # So we take the top elements and reverse them.
        temp_right = self.right_stack[-10:]
        right_part = "".join(reversed(temp_right))
        
        return left_part + right_part

def solve():
    """
    Example usage/test runner for the TextEditor class.
    """
    editor = TextEditor()
    
    # Test Case 1
    editor.addText("leetcode")
    print(editor.cursorLeft(4))    # Expected: "leet" (Wait, view is 10 before/after)
    # Actually, the problem says "return the text... up to 10 chars before and 10 after"
    # If cursor is at index 4, left is "leet", right is "code".
    # View: "leetcode"
    
    editor.cursorLeft(10)          # Move far left
    print(editor._get_view())      # Expected: "leetcode"
    
    editor.cursorRight(4)          # Move back to index 4
    print(editor._get_view())      # Expected: "leetcode"
    
    editor.deleteText(4)           # Delete "leet"
    print(editor._get_view())      # Expected: "code"
    
    editor.addText("love")         # Add "love" at cursor
    print(editor._get_view())      # Expected: "lovecode"
