class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        curr = 0
        ans = 0
        for i in range(k):
            curr += arr[i]
        curr
        if curr / k >= threshold:
            ans += 1

        for i in range(k, len(arr)):
            curr += arr[i]
            curr -= arr[i - k]
            if curr / k >= threshold:
                ans += 1
        
        return ans

        