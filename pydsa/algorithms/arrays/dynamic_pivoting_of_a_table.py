METADATA = {
    "id": 2252,
    "name": "Dynamic Pivoting of a Table",
    "slug": "dynamic_pivoting_of_a_table",
    "category": "Simulation",
    "aliases": [],
    "tags": ["hash_map", "simulation"],
    "difficulty": "medium",
    "time_complexity": "O(N)",
    "space_complexity": "O(N)",
    "description": "Simulate a table where rows and columns can be dynamically pivoted and values are retrieved based on current mapping.",
}

class Table:
    """
    A class representing a dynamic table that supports pivoting rows and columns.
    """

    def __init__(self, initial_data: list[list[str]]):
        """
        Initializes the table with initial data.

        Args:
            initial_data: A 2D list of strings representing the table.
        """
        # Store data in a nested dictionary: data[row_id][col_id] = value
        self.data: dict[str, dict[str, str]] = {}
        
        # Track current mapping of logical indices to physical IDs
        # row_map[logical_index] = physical_row_id
        self.row_map: list[str] = []
        self.col_map: list[str] = []

        # Populate initial data and mappings
        for r_idx, row in enumerate(initial_data):
            row_id = f"r{r_idx}"
            self.row_map.append(row_id)
            self.data[row_id] = {}
            for c_idx, val in enumerate(row):
                col_id = f"c{c_idx}"
                if col_id not in self.col_map:
                    self.col_map.append(col_id)
                self.data[row_id][col_id] = val

    def pivot_row(self, row_index: int) -> None:
        """
        Pivots a specific row by moving it to the end of the table.

        Args:
            row_index: The logical index of the row to pivot.
        """
        # Remove the row_id from the current logical mapping
        row_id = self.row_map.pop(row_index)
        # Append the row_id to the end of the logical mapping
        self.row_map.append(row_id)

    def pivot_col(self, col_index: int) -> None:
        """
        Pivots a specific column by moving it to the end of the table.

        Args:
            col_index: The logical index of the column to pivot.
        """
        # Remove the col_id from the current logical mapping
        col_id = self.col_map.pop(col_index)
        # Append the col_id to the end of the logical mapping
        self.col_map.append(col_id)

    def get_value(self, row_index: int, col_index: int) -> str:
        """
        Retrieves the value at the specified logical row and column.

        Args:
            row_index: The logical index of the row.
            col_index: The logical index of the column.

        Returns:
            The string value at the given position.
        """
        # Map logical indices to the actual physical IDs stored in the hash map
        row_id = self.row_map[row_index]
        col_id = self.col_map[col_index]
        
        # Return the value from the nested dictionary
        return self.data[row_id].get(col_id, "")

def solve(commands: list[list[str]]) -> list[str]:
    """
    Processes a list of commands to perform table operations.

    Args:
        commands: A list of commands where each command is a list of strings.
            - ["GET", "row_idx", "col_idx"]
            - ["PIVOT_ROW", "row_idx"]
            - ["PIVOT_COL", "col_idx"]
            Note: The first command is assumed to be the initialization with data.
            However, based on standard LeetCode patterns for this problem, 
            the first command is usually the data itself.

    Returns:
        A list of strings representing the results of "GET" operations.

    Examples:
        >>> solve([["DATA", "a,b", "c,d"], ["GET", "0", "0"], ["PIVOT_ROW", "0"], ["GET", "0", "0"]])
        ['a', 'c']
    """
    # This implementation assumes the first command is the data initialization
    # as per the problem's typical structure.
    
    # Extract initial data from the first command
    # Format: ["DATA", "row1_col1,row1_col2", "row2_col1,row2_col2"]
    data_cmd = commands[0]
    initial_rows = []
    for i in range(1, len(data_cmd)):
        row_str = data_cmd[i]
        initial_rows.append(row_str.split(','))
    
    table = Table(initial_rows)
    results = []

    # Process subsequent commands
    for cmd in commands[1:]:
        action = cmd[0]
        
        if action == "GET":
            r_idx = int(cmd[1])
            c_idx = int(cmd[2])
            results.append(table.get_value(r_idx, c_idx))
        elif action == "PIVOT_ROW":
            r_idx = int(cmd[1])
            table.pivot_row(r_idx)
        elif action == "PIVOT_COL":
            c_idx = int(cmd[1])
            table.pivot_col(c_idx)
            
    return results
