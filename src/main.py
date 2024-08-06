import sys
import os
from rich.console import Console
from rich.table import Table
from problem_mgr import ProblemMgr

# Add the current directory to the system path to allow importing modules from the 'problems' package
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

console = Console()

def print_help():
    table = Table(title="Available Commands", show_lines=True)  # Enable horizontal lines

    # Add columns to the table
    table.add_column("Command", justify="left", style="cyan", no_wrap=True)
    table.add_column("Description", justify="left")

    # Add rows to the table
    table.add_row("display", "Display all completed problems")
    table.add_row("test", "Test all completed problems")
    table.add_row("count", "Display count of problems by difficulty")
    table.add_row("tags", "Display tag frequency")
    table.add_row("help", "Show this help message")
    table.add_row("quit", "Exit the program")

    # Print the table to the console
    console.print()
    console.print(table)
    console.print()

def main():
    problem_mgr = ProblemMgr(console)
    console.print("\n[magenta]Welcome to the LeetCode Problem Manager![/magenta]")
    print_help()

    while True:
        # Get user input
        console.print("Enter a command:", style="magenta", end=" ")
        command = input().strip().lower()

        if command == "problems":
            problem_mgr.display_problems()
        elif command == "tests":
            problem_mgr.test_problems()
        elif command == "help":
            print_help()
        elif command == "tags":
            problem_mgr.display_tags()
        elif command == "quit":
            print("Exiting the program. Goodbye!\n")
            break
        else:
            console.print("[red]Invalid command.[/red] Type 'help' to see available commands.")

if __name__ == "__main__":
    main()