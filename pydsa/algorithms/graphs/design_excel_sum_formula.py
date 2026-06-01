METADATA = {
    "id": 631,
    "name": "Design Excel Sum Formula",
    "slug": "design-excel-sum-formula",
    "category": "Design",
    "aliases": [],
    "tags": ["design", "recursion", "graph"],
    "difficulty": "hard",
    "time_complexity": "O(N) per get/set/sum where N is number of cells",
    "space_complexity": "O(N) where N is number of cells",
    "description": "Design an Excel spreadsheet that supports setting values, getting values, and calculating sum formulas based on cell ranges.",
}

class Excel:
    def __init__(self):
        self.cells = {}
        self.formulas = {}

    def get(self, row: int, column: int) -> int:
        """
        Args:
            row: The row index.
            column: The column index.

        Returns:
            The integer value of the cell.
        """
        key = (row, column)
        if key in self.formulas:
            return self._evaluate_formula(key)
        return self.cells.get(key, 0)

    def set(self, row: int, column: int, val: int) -> None:
        """
        Args:
            row: The row index.
            column: The column index.
            val: The integer value to set.
        """
        key = (row, column)
        if key in self.formulas:
            del self.formulas[key]
        self.cells[key] = val

    def sum(self, row: int, column: int, topLeft: list[int], bottomRight: list[int]) -> int:
        """
        Args:
            row: The row index.
            column: The column index.
            topLeft: A list containing [row, column] of the top-left cell.
            bottomRight: A list containing [row, column] of the bottom-right cell.

        Returns:
            The integer value of the sum formula.
        """
        key = (row, column)
        range_cells = []
        for r in range(topLeft[0], bottomRight[0] + 1):
            for c in range(topLeft[1], bottomRight[1] + 1):
                range_cells.append((r, c))
        
        self.formulas[key] = range_cells
        return self.get(row, column)

    def _evaluate_formula(self, key: tuple[int, int]) -> int:
        """
        Args:
            key: The coordinate tuple of the cell.

        Returns:
            The calculated sum value.
        """
        total = 0
        for cell_coord in self.formulas[key]:
            total += self.get(cell_coord[0], cell_coord[1])
        return total

def solve():
    pass