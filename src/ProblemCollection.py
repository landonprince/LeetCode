import importlib.util
import pkgutil
import os
from Problems.AbstractProblem import AbstractProblem
from typing import List

def import_submodules(package_name: str):
    """Dynamically import all submodules within a package."""
    package = importlib.import_module(package_name)
    package_dir = os.path.dirname(package.__file__)
    
    for _, module_name, is_pkg in pkgutil.iter_modules([package_dir]):
        full_module_name = f"{package_name}.{module_name}"
        if is_pkg:
            import_submodules(full_module_name)
        else:
            importlib.import_module(full_module_name)

# Dynamically import all modules in Problems
import_submodules('Problems')

class ProblemCollection:
    def __init__(self):
        self.problemList = self.collectProblems()
        self.difficultyList = self.collectDifficulties()

    def collectProblems(self) -> List[AbstractProblem]:
        # Discover all subclasses of AbstractProblem
        problem_classes = AbstractProblem.__subclasses__()
        return [cls() for cls in problem_classes]

    def collectDifficulties(self) -> List[str]:
        return [problem.instructions for problem in self.problemList]

    def count_by_difficulty(self, difficulty: str) -> int:
        return sum(1 for problem in self.problemList if problem.difficulty == difficulty)

    def display_all_problems(self):
        for problem in self.problemList:
            print(f"\n{problem}\n")

    def test_all_problems(self):
        for problem in self.problemList:
            print(f"\nTesting Problem: {problem.link}")
            problem.test()
