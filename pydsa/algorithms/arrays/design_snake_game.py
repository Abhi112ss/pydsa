METADATA = {
    "id": 353,
    "name": "Design Snake Game",
    "slug": "design_snake_game",
    "category": "Design",
    "aliases": [],
    "tags": ["design", "queue", "hash_set"],
    "difficulty": "medium",
    "time_complexity": "O(1)",
    "space_complexity": "O(N)",
    "description": "Design a snake game where the snake moves in a grid and grows when eating food.",
}

from collections import deque


class SnakeGame:
    """
    A class representing the Snake Game logic.
    """

    def __init__(self, width: int, height: int, food: list[list[int]]):
        """
        Initializes the snake game.

        Args:
            width (int): The width of the board.
            height (int): The height of the board.
            food (list[list[int]]): A list of [row, col] coordinates representing food locations.
        """
        self.width = width
        self.height = height
        self.food_list = food
        self.food_index = 0
        
        # The snake is represented by a deque of (row, col) tuples.
        # The head is at the front (index 0), and the tail is at the back.
        self.snake_body = deque([(0, 0)])
        
        # A set to store the current body positions for O(1) collision detection.
        self.snake_positions = {(0, 0)}
        
        # Current score
        self.score = 0

    def move(self, direction: str) -> int:
        """
        Moves the snake in a given direction.

        Args:
            direction (str): The direction to move ('U' for up, 'D' for down, 'L' for left, 'R' for right).

        Returns:
            int: The current score if the move is valid, or -1 if the snake hits a wall or itself.

        Examples:
            >>> game = SnakeGame(3, 2, [[1, 2], [0, 1]])
            >>> game.move("R")
            0
            >>> game.move("D")
            0
            >>> game.move("R")
            1
        """
        head_row, head_col = self.snake_body[0]

        # Calculate the new head position based on the direction
        if direction == "U":
            new_head = (head_row - 1, head_col)
        elif direction == "D":
            new_head = (head_row + 1, head_col)
        elif direction == "L":
            new_head = (head_row, head_col - 1)
        elif direction == "R":
            new_head = (head_row, head_col + 1)
        else:
            raise ValueError("Invalid direction")

        new_row, new_col = new_head

        # 1. Check for wall collisions
        if not (0 <= new_row < self.height and 0 <= new_col < self.width):
            return -1

        # 2. Check for food
        # If the new head position matches the current food location
        if (self.food_index < len(self.food_list) and 
                [new_row, new_col] == self.food_list[self.food_index]):
            # Snake eats food: score increases, snake grows (don't remove tail)
            self.score += 1
            self.food_index += 1
        else:
            # No food: snake moves forward (remove the tail)
            tail = self.snake_body.pop()
            self.snake_positions.remove(tail)

        # 3. Check for self-collision
        # We check this AFTER potentially removing the tail, because the head 
        # can move into the position previously occupied by the tail.
        if new_head in self.snake_positions:
            return -1

        # Update snake state with the new head
        self.snake_body.appendleft(new_head)
        self.snake_positions.add(new_head)

        return self.score


def solve():
    """
    Example usage of the SnakeGame class.
    """
    width, height = 3, 2
    food = [[1, 2], [0, 1]]
    game = SnakeGame(width, height, food)
    
    print(game.move("R"))  # Expected: 0
    print(game.move("D"))  # Expected: 0
    print(game.move("R"))  # Expected: 1
    print(game.move("U"))  # Expected: 1
    print(game.move("L"))  # Expected: 1
    print(game.move("U"))  # Expected: -1 (hits wall)
