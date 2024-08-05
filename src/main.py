import sys
import os
from rich.console import Console
from problem_collection import ProblemCollection

# Add the current directory to the system path to allow importing modules from the 'problems' package
sys.path.append(os.path.abspath(os.path.dirname(__file__)))
console = Console()

def print_help():
    print("\nAvailable commands:\n")
    print("  display ........ Display all completed problems")
    print("  test ........... Test all completed problems")
    print("  count .......... Display count of problems by difficulty")
    print("  help ........... Show this help message")
    print("  quit ........... Exit the program\n")

def main():
    problem_collection = ProblemCollection()
    console.print("\n[green]Welcome to the LeetCode Problem Manager![/green]")
    print_help()

    while True:
        # Get user input
        command = input("Enter a command: ").strip().lower()

        if command == "display":
            problem_collection.display_all_problems()
        elif command == "test":
            problem_collection.test_all_problems()
        elif command == "count":
            problem_collection.print_difficulty_count()
        elif command == "help":
            print_help()
        elif command == "quit":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid command. Type 'help' to see available commands.")

if __name__ == "__main__":
    main()