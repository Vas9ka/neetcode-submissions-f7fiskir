class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def check(capacity):
            req_days = 1
            curr_sum = 0
            for i in range(len(weights)):
                if curr_sum + weights[i] > capacity:
                    req_days += 1
                    curr_sum = weights[i]
                else:
                    curr_sum += weights[i]
            
            return req_days <= days
        
        left = max(weights)
        right = 50000

        while left <= right:
            check_v = (left + right) // 2
            if check(check_v):
                right = check_v - 1
            else:
                left = check_v + 1
        
        return left

