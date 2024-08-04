import importlib.util # Utility functions for importing modules
import pkgutil # Utilities for package manipulation and module iteration
import os  
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
        # Initialize the problem collection by discovering and storing problems
        self.problemList = self.collectProblems()
        
        # Collect the difficulties of the problems in the collection
        self.difficultyList = self.collectDifficulties()

    def collectProblems(self) -> List[AbstractProblem]:
        # Discover all subclasses of AbstractProblem
        problem_classes = AbstractProblem.__subclasses__()
        
        # Instantiate each discovered problem class and return the list
        return [cls() for cls in problem_classes]

    def collect_difficulties(self) -> List[str]:
        # Gather instructions from each problem in the problem list
        return [problem.instructions for problem in self.problemList]

    def count_by_difficulty(self, difficulty: str) -> int:
        # Count and return the number of problems matching the specified difficulty
        return sum(1 for problem in self.problemList if problem.difficulty == difficulty)

    def display_all_problems(self):
        # Print details for each problem in the problem list
        for problem in self.problemList:
            print(f"\n{problem}\n")

    def test_all_problems(self):
        # Test each problem by calling its test method and print the results
        for problem in self.problemList:
            print(f"\nTesting Problem: {problem.link}")
            problem.test()
