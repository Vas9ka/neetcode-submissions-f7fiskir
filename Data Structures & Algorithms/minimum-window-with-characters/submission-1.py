from collections import defaultdict, Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        formed = 0
        t_counts = Counter(t)
        required = len(t_counts)
        left = 0
        best_len = float('inf')
        best_l = best_r = 0
        moving_dict = defaultdict(int)
        for right in range(len(s)):
            moving_dict[s[right]] += 1
            if s[right] in t_counts and moving_dict[s[right]] == t_counts[s[right]]:
                formed += 1
            while formed == required:
                if right - left + 1 < best_len:
                    best_len = right - left + 1
                    best_l = left
                    best_r = right
                moving_dict[s[left]] -= 1
                if s[left] in t_counts and moving_dict[s[left]] < t_counts[s[left]]:
                    formed -= 1
                left += 1
        if best_len == float('inf'):
            return ""
        return s[best_l:best_r + 1]