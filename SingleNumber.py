class SingleNumber:
    def __init__(self):
        self.difficulty = "easy"
        self.link = "https://leetcode.com/problems/single-number/description/"
        self.instructions = (
            "Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.\n"
            "You must implement a solution with a linear runtime complexity and use only constant extra space."
        )
        self.tags = ["Array", "Bit Manipulation"]

    def solution(self, nums: list[int]) -> int:
        # XOR all numbers in the array
        result = 0
        for num in nums:
            result ^= num  # XOR with each number

        return result

    def test(self):
        # Test cases
        test_cases = [
            ([1, 1, 2, 2, 3, 3, 4, 5, 5], 4),
            ([4, 1, 2, 1, 2], 4),
            ([2, 2, 1], 1),
            ([1], 1),  # Single element
            ([0, 0, 1], 1)
        ]

        for nums, expected in test_cases:
            result = self.solution(nums)
            assert result == expected, f"Test failed: expected {expected}, got {result}"
            print(f"Test passed for nums = {nums}: {result}")

    def __str__(self):
        return (
            f"Problem: Single Number\nDifficulty: {self.difficulty}\nLink: {self.link}\n"
            f"Instructions: {self.instructions}\nTags: {', '.join(self.tags)}"
        )

# Create an instance of the problem
solution = SingleNumber()
print(solution)  # Display problem information
solution.test()  # Run tests
