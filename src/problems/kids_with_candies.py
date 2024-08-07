from typing import List
from problems.abstract_problem import AbstractProblem

class KidsWithCandies(AbstractProblem):
    def __init__(self):
        super().__init__(
                name = "Kids With Greatest Number of Candies",
                difficulty = "Easy",
                link = "https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/",
                instructions = (
                    "Return a boolean array result of length n, where result[i] is true if, "
                    "after giving the ith kid all the extraCandies, they will have the greatest "
                    "number of candies among all the kids, or false otherwise."
                ),
                tags = ["Array"]
            )
        
    def solution(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candies = max(candies)
        return [c + extraCandies >= max_candies for c in candies]
    
    def test(self):
        # Reset test counters
        self.tests_passed = 0
        self.total_tests = 0
        
        # Test cases
        test_cases = [
            ([1, 1, 2, 3], 3, [True, True, True, True]),
            ([2, 2, 4, 4], 1, [False, False, True, True]),
            ([4, 2, 1, 1, 2], 1, [True, False, False, False, False])
        ]
        
        # Run each test case
        for candies, extraCandies, expected in test_cases:
            self.total_tests += 1
            result = self.solution(candies, extraCandies)
            if result == expected:
                self.tests_passed += 1