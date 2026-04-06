class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = {}
        def dp(day,holding):
            if day == len(prices):
                return 0
            if (day, holding) in memo:
                return memo[(day, holding)]
            ans = dp(day + 1, holding)
            if holding:
                ans = max(ans, prices[day] + dp(day + 1, False))
            else:
                ans = max(ans, -prices[day] + dp(day + 1, True))
            
            memo[(day, holding)] = ans
            return memo[(day, holding)]
        
        return dp(0, False)
        