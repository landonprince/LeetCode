from problems.abstract_problem import AbstractProblem

class GuessNumberHigherOrLower(AbstractProblem):
    def __init__(self):
        super().__init__(
            name = "Guess Number Higher or Lower",
            difficulty = "Easy",
            link = "https://leetcode.com/problems/guess-number-higher-or-lower/description/",
            instructions = (
                "We are playing the Guess Game. The game is as follows:\n"
                "I pick a number from 1 to n. You have to guess which number I picked.\n"
                "Every time you guess wrong, I will tell you whether the number I picked is higher or lower than your guess.\n"
                "You call a pre-defined API int guess(int num) which returns:\n"
                "-1 if num is higher than the number I picked (your guess is too high)\n"
                "1 if num is lower than the number I picked (your guess is too low)\n"
                "0 if num is equal to the number I picked (your guess is correct)\n"
                "Return the number I picked."
            ),
            tags = ["Binary Search"],
        )

    def guess(self, num: int) -> int:
        if num < self.picked_number:
            return 1
        elif num > self.picked_number:
            return -1
        else:
            return 0

    def solution(self, n: int) -> int:
        min_val = 1
        max_val = n

        # Binary search to find the picked number
        while min_val <= max_val:
            mid = min_val + (max_val - min_val) // 2

            # Use the guess API to determine the next step
            result = self.guess(mid)

            if result == 1:
                min_val = mid + 1
            elif result == -1:
                max_val = mid - 1
            else:
                return mid
        return -1

    def test(self):
        # Reset test counters
        self.tests_passed = 0
        self.total_tests = 0

        # Test cases
        test_cases = [
            (10, 6),
            (1, 1),
            (100, 67),
            (1000, 999),
            (500, 123)
        ]

        # Run each test case
        for n, expected in test_cases:
            self.total_tests += 1
            self.picked_number = expected
            result = self.solution(n)
            if result == expected:
                self.tests_passed += 1


