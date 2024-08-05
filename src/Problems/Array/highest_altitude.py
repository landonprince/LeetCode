from typing import List
from problems.abstract_problem import AbstractProblem

class HighestAltitude(AbstractProblem):
    def __init__(self):
        super().__init__(
            name = "Find the Highest Altitude",
            difficulty = "easy",
            link = "https://leetcode.com/problems/find-the-highest-altitude/description/",
            instructions = (
                "There is a biker going on a road trip. The road trip consists of n + 1 points at different altitudes. "
                "The biker starts his trip on point 0 with altitude equal 0.\n"
                "You are given an integer array gain of length n where gain[i] is the net gain in altitude between points i "
                "and i + 1 for all (0 <= i < n).\n"
                "Return the highest altitude of a point."
            ),
            tags = ["Array"]
        )

    def solution(self, gain: List[int]) -> int:
        max_altitude = 0
        current_altitude = 0

        # Add each altitude gain to the current altitude and update the max altitude if necessary
        for altitude_gain in gain:
            current_altitude += altitude_gain
            max_altitude = max(max_altitude, current_altitude)

        return max_altitude

    def test(self):
        # Test cases
        test_cases = [
            ([-5, 1, 5, 0, -7], 1),  # Correct: max altitude is 1
            ([-4, -3, -2, -1, 4, 3, 2], 0),  # Correct: max altitude is 0
            ([10, -10, 5, -3, 7], 10),  # Correct: max altitude is 10
            ([1, 2, 3, 4, 5], 15),  # Correct: max altitude is 15
            ([-1, -2, -3, -4], 0),  # Correct: max altitude is 0
        ]
        
        for gain, expected in test_cases:
            result = self.solution(gain)
            assert result == expected, f"Test failed: expected {expected}, got {result}"
            print(f"Test passed for gain = {gain}: {result}")

    def __str__(self):
        return super().__str__()
            
        


