from typing import List

class AbstractProblem:
    def __init__(self, name: str, difficulty: str, link: str, instructions: str, tags: List[str]):
        # Initialize the problem with the given attributes
        self.name = name
        self.difficulty = difficulty
        self.link = link
        self.instructions = instructions
        self.tags = tags

    def solution(self):
        raise NotImplementedError("Subclasses should implement this method.")

    def test(self):
        raise NotImplementedError("Subclasses should implement this method.")

    def __str__(self):
        # Return a formatted string representation of the problem
        return (
            f"Problem Name: {self.name}\n"
            f"Difficulty: {self.difficulty}\n"
            f"Link: {self.link}\n"
            f"Instructions: {self.instructions}\n"
            f"Tags: {', '.join(self.tags)}"
        )
