# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        left = 1
        right = n
        pred = (left + right) // 2
        while guess(pred) != 0:
            if guess(pred) == 1:
                left = pred + 1
            else:
                right = pred - 1
            
            pred = (left + right) // 2

        
        return pred