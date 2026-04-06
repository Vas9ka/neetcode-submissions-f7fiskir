from collections import Counter, defaultdict
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        s1_dict = Counter(s1)
        moving_dict = defaultdict(int)
        k = len(s1)
        for i in range(k):
            moving_dict[s2[i]] += 1
        if moving_dict == s1_dict:
            return True
        for i in range(k, len(s2)):
            moving_dict[s2[i]] += 1
            moving_dict[s2[i - k]] -= 1
            if moving_dict[s2[i - k]] == 0:
                del moving_dict[s2[i - k]]
            if moving_dict == s1_dict:
                return True
        return False