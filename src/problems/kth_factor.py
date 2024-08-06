from problems.abstract_problem import AbstractProblem

class KthFactor(AbstractProblem):
    def __init__(self):
        super().__init__(
            name = "The Kth Factor of N",
            difficulty = "Medium",
            link = "https://leetcode.com/problems/the-kth-factor-of-n/description/",
            instructions = (
                "Given two positive integers n and k, return the kth factor of n."
                "A factor of an integer n is defined as an integer i where n % i == 0.\n"
                "If there are fewer than k factors, return -1."
            ),
            tags = ["Math"]
        )

    def solution(self, n: int, k: int) -> int:
        factors = []

        # Find all factors of n and store them in the factors list
        for i in range(1, n + 1):
            if n % i == 0:
                factors.append(i)
                # Early exit if we have found k factors
                if len(factors) == k:
                    return factors[-1]

        # If there are fewer than k factors, return -1
        return -1

    def test(self):
        # Reset test counters
        self.tests_passed = 0
        self.total_tests = 0

        # Test cases
        test_cases = [
            (12, 3, 3),
            (7, 2, 7),
            (4, 4, -1),
            (6, 1, 1),
            (16, 5, 16)
        ]

        # Run each test case
        for i, (n, k, expected) in enumerate(test_cases, start=1):
            self.total_tests += 1
            result = self.solution(n, k)
            if result == expected:
                self.tests_passed += 1


