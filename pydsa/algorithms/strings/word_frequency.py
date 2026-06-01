METADATA = {
    "id": 192,
    "name": "Word Frequency",
    "slug": "word_frequency",
    "category": "Shell",
    "aliases": [],
    "tags": ["shell"],
    "difficulty": "medium",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(n)",
    "description": "Count the frequency of each word in a text file and output them in descending order.",
}

import subprocess
from typing import Optional


def solve(file_path: str) -> Optional[str]:
    """Count word frequencies from a file and return sorted results.

    Uses a shell pipeline to:
    1. Read the file with cat
    2. Replace newlines with spaces using tr to normalize whitespace
    3. Split into one word per line using tr
    4. Sort words alphabetically (required for uniq -c to work correctly)
    5. Count consecutive duplicates with uniq -c
    6. Sort by count in descending order

    Args:
        file_path: Path to the input text file.

    Returns:
        A string with lines of "count word" sorted by frequency descending,
        or None if an error occurs.

    Examples:
        >>> # Assuming input.txt contains "the day is sunny the the\\nthe sunny is is"
        >>> result = solve("input.txt")
        >>> # Expected output (order matters):
        >>> # 4 the
        >>> # 3 is
        >>> # 2 sunny
        >>> # 1 day
    """
    try:
        # Build the shell pipeline: cat -> tr (normalize whitespace) -> tr (split words) -> sort -> uniq -c -> sort -rn
        # Step 1: cat reads the file content
        cat_proc = subprocess.Popen(["cat", file_path], stdout=subprocess.PIPE)

        # Step 2: Replace all whitespace (including newlines) with single newlines to split words
        # tr -s ' ' squeezes multiple spaces, then we replace spaces with newlines
        tr_proc = subprocess.Popen(
            ["tr", "-s", "[:space:]", "\n"],
            stdin=cat_proc.stdout,
            stdout=subprocess.PIPE,
        )
        cat_proc.stdout.close()

        # Step 3: Sort words alphabetically (required before uniq -c)
        sort_proc = subprocess.Popen(
            ["sort"],
            stdin=tr_proc.stdout,
            stdout=subprocess.PIPE,
        )
        tr_proc.stdout.close()

        # Step 4: Count consecutive identical lines
        uniq_proc = subprocess.Popen(
            ["uniq", "-c"],
            stdin=sort_proc.stdout,
            stdout=subprocess.PIPE,
        )
        sort_proc.stdout.close()

        # Step 5: Sort by count in descending numerical order
        sort_rn_proc = subprocess.Popen(
            ["sort", "-rn"],
            stdin=uniq_proc.stdout,
            stdout=subprocess.PIPE,
        )
        uniq_proc.stdout.close()

        # Collect the final output
        output, _ = sort_rn_proc.communicate()

        # Decode bytes to string and strip trailing whitespace
        result = output.decode("utf-8").strip()

        # Clean up: remove leading whitespace from uniq -c output and format nicely
        lines = result.split("\n")
        cleaned_lines = []
        for line in lines:
            # uniq -c outputs like "      4 the" — strip leading spaces
            cleaned_lines.append(line.strip())

        return "\n".join(cleaned_lines)

    except (FileNotFoundError, subprocess.SubprocessError, OSError):
        return None


if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        print("Usage: python solution.py <file_path>")
        sys.exit(1)

    result = solve(sys.argv[1])
    if result is not None:
        print(result)
    else:
        print("Error processing file.")
        sys.exit(1)