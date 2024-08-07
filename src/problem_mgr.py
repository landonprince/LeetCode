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

class ProblemMgr:
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
        table.add_column("#", justify="center", style="cyan", no_wrap=True)
        table.add_column("Level")
        table.add_column("Problem Name")

        # Define a sorting key to order problems by difficulty
        difficulty_order = {"easy": 0, "medium": 1, "hard": 2}

        # Sort the problem list by difficulty using the defined order
        sorted_problems = sorted(self.problem_list, key=lambda problem: difficulty_order[problem.difficulty.lower()])

        # Initialize counters for each difficulty level
        easy_count = 0
        medium_count = 0
        hard_count = 0

        # Add rows to the table
        for index, problem in enumerate(sorted_problems, start=1):
            # Increment counters based on the problem's difficulty
            if problem.difficulty.lower() == "easy":
                easy_count += 1
                difficulty_color = "green"
            elif problem.difficulty.lower() == "medium":
                medium_count += 1
                difficulty_color = "yellow"
            else:
                hard_count += 1
                difficulty_color = "red"

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

        # Print the summary of problem counts by difficulty level
        self.console.print(f"Easy: [green]{easy_count}[/green] | Medium: [yellow]{medium_count}[/yellow] | Hard: [red]{hard_count}[/red]\n")

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
        table = Table(title="Tag List",show_lines=True)

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

    def test_problems(self):
        # Create a rich table with two columns
        table = Table(title="Testing All Problems", show_lines=True)
        table.add_column("Problem Name", justify="left")
        table.add_column("Tests Passed", justify="center", style="cyan")

        all_tests_passed = 0
        all_total_tests = 0

        for problem in self.problem_list:
            # Run the test method to capture test results
            problem.test()

            # Add each problem's name and test results to the table
            table.add_row(problem.name, f"{problem.tests_passed}/{problem.total_tests}")

            # Accumulate the total tests passed and total tests for all problems
            all_tests_passed += problem.tests_passed
            all_total_tests += problem.total_tests

        # Print the table with all test results
        self.console.print()
        self.console.print(table)
        self.console.print()

        # Print the overall summary below the table with colored results
        self.console.print(f"Total Tests Passed: [green]{all_tests_passed}/{all_total_tests}[/green]\n")