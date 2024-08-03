class AbstractProblem:
    def __init__(self, difficulty: str, link: str, instructions: str, tags: list[str]):
        self.difficulty = difficulty
        self.link = link
        self.instructions = instructions
        self.tags = tags

    def solution(self):
        raise NotImplementedError("Subclasses should implement this method.")

    def test(self):
        raise NotImplementedError("Subclasses should implement this method.")

    def __str__(self):
        return (
            f"Difficulty: {self.difficulty}\n"
            f"Link: {self.link}\n"
            f"Instructions: {self.instructions}\n"
            f"Tags: {', '.join(self.tags)}"
        )
