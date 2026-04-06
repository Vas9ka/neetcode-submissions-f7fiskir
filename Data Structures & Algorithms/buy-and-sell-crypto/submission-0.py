class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        left = right = 0
        for right in range(len(prices)):
            while prices[right] - prices[left] < 0:
                left += 1
            ans = max(ans, prices[right] - prices[left])
        return ans

