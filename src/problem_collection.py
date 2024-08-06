import importlib
import pkgutil
import os
from rich.console import Console
from rich.table import Table
from problems.abstract_problem import AbstractProblem
from typing import List, Dict

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
    def __init__(self, console: Console):
        self.problem_list = self.collect_problems()
        self.console = console

    def collect_problems(self) -> List[AbstractProblem]:
        # Discover all subclasses of AbstractProblem
        problem_classes = AbstractProblem.__subclasses__()

        # Create instances of each subclass and store them in problem_list
        return [cls() for cls in problem_classes]
    
    def display_problems(self):
        # Create a rich table with horizontal lines
        table = Table(title="Problem List", show_lines=True)

        # Define table columns
        table.add_column("#", justify="right", style="cyan", no_wrap=True)
        table.add_column("Level")
        table.add_column("Problem Name")

        # Define a sorting key to order problems by difficulty
        difficulty_order = {"easy": 0, "medium": 1, "hard": 2}

        # Sort the problem list by difficulty using the defined order
        sorted_problems = sorted(self.problem_list, key=lambda problem: difficulty_order[problem.difficulty.lower()])

        # Add rows to the table
        for index, problem in enumerate(sorted_problems, start=1):
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
        self.console.print()
        self.console.print(table)
        self.console.print()
    
    def display_tags(self):
        # Dictionary to store tags and associated problem names
        tag_to_problems: Dict[str, List[str]] = {}

        # Populate the dictionary
        for problem in self.problem_list:
            for tag in problem.tags:
                if tag not in tag_to_problems:
                    tag_to_problems[tag] = []
                tag_to_problems[tag].append(problem.name)

        # Calculate the total number of unique tags and problems
        total_tags = len(tag_to_problems)
        total_problems = len(self.problem_list)

        # Sort tags by the number of associated problems (ascending order)
        sorted_tags = sorted(tag_to_problems.items(), key=lambda item: len(item[1]))

        # Create a rich table
        table = Table(
            title="Tag List",
            show_lines=True
        )

        # Add columns to the table with total counts
        table.add_column(f"Tag ({total_tags})", justify="left", style="cyan", no_wrap=True)
        table.add_column(f"Problems ({total_problems})", justify="left", style="cyan")

        # Define styles for alternating problem name colors
        problem_styles = ["white", "grey50"]  # Alternating between white and lighter gray

        # Add rows to the table
        for tag, problems in sorted_tags:
            # Alternate the color of problem names
            colored_problem_list = [
                f"[{problem_styles[i % len(problem_styles)]}]{problem}[/{problem_styles[i % len(problem_styles)]}]"
                for i, problem in enumerate(problems)
            ]
            problem_list = ", ".join(colored_problem_list)
            table.add_row(f"{tag} ({len(problems)})", problem_list)

        # Print the table
        self.console.print()
        self.console.print(table)
        self.console.print()

    def test_all_problems(self):
        for problem in self.problem_list:
            print(f"\nTesting Problem: {problem.link}")
            problem.test()
        print()