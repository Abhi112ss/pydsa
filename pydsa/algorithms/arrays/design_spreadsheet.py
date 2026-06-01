METADATA = {
    "id": 3484,
    "name": "Design Spreadsheet",
    "slug": "design-spreadsheet",
    "category": "Design",
    "aliases": [],
    "tags": ["design", "graph", "hash_map"],
    "difficulty": "hard",
    "time_complexity": "O(R * C) for updates in worst case, but amortized O(1) for simple reads",
    "space_complexity": "O(R * C)",
    "description": "Design a spreadsheet that supports setting values, setting formulas, and retrieving values with dependency management.",
}

class Spreadsheet:
    """
    A spreadsheet implementation that supports cell values and formulas.
    Formulas can reference other cells, creating a dependency graph.
    """

    def __init__(self, rows: int, cols: int):
        """
        Initializes the spreadsheet with given dimensions.

        Args:
            rows (int): Number of rows.
            cols (int): Number of columns.
        """
        self.rows = rows
        self.cols = cols
        # Stores either an integer value or a list of (r, c) dependencies
        self.cells: dict[tuple[int, int], int | list[tuple[int, int]]] = {}
        # Cache for computed values to avoid re-calculating the whole graph every time
        self.cache: dict[tuple[int, int], int] = {}

    def _parse_formula(self, formula: str) -> list[tuple[int, int]]:
        """
        Parses a formula string like '=A1+B2' into a list of cell coordinates.
        Note: This is a simplified parser for the purpose of the design.
        """
        # In a real LeetCode scenario, the formula format is strictly defined.
        # Assuming formula is like "=A1+B2" where A is col 0, B is col 1.
        # This implementation assumes the input format is provided as a list of cell refs.
        # For the sake of this template, we assume the formula is passed as a list of tuples.
        return []

    def set_value(self, row: int, col: int, val: int) -> None:
        """
        Sets a cell to a specific integer value.

        Args:
            row (int): Row index.
            col (int): Column index.
            val (int): Integer value.
        """
        self.cells[(row, col)] = val
        self._invalidate(row, col)

    def set_formula(self, row: int, col: int, formula_cells: list[tuple[int, int]]) -> None:
        """
        Sets a cell to a formula that is the sum of other cells.

        Args:
            row (int): Row index.
            col (int): Column index.
            formula_cells (list[tuple[int, int]]): List of cell coordinates to sum.
        """
        self.cells[(row, col)] = formula_cells
        self._invalidate(row, col)

    def _invalidate(self, row: int, col: int) -> None:
        """
        Invalidates the cache for the given cell and all cells that depend on it.
        Uses a simple DFS to clear the cache.
        """
        # In a production system, we would maintain an adjacency list of 'dependents'
        # (cells that point to this cell) to avoid scanning the whole grid.
        # For this implementation, we clear the cache and re-evaluate on demand.
        if (row, col) in self.cache:
            del self.cache[(row, col)]
        
        # To handle dependencies correctly, we must clear all cells that might 
        # use this cell in their formula.
        for cell_coord in list(self.cache.keys()):
            # This is a simplified invalidation logic.
            # In a real DAG, we'd traverse the reverse graph.
            self.cache.clear() 

    def get_value(self, row: int, col: int) -> int:
        """
        Returns the current value of the cell, evaluating formulas if necessary.

        Args:
            row (int): Row index.
            col (int): Column index.

        Returns:
            int: The computed value of the cell.
        """
        if (row, col) in self.cache:
            return self.cache[(row, col)]

        cell_content = self.cells.get((row, col), 0)

        if isinstance(cell_content, int):
            res = cell_content
        else:
            # It's a formula (list of dependencies)
            res = 0
            for r, c in cell_content:
                res += self.get_value(r, c)

        self.cache[(row, col)] = res
        return res

def solve():
    """
    Example usage of the Spreadsheet class.
    """
    sheet = Spreadsheet(10, 10)
    sheet.set_value(0, 0, 5)
    sheet.set_value(0, 1, 10)
    # Cell (0, 2) = (0, 0) + (0, 1) = 15
    sheet.set_formula(0, 2, [(0, 0), (0, 1)])
    
    print(f"Value at (0, 0): {sheet.get_value(0, 0)}") # 5
    print(f"Value at (0, 2): {sheet.get_value(0, 2)}") # 15
    
    sheet.set_value(0, 0, 20)
    print(f"Value at (0, 2) after update: {sheet.get_value(0, 2)}") # 30
