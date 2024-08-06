from typing import List

class AbstractProblem:
    def __init__(self, name: str, difficulty: str, link: str, instructions: str, tags: List[str]):
        # Initialize the problem with the given attributes
        self.name = name
        self.difficulty = difficulty
        self.link = link
        self.instructions = instructions
        self.tags = tags
        self.tests_passed = 0
        self.total_tests = 0

    def solution(self):
        raise NotImplementedError("Subclasses should implement this method.")

    def test(self):
        raise NotImplementedError("Subclasses should implement this method.")

