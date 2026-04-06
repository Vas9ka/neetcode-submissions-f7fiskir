from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        s_freqs = defaultdict(int)
        max_freq = 0
        left = ans = 0
        for right in range(len(s)):
            s_freqs[s[right]] += 1
            max_freq = max(max_freq, s_freqs[s[right]])
            while (right - left + 1) - max_freq > k:
                s_freqs[s[left]] -= 1
                left += 1
            ans = max(ans, right - left + 1)
        return ans

