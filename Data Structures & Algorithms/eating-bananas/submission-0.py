from math import ceil
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def check(bn_hour):

            ans = 0
            for pile in piles:
                ans += ceil(pile / bn_hour)
            return ans <= h
        
        right = max(piles)
        left = 1
        while left <= right:
            mid = (left + right) // 2
            if check(mid):
                right = mid - 1
            else:
                left = mid + 1
        return left
