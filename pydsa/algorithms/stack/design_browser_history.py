METADATA = {
    "id": 1472,
    "name": "Design Browser History",
    "slug": "design-browser-history",
    "category": "Design",
    "aliases": [],
    "tags": ["stack", "list", "design"],
    "difficulty": "medium",
    "time_complexity": "O(1) for all operations (amortized)",
    "space_complexity": "O(N) where N is the number of URLs visited",
    "description": "Design a class that simulates browser history with visit, back, and forward functionality.",
}

class BrowserHistory:
    """
    A class representing a browser history simulator.
    
    Uses a dynamic array (list) and a pointer to manage the history of visited URLs,
    allowing for efficient navigation through forward and backward history.
    """

    def __init__(self, homepage: str) -> None:
        """
        Initializes the browser history with a homepage.

        Args:
            homepage (str): The initial URL to start the history.
        """
        # history stores the sequence of visited URLs
        self.history: list[str] = [homepage]
        # current_index tracks the user's current position in the history
        self.current_index: int = 0
        # max_index tracks the boundary of the valid history (to handle forward navigation)
        self.max_index: int = 0

    def visit(self, url: str) -> None:
        """
        Visits a new URL. This clears all forward history.

        Args:
            url (str): The URL to visit.
        """
        self.current_index += 1
        
        # If we are not at the end of the list, overwrite the next element
        if self.current_index < len(self.history):
            self.history[self.current_index] = url
        else:
            # Otherwise, append the new URL to the list
            self.history.append(url)
            
        # Visiting a new URL invalidates all existing forward history
        self.max_index = self.current_index

    def back(self, steps: int) -> str:
        """
        Moves back in history by a given number of steps.

        Args:
            steps (int): The number of steps to move back.

        Returns:
            str: The URL at the new position.
        """
        # Move the pointer back, but do not go below index 0
        self.current_index = max(0, self.current_index - steps)
        return self.history[self.current_index]

    def forward(self, steps: int) -> str:
        """
        Moves forward in history by a given number of steps.

        Args:
            steps (int): The number of steps to move forward.

        Returns:
            str: The URL at the new position.
        """
        # Move the pointer forward, but do not exceed the max_index (valid history)
        self.current_index = min(self.max_index, self.current_index + steps)
        return self.history[self.current_index]


def solve() -> None:
    """
    Example usage of the BrowserHistory class.
    """
    browser = BrowserHistory("leetcode.com")
    print(browser.visit("google.com"))    # Returns None
    print(browser.visit("facebook.com"))  # Returns None
    print(browser.back(1))                # Returns "google.com"
    print(browser.back(1))                # Returns "leetcode.com"
    print(browser.forward(1))             # Returns "google.com"
    print(browser.visit("youtube.com"))   # Returns None
    print(browser.forward(2))             # Returns "youtube.com" (cannot go forward)
    print(browser.back(2))                # Returns "leetcode.com"
