import os
import re
from pathlib import Path

def final_sweep():
    # The exact 18 files that failed in your test run
    failed_modules = [
        "pydsa/algorithms/backtracking/word_squares_ii.py",
        "pydsa/algorithms/bit_manipulation/power_of_four.py",
        "pydsa/algorithms/graphs/flood_fill.py",
        "pydsa/algorithms/graphs/maximum_path_quality_of_a_graph.py",
        "pydsa/algorithms/linked_list/add_two_numbers_ii.py",
        "pydsa/algorithms/linked_list/delete_nodes_from_linked_list_present_in_array.py",
        "pydsa/algorithms/math/fizz_buzz_multithreaded.py",
        "pydsa/algorithms/strings/to_lower_case.py",
        "pydsa/algorithms/trees/binary_tree_preorder_traversal.py",
        "pydsa/algorithms/trees/clone_n_ary_tree.py",
        "pydsa/algorithms/trees/construct_quad_tree.py",
        "pydsa/algorithms/trees/construct_string_from_binary_tree.py",
        "pydsa/algorithms/trees/encode_n_ary_tree_to_binary_tree.py",
        "pydsa/algorithms/trees/maximum_binary_tree_ii.py",
        "pydsa/algorithms/trees/print_binary_tree.py",
        "pydsa/algorithms/trees/root_equals_sum_of_children.py",
        "pydsa/algorithms/trees/serialize_and_deserialize_n_ary_tree.py",
        "pydsa/algorithms/two_pointer/sort_array_by_parity_ii.py"
    ]

    broken_ids = []
    
    for filepath in failed_modules:
        path = Path(filepath)
        if not path.exists():
            continue
            
        try:
            # errors="ignore" handles that lingering null byte issue
            with open(path, "r", encoding="utf-8", errors="ignore") as f:
                content = f.read()
                
            id_match = re.search(r'"id":\s*(\d+)', content)
            if id_match:
                broken_ids.append(int(id_match.group(1)))
                
            # Delete the file so generate_solvers.py is forced to recreate it
            os.remove(path)
            print(f"Deleted {path.name}")
        except Exception as e:
            print(f"Error processing {path.name}: {e}")

    print("-" * 30)
    if broken_ids:
        # Sort and remove duplicates just in case
        ids_str = " ".join(map(str, sorted(list(set(broken_ids)))))
        print("Run this exact command to regenerate your final 18 files:")
        print(f"python generate_solvers.py --id {ids_str}")
    else:
        print("No files found. They might have already been deleted!")

if __name__ == "__main__":
    final_sweep()