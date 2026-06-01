METADATA = {
    "id": 194,
    "name": "Transpose File",
    "slug": "transpose_file",
    "category": "Shell",
    "aliases": [],
    "tags": ["shell"],
    "difficulty": "medium",
    "time_complexity": "O(n * m)",
    "space_complexity": "O(n * m)",
    "description": "Transpose the content of a file from rows to columns.",
}

def solve() -> str:
    """Return the awk command to transpose a file.

    Args:
        None (this is a shell command generator).

    Returns:
        A string containing the awk command that transposes the file.

    Examples:
        The command reads a file with:
            name age
            alice 21
            ryan 30
        And outputs:
            name alice ryan
            age 21 30
    """
    # Use awk to store all lines in a 2D array, then print column by column
    # NR is the current line number, NF is the number of fields in current line
    # In the END block, iterate over each column and print all row values for that column
    command = 'awk \'{ for (i=1; i<=NF; i++) { a[NR,i]=$i } } END { for (j=1; j<=NF; j++) { for (i=1; i<=NR; i++) { printf "%s", a[i,j]; if (i<NR) printf " " }; print "" } }\' file.txt'
    return command