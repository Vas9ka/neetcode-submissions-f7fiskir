class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        unique_ch = set()
        left = ans = 0
        for right in range(len(s)):
            while s[right] in unique_ch:
                unique_ch.remove(s[left])
                left += 1
            unique_ch.add(s[right])
            ans = max(ans, len(unique_ch))
        return ans
        
