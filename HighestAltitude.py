from typing import List

class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        max_altitude = 0
        current_altitude = 0

        # Calculate the maximum altitude by adding the altitude gain to the current altitude 
        for altitude_gain in gain:
            current_altitude += altitude_gain
            max_altitude = max(max_altitude, current_altitude)

        return max_altitude
    

gain = [-5,1,5,0,-7]
solution = Solution()
result = solution.largestAltitude(gain)

print()
print(f"gain = {gain}, result = {result}")
