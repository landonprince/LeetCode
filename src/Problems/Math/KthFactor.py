class KthFactor:
    def __init__(self):
        self.difficulty = "medium"
        self.link = "https://leetcode.com/problems/the-kth-factor-of-n/description/"
        self.instructions = (
            "Given two positive integers n and k, return the kth factor of n."
            "A factor of an integer n is defined as an integer i where n % i == 0.\n"
            "If there are fewer than k factors, return -1."
        )
        self.tags = ["Math"]

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
        # Test cases
        test_cases = [
            (12, 3, 3),
            (7, 2, 7),
            (4, 4, -1),
            (6, 1, 1),
            (16, 5, 16)
        ]

        for n, k, expected in test_cases:
            result = self.solution(n, k)
            assert result == expected, f"Test failed: expected {expected}, got {result}"
            print(f"Test passed for n = {n}, k = {k}: {result}")

    def __str__(self):
        return (
            f"Problem: The kth Factor of n\nDifficulty: {self.difficulty}\nLink: {self.link}\n"
            f"Instructions: {self.instructions}\nTags: {', '.join(self.tags)}"
        )

# Create an instance of the problem
solution = KthFactor()
print(solution)  # Display problem information
solution.test()  # Run tests