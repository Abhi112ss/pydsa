import os
import shutil
from pathlib import Path
import re

ALGO_DIR = Path("pydsa/algorithms")

def sweep():
    broken_ids = []
    bad_deleted = 0

    for root, _, files in os.walk(ALGO_DIR):
        for file in files:
            filepath = Path(root) / file
            
            # 1. Delete the useless .bad.py files
            if ".bad" in file:
                os.remove(filepath)
                bad_deleted += 1
                continue

            if not file.endswith(".py") or file == "__init__.py":
                continue

            # 2. Check for missing 'Optional' or '__future__' errors
            # Added errors="ignore" to bypass weird AI-generated characters
            with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
                content = f.read()

            needs_regen = False
            
            if "Optional[" in content and "from typing import" not in content and "import typing" not in content:
                needs_regen = True
            elif "from __future__" in content and not content.startswith("from __future__"):
                # If __future__ isn't the very first thing (ignoring whitespace)
                if not content.lstrip().startswith("from __future__"):
                    needs_regen = True
            elif "from typing import list" in content:
                needs_regen = True

            if needs_regen:
                id_match = re.search(r'"id":\s*(\d+)', content)
                if id_match:
                    broken_ids.append(int(id_match.group(1)))

    print(f"Deleted {bad_deleted} .bad.py files.")
    
    if broken_ids:
        ids_str = " ".join(map(str, sorted(list(set(broken_ids)))))
        print(f"\nRun this command to regenerate the files with bad imports:")
        print(f"python generate_solvers.py --id {ids_str}")

if __name__ == "__main__":
    sweep()