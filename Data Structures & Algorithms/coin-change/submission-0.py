class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        seen_sum = set()
        level = 0
        q = deque([0])
        if amount == 0:
            return 0
        while q:
            level += 1
            for _ in range(len(q)):
                curr_sum = q.popleft()
                for coin in coins:
                    next_sum = curr_sum + coin
                    if next_sum == amount:
                        return level
                    if next_sum < amount and next_sum not in seen_sum:
                        q.append(next_sum)
                        seen_sum.add(next_sum) 
        
        return -1