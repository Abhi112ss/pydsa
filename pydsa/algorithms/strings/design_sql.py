METADATA = {
    "id": 2408,
    "name": "Design SQL",
    "slug": "design-sql",
    "category": "Design",
    "aliases": [],
    "tags": ["hash_map", "strings", "design"],
    "difficulty": "medium",
    "time_complexity": "O(1) per operation on average",
    "space_complexity": "O(N) where N is the total number of elements stored",
    "description": "Implement a simplified SQL-like system to create tables and insert/retrieve values.",
}

class SQL:
    def __init__(self) -> None:
        """
        Initializes the SQL system.
        
        The system uses a nested dictionary structure:
        self.tables[table_name][column_name] = value
        """
        self.tables: dict[str, dict[str, int]] = {}

    def createTable(self, tableName: str) -> None:
        """
        Creates a new table.

        Args:
            tableName: The name of the table to create.
        """
        if tableName not in self.tables:
            self.tables[tableName] = {}

    def insertIntoTable(self, tableName: str, column: str, value: int) -> None:
        """
        Inserts a value into a specific column of a table.

        Args:
            tableName: The name of the table.
            column: The name of the column.
            value: The integer value to insert.
        """
        # Since the problem implies tables are created before insertion,
        # we directly update the nested dictionary.
        self.tables[tableName][column] = value

    def selectFromTable(self, tableName: str, column: str) -> int:
        """
        Retrieves the value from a specific column in a table.

        Args:
            tableName: The name of the table.
            column: The name of the column.

        Returns:
            The value stored in the specified column, or -1 if not found.
        """
        # Access the table first, then the column. 
        # Using .get() ensures we handle missing keys gracefully.
        table = self.tables.get(tableName)
        if table is not None:
            return table.get(column, -1)
        return -1

def solve():
    """
    Example usage of the SQL class.
    """
    sql = SQL()
    sql.createTable("Users")
    sql.insertIntoTable("Users", "name", 1)
    print(sql.selectFromTable("Users", "name"))  # Expected: 1
    print(sql.selectFromTable("Users", "age"))   # Expected: -1
