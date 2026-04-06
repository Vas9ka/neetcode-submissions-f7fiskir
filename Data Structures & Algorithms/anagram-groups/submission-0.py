class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for word in strs:
            letters = [0] * 26
            for i in range(len(word)):
                letter_index = ord(word[i]) - ord('a')
                letters[letter_index] += 1
            letters = tuple(letters)
            if letters in groups:
                groups[letters].append(word)
            else:
                groups[letters] = [word]
        ans = []
        for group in groups.values():
            ans.append(group)
        return ans