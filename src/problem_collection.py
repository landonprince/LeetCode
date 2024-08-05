import importlib
import pkgutil
import os
from collections import Counter
from rich.console import Console
from rich.table import Table
from problems.abstract_problem import AbstractProblem
from typing import List

def import_submodules(package_name: str):
    # Import the package using its name to get the package object
    package = importlib.import_module(package_name)
    
    # Get the directory path of the package
    package_dir = os.path.dirname(package.__file__)
    
    # Iterate over all modules and packages within the package directory
    for _, module_name, is_pkg in pkgutil.iter_modules([package_dir]):
        # Construct the full module name by combining package and module names
        full_module_name = f"{package_name}.{module_name}"
        
        if is_pkg:
            # If the current item is a package, recursively import its submodules
            import_submodules(full_module_name)
        else:
            # If the current item is a module, import it directly
            importlib.import_module(full_module_name)

# Import all submodules within the 'problems' package
import_submodules('problems')

class ProblemCollection:
    def __init__(self):
        self.problem_list = self.collect_problems()

    def collect_problems(self) -> List[AbstractProblem]:
        # Discover all subclasses of AbstractProblem
        problem_classes = AbstractProblem.__subclasses__()

        # Create instances of each subclass and store them in problem_list
        return [cls() for cls in problem_classes]

    def print_difficulty_count(self):
        print("\nEasy Problems: ", sum(1 for problem in self.problem_list if problem.difficulty == "Easy"))     
        print("Easy Problems: ", sum(1 for problem in self.problem_list if problem.difficulty == "Medium")) 
        print("Easy Problems: ", sum(1 for problem in self.problem_list if problem.difficulty == "hard")) 
        print()

    def display_tag_frequency(self):
        # Use a Counter to count the frequency of each tag
        tag_counter = Counter()
        for problem in self.problem_list:
            tag_counter.update(problem.tags)

        # Sort tags by frequency (descending)
        sorted_tags = sorted(tag_counter.items(), key=lambda item: item[1])

        # Create a Rich console and table
        console = Console()
        table = Table(title="Tag Frequency")

        # Add columns to the table
        table.add_column("Problem Tag", justify="left", no_wrap=True)
        table.add_column("#", justify="right", style="magenta")

        # Add rows to the table
        for tag, frequency in sorted_tags:
            table.add_row(tag, str(frequency))

        # Print the table to the console
        console.print()
        console.print(table)
        console.print()

    def display_all_problems(self):
        console = Console()
        table = Table(title="Problem List")

        # Define table columns
        table.add_column("#", justify="right", style="cyan", no_wrap=True)
        table.add_column("Level")
        table.add_column("Problem Name")

        # Add rows to the table
        for index, problem in enumerate(self.problem_list, start=1):
            # Change the color of the difficulty based on its value
            difficulty_color = "green" if problem.difficulty.lower() == "easy" else \
                            "yellow" if problem.difficulty.lower() == "medium" else \
                            "red"

            # Add a row to the table with colored difficulty
            table.add_row(
                str(index),
                f"[{difficulty_color}]{problem.difficulty}[/{difficulty_color}]",
                f"{problem.name}"
            )
        # Print the table
        console.print()
        console.print(table) 
        console.print()

    def test_all_problems(self):
        for problem in self.problem_list:
            print(f"\nTesting Problem: {problem.link}")
            problem.test()
        print()