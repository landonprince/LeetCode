import importlib.util 
import pkgutil 
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
        # Create the main problem list where each problem is a list of [name, difficulty, tags]
        self.problem_list = self.collect_problems()
            
    def collect_problems(self) -> List[List]:
        # Discover all subclasses of AbstractProblem
        problem_classes = AbstractProblem.__subclasses__()
        
        # Create a list for each problem with name, difficulty, and tags
        problem_data = [
            [cls().name, cls().difficulty, cls().tags]
            for cls in problem_classes
        ]
        return problem_data

    def count_by_difficulty(self, difficulty: str) -> int:
        # Count and return the number of problems matching the specified difficulty
        return sum(1 for problem in self.problem_list if problem[1] == difficulty)

    def display_all_problems(self):
        # Print details for each problem in the problem list
        for problem in self.problem_list:
            print(f"\nProblem Name: {problem[0]}\nDifficulty: {problem[1]}\nTags: {problem[2]}")
        print()

    def test_all_problems(self):
        # Test each problem by calling its test method and print the results
        problem_classes = AbstractProblem.__subclasses__()
        for cls in problem_classes:
            problem = cls()
            print(f"\nTesting Problem: {problem.link}")
            problem.test()
        print()