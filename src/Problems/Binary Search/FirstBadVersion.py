from Problems.AbstractProblem import AbstractProblem

class FirstBadVersion(AbstractProblem):
    def __init__(self):
        super().__init__(
            problem = "First Bad Version",
            difficulty = "easy",
            link = "https://leetcode.com/problems/first-bad-version/description/",
            instructions = (
                "You are a product manager and currently leading a team to develop a new product. "
                "Unfortunately, the latest version of your product fails the quality check. Since each version is developed "
                "based on the previous version, all the versions after a bad version are also bad.\n"
                "Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, "
                "which causes all the following ones to be bad.\n"
                "You are given an API bool isBadVersion(version) which returns whether version is bad. Implement a function "
                "to find the first bad version. You should minimize the number of calls to the API."
            ),
            tags = ["Binary Search"]
        )

    def solution(self, n: int) -> int:
        # Initialize the left and right pointers
        left = 1
        right = n

        # Perform binary search until the left pointer is less than the right pointer
        while left < right:
            # Calculate the middle index
            mid = left + (right - left) // 2

            # If the middle version is bad, update the right pointer to be the middle index
            if isBadVersion(mid):
                right = mid
            # If the middle version is good, update the left pointer to be one more than the middle index
            else:
                left = mid + 1

        # Return the left pointer, which represents the first bad version
        return left

    def test(self):
        global isBadVersion

        # Define the isBadVersion function within the test method for testing
        def isBadVersion(version: int) -> bool:
            # This is a mock implementation for testing purposes
            return version >= bad

        isBadVersion = isBadVersion  # Use the mock isBadVersion in the test

        # Test cases
        test_cases = [
            (5, 10, 5),
            (1, 1, 1),
            (100, 150, 100),
            (5, 1345, 5)
        ]

        for bad, n, expected in test_cases:
            result = self.solution(n)
            assert result == expected, f"Test failed: expected {expected}, got {result}"
            print(f"Test passed for bad = {bad}, n = {n}: {result}")

    def __str__(self):
        return super().__str__()


