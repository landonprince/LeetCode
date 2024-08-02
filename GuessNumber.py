# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        min = 1
        max = n

        # Binary search to find the picked number
        while min <= max:
            mid = min + (max - min) // 2

            if guess(mid) == 1:
                min = mid + 1
            elif guess(mid) == -1:
                max = mid - 1
            else:
                return mid
        return -1

def guess(self, num: int) -> int:
    return 0