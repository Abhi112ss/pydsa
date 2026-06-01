METADATA = {
    "id": 348,
    "name": "Design Tic-Tac-Toe",
    "slug": "design-tic-tac-toe",
    "category": "Design",
    "aliases": [],
    "tags": ["design", "matrix"],
    "difficulty": "medium",
    "time_complexity": "O(1)",
    "space_complexity": "O(n)",
    "description": "Design a Tic-Tac-Toe game that allows players to make moves and checks for a winner in constant time.",
}

class TicTacToe:
    """
    A class representing a Tic-Tac-Toe game board of size n x n.
    
    The game tracks moves for two players and determines if a player has won
    by checking rows, columns, and diagonals in O(1) time.
    """

    def __init__(self, n: int):
        """
        Initializes the Tic-Tac-Toe game board.

        Args:
            n (int): The size of the n x n board.
        """
        self.n = n
        # rows[i] stores the cumulative score for row i
        self.rows = [0] * n
        # cols[j] stores the cumulative score for column j
        self.cols = [0] * n
        # diag stores the cumulative score for the main diagonal (top-left to bottom-right)
        self.diag = 0
        # anti_diag stores the cumulative score for the anti-diagonal (top-right to bottom-left)
        self.anti_diag = 0
        # player_val is the value added for player 1 and subtracted for player 2
        # However, to handle both players simply, we use 1 for player 1 and -1 for player 2.
        # The win condition is reaching n or -n.

    def move(self, row: int, col: int, player: int) -> int:
        """
        Records a move and checks if the move results in a win.

        Args:
            row (int): The row index of the move.
            col (int): The column index of the move.
            player (int): The player number (1 or 2).

        Returns:
            int: The winner (1 or 2) if the move results in a win, otherwise 0.

        Examples:
            >>> game = TicTacToe(3)
            >>> game.move(0, 0, 1)
            0
            >>> game.move(0, 1, 2)
            0
            >>> game.move(0, 2, 1)
            0
            >>> game.move(1, 1, 2)
            0
            >>> game.move(1, 0, 1)
            0
            >>> game.move(1, 2, 2)
            0
            >>> game.move(2, 2, 1)
            1
        """
        # Map player 1 to +1 and player 2 to -1 to use summation for win detection
        val = 1 if player == 1 else -1

        # Update the score for the specific row and column
        self.rows[row] += val
        self.cols[col] += val

        # Update the main diagonal if the move is on it (row == col)
        if row == col:
            self.diag += val

        # Update the anti-diagonal if the move is on it (row + col == n - 1)
        if row + col == self.n - 1:
            self.anti_diag += val

        # Check if the current move completed a row, column, or diagonal
        # A win occurs if the absolute sum reaches the board size n
        target = self.n
        if (abs(self.rows[row]) == target or 
            abs(self.cols[col]) == target or 
            abs(self.diag) == target or 
            abs(self.anti_diag) == target):
            return player

        return 0

def solve():
    """
    Placeholder function to satisfy the structure requirements.
    In a real LeetCode environment, the class above is what is tested.
    """
    pass
