from src.Problems.AbstractProblem import AbstractProblem
from typing import List

class ProblemCollection:
    def __init__(self):
        self.problemList = self.collectProblems()
        self.difficultyList = self.collectDifficulties() 

    def collectProblems(self) -> List[AbstractProblem]:
        # Discover all subclasses of AbstractProblem
        problem_classes = AbstractProblem.__subclasses__()
        # Instantiate each problem class
        return [cls() for cls in problem_classes]

    def collectDifficulties(self) -> List[str]:
        # Gather instructions from each problem
        return [problem.instructions for problem in self.problems]

    def count_by_difficulty(self, difficulty: str) -> int:
        return sum(1 for problem in self.problems if problem.difficulty == difficulty)

    def display_all_problems(self):
        for problem in self.problems:
            print(f"\nProblem:\n{problem}\n")

    def test_all_problems(self):
        for problem in self.problems:
            print(f"\nTesting Problem: {problem.link}")
            problem.test()
