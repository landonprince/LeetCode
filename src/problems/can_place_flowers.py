from typing import List
from problems.abstract_problem import AbstractProblem

class CanPlaceFlowers(AbstractProblem):
    def __init__(self):
        super().__init__(
            name = "Can Place Flowers",
            difficulty = "Easy",
            link = "https://leetcode.com/problems/can-place-flowers/",
            instructions = (
                "Given an integer array flowerbed containing 0's and 1's, "
                "where 0 means empty and 1 means not empty, and an integer n, "
                "return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise."
            ),
            tags = ["Array"]
        )
        
    def solution(self, flowerbed: List[int], n: int) -> bool:
        # Initialize the count of flowers planted to 0
        count = 0
        
        # Iterate over the flowerbed
        for i in range(len(flowerbed)):
            # If the current position is 0 (empty) and the previous and next positions are also empty (or there is a flower), plant a flower
            if flowerbed[i] == 0 and (i == 0 or flowerbed[i-1] == 0) and (i == len(flowerbed) - 1 or flowerbed[i+1] == 0):
                flowerbed[i] = 1
                count += 1
        
        # Return true if the required number of flowers has been planted
        return count >= n
                
    def test(self):
        # Reset test counters
        self.tests_passed = 0
        self.total_tests = 0
        
        # Test cases
        test_cases = [
            ([1,0,0,0,1], 1, True),
            ([1,0,0,0,1], 2, False),
            ([1,0,0,0,0,1], 1, True),
            ([0,0,0,0,0,0], 2, True),
            ([1,0,0,0,0,0,1], 2, True),
            ([1,0,0,0,0,0,1,0,0], 5, False),
        ]
        
        # Run each test case
        for flowerbed, n, expected in test_cases:
            self.total_tests += 1
            result = self.solution(flowerbed, n)
            if result == expected:
                self.tests_passed += 1