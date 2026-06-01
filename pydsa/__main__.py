import argparse
import sys
import ast
import inspect
from rich.console import Console
from rich.syntax import Syntax
from rich.table import Table
from rich.panel import Panel
from rich import box

# Import the core engine you built
from pydsa import solve as _solve, search as _search, info as _info
from pydsa.core.exceptions import PyDSAError

def copy_to_clipboard(text: str):
    """Safely attempts to copy text to the system clipboard."""
    try:
        import pyperclip
        pyperclip.copy(text)
        console.print("[bold green]✓ Source code copied to clipboard![/bold green]\n")
    except ImportError:
        console.print("[yellow]💡 Tip: Run 'pip install pyperclip' to enable the --copy flag.[/yellow]\n")
    except Exception as e:
        console.print(f"[red]Failed to copy to clipboard: {e}[/red]\n")

# Initialize the Rich console for UI rendering
console = Console()

def get_difficulty_color(diff: str) -> str:
    """Helper to color-code LeetCode difficulties."""
    d = diff.lower()
    if d == "easy": return "[bold green]Easy[/bold green]"
    if d == "medium": return "[bold yellow]Medium[/bold yellow]"
    if d == "hard": return "[bold red]Hard[/bold red]"
    return diff

def parse_cli_args(cli_args: list[str]) -> list:
    """Safely converts string inputs like '[1,2,3]' into actual Python lists."""
    parsed = []
    for arg in cli_args:
        try:
            parsed.append(ast.literal_eval(arg))
        except (ValueError, SyntaxError):
            parsed.append(arg)  # Keep as string if it's not a list/dict/number
    return parsed

def run_solve(args):
    parsed_inputs = parse_cli_args(args.inputs)
    
    # --- NEW LOGIC: Bypass execution if no inputs are provided ---
    if not parsed_inputs:
        if not args.show_code and not args.copy:
            console.print("\n[bold red]Error:[/bold red] You must provide inputs to execute the algorithm, OR use [yellow]--show-code[/yellow] to view the source code.\n")
            return
            
        # Use the AI search to route the query to the best problem without executing it
        with console.status(f"[bold cyan]Routing query '{args.query}'...", spinner="dots"):
            problems = _search(args.query, limit=1)
            
        if not problems:
            console.print(f"\n[bold red]X[/bold red] No problems found matching '[yellow]{args.query}[/yellow]'.\n")
            return
            
        problem_obj = problems[0]
        
        # Print Header & Code, then exit early!
        console.print()
        console.print(Panel(f"[bold white]{problem_obj.name}[/bold white]  [dim]({problem_obj.category})[/dim]", expand=False, border_style="cyan"))
        
        source_code = inspect.getsource(problem_obj.solver)

        #COPY THE SOURCE CODE TO CLIPBOARD IF THE FLAG IS SET
        if args.copy:
            copy_to_clipboard(source_code)
            if not args.show_code:
                return 
        console.print()
        console.print(Panel(f"[bold white]{problem_obj.name}[/bold white]  [dim]({problem_obj.category})[/dim]", expand=False, border_style="cyan"))

        syntax = Syntax(source_code, "python", theme="monokai", line_numbers=True)
        
        console.print()
        console.print(Panel(syntax, title=f"[bold green]Source Code: {problem_obj.name}[/bold green]", border_style="green", expand=False))
        console.print()
        return
    # --- END NEW LOGIC ---
    
    # The loading spinner! (Original execution logic resumes here)
    with console.status(f"[bold cyan]Routing query '{args.query}' to the AI Brain...", spinner="dots"):
        result = _solve(args.query, *parsed_inputs, trace=args.trace)

    # 1. The Header Panel
    console.print()
    console.print(Panel(
        f"[bold white]{result.problem}[/bold white]  [dim]({result.category})[/dim]", 
        expand=False, 
        border_style="cyan"
    ))

    # 2. The Complexity Table
    table = Table(box=box.SIMPLE, show_header=False)
    table.add_column("Metric", style="bold dim")
    table.add_column("Value")
    table.add_row("Difficulty", get_difficulty_color(result.difficulty))
    table.add_row("Time Complexity", f"[magenta]{result.time_complexity}[/magenta]")
    table.add_row("Space Complexity", f"[blue]{result.space_complexity}[/blue]")
    console.print(table)

    # 3. The Output Answer
    console.print("[bold yellow]Result:[/bold yellow]")
    console.print(result.answer)
    
    # 4. (Optional) The Source Code Viewer
    if args.show_code or args.copy:
        # 1. Fetch the full Problem object using the exact name returned by the result
        problem_obj = _info(result.problem)
        
        # 2. Extract the raw source code of the function in memory
        source_code = inspect.getsource(problem_obj.solver)

        # --- ADD COPY LOGIC HERE ---
        if args.copy:
            copy_to_clipboard(source_code)

        if args.show_code:
        # 3. Render it beautifully with syntax highlighting
            syntax = Syntax(source_code, "python", theme="monokai", line_numbers=True)

            console.print()
            console.print(Panel(
                syntax, 
                title=f"[bold green]Source Code: {result.problem}[/bold green]",
                border_style="green",
                expand=False
            ))
            console.print()
        
    # 5. The Execution Trace
    if args.trace and result.trace_history:
        console.print(f"\n[bold magenta]🔍 Algorithm Execution Trace (First {len(result.trace_history)} steps)[/bold magenta]")
        
        trace_table = Table(box=box.MINIMAL_DOUBLE_HEAD, show_lines=True)
        trace_table.add_column("Step", justify="center", style="dim")
        trace_table.add_column("Line No.", justify="center", style="cyan")
        trace_table.add_column("Local Variables State", style="green")

        for step, (line_no, variables) in enumerate(result.trace_history):
            # Format the dictionary into a nice string: "i: 0 | target: 9 | map: {}"
            var_str = "\n".join([f"[bold white]{k}[/bold white]: {v}" for k, v in variables.items()])
            trace_table.add_row(str(step + 1), str(line_no), var_str)

        console.print(trace_table)
    console.print()

def run_search(args):
    with console.status(f"[bold cyan]Searching registry for '{args.query}'...", spinner="dots"):
        problems = _search(args.query, limit=args.limit)

    if not problems:
        console.print(f"\n[bold red]X[/bold red] No problems found matching '[yellow]{args.query}[/yellow]'.\n")
        return

    # Build the Search Results Table
    table = Table(title=f"Search Results for '{args.query}'", box=box.ROUNDED, border_style="dim")
    table.add_column("ID", justify="right", style="cyan", no_wrap=True)
    table.add_column("Problem Name", style="bold white")
    table.add_column("Difficulty")
    table.add_column("Tags", style="dim")

    for p in problems:
        tags = ", ".join(p.tags[:3]) + ("..." if len(p.tags) > 3 else "")
        table.add_row(str(p.id), p.name, get_difficulty_color(p.difficulty), tags)

    console.print()
    console.print(table)
    console.print()

def main():
    parser = argparse.ArgumentParser(prog="pydsa", description="A semantic DSA execution engine.")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # CLI Command: solve
    solve_parser = subparsers.add_parser("solve", help="Solve a problem by description or ID")
    solve_parser.add_argument("query", help="Natural language description or problem ID")
    solve_parser.add_argument("inputs", nargs="*", help="The inputs to pass to the algorithm")
    solve_parser.add_argument("--show-code", action="store_true", help="Display the Python source code of the solver")
    solve_parser.add_argument("--copy", action="store_true", help="Copy the source code directly to your clipboard")
    solve_parser.add_argument("--trace", action="store_true", help="Visualize variable state step-by-step")
    
    # CLI Command: search
    search_parser = subparsers.add_parser("search", help="Browse the algorithm registry")
    search_parser.add_argument("query", help="Topic, tag, or keyword")
    search_parser.add_argument("--limit", type=int, default=10, help="Max results to show")

    # CLI Command: serve
    serve_parser = subparsers.add_parser("serve", help="Start the FastAPI REST server")
    serve_parser.add_argument("--port", type=int, default=8000, help="Port to run the server on")


    args = parser.parse_args()

    try:
        if args.command == "solve":
            run_solve(args)
        elif args.command == "search":
            run_search(args)
        elif args.command == "serve":
            # Start the web server!
            import uvicorn
            console.print(f"[bold green]Starting PyDSA API Server on http://127.0.0.1:{args.port}[/bold green]")
            uvicorn.run("pydsa.api.server:app", host="127.0.0.1", port=args.port, reload=False)

    except PyDSAError as e:
        console.print(f"\n[bold red]Error:[/bold red] {e}\n")
        sys.exit(1)

if __name__ == "__main__":
    main()