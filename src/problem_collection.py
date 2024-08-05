import importlib
import pkgutil
import os
from problems.abstract_problem import AbstractProblem
from typing import List, Tuple

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
        print("\nEasy Problems: ", sum(1 for problem in self.problem_list if problem.difficulty == "easy"))     
        print("Easy Problems: ", sum(1 for problem in self.problem_list if problem.difficulty == "medium")) 
        print("Easy Problems: ", sum(1 for problem in self.problem_list if problem.difficulty == "hard")) 
        print()

    def display_all_problems(self):
        for problem in self.problem_list:
            print(f"\n{problem.name}")
        print()

    def test_all_problems(self):
        for problem in self.problem_list:
            print(f"\nTesting Problem: {problem.link}")
            problem.test()
        print()